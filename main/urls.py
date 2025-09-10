from django.urls import path
from main.views import show_main, create_news, show_news, show_json, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-news/', create_news, name='create_news'),
    path('news/<str:id>/', show_news, name='show_news'),
    path('json/', show_json, name='show_json'),
    path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
]