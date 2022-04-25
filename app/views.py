from django.shortcuts import render, redirect
from app.forms import cadastroForm, movimentoForm
from app.models import cadastro, movimento
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    data = {}
    all = cadastro.objects.all()
    paginator = Paginator(all, 5)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)


def form(request):
    data = {'form': cadastroForm()}
    return render(request, 'form.html', data)


def create(request):
    form = cadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = movimentoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('relatorio')

        context = {'form': form}
        return render(request, 'moveform.html', context)


def edit(request, pk):
    data = {'db': cadastro.objects.get(pk=pk)}
    data['form'] = cadastroForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {'db': cadastro.objects.get(pk=pk)}
    form = cadastroForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = cadastro.objects.get(pk=pk)
    db.delete()
    return redirect('home')


def relatorio(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = movimento.objects.filter(idcontainer__idContainer__contains=search)
    else:
        data['db'] = movimento.objects.all()
    return render(request, 'relatorio.html', data)


def moveform(request):
    data = {'form': movimentoForm()}
    return render(request, 'moveform.html', data)

