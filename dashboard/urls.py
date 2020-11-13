from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('message', views.create_message),
    path('comment/<int:post_id>', views.create_comment),
    path('<int:post_id>/delete', views.delete_mess),
    path('<int:comm_id>/delete_comm', views.delete_comm),
    path('<int:comm_id>/edit_comm', views.edit_comm),
    path('<int:post_id>/edit_mess', views.edit_mess),
    path('<int:post_id>/like', views.like),
    path('<int:post_id>/unlike', views.unlike)
]