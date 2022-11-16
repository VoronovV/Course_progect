

class Diagnosis:
    def __init__(self, ticket_number, disease):
        self.__ticket_number = ticket_number
        self.__disease = disease

    @property
    def ticket_number(self):
        return self.__ticket_number

    @ticket_number.setter
    def ticket_number(self, ticket_number):
        self.__ticket_number = ticket_number

    @property
    def disease(self):
        return self.__disease

    @disease.setter
    def disease(self, disease):
        self.__disease = disease