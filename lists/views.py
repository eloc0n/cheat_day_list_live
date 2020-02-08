from django.shortcuts import render, redirect

from .models import *
from .forms import *

# Create your views here.
def index(request):
    lists = List.objects.all()
    form = ListForm()

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'lists': lists,
        'form': form,
    }
    
    return render(request, 'lists/index.html', context)


def updateList(request, pk):
    list = List.objects.get(id=pk)

    form = ListForm(instance=list)

    if request.method == 'POST':
        form = ListForm(request.POST, instance=list)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {
        'form':form,
    }

    return render(request, 'lists/update_list.html', context)


def deleteList(request, pk):
    item = List.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {
        'item':item,
    }

    return render(request, 'lists/delete.html', context)

