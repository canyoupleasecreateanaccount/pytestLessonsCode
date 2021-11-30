

class Person:

    def __init__(self, age, gender, name, car_color=None):
        self.age = age
        self.gender = gender
        self.name = name
        self.car_color = car_color

    def say_name(self, last_name):
        print(f"My name is {self.name} {last_name}")




person_one = Person(age=13, gender='male', name='Anton', car_color='black')
person_two = Person(12, 'female', 'Ann')


print(person_one.gender, person_one.age, person_one.name, person_one.car_color)
print(person_two.gender, person_two.age, person_two.name, person_two.car_color)


person_two.say_name('Petrova')









