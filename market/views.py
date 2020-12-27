from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AddItemForm
from .models import Item

# Create your views here.
def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('Successfully uploaded')
    else:
        form = AddItemForm()
    return render(request, 'add_item.html', {'form': form})

def success(request):
    return HttpResponse('Successfully uploaded')