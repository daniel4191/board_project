from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [    
    path("", views.post_list, name = "post_list"),
    path("add/", views.post_add, name= "post_add"),
    path("<int:pk>/", views.post_detail, name = "post_detail"),
    path("<int:pk>/edit/", views.post_edit, name = "post_edit"),
    path("<int:pk>/delete/", views.post_delete, name = "post_delete"),
    path("comment/<int:pk>/edit/", views.comment_edit, name = "comment_edit"),
    path("comment/<int:pk>/delete/", views.comment_delete, name = "comment_delete")
]