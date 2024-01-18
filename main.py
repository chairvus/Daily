menu = {}
file_path = 'menu.json'
waktu = datetime.now()
format_waktu = waktu.strftime("%Y-%m-%d %H:%M:%S")
kodetransaksi = waktu.strftime("%Y%m%d%H%M%S")

try:
    with open(file_path, 'r') as file:
        menu = json.load(file)

except Exception as e:
    print(f"Terjadi kesalahan : {e}")

print()
print('|=========================================|')
print('|                DAFTAR MENU              |')
print('|=========================================|')
print(f"|{'  Kode':7} | {'     Menu':15} | {'    Harga':8}    |")
print('|=========================================|')
for item, info in menu.items():
    print(f"|   {info['kode']:4} | {item:14}  | Rp{info['harga']:8}   |")
print('|=========================================|')


def take_order(menu):
    nama = input("Nama Pelanggan : ")
    orders = []
    total_harga = 0
    uang_pelanggan = 0
    print("Masukan kode menu dan porsi (Contoh : 3,2)")
    print('(Pilih nomor 0 untuk selesai)')
    while True:
        try:
            order = input("Pesanan : ")
            if order.lower() == '0':
                print(f"Total Harga  : Rp {total_harga}")
                uang_pelanggan = int(input("Masukan Jumlah Uang Bayar : Rp "))
                break
            kode_pesanan, porsi = order.split(",")
            if kode_pesanan in [info['kode'] for info in menu.values()]:
                item_terpilih = next(item for item, info in menu.items() if info['kode'] == kode_pesanan)
                harga_terpilih = menu[item_terpilih]['harga']
                print(f"Anda memesan {item_terpilih} dengan harga Rp{harga_terpilih}.")
                if item in menu:
                    harga = harga_terpilih * int(porsi)
                    total_harga += harga
                    orders.append({'item': item_terpilih, 'porsi': int(porsi), 'harga': harga})
                else:
                    print(f"Item {item} tidak tersedia")
            else:
                print("Kode menu tidak valid.")
        except:
            print("Format input salah")

    return nama, orders, total_harga, uang_pelanggan


def save_order(nama_pelanggan, orders, total_harga):
    order_details = {
        'Nama Pelanggan': nama_pelanggan,
        'orders': orders,
        'total_harga': total_harga,
    }
    with open('pesanan.txt', 'a') as file:
        file.write(json.dumps(order_details) + "\n")


def read_order():
    with open('pesanan.txt', 'r') as file:
        lines = file.readlines()

        baris_terakhir = lines[-1]
        order_details = json.loads(baris_terakhir)
        print()
        print('|==========================================|')
        print(f'|Kode Transaksi : {kodetransaksi}           |')
        print('|==========================================|')
        print(f"|Nama Pelanggan: {order_details['Nama Pelanggan']:15}           |")
        print('|==========================================|')
        print(f'|Tanggal: {format_waktu}              |')
        print('|==========================================|')
        print('|              Detail Pesanan              |')
        print('|==========================================|')
        print(f"|{'         Menu':20} | {'Porsi':2} |  {'  Harga  ':6} |")
        print('|==========================================|')
        for order in order_details['orders']:
            print(f"|   {order['item']:17} |{order['porsi']:5}  | Rp{order['harga']:8} |")
            print('|==========================================|')
        print(f"|Total Harga {'':15}    Rp{order_details['total_harga']:8} |")
        print('|==========================================|')
        print(f'|Total Harga : Rp {total_harga:<25}|')
        print('|==========================================|')
        print(f'|Uang Bayar  : Rp {uang_pelanggan:<25}|')
        print('|==========================================|')
        print(f'|Kembalian   : Rp {uang_pelanggan - total_harga:<25}|')
        print('|==========================================|')
        print('|               Terimakasih                |')
        print('|==========================================|')


def kembalian():
    print("a")


nama_pelanggan, order, total_harga, uang_pelanggan = take_order(menu)
save_order(nama_pelanggan, order, total_harga)
read_order()
print()