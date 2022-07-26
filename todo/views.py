from django.shortcuts import render

# Create your views here.
todos=[]

def index(request):
    # print(request.method)
    if request.method =='POST':
        # print(request.POST['text'])
        todos.append(request.POST['text'])
        context={'todos':todos}
        return render(request,'todo/index.html',context)
    
    context={'todos':todos}
    return render(request,'todo/index.html', context)
