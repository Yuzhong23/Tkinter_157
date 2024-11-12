import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    # Mengecek apakah ada input yang kosong
    for entry in entries:
        if entry.get() == "":
            messagebox.showwarning("Peringatan", "Semua nilai mata pelajaran harus diisi!")
            return  # Keluar dari fungsi jika ada input kosong

    # Jika semua input terisi, tampilkan hasil prediksi
    label_hasil.config(text="Prediksi Prodi: Teknologi Informasi", )

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("600x700")  # Menentukan ukuran jendela

# Menambahkan Baground Warna
root.configure(background="Light Grey")

# Label judul
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", background="Dark Grey", foreground="Black", font=("Times New Roman", 16))
label_judul.pack(pady=10)

# Membuat frame untuk menampung input nilai
frame_input = tk.Frame(root)
frame_input.pack(pady=20)

# Membuat 10 input nilai mata pelajaran
entries = []
for i in range(10):
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}")
    label.grid(row=i, column=0, padx=5, pady=5)
    entry = tk.Entry(frame_input)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

# Button untuk menampilkan hasil prediksi
btn_prediksi = tk.Button(root, text="Hasil Prediksi",background="light Grey", foreground="Black", command=hasil_prediksi)
btn_prediksi.pack(pady=10)


# Label untuk menampilkan hasil prediksi
label_hasil = tk.Label(root, text="", font=("Times New Roman", 14, ), background="light grey", foreground="Blue")
label_hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()


