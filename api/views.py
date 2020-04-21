from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated
from . import serializers
from .permissions import IsReporter
from projects.models import Issue


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'issues': reverse('api:create_issue', request=request, format=format),
    })


class IssueCreateAPI(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing issues.

    post:
    Create a new issue instance.
    """
    queryset = Issue.objects.all()
    serializer_class = serializers.IssueSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        # saves the user as 'reporter' of the issue
        serializer.save(reporter=self.request.user)


class IssueDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    retrieve:
    Return the given issue.

    update:
    Updates the given issue.

    destroy:
    Deletes the given issue.
    """
    queryset = Issue.objects.all()
    serializer_class = serializers.IssueSerializer
    permission_classes = (IsAuthenticated, IsReporter,)
