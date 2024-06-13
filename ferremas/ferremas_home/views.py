from django.shortcuts import render

# Create your views here.
class persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        super().__init__()  

def index(request):

    hijo = persona("Juan Perez","8")

    lista = ["Lazaña","Charquican","Porotos"]
 
    context={"hijo":hijo,"nombre":"Claudia","comidas":lista}

    return render(request, 'ferremas_home/index.html',context)