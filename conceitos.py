from dataclasses import dataclass

def somar(a: int, b: int) -> int:
    """Soma dois números inteiros."""
    return a + b

def criar_usuario(nome: str, ativo: bool = True) -> dict:
    return {nome: nome, 'ativo': ativo}


def buscar_produto(produtos: dict, nome:str) -> dict:
    if nome not in produtos:
        raise ValueError(f"Produto '{nome}' não encontrado.")
    return produtos[nome]



@dataclass
class Produto:
    nome: str
    preco: float
    estoque: int = 0

    def disponível(self) -> bool:
        return self.estoque > 0

p1= Produto(nome="Teclado", preco= 150.0, estoque=5)    
p2 = Produto(nome="Mouse", preco= 80.0)  # estoque padrão é 0

precos= [ 10,25,8,42,15,33]
caros = [preco for preco in precos if preco > 10]
com_desconto = [round(preco * 0.9 , 2) for preco in precos]

produtos = ["teclado", "mouse", "monitor"]
estoque = {nome: 0 for nome in produtos}

catalogo = {
    "teclado": {"preco": 150.0, "estoque": 5},
    "mouse": {"preco": 80.0, "estoque": 0}
    }

try:
    print(buscar_produto(catalogo, "teclado"))
    print(buscar_produto(catalogo, "headset"))
except ValueError as e:
    print(f"Erro: {e}")

