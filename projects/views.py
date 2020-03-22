from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django_tables2 import SingleTableView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models
from . import tables


# Create your views here.
class ProjectCategoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.ProjectCategory
    fields = ('name',)


class ProjectCategoryDetailView(generic.DetailView):
    model = models.ProjectCategory


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Project
    fields = ('category', 'name', 'description', 'image')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user   # form.instance.created_by
        self.object.save()
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = models.Project
    fields = ('category', 'name', 'description', 'image')

    # Only the project creator can update the project
    def test_func(self):
        project = self.get_object()
        if self.request.user == project.created_by:
            return True
        return False


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = models.Project
    success_url = '/projects'

    # Only the creator can update the project
    def test_func(self):
        project = self.get_object()
        if self.request.user == project.created_by:
            return True
        return False


class ProjectListView(SingleTableView):
    model = models.Project
    table_class = tables.ProjectTable
    table_pagination = {
        "per_page": 5
    }


class ProjectDetailView(generic.DetailView):
    model = models.Project


class IssueCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Issue
    fields = ('title', 'priority', 'description', 'assignee', 'attachment')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.reporter = self.request.user
        self.object.project = get_object_or_404(models.Project, pk=self.kwargs['project_pk'])
        self.object.save()
        return super().form_valid(form)


class IssueDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Issue


class UserIssueListView(LoginRequiredMixin, generic.ListView):
    template_name = 'projects/user_issues.html'
    context_object_name = 'issues'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return models.Issue.objects.filter(assignee=user).order_by('-pk')


# TODO need fixing
class ProjectIssueListView(LoginRequiredMixin, generic.ListView):
    template_name = 'projects/project_issues.html'
    context_object_name = 'issues'
    # paginate_by = 5

    def queryset(self):
        return models.Issue.objects.filter(project_id=self.kwargs['project_pk'])


@login_required()
def issue_change_status(request, pk):
    issue = get_object_or_404(models.Issue, pk=pk)

    if request.method == 'POST':
        if 'IP' in request.POST:
            issue.status = 'IP'
        elif 'DN' in request.POST:
            issue.status = 'DN'
        elif 'CN' in request.POST:
            issue.status = 'CN'
        issue.save()

    return redirect('projects:issue_detail', pk=pk)
