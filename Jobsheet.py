import json
from datetime import datetime

menu = {}
file_path = 'menu.json'
waktu = datetime.now()
format_waktu = waktu.strftime("%Y-%m-%d %H:%M:%S")
kodetransaksi = waktu.strftime("%Y%m%d%H%M%S")

try :
    with open(file_path, 'r') as file:
        menu = json.load(file)

except Exception as e :
    print(f"Terjadi Kesalahan: {e}")

#menampilkan menu
print()
print('|===============================================|')
print('|                  DAFTAR MENU                  |')
print('|===============================================|')
print(f"|{'   Kode':7} | {'      Menu':15} | {'        Harga   ':8}   |")
print('|===============================================|')
for item, info in menu.items():
    print(f"|    {info[  'kode']:4}  | {   item:14}   | Rp{info['harga']:8}      |")
print('|===============================================|')

#fungsi pesanan pelanggan
def take_order(menu):
    name = input("Nama Pelanggan : ")
    orders = []
    total_harga = 0
    uang_pelanggan = 0
    print("Masukan kode menu dan porsi(Contoh : 3, 2)")
    print('(Pilih nomor 0 untuk selesai')
    while True:
        try:
            order = input("Pesanan: ")
            if order.lower() == '0':
                print(f"total harga              : Rp {total_harga}")
                uang_pelanggan = int(input("masukan uang: Rp"))
                break
            kode_pesanan, porsi = order.split(", ")
            if kode_pesanan in [info['kode'] for info in menu.values()]:
                item_terpilih = next(item for item, info in menu.items() if info['kode'] == kode_pesanan)
                harga_terpilih = menu[item_terpilih]['harga']
                print(f"Anda memesan {item_terpilih} dengan harga Rp{harga_terpilih}.")
                if item in menu:
                    harga = harga_terpilih * int(porsi)
                    total_harga += harga
                    orders.append({'item': item_terpilih, 'porsi': int(porsi), 'harga': harga})
                else:
                    print(f"item {item} tidak tersedia di menu.")
            else:
                print("Kode menu tidak valid.")
        except:
            print("Format input salah.")
    return name, orders, total_harga, uang_pelanggan

#fungsi menyimpan pesanan
def save_order(kodetransaksi, nama_pelanggan, orders, total_harga, kembalian):
    order_details = {
        'kode transaksi': kodetransaksi,
        'Nama Pelanggan': nama_pelanggan,
        'orders': orders,
        'total harga': total_harga,
        'kembalian': kembalian
    }
    with open('pesanan.txt', 'a') as file:
        file.write(json.dumps(order_details) + "\n")

#fungsi membaca dan menyimpan pesanan ke file
def change(total, uang):
    kembalian = uang_pelanggan - total
    return int(kembalian)

def read_orders():
    with open('pesanan.txt', 'r') as file:
        lines = file.readlines()
        baris_terakhir = lines[-1]
        order_details = json.loads(baris_terakhir)
        print()
        print('|==============================================================|')
        print(f'|Kode Transaksi : {kodetransaksi}                               |')
        print('|==============================================================|')
        print(f"|Nama Pelanggan: {order_details['Nama Pelanggan']:46}|")
        print('|==============================================================|')
        print(f'|Tanggal: {format_waktu}                                  |')
        print('|==============================================================|')
        print("|                       Detail Pesanan                         |")
        print('|==============================================================|')
        print(f"|{'Menu':17}   |    {'Porsi':8} |        {'Harga':19}|")
        print('|==============================================================|')
        for order in order_details['orders']:
            print(f'|  {order['item']:16}  |      {order['porsi']:6} |                    Rp{order['harga']:5}|')
            print('|==============================================================|')
        print(f"|Total Harga: {'':15}                           Rp{order_details['total harga']:3}|")
        print('|==============================================================|')
        print(f'|Uang Pelanggan  :                                      Rp{uang_pelanggan:>4}|')
        print('|==============================================================|')
        print(f'|Kembalian   :                                          Rp{kembalian:5}|')
        print('|==============================================================|')
        print('|                         Terima Kasih                         |')
        print('|==============================================================|')

#penggunaan fungsi
nama_pelanggan, orders, total_harga, uang_pelanggan = take_order(menu)
kembalian = change(total_harga, uang_pelanggan)
save_order(kodetransaksi, nama_pelanggan, orders, total_harga, kembalian)
read_orders()
print()
