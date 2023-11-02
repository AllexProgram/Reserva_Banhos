from django.shortcuts import render

from basic.forms import Contato


def reserva(requests):
    formulario = Contato(requests.POST or None)
    contexto = {"sucesso": False}
    if requests.method == "POST":
        formulario.save()
        contexto["sucesso"] = True
    contexto["formulario"] = formulario
    return render(requests, "contato.html", contexto)   







