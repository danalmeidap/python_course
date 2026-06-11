def calcular_frete(valor_pedido:float) -> tuple[float, float]:
    """Calcula o valor do frete e o cupom de desconto com base no valor do pedido.
    Args:  valor_pedido (float): O valor total do pedido.
    Returns: tuple: Uma tupla contendo o valor do frete e o valor do cupom de desconto.
    Raises:  ValueError: Se o valor do pedido for negativo."""
    
    frete = 0.0
    cupom = 0.0
    if valor_pedido < 0:
        raise ValueError("Valor do pedido não pode ser negativo.")
    if valor_pedido < 100.0:
        frete = 15.0
    elif valor_pedido <= 250.0:
        frete = 10.0
    else:
        if valor_pedido >= 500.0:
            cupom = 0.05  
        frete = 0.0
    return frete, cupom
