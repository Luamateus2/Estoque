from django.shortcuts import render
from task.models import Produto
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    produtos = Produto.objects.all()
    context = {

        'produtos': produtos
    }
    return render(request, 'tasks/index.html', context)