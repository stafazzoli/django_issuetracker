from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.api_root, name='root'),
    path('issues/', views.IssueCreateAPI.as_view(), name="create_issue"),
    path('issues/<int:pk>/', views.IssueDetailsView.as_view(), name="detail_issue"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
