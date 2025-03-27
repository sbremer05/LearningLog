"""Defines URL patterns for learning_logs"""

from django.urls import path
from .import views

app_name = 'learning_logs'

urlpatterns = [
#     Home page
    path('', views.index, name = 'index'),

#     Page that shows all topics
    path('topics/', views.topics, name = 'topics'),

#     Detail page for a single topic
    path('topic/<int:topic_id>/', views.topic, name = 'topic'),

#     Page for adding a new topic
    path('new_topic/', views.new_topic, name = 'new_topic'),

#     Page for adding a new entry
    path('<int:topic_id>/new_entry/', views.new_entry, name = 'new_entry'),

#     Page for editing a topic
    path('<int:topic_id>/edit/', views.edit_topic, name = 'edit_topic'),

#     Page for editing an entry
    path('<int:topic_id>/<int:entry_id>/edit/', views.edit_entry, name = 'edit_entry'),

#     Page for deleting a topic
    path('<int:topic_id>/delete/', views.delete_topic, name = 'delete_topic'),

#     Page for deleting an entry
    path('<int:topic_id>/<int:entry_id>/delete/', views.delete_entry, name = 'delete_entry'),
]