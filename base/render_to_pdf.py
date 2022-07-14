#  Authors: 
#  Franyelyn Rodríguez
#  Christopher Gedler <cgedler@gmail.com>
#  File name: views.py
#  Version: 1.0
#  Last Change: 29.06.2022 21:07:30 -04
#  Description: Utilitario para PDF

# Imports base para el sistema:
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    #This part will create the pdf.
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding='UTF-8')
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class PdfResponseMixin(object, ):
    def write_pdf(self, file_object, ):
        context = self.get_context_data()
        template = self.get_template_names()[0]
        generate_pdf(template, file_object=file_object, context=context)
    def render_to_response(self, context, **response_kwargs):
        resp = HttpResponse(content_type='application/pdf')
        self.write_pdf(resp)
        return resp


class CoverPdfResponseMixin(PdfResponseMixin, ):
    cover_pdf = None
    def render_to_response(self, context, **response_kwargs):
        merger = PdfFileMerger()
        merger.append(open(self.cover_pdf, "rb"))
        pdf_fo = StringIO.StringIO()
        self.write_pdf(pdf_fo)
        merger.append(pdf_fo)
        resp = HttpResponse(content_type='application/pdf')
        merger.write(resp)
        return resp
