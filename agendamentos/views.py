from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pet, Veterinario, Servico, Agendamentos

def home(request):
    return render(request, 'home.html')

def agendar_consulta(request):
    if request.method == 'POST':
        # Pega as informações enviadas pelo formulário HTML
        pet_id = request.POST.get('pet')
        veterinario_id = request.POST.get('veterinario')
        servico_id = request.POST.get('servico')
        data = request.POST.get('data')
        horario = request.POST.get('horario')

        # Busca os objetos correspondentes no banco de dados
        pet = Pet.objects.get(id=pet_id)
        veterinario = Veterinario.objects.get(id=veterinario_id)
        servico = Servico.objects.get(id=servico_id)

        try:
            # Tenta salvar o novo agendamento (a nossa restrição UniqueConstraint vai validar aqui!)
            Agendamentos.objects.create(
                pet=pet,
                veterinario=veterinario,
                servico=servico,
                data=data,
                horario=horario
            )
            return redirect('home') # Se der certo, volta para a página inicial
        except:
            # Se a nossa regra de UniqueConstraint bloquear (horário duplicado)
            messages.error(request, "Erro: Este veterinário já possui um agendamento neste dia e horário!")

    # Carrega os dados existentes para preencher os selects do HTML
    contexto = {
        'pets': Pet.objects.all(),
        'veterinarios': Veterinario.objects.all(),
        'servicos': Servico.objects.all(),
    }
    return render(request, 'agendar.html', contexto)
