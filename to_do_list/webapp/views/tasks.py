from django.shortcuts import redirect
from webapp.forms import TaskForm
from webapp.models import Tasks
from django.views.generic import TemplateView



class TaskCreateView(TemplateView):
    template_name = 'task_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = TaskForm
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            Tasks.objects.create(**form.cleaned_data)
            return redirect('index')
