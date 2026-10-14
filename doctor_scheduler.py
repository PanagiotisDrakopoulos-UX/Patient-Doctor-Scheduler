class Patient:
     def __init__(self,name,age,appointment_date,appointment_time):
        self.name = name
        self.age = age
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time

class Doctor:
    def __init__(self, name, patients, appointments):
        self.name = name
        self.patients = patients
        self.appointments = appointments

    def schedule_appointment(self, patient):
        if len(self.appointments) >= 16:
            print("Ο γιατρός έχει συμπληρώσει το όριο των 16 ραντεβού για σήμερα.")
            return False
        
        def time_to_minutes(time_str):
            hours, minutes = map(int, time_str.split(":"))
            return hours * 60 + minutes
        
        new_patient_mins = time_to_minutes(patient.appointment_time)
        
        for i in self.appointments:
            if i.appointment_date == patient.appointment_date:
                existing_mins = time_to_minutes(i.appointment_time)
                
                if abs(new_patient_mins - existing_mins) < 30:
                    print(f"Αποτυχία για {patient.name}: Δεν υπάρχει τουλάχιστον 30 λεπτά κενό!")
                    return False
        
        self.appointments.append(patient)
        print(f"Το ραντεβού για τον {patient.name} κλείστηκε επιτυχώς!")
        return True

if __name__ == "__main__":
   patient1 = Patient("Petros",30,"28/10/2026","14:00")
   patient2 = Patient("Panos",25,"28/10/2026","14:15")
   patient3 = Patient("Dimitris",35,"28/10/2026","16:00")
   patient4 = Patient("Nikos",40,"28/10/2026","18:00")
   my_doctor = Doctor("Dr. House", [], [])
   
   my_doctor.schedule_appointment(patient1)
   my_doctor.schedule_appointment(patient3)
   my_doctor.schedule_appointment(patient4)
   
   for p in my_doctor.appointments:
       print(f"Ασθενής: {p.name}, Ημερομηνία: {p.appointment_date}, Ώρα: {p.appointment_time}")