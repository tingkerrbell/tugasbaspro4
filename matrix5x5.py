# matrix_generator.py

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