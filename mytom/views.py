from django.views.generic import TemplateView
from tom_targets.models import Target
from django.shortcuts import get_object_or_404, render

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        return {'targets': Target.objects.all()}

def targets(request, id):
    target = get_object_or_404(Target, id=id)
    return render(request, 'targets.html', {'target': target})

