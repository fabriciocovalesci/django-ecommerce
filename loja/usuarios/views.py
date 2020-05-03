from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect, resolve_url
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import UpdateView
from loja.produtos.models import Produto, CompraEfetuada
from loja.usuarios.forms import AddProduto, CompraProduto
from django.views.generic import TemplateView
from django.http import JsonResponse
from django_ajax.decorators import ajax
import json


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


def finalizando_compra(request):
    return render(request, 'finaliza_compra.html')


def add_carrinho(request):
    produto =  CompraEfetuada.objects.all()
    response_data = {}

    if  request.POST.get('action') == 'post':
        total_paga = request.POST.get('total')
        quantidade = request.POST.get('quantidade')

        quantidade = int(quantidade) # parseado de str para int
     
        total_paga = total_paga[3:] # removendo letras, espaços e caracteres especiais
        total_paga = float(total_paga) # parseado de str para float
  
        response_data['total_paga'] = total_paga
        response_data['quantidade'] = quantidade
        print(response_data)

        CompraEfetuada.objects.create(
            quantidade = quantidade,
            preco = total_paga,
        )

        return JsonResponse(response_data)
        
    
    return render(request, 'finaliza_compra.html', {'produto':produto})     

  