from rest_framework import serializers
from projects.models import Issue


class IssueSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    reporter = serializers.ReadOnlyField(source='reporter.username')

    class Meta:
        model = Issue
        fields = ('id', 'title', 'description', 'priority', 'project', 'reporter', 'assignee')
        read_only_fields = ('create_date', 'update_date', 'reporter')
