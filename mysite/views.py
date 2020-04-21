from django.shortcuts import render
from django.views import generic
from projects.models import Project, Issue


class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()[:10]
        context['issues'] = Issue.objects.all()[:10]
        return context
