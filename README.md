# Telegram Adder

## Deskripsi

Script **Telegram Adder** adalah alat untuk menambahkan member ke grup atau saluran Telegram dengan menggunakan data dari file `members.txt`. Sebelum menjalankan proses penambahan member, pengguna diharuskan untuk berlangganan saluran YouTube tertentu. Script ini juga menyediakan opsi untuk mengambil member dari grup atau saluran lain dan menyimpannya ke dalam file `members.txt`.

## Fitur

- **Ambil Member:** Mengambil ID member dari grup atau saluran Telegram lain dan menyimpannya ke dalam file `members.txt`.
- **Tambah Member:** Menambahkan member dari file `members.txt` ke grup atau saluran Telegram.
- **Verifikasi Langganan YouTube:** Memeriksa apakah pengguna telah berlangganan saluran YouTube sebelum melanjutkan proses penambahan member.
- **Gambar Loading:** Menampilkan gambar animasi saat proses penambahan member sedang berlangsung.
- **Pengguna** akan dialihkan untuk berlangganan saluran YouTube jika belum melakukannya.

## Persyaratan

1. ***Python 3.7+***
   - [Download Python](https://www.python.org/downloads/) dan pastikan `python` dan `pip` terpasang dengan benar.

2. ***Paket Python**
   - Install paket yang diperlukan dengan perintah berikut:
     ```bash
     pip install telethon requests pillow
     ```
3. ***Clone This Script***
     ```bash
     git clone https://github.com/kdsmedia/teladd
     ```
3. ***Run***
     ```bash
     add.py
     ```
