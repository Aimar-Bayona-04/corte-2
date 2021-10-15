from django.http import HttpResponse
import datetime
from django.template import Template, Context

class persona(object):
    
    def __init__(self, nombre, apellido):

        self.nombre = nombre
        self.apellido = apellido


def hola(request): 

    obj = persona("Aimar", "Bayona Barrientos")
    doc_externo = open('C:/Users/AIMAR/Desktop/Universidad/semestre 5/Desarrollo orientado a plataformas/corte 2/Django/sitio/sitio/Plantillas/primer plantilla.html')
    plt = Template(doc_externo.read())
    fecha = datetime.datetime.now()
    nombre = "aimar"
    doc_externo.close()
    ctx = Context({"nombre_persona":obj.nombre, "apellido_persona":obj.apellido,"fecha":fecha})
    mensaje=plt.render(ctx)
 
    return HttpResponse(mensaje)
 
def fechaactual(request):
 fecha = datetime.datetime.now()
 mensaje = """
 <html>
 <body>
 <h5>
 fecha y hora actual %s 
 </h5>
 </body>
 </html>
 """ % fecha
 return HttpResponse(mensaje)
 
def calculaEdad(request, anio):
    edadActual = 19
    periodo = anio - 2021
    edadFutura = edadActual + periodo
    if edadFutura > edadActual:
     mensaje = """
     <html>
     <body>
     <h3>
     En el anio %s tendras %s años
     </h3>
     </body>
     </html>
     """ %(anio, edadFutura)
     return HttpResponse(mensaje)
    else:
     mensaje = """
     <html>
     <body>
     <h3>
     Desde el %s hasta este han pasado %s años
     </h3>
     </body>
     </html>
     """ %(anio, periodo)
     return HttpResponse(mensaje)