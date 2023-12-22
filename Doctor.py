class Doctor:
    def __init__(self, doctorId, firstName, lastName, specialization, contactNumber):
        self._doctorId = doctorId
        self._firstName = firstName
        self._lastName = lastName
        self._specialization = specialization
        self._contactNumber = contactNumber

    def get_doctorId(self):
        return self._doctorId

    def set_doctorId(self, doctorId):
        self._doctorId = doctorId

    def get_firstName(self):
        return self._firstName

    def set_firstName(self, firstName):
        self._firstName = firstName

    def get_lastName(self):
        return self._lastName

    def set_lastName(self, lastName):
        self._lastName = lastName

    def get_specialization(self):
        return self._specialization

    def set_specialization(self, specialization):
        self._specialization = specialization

    def get_contactNumber(self):
        return self._contactNumber

    def set_contactNumber(self, contactNumber):
        self._contactNumber = contactNumber

    def print_info(self):
        print(f"Doctor ID: {self._doctorId}")
        print(f"First Name: {self._firstName}")
        print(f"Last Name: {self._lastName}")
        print(f"Specialization: {self._specialization}")
        print(f"Contact Number: {self._contactNumber}")

