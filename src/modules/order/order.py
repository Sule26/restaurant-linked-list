class Order:
    def __init__(self, nome: str, code: int, price: float, quantity: int) -> None:
        self.nome = nome
        self.code = code
        self.price = price
        self.quantity = quantity
        self.next: Order | None = None
