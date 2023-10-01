from src.modules.order.order import Order


class OrderList:
    def __init__(self) -> None:
        self.head: Order | None = None
        self.size: int = 0

    def new_order(self) -> Order:
        new = Order()
        new.next = None
        return new

    def insert(self, order: "Order") -> None:
        # Check whether the head is Non
        if self.head is None:
            # Update the head and tail
            self.head = order

        # If not, go to the last Table and insert in at the end
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = order

    def display(self) -> None:
        current = self.head
        while current is not None:
            print(
                f"""
                    Table {current.number}:
                        Waiter Code: {current.waiter_code}
                """
            )
            current = current.next

