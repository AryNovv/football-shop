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


## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas html
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

## Jelaskan peran `settings.py` dalam proyek Django
```
Dalam sebuah proyek djang, settings.py sangat penting karena file itu berfungsi sebagai pusat konfigurasi dari proyek Django tersebut. disitulah dimana semua setting utama proyek django didefinisikan, Setting setting seperti:
- Konfigurasi database 
- aplikasi yang digunakan (Installled_apps)
- Middleware yang mengatur request/response
- Template engine yang digunakan
dan setting lainnya yang membuat settings.py inti pengaturan proyek Django.
```

## Bagaimana cara kerja migrasi database di Django?
Migrasi model/database adalah cara django keeping-track perubahan yang dilakukan pada database dengan cara menyinkronkan perubahan model dengan struktur tabel di database. Cara kerja Migrasi database Django 

1)Definisi Model
membuat atau mengubah model di models.py.

2)Membuat Migrasi (python manage.py makemigrations)
Django membaca perubahan pada model dan menghasilkan file migrasi (berisi instruksi SQL yang akan dijalankan).

3)Menerapkan Migrasi (python manage.py migrate)
Django menjalankan file migrasi tersebut ke database sehingga tabel, kolom, atau relasi sesuai dengan model.

4)Pencatatan Migrasi
Django menyimpan history migrasi yang sudah diterapkan di tabel khusus (django_migrations)dimana bisa dilihat migrasi yang sudah diterapkan dan yang belum.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, framework Django merupakan tempat yang ideal untuk belajar pengembangan software karena Django mempunyai fitur
bawaan lengkap yang membuat implementasi mudah untuk pemula, ditambahkan django memiliki struktur yang jelas (MVT) dan sintaks python yang mudah,
semua ini membuat Django framework ideal untuk pemula.

## Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Asdos sudah sangat membantu dan standby untuk menjawab pertanyaan=pertanyaan saat sesi tutorial

# Tugas 3
## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
- Agar data dapat diakses oleh berbagai client di berbagai tempat , 
  sehingga memungkinkan data tersebut bisa dikirim dari client ke server atau sebaliknya (Client -> Server or Server -> Client), 
  lalu disimpan ke dalam database. 
- sebagai "jembatan" pada komponen-komponen pada sebuah platform (database SQL,NoSQL, API REST, etc)
  supaya sistem-sistem ini bisa berkomunikasi
- menghasilkan user experience yang lebih baik karena memastikan data dapat di akses secara cepat dan tepat waktu.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Saya Sendiri lebih memilihi JSON karena
- JSON memiliki Sytax dan Format mirip JavaScript yang membuatnya lebih mudah di baca
- JSON lebih ringan dan efisien
- Didukung luas di berbagai APi pada web

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
`is_valid()` berguna untuk memvalidasi input dari form sudah sesuai dengan aturan field di models.py atau aturan django tentang isi form tersebut.Jika `is_valid()` tidak digunakan, 
maka ketika user menginput form tersebut dan masuk ke database, maka ketika database ingin menggunakan data tersebut ada kemungkinan menyebabkan crash karena tidak sesuai dengan aturan field di models.py atau django

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
- CSRF(Cross-Site Request Forgery) adalah jenis serangan web/CyberSecurity flaw dimana penyerang mengirim request ke server saat loading sebuah form (ex : login bank) 
sehingga penyerang dapat mengirim request selagi meyamar sebagai client. penyerang dapat menyamar sebagai client karena meng-intersepsi session cookie yang telah di kirim oleh server ke client
- `csrf_token` dibuat untuk menanggulangi csrf, dengan cara server mengirim semacam kode kepada client, dan ketika melakukan request, client harus mengembalikkan kode tersebut ke server, 
jika tidak menggunakan csrf_token, maka penyerang dapat melakukan request kepada server tanpa verifikasi dengan form tersebut.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID objek, dan JSON by ID objek.
- untuk menunjukkan objek dalam fungsi XML, saya memakai fungsi:
```
def show_xml(request):
     products_list = Product.objects.all()
     xml_data = serializers.serialize("xml", products_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Produk.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

```
- disini fungsi mengambil semua object, lalu dengan menggunakan library serializer, library tersebut mengubah semua format object menjadi xml/json. lalu fungsi mengembalikan response berupa page dengan semua xml/json.

```
def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product_item  = Produk.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product_item])
        return HttpResponse(json_data, content_type="application/json")
    except:
        return HttpResponse(status=404)
```
- disini fungsi mengambil object dengan id yang sama dengan request . Lalu diserialize ke xml/json, setelah itu mengembalikan respons page berupa xml/json dengan id yang sama. Jika object dengan id request tidak ada, mengembalikan response page 404.

