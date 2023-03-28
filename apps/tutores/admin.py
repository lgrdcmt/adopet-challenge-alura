from django.contrib import admin
from apps.tutores.models import Tutor


class ListandoTutores(admin.ModelAdmin):
    list_display = ("id", "nome", "email")
    list_display_links = ("id", "nome")
    search_fields = ("id", "nome", "email")
    list_per_page = 10

admin.site.register(Tutor, ListandoTutores)