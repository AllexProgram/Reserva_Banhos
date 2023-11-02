from django.contrib import admin
from basic.models import ReservaModels
from django.contrib import messages

# CRIANDO UM AÇÃO
@admin.action(description="Marcar formulário(s) como lido(s)")
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(
        lido=True
    )  # Consulta no modelo em questão, filtrado pelo resgistro selecionado.
    modeladmin.message_user(
        request, "Fomulário de reserva marcada(as) com lida(as)", messages.SUCCESS
    )


# Registrando modelo
@admin.register(ReservaModels)
class ReservaModelsAdmin(admin.ModelAdmin):
    # Lista de campos com os nomes que irão aparecer na lista de registro.
    list_display = ["nome_do_pet", "telefone", "data_da_reserva", "lido"]
    # Lista de campos com os nomes que se deseja realizar buscas
    search_fields = ["nome_do_pet", "telefone", "categoria"]
    # Lista de campos que se deseja filtrar-posicionado na parte esquerda da página.
    list_filter = ["nome_do_pet", "lido"]
    actions = [marcar_como_lido]
