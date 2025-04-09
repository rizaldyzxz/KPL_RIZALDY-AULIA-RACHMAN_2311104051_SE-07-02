from enum import Enum
import time
# Automata: Enum => State
class TrafficLightState(Enum):
    MERAH = "Merah"
    HIJAU = "Hijau"
    KUNING = "Kuning"

# Automata: Transisi atau Perubahan State
state_transititions = {
    TrafficLightState.MERAH: TrafficLightState.HIJAU,
    TrafficLightState.HIJAU: TrafficLightState.KUNING,
    TrafficLightState.KUNING: TrafficLightState.MERAH
}

# Automata: Trigger Durations (Waktu Durasi/Habis)
state_durations = {
    TrafficLightState.MERAH: 5,
    TrafficLightState.HIJAU: 6,
    TrafficLightState.KUNING: 1
}

# Current State/State Awal
current_state = TrafficLightState.MERAH

while True:
    print(f"Traffic Light is {current_state.value}")
    time.sleep(state_durations[current_state])
    current_state = state_transititions[current_state]
