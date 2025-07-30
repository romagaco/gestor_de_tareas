
from django.contrib import admin
from django.urls import path

from .views import HomeView, LoginView, RegisterView, ContactView, LegalView, logout_view
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('legal/', LegalView.as_view(), name='legal'),
    path("admin/", admin.site.urls),
]

