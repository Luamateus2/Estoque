from django.shortcuts import render,redirect
from task.models import Produto
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao', '')
        preco_compra = request.POST.get('preco_compra')
        preco_venda = request.POST.get('preco_venda')
        quantidade_estoque = request.POST.get('quantidade_estoque')
        tamanho = request.POST.get('tamanho', '')
        cor = request.POST.get('cor', '')
        imagem = request.FILES.get('imagem')

        if not nome or not preco_compra or not preco_venda or not quantidade_estoque or not imagem:
            messages.error(request, "Todos os campos obrigatórios devem ser preenchidos.")
            return render(request, 'tasks/cadastrar_roupa.html')

        try:
            preco_compra = float(preco_compra)
            preco_venda = float(preco_venda)
            quantidade_estoque = int(quantidade_estoque)
        except ValueError:
            messages.error(request, "Os campos de preço e quantidade devem ser numéricos.")
            return render(request, 'tasks/cadastrar_roupa.html')

        produto = Produto(
            nome=nome,
            descricao=descricao,
            preco_compra=preco_compra,
            preco_venda=preco_venda,
            quantidade_estoque=quantidade_estoque,
            tamanho=tamanho,
            cor=cor,
            imagem=imagem
        )
        produto.save()
        return render(request,'tasks/cadastrar_roupa.html')

    return render(request, 'tasks/cadastrar_roupa.html')

@login_required
def roupa_views(request, pk):
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'tasks/descricao_roupa.html', context)

@login_required
def lista_produtos(request):
    produtos = Produto.objects.all().values('nome', 'imagem', 'descricao') 
    context = {
        'produtos': produtos
    }
    return render(request, 'tasks/index.html', context)
