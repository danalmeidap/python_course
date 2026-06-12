import pytest
from frete import calcular_frete


def test_frete_pedido_barato():
    frete, cupom = calcular_frete(50.0)
    assert frete == 15.0
    assert cupom == 0.0


def test_frete_pedido_medio():
    frete, cupom = calcular_frete(150.0)
    assert frete == 10.0
    assert cupom == 0.0

def test_frete_pedido_acima_250():
    frete, cupom = calcular_frete(300.0)
    assert frete == 0.0
    assert cupom == 0.0


def test_frete_valor_exato_100():
    frete, cupom = calcular_frete(100.0)
    assert frete == 10.0
    assert cupom == 0.0


def test_frete_valor_exato_250():
    frete, cupom = calcular_frete(250.0)
    assert frete == 10.0
    assert cupom == 0.0

def test_frete_pedido_premium():
    frete, cupom = calcular_frete(600.0)
    assert frete == 0.0
    assert cupom == 0.05

def test_frete_pedido_normal_sem_cupom():
    frete, cupom = calcular_frete(50.0)
    assert frete == 15.0
    assert cupom == 0.0


def test_frete_pedido_valor_negativo():
    with pytest.raises(ValueError):
        calcular_frete(-10.0)
