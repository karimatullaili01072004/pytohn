# Daftar barang beserta harganya
daftar_barang = {
    "Beras": 10000,
    "Gula" : 8000,
    "Telur": 2000,
    "Minyak goreng": 15000,
    "Garam" : 5000,
}

# Menampilkan daftar barang
print("Daftar Barang:")
for barang, harga in daftar_barang.items():
    print(f"{barang}: Rp {harga}")

# input jumlah barang yang dibeli
total_belanja = 0
jumlah_barang = int(input("\nMasukan jumlah barang yang dibeli: "))

# Menghitung total belanjaan
for i in range(jumlah_barang):
    barang = input(f"Masukan nama barang barang ke-{i+1}: ")
    if barang in daftar_barang:
        total_belanja += daftar_barang[barang]
    else:
            print(f"{barang} tidak ada dalam daftar barang.")

# Menampilkan total belanjaan
print(f"\Total belanjaan anda: Rp {total_belanja}")
