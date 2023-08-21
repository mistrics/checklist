from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def list(request):
    user = request.user
    checklist_instances = user.checklist_instances.all()
    return render(request, 'checklist/list.html', {
        'checklist_instances': checklist_instances
    })