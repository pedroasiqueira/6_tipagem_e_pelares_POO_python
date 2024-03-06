class MonthlyExpense:
    def __init__(self, internet, grocery, power, water, rent) -> None:
        self.internet = internet
        self.grocery = grocery
        self._power = power
        self._water = water
        self.__rent = rent

    def get_power(self):
        return self._power

    def get_water(self):
        return self._water

    def set_power(self, new_power):
        self.get_power = new_power

    def set_water(self, new_water):
        self.get_water = new_water
