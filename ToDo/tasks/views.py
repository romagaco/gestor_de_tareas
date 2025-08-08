from django.views.generic.edit import CreateView
from tasks.models import Task
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from .forms import CommentCreateForm
from .forms import TaskCreateForm

from django.http import JsonResponse


@method_decorator(login_required, name='dispatch')
class TaskCreateView(CreateView):
    template_name = "tasks/task_create.html"
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, "Tarea creada correctamente.")
        return super(TaskCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class TaskDetailView(DetailView, CreateView):
    template_name = "tasks/task.html"
    model = Task
    context_object_name = 'task'
    form_class = CommentCreateForm

    def form_valid(self, form):
      form.instance.user = self.request.user
      form.instance.post = self.get_object()
      return super(TaskDetailView, self).form_valid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Comentario añadido correctamente.")
        return reverse('post_detail', args=[self.get_object().pk])


@method_decorator(login_required, name='dispatch')
class TaskDeleteView(CreateView):
    template_name = "tasks/task_delete.html"
    model = Task
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        if task.user != request.user:
            messages.add_message(request, messages.ERROR, "No tienes permiso para eliminar esta tarea.")
            return HttpResponseRedirect(reverse('home'))
        return super(TaskDeleteView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Tarea eliminada correctamente.")
        return super(TaskDeleteView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class TaskUpdateView(CreateView):
    template_name = "tasks/task_update.html"
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        if task.user != request.user:
            messages.add_message(request, messages.ERROR, "No tienes permiso para editar esta tarea.")
            return HttpResponseRedirect(reverse('home'))
        return super(TaskUpdateView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Tarea actualizada correctamente.")
        return super(TaskUpdateView, self).form_valid(form)
    

@method_decorator(login_required, name='dispatch')
class TaskListView(CreateView):
    template_name = "tasks/task_list.html"
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.get_queryset()
        return context