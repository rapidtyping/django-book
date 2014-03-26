# -*- encoding: utf-8 -*-
from django.http import HttpResponse
# 1.
from django.template import Template, Context
# 2. Agregado para usar la funcion de get_template
from django.template.loader import get_template
# 3.
from django.shortcuts import render_to_response
import datetime

def hora_actual(request):
    ahora = datetime.datetime.now()
    html = "<html><body>El momento actual es %s. </body></html>" % ahora
    return HttpResponse(html)
    
# 1. Usando el sistema de plantillas de django

def hora_actual2(request):
    ahora = datetime.datetime.now()
    t = Template("<html><body>El momento actual es {{ fecha_actual }}. </body></html>")
    html = t.render(Context({'fecha_actual': ahora}))
    return HttpResponse(html)
# 2. Separando aun mas la vista en un fichero html
def hora_actual3(request):
    ahora = datetime.datetime.now()
    t = get_template('fecha_actual3.html')
    html = t.render(Context({'fecha_actual': ahora}))
    return HttpResponse(html)
    
# 3. Pero que pesado! hacer como (2), mejor así:
def hora_actual4(request):
    ahora = datetime.datetime.now()
    return render_to_response('fecha_actual4.html', {'fecha_actual': ahora})    

# 4. Que (3) esta aun muy largo?:
def hora_actual5(request):
    ahora = datetime.datetime.now()
    return render_to_response('fecha_actual5.html', locals())    

# 5. Usando una plantilla heredada:
def hora_actual6(request):
    ahora = datetime.datetime.now()
    return render_to_response('fecha_actual6.html', locals())    
