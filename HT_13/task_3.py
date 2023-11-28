# 3. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.

class CountInstances:
    counter = 0

    def __new__(self):
        self.counter += 1

count_1 = CountInstances()
count_2 = CountInstances()
count_3 = CountInstances()
count_4 = CountInstances()
print(CountInstances.counter)
