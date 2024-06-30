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

1. **Python 3.7+**
   - [Download Python](https://www.python.org/downloads/) dan pastikan `python` dan `pip` terpasang dengan benar.

2. **Paket Python**
   - Install paket yang diperlukan dengan perintah berikut:
     ```bash
     pip install telethon requests pillow
     ```

3. **API Key YouTube**
   - Dapatkan dari [Google Developers Console](https://console.developers.google.com/).

4. **Link dan ID Saluran YouTube**
   - Salin dari YouTube Studio.

5. **Gambar `loading.gif`**
   - Siapkan gambar animasi atau statis dengan nama `loading.gif` di direktori yang sama dengan script.

## Instalasi

1. **Download Script:**
   - Clone repository atau unduh file `tele_adder.py` dari [link ini](#).

2. **Siapkan API Key dan Saluran YouTube:**
   - Ikuti langkah-langkah berikut untuk mendapatkan API Key YouTube dan ID Saluran:

     **Mendapatkan API Key:**
     - Masuk ke [Google Developers Console](https://console.developers.google.com/).
     - Buat proyek baru atau pilih proyek yang ada.
     - Aktifkan **YouTube Data API v3** dari Library.
     - Buat **API Key** di tab Credentials dan salin key tersebut.

     **Mendapatkan ID Saluran:**
     - Kunjungi [YouTube Studio](https://studio.youtube.com/).
     - Buka saluran Anda dan salin ID dari URL saluran.

3. **Edit File `tele_adder.py`:**
   - Masukkan **API Key YouTube** dan **ID Saluran** ke dalam script.
   - Ganti path `LOADING_IMAGE_PATH` dengan lokasi gambar animasi yang ingin digunakan untuk loading.

   ```python
   # Link Saluran YouTube untuk langganan
   YOUTUBE_CHANNEL_URL = "https://www.youtube.com/channel/UCYOURCHANNELID"  # Ganti dengan link saluran YouTube Anda
   YOUTUBE_CHANNEL_ID = "UCYOURCHANNELID"  # Ganti dengan ID saluran YouTube Anda

   # API Key YouTube
   api_key = "YOUR_YOUTUBE_API_KEY"  # Ganti dengan API Key YouTube Anda
