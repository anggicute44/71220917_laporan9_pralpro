
# # handle = open('laporan.txt', 'r')  # Membuka file untuk dibaca

# # Membuka file untuk ditulis (jika sudah ada, akan ditimpa)
# with open('laporan.txt', 'w') as file:
#     file.write("Baris pertama.\n")
#     file.write("Baris kedua.\n")
    
    
#     # Menambahkan konten ke laporan.txt
# with open('laporan.txt', 'a+') as file:
#     # Menambahkan data baru
#     file.write("\ntambahan cuy\n")
    
#     # Membaca seluruh isi file
#     file.seek(0)
#     print("\n=== hello anggi===")
#     print(file.read())

# # # Isi lama file output.txt (jika ada) akan hilang dan diganti dengan teks di atas.

# # handle = open('laporan.txt', 'r')
# # for baris in handle:
# #     print(baris.strip())  # Menghilangkan '\n' (enter)
# # handle.close()


# # # Contoh membaca laporan.txt
# # with open('laporan.txt', 'r') as file:
# #     # Menggunakan read()
# #     print("=== read() ===")
# #     print(file.read())
    
# #     # Kembali ke awal file
# #     file.seek(0)
    
# #     # Menggunakan readline()
# #     print("\n=== readline() ===")
# #     print(file.readline(), end='')  # baca baris pertama
# #     print(file.readline(), end='')  # baca baris kedua
    
# #     file.seek(0)


# # Menulis ke tes.py
# with open('tes.py', 'w') as file:
#     file.write("print('Hello World')\n")
#     file.write("x = 10\n")
#     file.write("y = 20\n")
#     file.write("print(x + y)\n")


# # Import paket os
# import os
# # Nama file yang akan diubah
# nama_file = "laporan.txt"
# # Buka file dalam mode "r+"
# with open(nama_file, "r+") as file:
#     # Baca isi file
#     isi_file = file.read()
#     # Tulis isi file ke layar
#     print(isi_file)
#     # Hapus semua isi file
#     file.truncate()
#     # Tulis "Hello, World!" ke file
#     file.write("Hello, World!")
#     # Tutup file
#     file.close()


with open('laporan.txt', 'w') as fout:
    fout.write('Ini adalah contoh teks yang ditulis ke file.')
    fout.write('\nIni adalah baris baru.')