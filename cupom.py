def aplicar_cupom(valor_pedido, cupom):
    """Aplica um cupom de desconto ao valor do pedido.
    Args:        valor_pedido (float): O valor total do pedido antes do desconto.
        cupom (float): O valor do cupom de desconto, representado como um número entre 0 e 1.
    Returns:        float: O valor do pedido após a aplicação do desconto.
    Raises:        ValueError: Se o valor do cupom for menor que 0 ou maior que 1.
    """
    if cupom < 0 or cupom > 1:
        raise ValueError("O valor do cupom deve ser entre 0 e 1 ")
    return valor_pedido * (1 - cupom)