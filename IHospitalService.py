from abc import ABC, abstractmethod
from typing import List
from dao.Appointment import Appointment # Replace with your actual package structure

class IHospitalService(ABC):

    @abstractmethod
    def getAppointmentById(self, appointmentId: int) -> Appointment:
        return [Appointment(appointmentId,123,456,"2023-12-21","routine checkup")]
        pass

    @abstractmethod
    def getAppointmentsForPatient(self, patientId: int) -> List[Appointment]:
        return [Appointment(1,patientId, 765, "2023-12-26", "followup")]
        pass

    @abstractmethod
    def getAppointmentsForDoctor(self, doctorId: int) -> List[Appointment]:
        return [Appointment(1,  765,  doctorId,"2023-12-26", "consolation")]
        pass

    @abstractmethod
    def scheduleAppointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def updateAppointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def cancelAppointment(self, appointmentId: int) -> bool:
        pass

