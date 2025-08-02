
from django.contrib import admin
from django.urls import path


from .views import HomeView, LoginView, RegisterView, ContactView, LegalView, logout_view, ProfileDetailView, ProfileUpdateView
from django.conf.urls.static import static
from django.conf import settings
from . import views
from Task.views import taskCreateView




urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('legal/', LegalView.as_view(), name='legal'),
    path('admin/', admin.site.urls),
    path('user_detail/', ProfileDetailView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('tasks/create/', taskCreateView.as_view(), name="task_list"),
    path('tasks/update-task/<int:pk>/', views.updateTask, name="update-task"),
    path('tasks/delete-task/<int:pk>/', views.deleteTask, name="delete-task"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

