from django.urls import path
from web import views as webviews


urlpatterns = [
    path('', webviews.home, name='home'),
    path('id', webviews.home_id, name='home_id'),
]
