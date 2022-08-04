from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import todo

# Create your views here.
def index(request):

    todos = todo.objects.all()

    if request.method=='POST':
        new_todo = todo(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/')

    return render(request,'index.html',{'todo':todos})

