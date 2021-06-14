import os
from django.conf import settings
from django.contrib.staticfiles.views import serve


# Create your views here.
def serve_index(request):
    return serve(request, 'mkdocs_build/index.html')


def serve_docs(request, path):
    path = os.path.join(settings.DOCS_STATIC_NAMESPACE, path)
    return serve(request, path.replace('\\', '/'))
