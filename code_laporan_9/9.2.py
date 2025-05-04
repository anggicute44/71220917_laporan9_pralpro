def menampilkansoal_dari_file(nama_file):
    print(f"nama file1: {nama_file}")
    
    try:
        with open(nama_file, 'r') as file:#membuka file
            #baris dibaca satu per satu
            for baris in file:
                if '||' in baris:
                    #Baris dipisahkan menjadi dua bagian menggunaka
                    soal, jwb_benar = baris.strip().split('||')
                    print(soal.strip() + "=")
                    #untuk memasukkan jawaban. strip() menghapus spasi, dan lower() mengubah input menjadi huruf kecil 
                    jwb_user = input("Jawab: ").strip().lower()
                    if jwb_user == jwb_benar.strip().lower():
                        print("Jawaban  benar!\n")
                    else:
                        print("Jawaban salah!\n")
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")

if __name__ == "__main__":
    nama_file = "laporan.txt"
    menampilkansoal_dari_file(nama_file)
