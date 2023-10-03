from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import itemForm,editForm

from .models import  category,items

def itemss(request):
    q = request.GET.get('searchItem', '')
    cat = request.GET.get('cat', '')
    
    catis = category.objects.all()
    itemss = items.objects.filter(isSold=False)
    if cat:
        itemss = items.objects.filter(itemCategory=cat)
    if q:
        itemss = items.objects.filter(name__contains=q)
            
    return render(request, "item/items.html" ,{
        "i": itemss,
        "ccc" : catis,
        "b": cat
    })
def detail(request,pk):
    i = get_object_or_404(items, pk=pk)
    ri = items.objects.filter(itemCategory=i.itemCategory).exclude(pk=pk)
    return render(request, "item/detail.html", {
        "ii" : i,
        "ri": ri
    })

@login_required
def addI(request):
    if request.method == "POST":
        form = itemForm(request.POST, request.FILES)
        if form.is_valid():
            i  = form.save(commit=False)
            i.createdBy = request.user
            i.save()
            return redirect('items:detail', pk=i.id)
    else: 
        form = itemForm()   
    return render(request, "item/from.html", {
        "formm" : form,
        "title" : "add item"
    })
@login_required
def editI(request, pk):
    i = get_object_or_404(items, pk=pk, createdBy=request.user)
    if request.method == "POST":
        form = editForm(request.POST, request.FILES, instance=i)
        if form.is_valid():
            form.save()
            return redirect('items:detail', pk=i.id)
    else: 
        form = editForm(instance=i)   
    return render(request, "item/from.html", {
        "formm" : form,
        "title" : "edit item"
    })

@login_required
def delete(request, pk):
    iToDel = get_object_or_404(items, pk=pk, createdBy=request.user)
    iToDel.delete()
    return redirect("dashboard:index")