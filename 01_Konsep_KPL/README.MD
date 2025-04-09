# Characteristic
#### Kompleksitas Minimal
```text
1. Gunakan fungsi modular daripada kode panjang dalam satu file.
2. Hindari penggunaan teknologi yang tidak perlu.
```
#### Kemudahan Pemeliharaan
- Gunakan naming convention yang jelas.
- Tambahkan komentar dan dokumentasi kode.
```python
def hitung_pajak(harga: float, pajak: float = 0.1) -> float:
    """
    Menghitung pajak dari suatu harga barang.
    :param harga: Harga barang sebelum pajak.
    :param pajak: Persentase pajak (default 10%).
    :return: Harga setelah pajak.
    """
    return harga + (harga * pajak)
```
#### Loose Coupling
- Gunakan desain yang modular.
- Pisahkan backend dan frontend.
#### Extendibility
- Gunakan Open-Closed Principle (OCP) → kode harus terbuka untuk ekstensi tetapi tertutup untuk modifikasi.
```python
class Pembayaran:
    def proses(self):
        pass

class PembayaranKredit(Pembayaran):
    def proses(self):
        return "Pembayaran via Kartu Kredit"

class PembayaranEWallet(Pembayaran):
    def proses(self):
        return "Pembayaran via E-Wallet"

pembayaran = PembayaranEWallet()
print(pembayaran.proses())  # Bisa diperluas tanpa mengubah kelas utama
```
#### Reusability
- Gunakan fungsi atau class yang fleksibel.
```python
def format_uang(jumlah, simbol="Rp"):
    return f"{simbol} {jumlah:,.2f}"

print(format_uang(1000000))  # Output: Rp 1,000,000.00
print(format_uang(1000000, "$"))  # Output: $ 1,000,000.00
```
#### High Fan-In
- Gunakan library atau helper functions yang bisa dipanggil dari berbagai tempat.
```python
class Logger:
    @staticmethod
    def log(pesan):
        print(f"[LOG]: {pesan}")

Logger.log("Aplikasi dimulai")  # Bisa digunakan di berbagai bagian kode
```
#### Portability
- Gunakan Docker untuk memastikan aplikasi dapat berjalan di mana saja.
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```
#### Leanness (Ringan dan Efisien)
- Gunakan list comprehension untuk perulangan yang lebih cepat.
```python
# Cara lama
angka_ganjil = []
for i in range(10):
    if i % 2 != 0:
        angka_ganjil.append(i)

# Cara lebih efisien
angka_ganjil = [i for i in range(10) if i % 2 != 0]
print(angka_ganjil)
```
#### Stratification (Berjenjang & Terstruktur)
- Gunakan desain yang terstruktur dan terorganisir.
- Terapkan seperti MVC, MVVM, atau arsitektur lainnya.
#### Standard Techniques (Menggunakan Teknik Standar)
- Menggunakan PEP 8 (Python) untuk coding style. 
- Menggunakan RESTful API untuk komunikasi antar layanan.
