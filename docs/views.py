import os
from django.conf import settings
# from django.contrib.staticfiles.views import serve
from django.views.static import serve


def serve_docs(request, path):
    docs_path = os.path.join(settings.DOCS_DIR, path)

    if os.path.isdir(docs_path):
        path = os.path.join(path, 'index.html')

    path = os.path.join(settings.DOCS_DIR, path)
    # conver windows path to unix path
    path = path.replace('\\', '/')
    return serve(request, path, settings.DOCS_DIR)
