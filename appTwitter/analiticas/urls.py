from django.urls import include, path
from .views import conexion, prueba, home, analitica1, analitica2, analitica3, analitica4

app_name='analiticas'

urlpatterns = [
    #path("pruebas/", .as_view(), name=""),
    path("", home, name="home"),
    path("prueba/", prueba, name='prueba'),
    path('analitica1/', analitica1, name='analitica1'),
    path('analitica2/', analitica2, name='analitica2'),
    path('analitica3/', analitica3, name='analitica3'),
    path('analitica4/', analitica4, name='analitica4'),
]
