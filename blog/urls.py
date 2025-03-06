from . import views
from django.urls import path

urlpatterns = [
    # assigns a view called PostList to the root URL. name='home' is the name of the URL that will be used to identify the view
    path('', views.PostList.as_view(), name='home'),
    # assigns a view called post_detail to the slug URL. name='post_detail' is the name of the URL that will be used to identify the view
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    # assigns a view called comment_edit to the slug URL. name='comment_edit' is the name of the URL that will be used to identify the view
    path('<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),

]