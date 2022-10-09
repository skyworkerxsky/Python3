from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

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

def new_topic(request):
    """ Определяет новую тему. """
    if request.method != 'POST':
        # Данные не отправлялись, создается пустая форма
        form = TopicForm()
    else:
        # Отправлены данные POST, обработать данные
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """ Добавляет новую запись по конкретной теме. """
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = EntryForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Вывести пустую или недействительную форму
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """ Редактирует существующую запись. """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Исходный запрос, форма заполняется данными текущей записи
        form = EntryForm(instance=entry)
    else:
        # Отправка данных POST, обработать данные
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
