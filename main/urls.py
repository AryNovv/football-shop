from django.urls import path
from main.views import show_main, create_listing, show_catalog,show_xml,show_json,show_xml_by_id, show_json_by_id,register,login_user,logout_user,edit_listing,delete_Listing,add_listing_entry_ajax,sort_listing_with_ajax,create_product_flutter, proxy_image

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-listing/', create_listing, name='create_listing'),
    path('catalog/<str:id>/', show_catalog, name='show_catalog'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('news/<uuid:id>/edit', edit_listing, name='edit_listing'),
    path('news/<uuid:id>/delete', delete_Listing, name='delete_Listing'),
    path('create-listing-ajax', add_listing_entry_ajax, name='add_listing_entry_ajax'),
    path('sort-listing-ajax', sort_listing_with_ajax, name='sort_listing_with_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('proxy-image/', proxy_image, name='proxy_image'),

]
