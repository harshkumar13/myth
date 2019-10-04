from django.urls import path, include
from .views import AboutView, targets

urlpatterns = [
    path('', include('tom_common.urls')),
    path('about/', AboutView.as_view(template_name='about.html'), name='about'),
    path('about/<id>/',targets,name='targets')
]

