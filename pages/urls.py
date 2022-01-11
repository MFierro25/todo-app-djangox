from django.urls import path

from .views import AboutPageView, TodoListView, TodoDetailView, TodoCreateView, TodoDeleteView, TodoUpdateView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('about/', AboutPageView.as_view(), name='about'),
    path("<int:pk>/", TodoDetailView.as_view(), name='todo_detail'),
    path('create/', TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='todo_update'),
]
