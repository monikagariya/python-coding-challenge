class Patient:
    def __init__(self, patientId, firstName, lastName, dateOfBirth, gender, contactNumber, address):
        self._patientId = patientId
        self._firstName = firstName
        self._lastName = lastName
        self._dateOfBirth = dateOfBirth
        self._gender = gender
        self._contactNumber = contactNumber
        self._address = address

    def get_patientId(self):
        return self._patientId

    def set_patientId(self, patientId):
        self._patientId = patientId

    def get_firstName(self):
        return self._firstName

    def set_firstName(self, firstName):
        self._firstName = firstName

    def get_lastName(self):
        return self._lastName

    def set_lastName(self, lastName):
        self._lastName = lastName

    def get_dateOfBirth(self):
        return self._dateOfBirth

    def set_dateOfBirth(self, dateOfBirth):
        self._dateOfBirth = dateOfBirth

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        self._gender = gender

    def get_contactNumber(self):
        return self._contactNumber

    def set_contactNumber(self, contactNumber):
        self._contactNumber = contactNumber

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address


def print_info(self):
    print(f"Patient ID: {self._patientId}")
    print(f"First Name: {self._firstName}")
    print(f"Last Name: {self._lastName}")
    print(f"Date of Birth: {self._dateOfBirth}")
    print(f"Gender: {self._gender}")
    print(f"Contact Number: {self._contactNumber}")
    print(f"Address: {self._address}")



