from django.contrib import admin
from .models import Category

#Crear clase para hacer que el slug sea el mismo que el nombre de la categoria
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug':('category_name',)}

    list_display = ('category_name', 'slug')

# Register your models here.
#Lo añadimos a su correspondiente modelo
admin.site.register(Category, CategoryAdmin)