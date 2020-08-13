from django.shortcuts import render
from django.template.loader import get_template, render_to_string
from weasyprint import HTML, CSS
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
import io

from django_datatables_view.base_datatable_view import BaseDatatableView
from cms.models import Person
from weasyprint import CSS, HTML
from django.template.loader import render_to_string


class IndexDatatableView(BaseDatatableView):
    model = Person 
    # この順番で表示される。
    columns = ['name', 'prefecture__name', 'age']

    def render_column(self, row, col):
        if col == 'prefecture__name':
            return row.prefecture.name
        return super().render_column(row, col)

    def prepare_results(self, qs):
        """PDF出力様に、ソートやフィルター後のquerysetを保持"""
        self.query_set_for_pdf = qs
        return super().prepare_results(qs)

    def render_to_response(self, context):
        """ output=pdfのクエリパラメータが存在するときPDFを出力"""
        if self._querydict.get('output', 0) == 'pdf':
            return self.create_pdf()
        return super().render_to_response(context)

    def get_dataset_for_pdf(self):
        return {
            'dataset': (
                    [person.name, person.prefecture.name, person.age]
                    for person in self.query_set_for_pdf
                )
        }

    def create_pdf(self):
        context = self.get_dataset_for_pdf()
        html_string = render_to_string(
                template_name='cms/pdf_template.html',
                context=context,
                request=self.request)
        stream = io.BytesIO()
        HTML(string=html_string).write_pdf(
                target=stream,
                stylesheets=[CSS('cms/static/css/pdf.css')])
        stream.seek(0)
        return FileResponse(
                stream, as_attachment=True, filename='test.pdf')
