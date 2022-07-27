from django.shortcuts import redirect, render
from .models import Todo

# Create your views here.
def index(request):
    # print(request.method)
    if request.method =='POST':
        # print(request.POST['text'])
        text=request.POST['text']
        Todo.objects.create(item=text)
        return redirect('index')
    todos=Todo.objects.all()    
    context={'todos':todos}
    return render(request,'todo/index.html', context)

def delete(request,id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    # print(todo.item)
    # print('start')
    # print(id)
    # print('end')
    return redirect('index')

def check(request,id):
    todo=Todo.objects.get(id=id)
    todo.done=todo.strike() #strike method is to toggle the boolean done value
    todo.save(update_fields=['done'])
    return redirect('index')


