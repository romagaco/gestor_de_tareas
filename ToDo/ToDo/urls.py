
from django.contrib import admin
from django.urls import path


from .views import HomeView, LoginView, RegisterView, ContactView, LegalView 
from .views import logout_view, ProfileDetailView, ProfileUpdateView, CalendarView
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import TaskView, TaskListView, taskCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('my_profile/', ProfileDetailView.as_view(), name='my_profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('calendar/', CalendarView.as_view(), name='register'),
    path('task/<int:pk>', TaskView.as_view(), name="task_list"),
    path('task/task_list/<int:pk>', TaskListView.as_view(), name="task_list"),
    path('tasks/create/', taskCreateView.as_view(), name="task_create"),
    path('tasks/update-task/<int:pk>/', views.updateTask, name="update-task"),
    path('tasks/delete-task/<int:pk>/', views.deleteTask, name="delete-task"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)