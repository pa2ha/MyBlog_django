from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/<slug:category_slug>/', views.CategoryPosts.as_view(),
         name='category_posts'),
    path('profile/<username>/', views.Profile.as_view(), name='profile'),
    path('profile/<int:pk>/edit/',
         views.EditProfile.as_view(), name='edit_profile'),
    path('posts/create/', views.CreatePost.as_view(), name='create_post'),
    path('posts/<int:pk>/edit/', views.EditPost.as_view(), name='edit_post'),
    path('posts/<int:pk>/delete/',
         views.DeletePost.as_view(), name='delete_post'),
    path('<int:pk>/comment/', views.AddComment.as_view(), name='add_comment'),
    path('posts/<int:post_id>/edit_comment/<int:pk>/',
         views.EditComment.as_view(), name='edit_comment'),
    path('posts/<int:post_id>/delete_comment/<int:pk>/',
         views.DeleteComment.as_view(), name='delete_comment')
]
