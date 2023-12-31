
from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
layout="""
    <h1> Proyecto Web (LP3) | Jefferson Justo </h1>
<hr/>
<ul>
<li>
<a href="/inicio"> Inicio</a>
</li>
<li>
<a href="/saludo"> Mensaje de Saludo</a>
</li>
<li>
<a href="/rango"> Mostrar Números [a,b]</a>
</li>
<li>
<a href="/rango2/15/30"> Mostrar Números [15,30]</a>
</li>
</ul>
<hr/>
"""
def index(request):
    estudiantes = [ 'Isabella Caballero', 
                    'Alejandro Hermitaño',
                    'Joan Palomino',
                    'Pierre Bernaola']

    #Para que este vacio
    #estudiantes = []

    return render(request, 'index.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto web con DJango',
        'estudiantes': estudiantes
    })

def saludo(request):
    return render(request, 'saludo.html',{
        'titulo':'Saludo',
        'autor_saludo':'Ing. Jefferson Daniel Justo Geri'
    })

def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a,b+1)
    return render(request,'rango.html',{
        'titulo':'Rango',
        'a':a,
        'b':b,
        'rango_numeros':rango_numeros
    })

    resultado =f"""
        <h2>Números de [{a},{b}]</h2>
        Resultado: <br>
        <ul>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
    resultado +="</ul>"
    return HttpResponse(layout+resultado)

def rango2(request,a=0,b=100):
    if a>b:
        return redirect('rango2',a=b, b=a)
    resultado1 = f"""
        <h2> Números de [{a},{b}] </h2>
        Resultado: <br>
        <ul>
    """
    while a<=b:
        resultado1 += f"<li> {a} </li>"
        a+=1
    resultado1 += "</ul"
    return HttpResponse(layout + resultado1)