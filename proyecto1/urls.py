from django.contrib import admin
from django.urls import path
from proyecto1.views import saludo, probandotemplate, cargadores

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('probandotemplate/', probandotemplate),
    path('cargadores/', cargadores),

]
