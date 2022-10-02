import requests
from plotly.graph_objs import Bar
from plotly import offline

# Создание вызова API и сохранение ответа.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)

# Сохранение ответа API в переменной.
response_dict = r.json()

repo_dicts = response_dict['items']
stars, labels, repo_links = [], [], []

for repo_dict in repo_dicts:
    stars.append(repo_dict['stargazers_count'])

    # tooltip description
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner} <br />{description}"
    labels.append(label)

    # repo url
    name = repo_dict['name']
    url = repo_dict['html_url']
    repo_link = f"<a href='{url}'>{name}</a>"
    repo_links.append(repo_link)

# Построение визуализации.
data = {
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(197, 25, 230)',
        'line': {
            'width': 1,
            'color': 'rgb(25, 25, 25)'
        }
    },
    'opacity': 0.6,
}

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {
        'size': 28
    },
    'xaxis': {
        'title': 'Repository',
        'titlefont': {
            'size': 24
        },
        'tickfont': {
            'size': 12
        },
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {
            'size': 24
        },
        'tickfont': {
            'size': 12
        },
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')