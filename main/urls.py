from django.urls import path
from main.views import show_main, create_listing, show_catalog

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-listing/', create_listing, name='create_listing'),
    path('catalog/<str:id>/', show_catalog, name='show_catalog'),
]
