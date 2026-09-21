from django.conf import settings
from django.urls import path, re_path
from django.views.generic import RedirectView
from django.views.static import serve

# Les prototypes sont des pages HTML autonomes : on les sert telles quelles
# (pas de moteur de templates, leur JavaScript contient des accolades).
urlpatterns = [
    path('', RedirectView.as_view(url='/prototypes/hero-v1.html', permanent=False)),
    re_path(r'^prototypes/(?P<path>.*)$', serve, {'document_root': settings.PROTOTYPES_DIR}),
]
