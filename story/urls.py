from django.urls import path

from . import views

app_name = 'story'

urlpatterns = [
    path('create/', views.create_story, name='create'),
    path('read/<slug:slug>/', views.story_detail, name='detail'),
    path('delete/<int:pk>/', views.story_delete, name='delete'),
    path('change/<int:pk>/', views.change_story, name='change_story'),
    path('update/<int:pk>/chapter/add/', views.add_chapter, name='add_chapter'),
    path('<int:story_pk>/chapter/<int:chapter_pk>/update/',
         views.update_chapter, name='update_chapter'),
]
