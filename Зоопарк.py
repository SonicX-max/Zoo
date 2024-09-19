import pickle

# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассах.")

    def eat(self):
        return f"{self.name} ест."


# Подклассы Bird, Mammal, и Reptile
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return f"{self.name} чирикает."

    def fly(self):
        return f"{self.name} летит с размахом крыльев {self.wing_span} метров."


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return f"{self.name} рычит."

    def run(self):
        return f"{self.name} бежит."


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        return f"{self.name} шипит."

    def crawl(self):
        return f"{self.name} ползет."


# Классы сотрудников
class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "ZooKeeper")

    def feed_animal(self, animal):
        return f"{self.name} кормит {animal.name}."


class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}."


# Класс Zoo с методами для добавления, удаления, сохранения и загрузки
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, name):
        self.animals = [animal for animal in self.animals if animal.name != name]

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def remove_staff(self, name):
        self.staff = [staff for staff in self.staff if staff.name != name]

    def show_animals(self):
        if self.animals:
            for animal in self.animals:
                print(f"{animal.name}, {animal.age} лет.")
        else:
            print("В зоопарке нет животных.")

    def show_staff(self):
        if self.staff:
            for staff_member in self.staff:
                print(f"{staff_member.name}, роль: {staff_member.role}")
        else:
            print("В зоопарке нет сотрудников.")

    def make_all_sounds(self):
        if self.animals:
            for animal in self.animals:
                print(animal.make_sound())
        else:
            print("В зоопарке нет животных.")

    def save_zoo(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_zoo(filename):
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("Файл не найден. Создается новый зоопарк.")
            return Zoo()


# Основная интерактивная программа
def main():
    zoo = Zoo.load_zoo("zoo_data.pkl")

    while True:
        print("\nМеню:")
        print("1. Добавить животное")
        print("2. Удалить животное")
        print("3. Показать всех животных")
        print("4. Добавить сотрудника")
        print("5. Удалить сотрудника")
        print("6. Показать всех сотрудников")
        print("7. Услышать звуки всех животных")
        print("8. Сохранить зоопарк")
        print("9. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            animal_type = input("Какое животное вы хотите добавить (Bird, Mammal, Reptile)? ").strip().lower()
            name = input("Имя животного: ")
            age = int(input("Возраст животного: "))

            if animal_type == "bird":
                wing_span = float(input("Размах крыльев: "))
                zoo.add_animal(Bird(name, age, wing_span))
            elif animal_type == "mammal":
                fur_color = input("Цвет шерсти: ")
                zoo.add_animal(Mammal(name, age, fur_color))
            elif animal_type == "reptile":
                scale_type = input("Тип чешуи: ")
                zoo.add_animal(Reptile(name, age, scale_type))
            else:
                print("Неправильный тип животного.")

        elif choice == '2':
            name = input("Имя животного, которое нужно удалить: ")
            zoo.remove_animal(name)

        elif choice == '3':
            zoo.show_animals()

        elif choice == '4':
            staff_type = input("Какого сотрудника вы хотите добавить (ZooKeeper, Veterinarian)? ").strip().lower()
            name = input("Имя сотрудника: ")

            if staff_type == "zookeeper":
                zoo.add_staff(ZooKeeper(name))
            elif staff_type == "veterinarian":
                zoo.add_staff(Veterinarian(name))
            else:
                print("Неправильный тип сотрудника.")

        elif choice == '5':
            name = input("Имя сотрудника, которого нужно удалить: ")
            zoo.remove_staff(name)

        elif choice == '6':
            zoo.show_staff()

        elif choice == '7':
            zoo.make_all_sounds()

        elif choice == '8':
            zoo.save_zoo("zoo_data.pkl")
            print("Зоопарк сохранен.")

        elif choice == '9':
            zoo.save_zoo("zoo_data.pkl")
            print("Программа завершена.")
            break

        else:
            print("Неправильный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
