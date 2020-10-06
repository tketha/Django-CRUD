from django.shortcuts import render,redirect
from .models import TodoModel

def todoview(request):
    mytodo = TodoModel.objects.all()
    return render(request, 'todoapp/homepage.html', {'mytodos':mytodo})

def addtask(request):
    mytask = request.POST['task']
    TodoModel(task = mytask).save()
    return redirect(request.META['HTTP_REFERER'])

def deletetask(request,taskpk):
    TodoModel.objects.filter(id = taskpk).delete()
    return redirect(request.META['HTTP_REFERER'])

def edittaskview(request,taskpk):
    return render(request, 'todoapp/edittask.html',{'todopk':taskpk})

def edit(request,taskpk):
    usertask = request.POST['task']
    todo = TodoModel.objects.get(id = taskpk)
    todo.task = usertask
    todo.save()
    return redirect('homepage')

