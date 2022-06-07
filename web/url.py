from django.urls import path
from web import views as webviews
from web.views import index

urlpatterns = [
    path('', webviews.home, name='index'),
    path('index',index.as_view(), name='home' ),

]
