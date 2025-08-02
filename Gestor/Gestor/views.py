from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import RegistrationForm, LoginForm
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.shortcuts import redirect

from Task.models import Task
from Task.forms import TaskForm
from User.models import Profile


class HomeView(TemplateView):
    template_name = "general/home.html"


class LoginView(FormView):
    template_name = "general/login.html"
    form_class = LoginForm

    def form_valid(self, form):
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=usuario, password=password)

        if user is not None:
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, f'Bienvenido de nuevo {user.username}')
            return HttpResponseRedirect(reverse('home'))

        else:
            messages.add_message(
                self.request, messages.ERROR, 'Usuario no válido o contraseña no válida')
            return super(LoginView, self).form_invalid(form)


class RegisterView(CreateView):
    template_name = "general/register.html"
    model = User
    success_url = reverse_lazy('login')
    form_class = RegistrationForm

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Usuario creado correctamente.")
        return super(RegisterView, self).form_valid(form)


class LegalView(TemplateView):
    template_name = "general/legal.html"


class ContactView(TemplateView):
    template_name = "general/contact.html"

@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Se ha cerrado sesión correctamente.")
    return HttpResponseRedirect(reverse('home'))


# Create your views here.
def task_list(request):  # Renamed from Task
    form = TaskForm()
    tasks = Task.objects.all()  # Now uses the Task model

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'tasks': tasks, 'TaskForm': form}
    return render(request, 'tasks/tasks.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'TaskForm': form, 'task': task}
    return render(request, 'tasks/update-task.html', context)


def deleteTask(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == 'POST':

        task.delete()

        return redirect('/')

    context = {'task': task}

    return render(request, 'tasks/delete-task.html', context)







@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = User
    template_name = "general/user_detail.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        return self.request.user


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = "general/profile_update.html"
    context_object_name = "profile"
    fields = ['bio', 'birth_date', 'first_name', 'last_name']


    def get_object(self, queryset=None):
        try:
            return self.request.user.profile
        except Profile.DoesNotExist:
            return Profile.objects.create(user=self.request.user)
    
    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Perfil editado correctamente.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile')