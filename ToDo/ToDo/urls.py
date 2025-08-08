
from django.contrib import admin
from django.urls import path


from .views import HomeView, LoginView, RegisterView, logout_view, ProfileDetailView, ProfileUpdateView, CalendarView
from django.conf.urls.static import static
from django.conf import settings
from . import views
from tasks.views import TaskDetailView, TaskCreateView, TaskDeleteView, TaskUpdateView, TaskListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('my_profile/', ProfileDetailView.as_view(), name='my_profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('task/', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


