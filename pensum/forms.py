from django import forms
from .models import Materia, Grado

class GradoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Grado
        fields = ('nombre','materias')

def __init__ (self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["materias"].help_text = "Ingrese Materias"
        self.fields["materias"].queryset = Materia.objects.all()

#class FacturaForm(forms.ModelForm):
#todos los campos de Pelicula
    #class Meta:
        #model = Cliente
        #fields = ('nit', 'nombre', 'apellido', 'direccion', 'email', 'telefono')
