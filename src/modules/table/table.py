class Table:
    def __init__(self, number: int, waiter_code: int) -> None:
        self.number = number
        self.waiter_code = waiter_code
        # self.order_list = order_list
        # self.total_price = total_price
        self.next: Table | None = None
        self.prev: Table | None = None
