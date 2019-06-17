from django.contrib import admin
from .models import Usuarios, Hashtags, Candidatos

# Register your models here.

@admin.register(Usuarios)
class AdminUsuarios(admin.ModelAdmin):
    list_display = ('id', 'arroba', 'nombre_cuenta')


@admin.register(Hashtags)
class AdminHashtags(admin.ModelAdmin):
    list_display = ('id', 'hashtag')

@admin.register(Candidatos)
class AdminCandidatos(admin.ModelAdmin):
    list_display = ('id', 'arroba', 'nombre_cuenta')