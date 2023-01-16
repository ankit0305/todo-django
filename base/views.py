from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
# def task_list(request):
#     return HttpResponse('Task list')

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
    
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    #field = ['title','description']
    success_url = reverse_lazy('tasks')
    
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    #field = ['title','description']
    success_url = reverse_lazy('tasks')
    
class TaskDelete(DeleteView):
    model = Task
    fields = '__all__'
    context_object_name = 'task'
    #field = ['title','description']
    success_url = reverse_lazy('tasks')  