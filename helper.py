from faker import Faker
import random


faker = Faker('ru_RU')

class GenerationData:

    @staticmethod
    def generate_name():
        return faker.first_name()

    @staticmethod
    def generate_last_name():
        return faker.last_name()

    @staticmethod
    def generate_address():
        address =  faker.street_name()
        house = faker.building_number().replace('/', '-')
        return f'{address}, {house}'

    @staticmethod
    def generate_phone():
        phone = faker.phone_number()
        return ''.join(filter(str.isdigit, phone))

    @staticmethod
    def generate_date():
        date = faker.date_this_month()
        return date.strftime('%d-%m-%Y')

    @staticmethod
    def generate_comment():
        return faker.text(50)

    @staticmethod
    def generate_random_number_metro():
        return random.randint(1, 237)

    @staticmethod
    def generate_random_number_rent_period():
        return random.randint(1, 7)

    @staticmethod
    def generate_random_number_color_scooter():
        return random.randint(1, 2)
