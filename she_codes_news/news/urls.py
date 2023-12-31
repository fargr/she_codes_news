from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('author/<str:username>', views.AuthorView.as_view(), name='profile'),
    path('edit/<int:pk>', views.UpdateStoryView.as_view(), name='update'),
    # path('<int:pk>/delete', views.DeleteStoryView.as_view(), name='delete'),

]