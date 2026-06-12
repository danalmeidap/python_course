import pytest
from cupom import aplicar_cupom


def test_aplicar_cupom_desconto():
    valor_total = 100.0
    cupom = 0.1
    valor_com_desconto = aplicar_cupom(valor_total, cupom)
    assert valor_com_desconto == 90.0

def test_aplicar_cupom_desconto_invalido():
    valor_total = 100.0
    cupom = -0.1
    with pytest.raises(ValueError):
        aplicar_cupom(valor_total, cupom)

def test_aplicar_cupom_desconto_acima_de_1():
    valor_total = 100.0
    cupom = 1.5
    with pytest.raises(ValueError):
        aplicar_cupom(valor_total, cupom)

def test_aplicar_cupom_desconto_zero():
    valor_total = 100.0
    cupom = 0.0
    valor_com_desconto = aplicar_cupom(valor_total, cupom)
    assert valor_com_desconto == 100.0

def test_aplicar_cupom_desconto_cupom_igual_a_1():
    valor_total = 100.0
    cupom = 1.0
    valor_com_desconto = aplicar_cupom(valor_total, cupom)
    assert valor_com_desconto == 0.0

