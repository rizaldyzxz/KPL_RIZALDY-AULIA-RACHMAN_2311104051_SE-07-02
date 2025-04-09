from enum import Enum

class JenisKelamin(Enum):
    LAKI_LAKI = 1
    PEREMPUAN = 2
    
patients = []

def add_patient(name: str, gender: JenisKelamin):
    if not isinstance(gender, JenisKelamin):
        raise ValueError("Jenis Kelamin harus JenisKelamin Enum (LAKI_LAKI, PEREMPUAN)")
    patients.append({"name": name, "gender": gender.name})
    
add_patient("Andi", JenisKelamin.LAKI_LAKI)
add_patient("Siti", JenisKelamin.PEREMPUAN)
add_patient("Lucinta Luna", "TRANSGENDER")

for patient in patients:
    print(f"Nama: {patient['name']}, Jenis Kelamin: {patient['gender']}")
    