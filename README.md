# Tugas 2
## Jelaskan bagaimana cara mengimplementasikan checklist di atas secara step-by-step.
### Membuat Projek Django Baru
- menginstall dependencies yang tercantum pada tutorial 0 dan membuat proyek bernama sepakbola_shop dengan menjalankan perintah `django-admin startproject football_shop .`
- Membuat dan mengkonfigurasi env dengan perintah ` python -m venv env`.
- mengkonfigurasi settings.py dengan memasukkan kredensial yang sudah diberikan oleh PBP yang di kirim di email.
- membuat .gitignore dna mnegisidengan berkas-berkas ynag tidka ingin dikirim ke git.
- Membuat repo baru di github.
- upload repo lokal ke repo github dengan git remote. 

### Membuat Aplikasi Baru (Main).
- aktifkan virtual enviroment dengan command env\Scripts\activate.
- Menjalankan perintah `python manage.py startapp main` untuk membuat aplikasi bernama main.

### Membuat model pada aplikasi main bernama Produk dan memiliki atribut wajib.
- buat class baru yang bernama Produk.
- isi class:

```
class Produk(models.Model):
    CATEGORY_CHOICES = [
        ('boots', 'Boots'),
        ('knee-guards', 'Knee-guards'),
        ('footballs', 'Footballs'),
        ('socks', 'Socks'),
        ('shirts', 'Shirts'),
        ('gloves', 'Gloves'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='boots')
    thumbnail = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name 
```

###  Membuat fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.
- Mengimport render pada `views.py`, `from django.shortcuts import render`
- membuat fungsi yang me-render html di `views.py`, `return render(request, "main.html")`
- Untuk membuat template html yang bisa menampilkan nama aplikasi, nama, dan kelas,  bisa langsung diedit di htmlnya atau bisa membuat html menampilkan variabel yang tertulis di `views.py`. contoh :
```
<h1>Football Shop</h1>

<h5>NPM: </h5>
<p>{{ npm }}</p>
<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}</p>
```

### Mendefinisikan rute di `urls.py` aplikasi main agar dapat memanggil fungsi dari views.py.
- Setelah mmengedit `views.py`, buat `urls.py` pada `main` yang berisi:
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

###  Melakukan deployment ke PWS sehingga dapat diakses oleh orang lain melalui Internet dan browser mereka.
- migrate program dengan perintah : - `python manage.py makemigrations`
                                    - `python manage.py migrate`
- buat proyek baru di PWS, tambahkan deployment url kepada bagian `ALLOWED_HOST` pada `settings.py`.
- lakukan git remote dengan server pws, lalu jalankan `git push pws master`.


## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
```

                                                                                                                Browser (client)
                                                                                                                	||  (HTTP REQUEST)
                                                                                                                	v
                                                                                                                 server
                                                                                                                    ||
                                                                                                                    v
                                                                                                                 Django
                                                                                                                    ||
                                                                                                                    v
                                                                                                                urls.py
                                                                                           (Mencocokkan URL yang diminta dengan pola yang tersedia)
                                                                                                                	||
                                                                                                                	v
                                                                                                                views.py
                                                                                 (Menangani logika, ambil data dari models.py atau langsung render template)
                                                                                                                	||
                                                                                                                	v
                                                                                                                models.py
                                                                                      (Berinteraksi dengan database (Create, Read, Update, Delete))
                                                                                                                	||
                                                                                                                	v
                                                                                                                views.py
                                                                                              (Mengembalikan data + memilih template HTML)
                                                                                                                	||
                                                                                                                	v
                                                                                                                template HTML
                                                                                              (Menampilkan data dalam bentuk halaman web)
                                                                                                                	|| (HTTP RESPONSE)
                                                                                                                	v
                                                                                                                  Django
                                                                                                                    ||
                                                                                                                     v 
                                                                                                                  server
                                                                                                                    ||
                                                                                                                     v
                                                                                                                Browser (Client)
```

## Jelaskan peran settings.py dalam proyek Django
```
Dalam sebuah proyek djang, settings.py sangat penting karena file itu berfungsi sebagai pusat konfigurasi dari proyek Django tersebut. disitulah dimana semua setting utama proyek django didefinisikan, Setting setting seperti:
- Konfigurasi database 
- aplikasi yang digunakan (Installled_apps)
- Middleware yang mengatur request/response
- Template engine yang digunakan
dan setting lainnya yang membuat settings.py inti pengaturan proyek Django.
```

## Bagaimana cara kerja migrasi database di Django?
```
Migrasi model/database adalah cara django keeping-track perubahan yang dilakukan pada database dengan cara menyinkronkan perubahan model dengan struktur tabel di database. Cara kerja Migrasi database Django 

1)Definisi Model
membuat atau mengubah model di models.py.

2)Membuat Migrasi (python manage.py makemigrations)
Django membaca perubahan pada model dan menghasilkan file migrasi (berisi instruksi SQL yang akan dijalankan).

3) Menerapkan Migrasi (python manage.py migrate)
Django menjalankan file migrasi tersebut ke database sehingga tabel, kolom, atau relasi sesuai dengan model.

4)Pencatatan Migrasi
Django menyimpan history migrasi yang sudah diterapkan di tabel khusus (django_migrations)dimana bisa dilihat migrasi yang sudah diterapkan dan yang belum.
```
## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
```
Menurut saya, framework Django merupakan tempat yang ideal untuk belajar pengembangan software karena Django mempunyai fitur
bawaan lengkap yang membuat implementasi mudah untuk pemula, ditambahkan django memiliki struktur yang jelas (MVT) dan sintaks python yang mudah,
semua ini membuat Django framework ideal untuk pemula.
```

## Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
```
Asdos sudah sangat membantu dan standby untuk menjawab pertanyaan=pertanyaan saat sesi tutorial
```

#Tugas 3
## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
```
- Agar data dapat diakses oleh berbagai client di berbagai tempat , 
  sehingga memungkinkan data tersebut bisa dikirim dari client ke server atau sebaliknya (Client -> Server or Server -> Client), 
  lalu disimpan ke dalam database. 
- sebagai "jembatan" pada komponen-komponen pada sebuah platform (database SQL,NoSQL, API REST, etc)
  supaya sistem-sistem ini bisa berkomunikasi
- menghasilkan user experience yang lebih baik karena memastikan data dapat di akses secara cepat dan tepat waktu.
```

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
```
Saya Sendiri lebih memilihi JSON karena
- JSON memiliki Sytax dan Format mirip JavaScript yang membuatnya lebih mudah di baca
- JSON lebih ringan dan efisien
- Didukung luas di berbagai APi pada web
```

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
```

```





