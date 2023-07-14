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
    path('live_data/', views.live_data, name='live_data'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
    path('my-url/', my_view, name='my_view')
]


