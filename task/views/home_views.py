from django.shortcuts import render
from task.models import Produto



def home(request):
    produtos = Produto.objects.all()
    context = {

        'produtos': produtos
    }
    return render(request, 'tasks/index.html', context)