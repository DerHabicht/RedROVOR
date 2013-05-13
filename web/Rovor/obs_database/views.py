# Create your views here.

from django.http import HttpResponse, Http404

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie


from redrovor import obsRecord
from dirmanage.toolset import process_path

import logging

logger = logging.getLogger('Rovor')


@login_required
@ensure_csrf_cookie
def upload_form(request):
    '''form fo uploading observation from a folder on the server''' 
    return render(request,'obs_database/upload_form.html')


@login_required
def processFolder(request):
    def procFunc(path):
        return '{"ok":true}'
    return process_path(request, procFunc)
    

