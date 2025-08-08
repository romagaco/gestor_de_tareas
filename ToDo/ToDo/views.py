from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import ListView

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import RegistrationForm
from profiles.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm

class HomeView(TemplateView):
    template_name = "general/Homepage.html"


class CalendarView(TemplateView):
    template_name = "profiles/calendar.html"


class LoginView(FormView):
    template_name = "general/login.html"
    form_class = AuthenticationForm  # Add this
    success_url = '/tasks/'  # Fallback URL if my_profile fails

    def form_valid(self, form):
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=usuario, password=password)

        if user is not None:
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, f'Bienvenido de nuevo {user.username}')
            return HttpResponseRedirect(reverse('my_profile'))
        else:
            messages.add_message(
                self.request, messages.ERROR, 'Usuario no válido o contraseña no válida')
            return super().form_invalid(form)


class RegisterView(CreateView):
    template_name = "general/register.html"
    model = User
    success_url = reverse_lazy('login')
    form_class = RegistrationForm

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Usuario creado correctamente.")
        return super(RegisterView, self).form_valid(form)


@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Se ha cerrado sesión correctamente.")
    return HttpResponseRedirect(reverse('home'))



@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = User
    template_name = "profiles/my_profile.html"
    context_object_name = "profile"

    def get_object(self):
        return self.request.user

    def get_initial(self):
        self.initial['profile_pk'] =  self.get_object().pk
        return super().get_initial()
    
    def get_success_url(self):
        return reverse('profile_detail', args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


class ProfileListView(ListView):
    model = UserProfile
    template_name = "profiles/profile_list.html"
    context_object_name = "profiles"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return UserProfile.objects.all().order_by('user__username').exclude(user=self.request.user)
        return UserProfile.objects.all().order_by('user__username')


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = UserProfile
    template_name = "profiles/profile_update.html"
    context_object_name = "profile"
    fields = ['profile_picture', 'bio', 'birth_date']


    def dispatch(self, request, *args, **kwargs):
        user_profile = self.get_object()
        if user_profile.user != self.request.user:
            return HttpResponseRedirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Perfil editado correctamente.")
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('profile_detail', args=[self.object.pk])
    
