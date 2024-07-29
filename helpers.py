import random
import data


def generate_metro_station_name():
    return random.choice(data.METRO_STATION_NAMES)


def generate_rental_period_days():
     return random.choice(data.RENTAL_DAYS)


def generate_scooter_color():
    return random.choice(data.SCOOTER_COLORS)


def generate_name():
    return random.choice(data.NAMES)


def generate_surname():
    return random.choice(data.SURNAMES)


def generate_address():
    return random.choice(data.ADDRESSES)


def generate_phone_number():
    number = random.randint(111111111,999999999)
    return f'+7{number}'
