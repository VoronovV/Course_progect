
class Client:
    def __init__(self, FIO, age, city, ticket_number, arrival_date, departure_date):
        self.__FIO = FIO
        self.__age = age
        self.__city = city
        self.__ticket_number = ticket_number
        self.__arrival_date = arrival_date
        self.__departure_date = departure_date

    @property
    def FIO(self):
        return self.__FIO

    @FIO.setter
    def FIO(self, FIO):
        self.__FIO = FIO

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def ticket_number(self):
        return self.__ticket_number

    @ticket_number.setter
    def ticket_number(self, ticket_number):
        self.__ticket_number = ticket_number

    @property
    def arrival_date(self):
        return self.__arrival_date

    @arrival_date.setter
    def arrival_date(self, arrival_date):
        self.__arrival_date = arrival_date

    @property
    def departure_date(self):
        return self.__departure_date

    @departure_date.setter
    def departure_date(self, departure_date):
        self.__departure_date = departure_date


