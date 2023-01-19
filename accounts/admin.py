from django.contrib import admin
from .models import Account
#Importaciones para editar el dashboard de la pagina admin en Accounts
from django.contrib.auth.admin import UserAdmin

#Creamos la clase que tendra los campos para personalizar el dashboard
class AccountAdmin(UserAdmin):

    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.
#Agregamos la clase al su register relacionada
admin.site.register(Account, AccountAdmin)