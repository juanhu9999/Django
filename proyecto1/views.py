from django.http import HttpResponse
from django.template import Template, Context, loader #este ultimo sirve para cargar plantillas

def saludo(request):
    return HttpResponse("hola")

def probandotemplate (request):

    ### varias para al template1

    nombre = "Juan"
    apellido = "Isabella"

    lista = (2,3,4,5)

    dicc = {"nombre": nombre, "apellido": apellido, "lista": lista}
    
    mihtml = open (r"C:\Users\juan.isabella\Desktop\ProyectoPythonClone\Djiango\proyecto1\plantillas\templates1.html")

    plantilla = Template(mihtml.read())

    mihtml.close()

    miContexto = Context(dicc)

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

def cargadores(request):

    var_uno = "juan"
    var_dos = "Isabella"

    contexto = {"nombre": var_uno, "apellido": var_dos}

    plantilla = loader.get_template("template2.html")

    documento = plantilla.render(contexto)

    return HttpResponse(documento)