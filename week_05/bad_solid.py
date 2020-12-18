class Administator:
    def prepare_documents(self):
        # все правильно, этим он и занимается
        return 'done'

    def water_flowers(self):
        # ну, пусть поливает цветочки
        return 'done'

    def repair_car(self):
        # погодите, что?
        return 'done'

    def clean_floor(self):
        # нет, это уже работа для уборщика
        return 'done'

    def perform_surgery(self):
        # но он ведь не доктор, эй!
        return 'done'


class Student(Administator):
    # постойте, мы правда хотим наследовать все эти ненужные методы?

    def method_only_for_student(self):
        return 'hehe, administrator cannot call me'

    def repair_car(self):
        method_only_for_student()
        return done

