from django.urls import path

from . import views

app_name = 'story'

urlpatterns = [
    path('create/', views.create_story, name='create'),
    path('read/<slug:slug>/', views.story_detail, name='detail'),
    path('delete/<int:pk>/', views.story_delete, name='delete'),
    path('change/<int:pk>/', views.change_story, name='change_story'),
    path('change/<int:pk>/chapter/add/',
         views.add_chapter, name='add_chapter'),
    path('<int:story_pk>/chapter/<int:chapter_pk>/update/',
         views.update_chapter, name='update_chapter'),
    path('<int:story_pk>/chapter/<int:chapter_pk>/delete/',
         views.delete_chapter, name='delete_chapter'),
    path('<slug:story_slug>/chapter/<int:chapter_pk>/',
         views.chapter_detail, name='chapter_detail'),
]
