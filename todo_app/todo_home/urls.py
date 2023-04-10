from django.urls import path
# from . import views as home_views
from .views import TaskListView,TaskCreateView,TaskUpdateView

urlpatterns=[
    # path('',home_views.home,name="todo-home"),
    path('',TaskListView.as_view(),name="todo-home"),
    path('create/',TaskCreateView.as_view(),name="todo-create"),
    path('update/<int:pk>',TaskUpdateView.as_view(),name="todo-update"),
]