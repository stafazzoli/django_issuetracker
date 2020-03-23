from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.FilteredProjectListView.as_view(), name='all'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='detail'),
    path('new/', views.ProjectCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.ProjectUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='delete'),

    path('category/new/', views.ProjectCategoryCreateView.as_view(), name='create_category'),
    path('category/<int:pk>/', views.ProjectCategoryDetailView.as_view(), name='category_detail'),

    path('<int:project_pk>/issue/new/', views.IssueCreateView.as_view(), name="create_issue"),
    path('issue/<int:pk>/', views.IssueDetailView.as_view(), name="issue_detail"),
    path('<int:project_pk>/issues/', views.ProjectIssueListView.as_view(), name="project_issues"),
    path('user/<str:username>/issues/', views.UserIssueListView.as_view(), name="user_issues"),

    path('issue/<int:pk>/changestatus/', views.issue_change_status, name="change_status"),
]
