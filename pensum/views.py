from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import GradoForm
from pensum.models import Grado, Seccion, Materia


def pensum_nuevo(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(
            nombre = formulario.cleaned_data['nombre'])
            for materia_id in request.POST.getlist('materias'):
                seccion = Seccion(materia_id=materia_id, grado_id = grado.id)
                seccion.save()
            messages.add_message(request, messages.SUCCESS, 'Exito.')
            return redirect('pensum_lista')
    else:
        formulario = ClienteForm()
    return render(request, 'pensum/pensum_nuevo.html', {'formulario': formulario})
