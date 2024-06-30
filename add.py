import os
import asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import InviteToChannelRequest
import tkinter as tk
from tkinter import messagebox, simpledialog
import webbrowser
import requests
from PIL import Image, ImageTk  # Menambahkan PIL untuk memanipulasi gambar

# Link Saluran YouTube untuk langganan
YOUTUBE_CHANNEL_URL = "https://www.youtube.com/channel/UCYOURCHANNELID"  # Ganti dengan link saluran YouTube Anda
YOUTUBE_CHANNEL_ID = "UCYOURCHANNELID"  # Ganti dengan ID saluran YouTube Anda

# Gambar untuk proses penambahan member
LOADING_IMAGE_PATH = "loading.gif"  # Ganti dengan path gambar animasi atau statis yang menarik

# Fungsi untuk memeriksa apakah pengguna telah berlangganan ke saluran YouTube
def check_youtube_subscription(youtube_channel_id):
    # API Key YouTube
    api_key = "YOUR_YOUTUBE_API_KEY"  # Ganti dengan API Key YouTube Anda
    youtube_api_url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails,statistics&id={youtube_channel_id}&key={api_key}"
    response = requests.get(youtube_api_url)
    data = response.json()

    # Memeriksa apakah API key valid dan mendapatkan status subscribe
    if "items" in data and len(data["items"]) > 0:
        return True
    return False

# Fungsi untuk mengambil ID member dari grup/channel dan menyimpannya ke members.txt
async def fetch_members_from_group(client, link):
    try:
        # Mendapatkan grup atau channel dari link
        invite = await client(ImportChatInviteRequest(link.split('/')[-1]))
        entity = invite.chat
        
        # Mengambil daftar member
        members = await client.get_participants(entity)
        
        # Menyimpan ID member ke members.txt
        with open('members.txt', 'w') as file:
            for member in members:
                file.write(f'{member.id}\n')
        
        print("Members fetched and saved to members.txt")
        messagebox.showinfo("Success", "Members have been fetched and saved to members.txt")
        
        # Kembali ke menu utama
        show_main_menu()

    except Exception as e:
        print(f"Error fetching members: {e}")
        messagebox.showerror("Error", f"Error fetching members: {e}")

# Fungsi untuk menambahkan member ke grup/channel dari members.txt
async def add_users_to_group(client, link):
    try:
        # Membaca ID member dari members.txt
        with open('members.txt', 'r') as file:
            members = [int(line.strip()) for line in file.readlines()]
        
        # Memeriksa apakah pengguna telah berlangganan YouTube
        if not check_youtube_subscription(YOUTUBE_CHANNEL_ID):
            # Menampilkan jendela untuk meminta pengguna untuk berlangganan YouTube
            response = messagebox.askyesno("Subscribe to YouTube", f"Please subscribe to our YouTube channel: {YOUTUBE_CHANNEL_URL}\n\nAfter subscribing, click 'Yes' to continue adding members.")
            if not response:
                messagebox.showwarning("Warning", "You need to subscribe to the YouTube channel to continue.")
                return
            
            # Membuka URL YouTube di browser
            webbrowser.open(YOUTUBE_CHANNEL_URL)
            
            # Menunggu beberapa detik untuk memberikan waktu kepada pengguna untuk berlangganan
            await asyncio.sleep(10)  # Tunggu selama 10 detik, sesuaikan jika perlu
            
            # Menampilkan jendela terima kasih setelah berlangganan
            messagebox.showinfo("Thank You", "Thank you for subscribing! Now the process of adding members will begin.")
        else:
            # Langganan sudah ada, lanjutkan proses
            messagebox.showinfo("Info", "You are already subscribed! Proceeding to add members.")

        # Tampilkan jendela loading saat menambahkan member
        show_loading_window()
        
        # Mendapatkan grup atau channel dari link
        invite = await client(ImportChatInviteRequest(link.split('/')[-1]))
        entity = invite.chat
        
        # Menambahkan member ke grup atau channel
        for member_id in members:
            await client(InviteToChannelRequest(entity, [member_id]))
        
        print("Members added to the group/channel")
        messagebox.showinfo("Success", "Members have been added to the group/channel")
        
        # Tutup jendela loading
        loading_window.destroy()
        
        # Kembali ke menu utama
        show_main_menu()

    except Exception as e:
        print(f"Error adding members: {e}")
        messagebox.showerror("Error", f"Error adding members: {e}")

        # Tutup jendela loading jika ada error
        loading_window.destroy()

# Fungsi untuk menampilkan jendela loading
def show_loading_window():
    global loading_window

    # Menyiapkan jendela loading
    loading_window = tk.Toplevel(window)
    loading_window.title("Processing")
    loading_window.geometry("300x150")
    loading_window.configure(bg="#f8f9fa")

    tk.Label(loading_window, text="Adding members, please wait...", bg="#f8f9fa", font=("Helvetica", 12)).pack(pady=10)

    # Menambahkan gambar loading
    img = Image.open(LOADING_IMAGE_PATH)
    img = img.resize((100, 100), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img)
    tk.Label(loading_window, image=img_tk, bg="#f8f9fa").pack(pady=10)
    
    loading_window.mainloop()

# Fungsi untuk menampilkan menu utama
def show_main_menu():
    def fetch_members():
        link = link_entry.get()
        if link:
            asyncio.run(fetch_members_from_group(client, link))
        else:
            messagebox.showwarning("Warning", "Please enter a group/channel link")

    def add_members():
        link = link_entry.get()
        if link:
            asyncio.run(add_users_to_group(client, link))
        else:
            messagebox.showwarning("Warning", "Please enter a group/channel link")

    # Menyiapkan jendela utama
    global window
    window = tk.Tk()
    window.title("Telegram Adder")

    tk.Label(window, text="Enter group/channel link").pack(pady=10)
    global link_entry
    link_entry = tk.Entry(window, width=50)
    link_entry.pack(pady=5)

    tk.Button(window, text="Fetch Members", command=fetch_members).pack(pady=10)
    tk.Button(window, text="Add Members", command=add_members).pack(pady=10)

    window.mainloop()

# Fungsi untuk memulai aplikasi
def main():
    global client

    # Mengambil API ID, API Hash, dan nomor telepon dari pengguna
    api_id = simpledialog.askstring("API ID", "Enter your API ID:")
    api_hash = simpledialog.askstring("API Hash", "Enter your API Hash:")
    phone_number = simpledialog.askstring("Phone Number", "Enter your phone number (with country code, e.g. +1234567890):")

    # Menginisialisasi klien Telegram
    client = TelegramClient(phone_number, api_id, api_hash)
    
    async def start_client():
        await client.start()
        print("Client started")
        show_main_menu()
    
    client.loop.run_until_complete(start_client())

if __name__ == "__main__":
    main()
