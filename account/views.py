import os
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings

# Create your views here.


def download_resume(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type='application/resume')
            response['Content-Disposition'] = 'inline;filename=' + \
                os.path.basename(file_path)
            return response
    raise Http404
