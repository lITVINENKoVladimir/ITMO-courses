import psycopg2

conn_params = {
  "host": "localhost",
  "database": "поликлиника",
  "user": "postgres",
  "password": "123123"
}

conn = psycopg2.connect(**conn_params)
cur = conn.cursor()


cur.execute("""
  CREATE TABLE IF NOT EXISTS Doctors (
    id SERIAL PRIMARY KEY,
    lastname VARCHAR(255) NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    patronymic VARCHAR(255),
    specialty VARCHAR(255)
  );
""")

# Создание таблицы Patients
cur.execute("""
  CREATE TABLE IF NOT EXISTS Patients (
    id SERIAL PRIMARY KEY,
    lastname VARCHAR(255) NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    patronymic VARCHAR(255),
    birthdate DATE,
    address VARCHAR(255),
    has_benefits BOOLEAN
  );
""")

# Создание таблицы Schedule
cur.execute("""
  CREATE TABLE IF NOT EXISTS Schedule (
    id SERIAL PRIMARY KEY,
    doctor_id INTEGER REFERENCES Doctors(id) NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL
  );
""")

# Создание таблицы Appointments
cur.execute("""
  CREATE TABLE IF NOT EXISTS Appointments (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES Patients(id) NOT NULL,
    schedule_id INTEGER REFERENCES Schedule(id) NOT NULL
  );
""")


conn.commit()
print("Таблицы созданы/проверены.")


doctors_data = [
  ("Иванов", "Иван", "Иванович", "Терапевт"),
  ("Петрова", "Мария", "Петровна", "Кардиолог"),
  ("Смирнов", "Алексей", "Сергеевич", "Хирург"),
  ("Сидорова", "Елена", "Владимировна", "Невролог"),
  ("Кузнецов", "Дмитрий", "Александрович", "Офтальмолог")
]

for doctor in doctors_data:
  cur.execute("INSERT INTO Doctors (lastname, firstname, patronymic, specialty) VALUES (%s, %s, %s, %s)", doctor)
conn.commit()
print("Данные о врачах вставлены.")


# Вставка данных для пациентов - расширенный список
patients_data = [
  ("Сидоров", "Петр", "Сидорович", "1990-03-15", "ул. Пушкина, 10", False),
  ("Кузнецова", "Анна", "Сергеевна", "1985-11-20", "пр. Ленина, 5", True),
  ("Васильев", "Иван", "Иванович", "1978-07-25", "ул. Грибоедова, 2", False),
  ("Петрова", "Ольга", "Петровна", "1995-01-10", "ул. Некрасова, 15", True),
  ("Михайлов", "Сергей", "Михайлович", "1982-09-05", "ул. Толстого, 8", False),
  ("Соколова", "Светлана", "Александровна", "2000-04-22", "ул. Лермонтова, 3", False),
  ("Андреев", "Андрей", "Андреевич", "1975-12-18", "ул. Чехова, 12", True),
  ("Иванова", "Ирина", "Ивановна", "1992-06-02", "ул. Достоевского, 7", False),
  ("Морозов", "Алексей", "Игоревич", "1988-08-11", "ул. Тургенева, 1", True),
  ("Федорова", "Елена", "Юрьевна", "1971-05-01", "ул. Горького, 17", False),

]

for patient in patients_data:
  cur.execute("INSERT INTO Patients (lastname, firstname, patronymic, birthdate, address, has_benefits) VALUES (%s, %s, %s, %s, %s, %s)", patient)
conn.commit()
print("Данные о пациентах вставлены.")


# Запросы (без изменений)
cur.execute("SELECT * FROM Doctors;")
doctors = cur.fetchall()
print("\nВрачи:")
for doctor in doctors:
  print(doctor)

cur.execute("SELECT * FROM Patients;")
patients = cur.fetchall()
print("\nПациенты:")
for patient in patients:
  print(patient)

cur.close()
conn.close()
