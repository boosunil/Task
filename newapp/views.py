from django.shortcuts import render, redirect
from django.http import HttpResponse
from newapp.models import Student
from newapp.forms import StudentForm
from django.views.generic import CreateView

# Create your views here.


def home(request):
    datas = Student.objects.all()
    context = {'datas': datas}
    return render(request, 'newapp/home.html', context)


def create(request):
    datas = Student.objects.all()
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form': form, 'datas': datas}
    return render(request, 'newapp/create.html', context)


def update(request, pk):
    datas = Student.objects.get(id=pk)
    form = StudentForm(instance=datas)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=datas)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form': form, 'datas': datas}
    return render(request, 'newapp/update.html', context)


def delete(request, pk):
    item = Student.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    context = {'item': item}
    return render(request, 'newapp/delete.html', context)
