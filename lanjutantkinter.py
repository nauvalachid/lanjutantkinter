import tkinter as tk
import sqlite3

def submit_data():
    # Mengambil input nilai
    nama_mahasiswa = nama_entry.get()
    biologi = int(biologi_entry.get())
    fisika = int(fisika_entry.get())
    inggris = int(inggris_entry.get())

    # Menentukan jurusan yang diprediksi + berdasarkan skor tertinggi
    if biologi > fisika and biologi > inggris:
        prediksi_fakultas = "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        prediksi_fakultas = "Teknik"
    else:
        prediksi_fakultas = "Bahasa"

    # Membuat tabel
    conn = sqlite3.connect("lanjutantkinter.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS nilai_mahasiswa (
            id INTEGER PRIMARY KEY,
            nama_mahasiswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    """
    )
    # Memperbarui label hasil
    result_label.config(text="Prodi: " + prediksi_fakultas)

    # Menyimpan data dalam database SQLite
    cursor.execute(
        """
        INSERT INTO nilai_mahasiswa (nama_mahasiswa, biologi, fisika, inggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)
    """,
        (nama_mahasiswa, biologi, fisika, inggris, prediksi_fakultas),
    )
    conn.commit()
    conn.close()

# Membuat main window
window = tk.Tk()
window.title("Aplikasi Prediksi Prodi Pilihan")
window.geometry("1080x1080")

# Membuat kolom input
nama_label = tk.Label(window, text="Nama Siswa")
nama_label.grid(row=0, column=0, padx=10, pady=10)
nama_entry = tk.Entry(window)
nama_entry.grid(row=0, column=1, padx=10, pady=10)

biologi_label = tk.Label(window, text="Nilai Biologi")
biologi_label.grid(row=1, column=0, padx=10, pady=10)
biologi_entry = tk.Entry(window)
biologi_entry.grid(row=1, column=1, padx=10, pady=10)

fisika_label = tk.Label(window, text="Nilai Fisika")
fisika_label.grid(row=2, column=0, padx=10, pady=10)
fisika_entry = tk.Entry(window)
fisika_entry.grid(row=2, column=1, padx=10, pady=10)

inggris_label = tk.Label(window, text="Nilai Inggris")
inggris_label.grid(row=3, column=0, padx=10, pady=10)
inggris_entry = tk.Entry(window)
inggris_entry.grid(row=3, column=1, padx=10, pady=10)

# Membuat tombol prediksi
button_submit = tk.Button(window, text="Submit Nilai", command=submit_data)
button_submit.grid(row=4, column=0, columnspan=2, pady=10)

#membuat tampilan kolom menjadi ke tengah
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# Membuat label resul
result_label = tk.Label(window, text="Prodi: ")
result_label.grid(row=5, columnspan=2)

window.mainloop()