# daftar barang beserta harganya
daftar_barang = {
    "beras": 10000,
    "gula": 8000,
    "telur": 2000,
    "minyak goreng": 15000,
    "garam": 5000
}

# menampilkan daftar barang
print("daftar barang:")
for barang, harga in daftar_barang.items():
    print(f"{barang}: rp {harga}")

# input jumlah barang yang dibeli
total_belanja = 0
jumlah_barang = int(input("\nMasukan jumlah barang yang dibeli: "))

# menghitung total belanjaan
for i in range(jumlah_barang):
    barang = input (f"masukan nama barang ke-{i+1}: ")
    if barang in daftar_barang:
        total_belanja += daftar_barang[barang]
    else:
        print(f"{barang} tidak ada dalam daftar barang.")

# menampilkan total belanjaan
print(f"\nTotal belanjaan anda: rp {total_belanja}")