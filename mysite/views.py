from django.views import generic
from projects.models import Project, Issue


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['issues'] = Issue.objects.all()
        return context
