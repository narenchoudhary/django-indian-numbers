from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'test/$', TemplateView.as_view(template_name='app/test.html'),
        name='test'),
    url(r'^$', TemplateView.as_view(template_name='app/demo.html'),
        name='demo'),    
]
