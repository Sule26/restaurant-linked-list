from src.modules.table.tableList import TableList
from src.modules.order.orderList import OrderList
from src.modules.others.waiter import Waiter
from src.modules.others.food import Food
from src.data.dataList import DATA_PATH, OPTION_LIST, waiters, foods, logo
import pandas as pd
import os


class App:
    def __init__(self):
        self.createOrReadFiles()

        self.createObjectsBasedOnFile()

        self.startOrderList()
        self.startTableList()

    def createOrReadFiles(self):
        if not os.path.exists(DATA_PATH):
            self.waiters = pd.DataFrame(waiters)
            self.waiters.index += 100
            self.waiters.index.name = "index"

            self.foods = pd.DataFrame(foods)
            self.foods.index += 1000
            self.foods.index.name = "index"

            with pd.ExcelWriter(DATA_PATH) as writer:
                self.waiters.to_excel(writer, sheet_name="waiters")
                self.foods.to_excel(writer, sheet_name="foods")
        else:
            self.waiters = pd.read_excel(DATA_PATH, sheet_name="waiters", index_col=0)
            self.foods = pd.read_excel(DATA_PATH, sheet_name="foods", index_col=0)

    def startTableList(self):
        self.tableList = TableList()

    def startOrderList(self):
        self.orderList = OrderList()

    def createObjectsBasedOnFile(self):
        self.waiters_list = []
        for index, row in self.waiters.iterrows():
            new_waiter = Waiter(row["name"], index)
            self.waiters_list.append(new_waiter)

        self.foods_list = []
        for index, row in self.foods.iterrows():
            new_food = Food(row["name"], index, row["price"])
            self.foods_list.append(new_food)

    def run(self):
        print(logo)
        while True:
            [
                print(f"[{index + 1}]{option}")
                for index, option in enumerate(OPTION_LIST)
            ]
            option_choosen = int(input("What would you like to do? "))
            match option_choosen:
                case 1:  # Add table
                    self.addTable()
                case 4:  # Show all tables
                    self.tableList.display()
                case _:  # Random option
                    print("No option available")

    def addTable(self):
        number_table = int(input("What's the table's number? "))
        [
            print(f"[{index}] {waiter_name}")
            for index, waiter_name in enumerate(waiters.name)
        ]
        waiter_choosen = int(
            input("Which waiter would you like to be responsible for your table? ")
        )
        self.tableList.sorted_insert(self.tableList.new_table(number_table, waiter_choosen))
