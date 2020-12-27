from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import add_item

urlpatterns = [
    path('add_item', add_item, name='add_item')
]