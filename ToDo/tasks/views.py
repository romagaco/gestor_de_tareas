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
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView


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
class TaskDetailView(DetailView):
    template_name = "tasks/task.html"
    model = Task
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.task = self.get_object()  # Fix: Use 'task' instead of 'post'
            comment.save()
            messages.add_message(self.request, messages.SUCCESS, "Comentario añadido correctamente.")
            return HttpResponseRedirect(reverse('task_detail', args=[self.get_object().pk]))
        return self.get(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class TaskDeleteView(DeleteView):
    template_name = "tasks/task_delete.html"
    model = Task
    success_url = reverse_lazy('task_list')  # Redirect to task list, not home

    def get_object(self, queryset=None):
        task = super().get_object(queryset)
        if task.user != self.request.user:
            messages.add_message(self.request, messages.ERROR, "No tienes permiso para eliminar esta tarea.")
            return HttpResponseRedirect(reverse('task_list'))
        return task

    def delete(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, "Tarea eliminada correctamente.")
        return super().delete(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class TaskUpdateView(UpdateView):
    template_name = "tasks/task_update.html"
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('task_list')  # Redirect to task list

    def get_object(self, queryset=None):
        task = super().get_object(queryset)
        if task.user != self.request.user:
            messages.add_message(self.request, messages.ERROR, "No tienes permiso para editar esta tarea.")
            return HttpResponseRedirect(reverse('task_list'))
        return task

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Tarea actualizada correctamente.")
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class TaskListView(ListView):
    template_name = "tasks/task_list.html"
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user).order_by('-created_at')
        print(queryset)  # Verifica que las tareas se estén obteniendo correctamente
        return queryset