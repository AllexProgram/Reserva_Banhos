from django.db import models


class ReservaModels(models.Model):

    CATEGORIA = (  # variáveis em maiúsculo indica a pretenção de não mecher na mesma.
        ("veterinário", "Serviços veterinários"),
        ("tosagem", "Tosagem"),
        ("alimentacao", "Rações"),
        ("limpeza_pet", "Banho Pet"),
    )
    nome_do_pet = models.CharField(verbose_name="Nome do pet", max_length=50)
    telefone = models.CharField(verbose_name="Telefone", max_length=50)
    data_da_reserva = models.DateField(verbose_name="Data de reserva")
    observacoes = models.TextField(verbose_name="Observações", default="nulo")
    categoria = models.CharField(
        verbose_name="Categorias",
        default="nulo",
        max_length=50,
        choices=CATEGORIA,  # a função "choices" recebe os valores da variável CATEGORIA
    )
    # A função auto_now_add seta automáticamente a data e hora do servidor toda vez que ReservaModels form salva
    enviado_em = models.DateTimeField(verbose_name="Eviado em", auto_now_add=True)
    # A função auto_now seta automáticamente a data e hora quando houver auteração.
    auteracao = models.DateTimeField(verbose_name="Auterado em", auto_now=True)
    # É exibido em forma de ícone vermelho
    lido = models.BooleanField(verbose_name="Lido", default=False, blank=False)
    # A função __str__ imprime as variáveis, "nomeando as colunas"
    def __str__(self):
        return f"{self.nome_do_pet} [{self.telefone}]"
    

    class Meta:
        # Nome exibido abaixo da lista
        verbose_name = "Formulário de reserva"
        # Nome exibido abaixo da lista
        verbose_name_plural = "Fomulários de reservas"
        # Ordena os registros na ordem decrescente
        ordering = ["-data_da_reserva"]
