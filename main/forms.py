from django.forms import ModelForm
from main.models import Produk

class ProductForm(ModelForm):
    class Meta:
        model = Produk
        fields = ["price", "name", "description", "category", "thumbnail","is_featured"]