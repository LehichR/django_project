from django.urls import path
from .views import index, top_sellers, new_ad

urlpatterns = [
    path('', index, name='/'),
    path('top', top_sellers, name='top'),
    path('post', new_ad),
]

