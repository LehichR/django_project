from django.urls import path
from .views import index, top_sellers, new_ad, register, user, auth

urlpatterns = [
    path('', index, name='/'),
    path('top', top_sellers, name='top'),
    path('new_ad', new_ad, name='post'),
    path('register', register, name='reg'),
    path('user', user, name='us'),
    path('log', auth, name='log'),
]

