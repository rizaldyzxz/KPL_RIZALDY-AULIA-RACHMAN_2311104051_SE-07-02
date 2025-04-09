from enum import Enum 

class JenisKelamin(Enum):
    LAKI_LAKI = 1
    PEREMPUAN = 2

print(JenisKelamin.LAKI_LAKI) ## JenisKelamin.LAKI_LAKI
print(JenisKelamin.LAKI_LAKI.value) ## 1
print(JenisKelamin.LAKI_LAKI.name) ## LAKI_LAKI