class PrettyTable:
    def __init__(self, table: list) -> None:
        self.table = table
        print(self.transform())

    def transform(self):
        result = ""
        ligne = "+---+---+---+\n"

        for i in self.table:
            result += ligne
            for j in i:
                result += f"| {j} "
            result += "|\n"
        result += ligne

        return result

