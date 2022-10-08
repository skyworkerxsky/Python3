from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """ Домашняя страница приложения Learning Log """
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ Выводит список тем. """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ Выводит тему и все её записи """
    topic = Topic.objects.get(id=topic_id) # функция get() используется для получения темы
    entries = topic.entry_set.order_by('-date_added') # Загружаются записи, связанные с данной темой, и они упорядочиваются по значению date_added: знак «минус» перед date_added сортирует результаты в обратном порядке,
    context = {'topic': topic, 'entries': entries} # Тема и записи сохраняются в словаре context
    return render(request, 'learning_logs/topic.html', context)