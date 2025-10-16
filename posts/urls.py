from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import post_add, post_list

app_name = "posts"

urlpatterns = [    
    path("", post_list, name = "post_list"),
    path("add/", post_add, name= "post_add")
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
