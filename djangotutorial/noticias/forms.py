from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Escreve o teu comentário aqui...',
                'class': 'form-control'
            })
        }
        labels = {
            'texto': 'Novo comentário'
        }