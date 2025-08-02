from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from .forms import CommentCreateForm
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


from django.http import JsonResponse



@method_decorator(login_required, name='dispatch')
class taskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    template_name = "tasks/tasks.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, "Tarea creada correctamente.")
        return super(taskCreateView, self).form_valid(form)


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