### Membuat routing URL untuk masing-masing fungsi views yang telah ditambahkan.
- import fungsi yang di tambahkan di `views.py` ke `urls.py`
- tambahkan path file xml/json masing-masing fungsi ke dalam `urlpatterns:`
```
        .
        .
        .
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
        .
        .
```

###  Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
- di main.html,  buat 2 button dengan tag button yang memiliki anchor (href) ke create_listing.html untuk menambahkan objek dan tag button lagi yang href ke product_detail untuk lihat detail objek
- jika sudah ada objek, menampilkan data objek dengan for-loop semua objek produk yang ada di database dan ambil semua field objeknya.
```
<a href="{% url 'main:create_listing' %}">
  <button>+ Add Listing</button>
</a>

<hr>

{% if not product_list %}
<p>Uh Oh! we have no listing at the moment, come back next time when a new drop has been announced!</p>
{% else %}

{% for produk in product_list %}
<div>
  <h2><a href="{% url 'main:show_catalog' produk.id %}">
    {{ produk.name }} ${{produk.price }}
    </a>
  </h2>

  <p><b>{{ produk.get_category_display }}</b>
    {% if produk.is_featured %} | <b>Featured</b>{% endif %}
    {% if produk.is_product_hot %} | <b>Hot</b>{% endif %}
    | <i>{{ produk.created_at|date:"d M Y H:i" }}</i>
    | Views: {{ produk.products_views }}
  </p>

  {% if produk.thumbnail %}
  <img src="{{ produk.thumbnail }}" alt="thumbnail" width="150" height="100">
  <br />
  {% endif %}

  <p>{{ produk.description|truncatewords:25 }}...</p>

  <p><a href="{% url 'main:show_catalog' produk.id %}"><button>Details</button></a></p>
</div>

<hr>
```

###  Membuat halaman form untuk menambahkan objek model.
- buat forms.py yang berisi field pada model apa saja yang ingin diisi.
```
from django.forms import ModelForm
from main.models import Produk

class ProductForm(ModelForm):
    class Meta:
        model = Produk
        fields = ["price", "name", "description", "category", "thumbnail","is_featured"]
```
- Lalu buat fungsi pada views.py yang bernama create_listing yang mengimport `forms.py` lalu diroute ke /create-listing di `urls.py`
```
def create_listing(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
```
```
path('create-listing/', create_listing, name='create_listing'),
```
- halaman form saya buat pada `create_listing` yang inti isinya adalah form dari forms.py, dan ada `csrf_token` untuk mencegah CSRF attack. terakhir, ada tombol submit yang akan mengirim data form ke database lewat `views.py` lalu redirect ke `main.html`.

### Membuat halaman yang menampilkan detail dari setiap data objek model.
- buat dulu fungsi yang bernama show_catalog. Fungsi ini bisa mengambil objek dan routing ke `product_detail.html` di `views.py`. Lalu routing fungsi tersebut di `urls.py`.
```
def show_catalog(request, id):
    products = get_object_or_404(Produk, pk=id)
    products.increment_views()

    context = {
        'products': products
    }

    return render(request, "product_detail.html", context)
```
```
path('catalog/<str:id>/', show_catalog, name='show_catalog'),
```
- Lalu pada `product_detail.html`, tambahkan header untuk semua field yang ada di objek tersebut. 
- Ditambahkan  button untuk kembali ke halaman utama dengan href `main.html`.


