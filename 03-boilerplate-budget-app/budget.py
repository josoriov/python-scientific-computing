from __future__ import annotations

TITLE_LINE_LENGTH = 30
DESCRIPTION_CUTOFF = 23
AMOUNT_CUTOFF = 7
DECIMAL_PLACES = 2
FILL_CHAR = "*"


class Category:

    def __init__(self, name: str):
        self.name: str = name
        self.ledger: list[dict] = []
        self.funds: float = 0.0

    def __str__(self) -> str:
        output = """"""
        # calculating title row
        name_length = len(self.name)
        remaining_chars = (TITLE_LINE_LENGTH - name_length)
        padding = remaining_chars // 2
        left_padding = padding + (remaining_chars % 2)
        output += f"{FILL_CHAR*left_padding}{self.name}{FILL_CHAR*padding}\n"
        # Calculating for the ledger
        output += self.format_ledger()
        # total line
        output += f"Total: {self.funds:.2f}"
        return output

    def format_ledger(self) -> str:
        output = ""
        for row in self.ledger:
            # formatting description
            description = row["description"]
            description = description[:DESCRIPTION_CUTOFF] if len(description) > DESCRIPTION_CUTOFF else description
            # formatting amount
            amount = f'{row["amount"]:.2f}'
            amount = amount[:AMOUNT_CUTOFF] if len(amount) > AMOUNT_CUTOFF else amount
            # calculating number of fill spaces
            fill_spaces = TITLE_LINE_LENGTH - len(description) - len(amount)
            output += f"{description}{fill_spaces*' '}{amount}\n"

        return output

    def check_funds(self, amount: float) -> bool:
        # False if amount is greater than the balance
        return False if amount > self.funds else True

    def deposit(self, amount: float, description: str = "") -> None:
        self.ledger.append({"amount": amount, "description": description})
        self.funds += amount
        return

    def withdraw(self, amount: float, description: str = "") -> bool:
        if self.check_funds(amount=amount):
            self.ledger.append({"amount": -1.0*amount, "description": description})
            self.funds -= amount
            return True
        return False

    def get_balance(self) -> float:
        return self.funds

    def transfer(self, amount: float, recieving_category: Category) -> bool:
        # check if funds are enough
        if self.check_funds(amount=amount):
            # create descriptions
            out_description = f"Transfer to {recieving_category.name}"
            in_description = f"Transfer from {self.name}"
            # do the transfers
            self.withdraw(amount=amount, description=out_description)
            recieving_category.deposit(amount=amount, description=in_description)
            return True
        return False


def create_spend_chart(categories):
    return
