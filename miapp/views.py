from django.shortcuts import render,HttpResponse

# Create your views here.

layout = """
    <h1>proyecto web (lp3) | alvaro </h1>
    <hr>
    <ul>
        <li>
            <a href="/inicio"> Inicio </a>
        </li>
        <li>
            <a href="/saludo"> mensaje saludo </a>
        </li>
        <li>
            <a href="/rango"> mostrar numero </a>
        </li>
    </ul>
    </hr>
    
"""

def index(request):
    
    return render(request, 'index.html')


def saludo(request):
    
    return render(request, 'saludo.html')

def rango(request):
    a = 10
    b = 20
    resultado = f"""
    <h2>numero de [{a},{b}]</h2>
    reultado : <br>
    <ul>
    
    """
    while a<=b :
        resultado +=f"<li>{a}</li>"
        a+=1
    resultado +="</ul"
    return HttpResponse(layout + resultado)

def rango2(request, a=0, b=100):

    if a>b:
        return redirect('rango2',a=b,b=a)

    resultado = f"""
    <h2>numero de [{a},{b}]</h2>
    reultado : <br>
    <ul>
    """

    while a <= b :
        resultado +=f"<li>{a}</li>"
        a+=1
    resultado +="</ul"
    return HttpResponse(layout + resultado)
