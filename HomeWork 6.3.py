# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surename, position, wage, bonus):
        self.name = name
        self.surename = surename
        self.position = position
        self._income = {"profit": wage, "Bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surename}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"


manager = Position("Виталий", "Михалыч", "CEO", 500000, 123000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_full_profit())

