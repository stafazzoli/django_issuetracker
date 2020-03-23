from django_tables2 import tables, TemplateColumn
from django.utils.html import format_html
from .models import Project
from django.db.models import F
import itertools


class ProjectTable(tables.Table):

    def render_row_number(self):
        self.row_number = getattr(self, 'row_number', itertools.count(self.page.start_index()))
        return next(self.row_number)

    def render_image(self, record):
        return format_html(f'<img src="{record.image.url}" style="width:30px;">')

    def render_issue_no(self, record):
        return record.issues.count()

    class Meta:
        model = Project
        attrs = {'class': 'table table-sm table-striped'}
        fields = ('row_number', 'image', 'name', 'category', 'create_date', 'created_by',)
        empty_text = 'No Projects Found.'

    row_number = tables.columns.Column(verbose_name='#', empty_values=(), orderable=False)
    image = tables.columns.Column(orderable=False)
    issue_no = tables.columns.Column(verbose_name='Issue No', empty_values=(), orderable=False)
    action = TemplateColumn(template_name='projects/_project_action_column.html', orderable=False)
