import tkinter as tk
from tkinter import ttk
import csv

# Standart bilgilerini csv dosyasından okuma fonksiyonu
def load_standards(filename):
    standards = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Başlık satırını atla
        for row in reader:
            # Standart bilgilerini alıyoruz (kategori artık yok)
            standards.append({'name': row[0], 'description': row[1]})
    return standards

# Standart bilgilerini görüntüleme fonksiyonu
def display_info(event):
    selected_standard = combobox.get()
    for standard in standards:
        if standard['name'] == selected_standard:
            # Text widget'ına bilgiyi ekle
            info_text.delete(1.0, tk.END)  # Eski bilgiyi temizle
            info_text.insert(tk.END, standard['description'])  # Yeni açıklamayı ekle
            break

# Kullanıcı tarafından eklenen standardı CSV dosyasına kaydetme
def add_new_standard():
    name = name_entry.get()
    description = description_text.get(1.0, tk.END).strip()

    if name and description:
        # Yeni veriyi CSV dosyasına ekle
        with open('standards.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, description])

        # Listede yeni standardı ekle
        standards.append({'name': name, 'description': description})
        update_combobox_values()

        # Başarı mesajı
        result_label.config(text="Yeni standart başarıyla eklendi!", fg="green")
        
        # Formu sıfırla
        name_entry.delete(0, tk.END)
        description_text.delete(1.0, tk.END)

    else:
        result_label.config(text="Lütfen tüm alanları doldurun!", fg="#f07373")

# Standartları combobox'a ekleme fonksiyonu
def update_combobox_values():
    standard_names = [standard['name'] for standard in standards]
    combobox['values'] = standard_names
    if standard_names:
        combobox.set(standard_names[0])  # İlk standardı seç

# Tkinter pencere ayarları
root = tk.Tk()
root.title("Standart Bilgisi")

# Pencereyi tam ortalamak için ekran boyutlarını alalım
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Pencereyi ortalama
window_width = 720
window_height = 700
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Pencere boyutlarını ve pozisyonunu belirleme
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
root.config(bg="#35374B")  # Arka plan rengini açık gri yapalım

# Veri yükleme
filename = 'standards.csv'  # CSV dosyanızın ismini buraya yazın
standards = load_standards(filename)

# Font ve stil tanımlamaları
font_large = ("Arial", 16, "bold")
font_medium = ("Arial", 14)
font_small = ("Arial", 12)

# Label ve diğer widget'ların font rengini beyaz yapma
font_color = "white"

# Dropdown menü
combobox_label = tk.Label(root, text="Standart Seçin:", font=font_large, fg=font_color, bg="#35374B")
combobox_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

standard_names = [standard['name'] for standard in standards]
combobox = ttk.Combobox(root, values=standard_names, width=50, font=font_medium)
combobox.grid(row=0, column=1, padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", display_info)

# Kaydırılabilir alan
info_label = tk.Label(root, text="Standart Bilgisi:", font=font_medium, fg=font_color, bg="#35374B")
info_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

# Text widget'ı ekleyelim, kaydırma çubuğu ile
info_text_frame = tk.Frame(root)
info_text_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Scrollbar ekleme
scrollbar = tk.Scrollbar(info_text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

info_text = tk.Text(info_text_frame, wrap=tk.WORD, width=75, height=10, yscrollcommand=scrollbar.set, font=font_small, bd=2, relief="solid")
info_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=info_text.yview)

# Kullanıcıdan yeni standart eklemek için form
new_standard_label = tk.Label(root, text="Yeni Standart Ekle", font=font_large, fg=font_color, bg="#35374B")
new_standard_label.grid(row=3, column=0, columnspan=2, padx=10, pady=20, sticky="w")

name_label = tk.Label(root, text="Standart Adı:", font=font_medium, fg=font_color, bg="#35374B")
name_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(root, width=50, font=font_small, bd=2, relief="solid")
name_entry.grid(row=4, column=1, padx=10, pady=5)

description_label = tk.Label(root, text="Açıklama:", font=font_medium, fg=font_color, bg="#35374B")
description_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
description_text = tk.Text(root, wrap=tk.WORD, width=50, height=6, font=font_small, bd=2, relief="solid")
description_text.grid(row=5, column=1, padx=10, pady=5)

# Yeni standardı eklemek için buton
add_button = tk.Button(root, text="Standart Ekle", command=add_new_standard, font=font_medium, bg="#35374B", fg="white", bd=0, relief="raised")
add_button.grid(row=6, column=0, columnspan=2, pady=20)

# Sonuç mesajı
result_label = tk.Label(root, text="", font=font_medium, fg=font_color, bg="#35374B")
result_label.grid(row=7, column=0, columnspan=2, pady=10)

# Standartları combobox'a ekleme
update_combobox_values()

# Uygulamayı çalıştır
root.mainloop()
