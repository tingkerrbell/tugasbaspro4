# 🧮 Tugas Bahasa Pemrograman 2 Matrix 5x5 

Program ini bertujuan untuk membuat sebuah matriks berukuran 5x5, 
di mana elemen-elemennya berupa angka dari 1 hingga 25 yang disusun
secara berurutan dari kiri ke kanan dan dari atas ke bawah.

---
## 🗂 Struktur Proyek
bahasa_pemrograman_2/         # Folder proyek utama

├── tugasbaspro_6/            # Folder proyek untuk tugas

│   ├── matrix5x5.py          # Skrip Python utama untuk menghasilkan matriks

│   └── README.md             # Dokumentasi tentang cara menjalankan proyek ini

---
## Kode Program
```python
# Membuat matriks 5x5 menggunakan append
matrix = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(i * 5 + j + 1)
    matrix.append(row)

# Menampilkan hasil matriks
for row in matrix:
    print(row)
```

## Penjelasan Kode

### 1. Inisialisasi Matriks Kosong
```python
matrix = []
```
Baris ini membuat sebuah list kosong bernama `matrix` yang akan digunakan untuk menyimpan baris-baris dari matriks.

### 2. Perulangan Luar (Membentuk Baris)
```python
for i in range(5):
```
Perulangan ini berjalan sebanyak 5 kali (i = 0 sampai 4), untuk membentuk 5 baris dalam matriks.

### 3. Inisialisasi Baris Kosong
```python
row = []
```
Pada setiap iterasi dari perulangan luar, dibuat list kosong `row` untuk menampung elemen-elemen dalam satu baris matriks.

### 4. Perulangan Dalam (Mengisi Kolom)
```python
for j in range(5):
```
Perulangan ini juga berjalan sebanyak 5 kali (j = 0 sampai 4), untuk mengisi 5 kolom dalam satu baris.

### 5. Menambahkan Elemen ke Baris
```python
row.append(i * 5 + j + 1)
```
Rumus ini digunakan untuk menghitung nilai dari elemen pada posisi ke-j dalam baris ke-i:
- `i * 5` akan memberikan kelipatan 5 berdasarkan indeks baris.
- `j` adalah indeks kolom yang sedang diisi.
- `+1` agar angka dimulai dari 1, bukan dari 0.

Contoh:
- Saat `i = 0` dan `j = 0`: `0 * 5 + 0 + 1 = 1`
- Saat `i = 1` dan `j = 2`: `1 * 5 + 2 + 1 = 8`

### 6. Menambahkan Baris ke Matriks
```python
matrix.append(row)
```
Setelah satu baris lengkap terisi 5 angka, baris tersebut ditambahkan ke list `matrix`.

### 7. Menampilkan Matriks
```python
for row in matrix:
    print(row)
```
Perulangan ini mencetak setiap baris dalam matriks, satu per satu.

## Output Program
```
[1, 2, 3, 4, 5]
[6, 7, 8, 9, 10]
[11, 12, 13, 14, 15]
[16, 17, 18, 19, 20]
[21, 22, 23, 24, 25]
```

## Kesimpulan
Program ini menunjukkan bagaimana cara membuat dan menampilkan matriks 2 dimensi menggunakan nested loop (perulangan bersarang) dalam Python. Teknik ini sangat berguna untuk manipulasi data berbentuk tabel atau grid.

👩‍💻 Dibuat oleh

🖊 Nama: Layyinnida Indah Ramadhan

📅 Tanggal: 14/04/2025

💡 Tugas Bahasa Pemrograman 2 ke 4
