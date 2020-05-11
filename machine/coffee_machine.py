class CoffeeMaker:
    def __init__(self):
        self.machine = [400, 540, 120, 9, 550]

    def __str__(self):
        return '''The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
{} of money'''.format (self.machine[0], self.machine[1], self.machine[2], self.machine[3], self.machine[4] if self.machine[4] == 0 else "$"+str(self.machine[4]))

    def can_make(self, needed):
        items = ["water", "milk", "coffee beans", "disposable cups"]
        for item, have, need in zip(items, self.machine[0:4], needed):
            if need > have:
                print("Sorry, not enough " + item + "!")
                return False
        print("I have enough resources, making you a coffee!")
        return True

    def buy(self):
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu:\n")
        if coffee_type == '1':
            if self.can_make([250, 0, 16, 1]):
                self.machine = [self.machine[0] - 250, self.machine[1], self.machine[2] - 16, self.machine[3] - 1,
                                self.machine[4] + 4]
        elif coffee_type == '2':
            if self.can_make([350, 75, 20, 1]):
                self.machine = [self.machine[0] - 350, self.machine[1] - 75, self.machine[2] - 20, self.machine[3] - 1,
                                self.machine[4] + 7]
        elif coffee_type == '3':
            if self.can_make([200, 100, 12, 1]):
                self.machine = [self.machine[0] - 200, self.machine[1] - 100, self.machine[2] - 12, self.machine[3] - 1,
                                self.machine[4] + 6]
        elif coffee_type == "back":
            pass

    def fill(self):
        self.machine[0] += int(input("\nWrite how many ml of water do you want to add:\n"))
        self.machine[1] += int(input("Write how many ml of milk do you want to add:\n"))
        self.machine[2] += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.machine[3] += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        print("\nI gave you $" + str(self.machine[4]))
        self.machine[4] = 0


user = CoffeeMaker()
while True:
    input_ = input("\nWrite action (buy, fill, take, remaining, exit):\n")
    if input_ == "buy":
        user.buy()
    elif input_ == "fill":
        user.fill()
    elif input_ == "take":
        user.take()
    elif input_ == "remaining":
        print("\n" + str(user))
    elif input_ == "exit":
        break
