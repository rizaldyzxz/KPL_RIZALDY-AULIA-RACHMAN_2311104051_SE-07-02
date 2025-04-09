from enum import Enum

# State untuk Status Mahasiswa
class StudentStatusState(Enum):
    TERDAFTAR = "Terdaftar"
    AKTIF = "Aktif"
    LULUS = "Lulus" # State Final (End State) => tidak punya transisi
    CUTI = "Cuti"

# State untuk Trigger Input
class TriggerInputState(Enum):
    CETAK_KSM = "Cetak KSM"
    LULUS = "Lulus"
    MENGAJUKAN_CUTI = "Mengajukan Cuti"
    MENYELESAIKAN_CUTI = "Menyelesaikan Cuti"

state_transitions = {
    StudentStatusState.TERDAFTAR: {
        TriggerInputState.CETAK_KSM: StudentStatusState.AKTIF,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI
    },
    StudentStatusState.AKTIF: {
        TriggerInputState.LULUS: StudentStatusState.LULUS,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI
    },
    StudentStatusState.CUTI: {
        TriggerInputState.MENYELESAIKAN_CUTI: StudentStatusState.TERDAFTAR
    }
}

def change_state(current_state, trigger):
    if current_state in state_transitions and trigger in state_transitions[current_state]:
        return state_transitions[current_state][trigger]
    return "State atau transisi tidak valid"

# Testing
current_state = StudentStatusState.TERDAFTAR
new_state = change_state(current_state, TriggerInputState.CETAK_KSM)
print(f"State sebelumnya: {current_state}, Trigger: {TriggerInputState.CETAK_KSM}, State baru: {new_state}")

new_state = change_state(current_state, TriggerInputState.LULUS)
print(f"State sebelumnya: {current_state}, Trigger: {TriggerInputState.LULUS}, State baru: {new_state}")