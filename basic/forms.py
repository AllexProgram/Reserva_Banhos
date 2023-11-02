"""
Comando para a verificação do formulárai - neste caso - forms.is_valid()
Comando para criação da html
Comando no terminal do python com o abiente do django - python manage.py shell

"""

from typing import Any, Dict
from django import forms
from basic.models import ReservaModels


class Contato(forms.ModelForm):
    class Meta:
        model = ReservaModels
        fields = [
            "categoria",
            "nome_do_pet",
            "telefone",
            "data_da_reserva",
            "observacoes",
            "lido",           
            
        ]

