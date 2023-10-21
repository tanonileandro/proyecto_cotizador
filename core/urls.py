from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from cotizador import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/calcular/', views.calcular, name='calcular'),
    
]


urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]