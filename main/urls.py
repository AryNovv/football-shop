from django.urls import path
from main.views import show_main, create_listing, show_catalog,show_xml,show_json,show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-listing/', create_listing, name='create_listing'),
    path('catalog/<str:id>/', show_catalog, name='show_catalog'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
]
