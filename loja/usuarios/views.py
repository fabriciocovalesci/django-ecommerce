from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, resolve_url
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import UpdateView
from loja.produtos.models import Produto
from loja.usuarios.forms import AddProduto, CompraProduto


def home(request):
    return render(request, 'base.html')

    
class Login(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'



def produtos(request):
    prod = Produto.objects.all()
    return render(request, 'listaProduto.html', {"prod":prod})


def produtos_detalhe(request, pk):
    prod = get_object_or_404(Produto, pk=pk)
    return render(request, 'produtos_detalhe.html', {"prod": prod})


@login_required()
def cadastrar_produto(request):
    if request.method == "POST":
        form = AddProduto(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.author = request.user
            prod.created_date = timezone.now()
            prod.save()
            return redirect('produtos_detalhe', pk=prod.pk)
    else:
        form = AddProduto()
        return render(request, "add_produto.html", {"form": form})
        

@login_required()
def produto_editar(request, pk):
    prod = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = AddProduto(request.POST, instance=prod)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.author = request.user
            prod.created_date = timezone.now()
            prod.save()
            return redirect('finalizando_compra', pk=prod.pk)
    else:
        form = AddProduto(instance=prod)
    return render(request, "compra2.html", {"form":form})

@login_required()
def compra_produto(request, pk):
    prod = get_object_or_404(Produto, pk=pk)
    messages.add_message(request, messages.INFO, 'Comprando')
    return render(request, 'compra_produto.html', {"prod":prod})

@login_required()
def compra_produto_form(request, pk):
    prod = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = CompraProduto(request.POST)
        if form.is_valid():
            nome_produto = form.cleaned_data['nome_produto']
            qtde_solicitada = form.cleaned_data['qtde_solicitada']
            total_pagar = form.cleaned_data['total_pagar']
            form.save()
            return redirect('finalizando_compra',{"form": form}, pk=prod.pk)
    else:
        form = CompraProduto()
        return render(request, "compra2.html", {"form": form})


def finalizando_compra(request, pk):
    prod = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = AddProduto(request.POST, instance=prod)
        if form.is_valid():
            prod.nome_produto = form.cleaned_data['nome_produto']
            prod.quantidade = form.cleaned_data['qtde_solicitada']
            prod.total_pagar = form.cleaned_data['total_pagar']
            prod.save()
            return redirect('finalizando_compra', {"prod":prod})
    else:
        return render(request, 'finaliza_compra.html', {"prod":prod})