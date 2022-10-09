"""Определяет схемы URL для learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
      # Домашняя страница
      path('', views.index, name='index'),
      # Список тем
      path('topics', views.topics, name='topics'),
      # Страница с подробной информацией по отдельной теме
      path('topics/<int:topic_id>/', views.topic, name='topic'),
      # Страница для добавления новой темы
      path('new_topic/', views.new_topic, name='new_topic'),
      # Станица для добавления новой записи
      path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'), # Код <int:topic_id> захватывает числовое значение и сохраняет его в переменной topic_id
]