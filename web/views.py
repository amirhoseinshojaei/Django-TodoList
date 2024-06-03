from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.


def index(request):

    item_list = Todo.objects.filter('-published_at')

    if request.method == 'POST':

        form = TodoForm(request.form)

        if form.is_valid:

            form.save()
            return redirect('todo')
        
    else:

        form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)
