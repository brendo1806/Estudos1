from django import template
from Tarefa2.controledefornecedores.models import Controle


register = template.Library()

@register.filter
def tipo_choices(value):
    return dict(Controle.TIPO).get(value, "")
