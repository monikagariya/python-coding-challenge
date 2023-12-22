class Appointment:
    def __init__(self, appointmentId, patientId, doctorId, appointmentDate, description):
        self._appointmentId = appointmentId
        self._patientId = patientId
        self._doctorId = doctorId
        self._appointmentDate = appointmentDate
        self._description = description

    def get_appointmentId(self):
        return self._appointmentId

    def set_appointmentId(self, appointmentId):
        self._appointmentId = appointmentId

    def get_patientId(self):
        return self._patientId

    def set_patientId(self, patientId):
        self._patientId = patientId

    def get_doctorId(self):
        return self._doctorId

    def set_doctorId(self, doctorId):
        self._doctorId = doctorId

    def get_appointmentDate(self):
        return self._appointmentDate

    def set_appointmentDate(self, appointmentDate):
        self._appointmentDate = appointmentDate

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def print_info(self):
        print(f"Appointment ID: {self._appointmentId}")
        print(f"Patient ID: {self._patientId}")
        print(f"Doctor ID: {self._doctorId}")
        print(f"Appointment Date: {self._appointmentDate}")
        print(f"Description: {self._description}")

