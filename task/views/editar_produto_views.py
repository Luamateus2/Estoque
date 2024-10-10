from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from ..models import Produto  

def editar_produto(request,pk):
    produto = get_object_or_404(Produto, id=pk)

    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao', '') 
        produto.preco_compra = request.POST.get('preco_compra')
        produto.preco_venda = request.POST.get('preco_venda')
        produto.quantidade_estoque = request.POST.get('quantidade_estoque')
        produto.tamanho = request.POST.get('tamanho', '')  
        produto.cor = request.POST.get('cor', '')  

        if 'imagem' in request.FILES:
            produto.imagem = request.FILES['imagem']

        # Verificação de campos obrigatórios
        if not produto.nome or not produto.preco_compra or not produto.preco_venda or not produto.quantidade_estoque:
            messages.error(request, "Todos os campos obrigatórios devem ser preenchidos.")
            return render(request, 'tasks/editar_produto.html', {'produto': produto})

        try:
            produto.save()
            return redirect('home') 
        except Exception as e:
            messages.error(request, f"Ocorreu um erro ao salvar o produto: {e}")
            return render(request, 'tasks/editar_produto.html', {'produto': produto})
    return render(request, 'tasks/editar_produto.html', {'produto': produto})
