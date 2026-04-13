from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Artigo, Comentario
from .forms import ComentarioForm

def artigo_list(request):
    artigos = Artigo.objects.all()
    return render(request, 'noticias/artigo_list.html', {'artigos': artigos})

def artigo_detail(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    return render(request, 'noticias/artigo_detail.html', {'artigo': artigo})

def comentarios_view(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    comentarios = artigo.comentarios.all().order_by('-data_criacao')
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.save()
            messages.success(request, '✅ Comentário publicado com sucesso!')
            return redirect('noticias:comentarios', pk=artigo.pk) 
    else:
        form = ComentarioForm()
    
    return render(request, 'noticias/comentarios.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form': form,
    })