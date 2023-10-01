from src.modules.table.table import Table


class TableList:
    def __init__(self) -> None:
        self.head: Table | None = None
        self.size: int = 0

    def new_table(self, number: int) -> Table:
        new = Table(number)
        new.next = None
        new.prev = None
        return new

    def sorted_insert(self, table: "Table") -> None:

        # Check whether the head is Noneval
        if self.head is None:
            # Update the head and tail
            self.head = table

        # Check whether it will be inserted as the first Table
        elif table.number < self.head.number:
            table.next = self.head
            table.prev = None
            self.head.prev = None
            self.head = table

        # In the middle or at the end
        else:
            current = self.head
            while current.next is not None and current.next.number < table.number:
                current = current.next

            table.next = current.next

            # Check if current.next is None because if it is not, it needs to update the current.next.prev
            if current.next is not None:
                current.next.prev = table

            current.next = table
            table.prev = current

        self.size += 1

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
