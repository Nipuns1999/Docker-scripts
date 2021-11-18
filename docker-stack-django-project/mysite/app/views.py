from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoItem

# Create your views here.

def myView(request):
    return HttpResponse("hello, World ahhh")

#showing data function 
def showData(request):
    data_items = ToDoItem.objects.all()
    return render(request, 'hello.html', {'items': data_items})

#add data function 
def addData(request):
    name = request.POST['content']
    new_item = ToDoItem(content= name)
    new_item.save()
    return HttpResponseRedirect('/')

#delete data function 
def deleteData(request, todo_id):
    item_to_delete  = ToDoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')
# Create your views here.