## Screenshot 4 URL di Postman
- XML:  
![showxml](https://drive.google.com/uc?export=view&id=1DxTfioyXXgnpunl6mPvSomIlQ7Llcaai))

- JSON:  
![showjson](https://drive.google.com/uc?export=view&id=1ljKUa1BnFqqUTBCpuNcZEBL6dKd4YA3i)

- XMLByID:  
![showxmlById](https://drive.google.com/uc?export=view&id=1O3LCve4znddoCEvYG96x5ZYVXiP2mJbV)

- JSONByID:  
![showjsonById](https://drive.google.com/uc?export=view&id=178RQZIOIsjRjLPC6lmsl4lx21JZaWK0I)

# Tugas 4
## Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
- Django AuthencticationForm merupakan fungsi bawaan django yang digunakan dalam proses "login" oleh user, dilakukan dalam bentuk form berisi field username dan password. 
  Setelah selesai, fungsi tersebut akan mengembalikan objek "user" yang merupakan akun unik user. 
Kelebihan:
- Developer tidak perlu membuat form login baru, mudah dipakai, serta langsung terintegrasi dengan sistem django.
-
Kekurangan:
- Sangat sederhana dalam segi UI/UX. Hanya memperlihatkan field username dan password yang harus diisi yang terkesan cukup "barebones".
-

## Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
- Autentikasi = proses memverifikasi identitas suatu user/client.
- otorisasi = proses menentukan hak akses terhadap sesuatu user/client yang di ketahui.
- Django mengimplementasikan autentikasi dengan fungsi2 bawaan pada library `django.contrib.auth` yang berisi hal-hal seperti login, logout, dan authenticate.
- otorisasi di django dilakukan dengan fungsi-fungsi yang melihat apakah suatu user memiliki izin untuk suatu fungsi, seperti user.has.perm(). 
- ada jugadecorators seperti @login_required, yang hanya mengizinkan user yang sudah tersimpan untuk mengakses suatu fungsi.

## Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Session dan cookies berguna agar user tidak perlu login berkali-kali jika semisal user berpindah dari satu web ke lainnya.
Cookies:
- lebih mudah digunakan
- tidak aman
- ukuran terbatas
- jika data dicuri oleh penyerang, yang membuat penyerang tersebut bisa memiliki terhadap akun jika cookie tidak direset
Session:
- session lebih aman karena disimpan di server
- Session  hanya bertahan sampai user logout
- penyerang bisa mengambil akses session yang sedang berlangsung

##  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
- Cookies tidak selalu aman, karena sifat cookies yang disimpan secara lokal (pada sistem client/user), jadi jika developer menyimpan username atau password ataupun informasi penting lainnya, informasi tersebut bisa diambil melalui malware cookie stealer, XSS, dan CSRF. 
- Django membuat server-side session (Session ID). Sekarang informasi penting disimpan pada server dan cookie hanya menyimpan SessionID. Jadi semisal cookie yang ada di client dicuri, cookie tersebut hanya valid sampe session itu berakhir saja.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
###  Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
- import libary-libary y `django.contrib.auth` yang berisi fungsi-fungsi login, serta decoratornya. 
- Lalu buat fungsi register: 
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

```
- Fungsi ini akan membuat form register menggunakan `UserCreationForm` yang merupakan form bawaan django untuk penambahan use yang memiliki field Username dan Password. Fungsi ini akan dipanggil melalui /register.html
`register.html`  routing pada urls.py yang mengarah ke register.html. Html tersebut hanya berfungsi untuk menampilkan `UserCreationForm` dengan method `POST`.

- Lalu buat fungsi login :
```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```
- Fungsi dipanggil melalui /login, jadi buat dulu routingnya . Fungsi ini membuat form login dari `AuthenticationForm`, lalu fungsi akan mengambil user dan diteruskan ke fungsi login django `login(request, user)`. Setelah itu user bisa masuk ke website.
- Lalu buat page login dengan membuat login.html. Disini user bisa login dengan memasukkan kredensialnya, atau tersedia button yang memanggil page register. 
-  tambahkan decorator `@login_required(login_url='/login')` pada fungsi `show_main` dan `show_product` agar hanya user terdaftar yang bisa mengakses 2 fungsi tersebut, jika user belum terdaftar atau belum login, redirect ke page login.
  
- Lalu buat fungsi logout:
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
- Fungsi ini dipanggil melalui /logout, jadi tambahkan routing pada `urls.py` . Fungsi digunakan jika user ingin logout dengan cara memanggil logout(request) yang menghapus data session di server, lalu redirect ke halaman login. 
- Fungsi dapat dipanggil lewat main.html. Jadi saat user ingin logout, tekan button yang ada di page main.
- kode buttonnya seperti ini:
```
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```

###  Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
- Buat akun baru, lalu tambahkan product dengan isi field-field yang tersedia, repeat 3x.

###  Menghubungkan model Product dengan User.
- buat field user pada models. Lalu tambahkan bagian kode pada `views.py`, spesifiknya pada create_product:
```        
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
```
- Di bagian ini, field user akan diisi dengan user yang sedang terlogin pada saat ini, jadi membuat hubungan "one-to-many" antara user dengan product.

###  Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
- Pada main.html, ditambahkan:
```
<h5>Logged in as: {{ logged }}</h5>
<h5>Sesi terakhir login: {{ last_login }}</h5>
<hr>
```
- Potongan kode ini akan mengambil pengguna yang sedang logged dan waktu last_login user tersebut yang diambil dari context showmain pada `views.py` yang berisi seperti ini:
```
    context = {
        'npm' : '2406495590',
        'name': 'Arya Novalino Pratama',
        'class': 'PBP B'
        'logged': request.user.username,,
        'Aplikasi' : 'FootballShop',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
```
- Pada potongan kode tersebut, variabel logged diambil dari user yang sedang terlogin pada saat itu dan diambil usernamenya.
- Sedangkan last_login adalah variabel yang mengambil waktu last_login dari cookies, ketika variabel tersebut ada isinya, maka ambil isi tersebut. Jika tidak ada isi, maka tampilkan 'Never"



