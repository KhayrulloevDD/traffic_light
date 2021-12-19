from django.urls import path
from company import apis

urlpatterns = [
    path('get_all', apis.get_all, name='get_all'),
]