from django.urls import path
from.import views
from django.views.generic import RedirectView
from .views import my_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name="index"),
    path('signup.html', views.signup, name="signup"),
    path('login.html', views.loginn, name="login"),
    path('live_data.html', views.live_data, name='live_data'),
    path('live_data/', views.live_data, name='live_data'),
    path('options/live_data.html', views.live_data, name='live_data'),
    path('options/', views.cards, name='cards'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
    path('my-url/', my_view, name='my_view'),
    path('live_data1.html', views.live_data1, name='live_data1'),
    path('options/live_data1.html', views.live_data1, name='live_data1'),
    path('live_data1/', views.live_data1, name='live_data1'),
    path('live_data2.html', views.live_data2, name='live_data2'),
    path('options/live_data2.html', views.live_data2, name='live_data2'),
    path('live_data2/', views.live_data2, name='live_data2'),
]