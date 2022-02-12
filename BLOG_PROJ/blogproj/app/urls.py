from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', views.blog_content, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_profile_page, name='profile'),
    path('delete/<str:id>/', views.blog_delete, name='delete'),
    path('create/', views.create_blog, name='create'),
    path('edit/<str:id>/', views.edit_blog, name='edit'),
    path('like/<int:pk>/', views.like_view, name='like_post'),
    path('singleblog/<int:pk>/', views.single_blog, name='single_blog'),
    path('comment/<int:pk>/', views.add_comment, name='comment_blog'),
    path('reply/<int:post_pk>/<int:comment_pk>/', views.add_reply, name='reply'),
    path('results/', views.search_results, name='results_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

