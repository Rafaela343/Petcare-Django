from django.contrib import admin
from .models import Cliente, Pet, Veterinario, Servico, Agendamentos
admin.site.register(Cliente)
admin.site.register(Pet)
admin.site.register(Veterinario)
admin.site.register(Servico)
admin.site.register(Agendamentos)