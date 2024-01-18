from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('show_records', views.show_records, name='show_records'),
    path('show_items', views.show_items, name='show_items'),
    path('add_record', views.add_record, name="add_record"),
    path('add_item', views.add_item, name='add_item'),
    path('llm', views.llm, name='llm'),
    path('llm2', views.llm2, name='llm2'),


]