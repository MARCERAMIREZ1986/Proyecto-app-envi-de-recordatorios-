from django import forms
from .models import Cliente, Cita


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields='__all__'

class CitaForm(forms.ModelForm):
    
    fecha_cita = forms.DateTimeField(
        # Agregamos %Y-%m-%dT%H:%M que es el formato estándar de los navegadores
        input_formats=['%Y-%m-%dT%H:%M', '%Y-%m-%d %H:%M:%S', '%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control' # Opcional: para estilos CSS
            }
        )
    )

    class Meta:
        model = Cita
        fields = '__all__'