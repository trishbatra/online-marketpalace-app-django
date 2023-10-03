from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from items.models import items 
# Create your views here.
@login_required
def index(request):
    ii = items.objects.filter(createdBy = request.user)
    return  render(request, "dashboard/index.html", {
        "iii": ii
    })
@login_required
def delete(request, pk):
    iToDel = get_object_or_404(items, pk=pk, createdBy=request.user)
    iToDel.delete()
    return redirect("dashboard:index")