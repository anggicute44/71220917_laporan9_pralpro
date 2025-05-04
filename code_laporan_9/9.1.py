def perbandinagan(file1, file2):
    try:
        #Membuka Dua File Secara bersamaan
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            baris1 = f1.readlines()
            baris2 = f2.readlines()


            #Mengecek Jumlah Baris pada kedua file
            if len(baris1) != len(baris2 ):
                print(f"File memiliki jumlah baris yang berbeda. {file1} memiliki{len(baris1)} baris, dan {file2} memiliki {len(baris2 )} lines.")

            #Membandingkan Isi Baris per Baris
            #zip(baris1, baris2) untuk menggabungkan isi kedua file secara berpasangan perbaris.
            #enumerate(..., start=1) menambahkan nomor baris dimulai dari 1
            for i, (line1, line2) in enumerate(zip(baris1, baris2 ), start=1):
                if line1 != line2:
                    print(f"Line {i} is different:")
                    print(f"File 1 ({file1}): {line1.strip()}")
                    print(f"File 2 ({file2}): {line2.strip()}")
                    print()  
    #output Menangani File Tidak Ditemukan
    except FileNotFoundError:
        print("Satu atau kedua file tidak ada.")


if __name__ == "__main__":
    file1 = input("Masukkan file pertama(txt): ")
    file2 = input("Masukkan file kedua(txt):")
    perbandinagan(file1, file2)
