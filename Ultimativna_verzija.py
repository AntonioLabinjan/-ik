import tkinter as tk
from tkinter import filedialog
import qrcode
import barcode
from barcode import get_barcode_class, errors
from barcode.writer import ImageWriter
from tkinter import messagebox
from cryptography.fernet import Fernet

# Generiranje ključa za kriptiranje/dekriptiranje
def generiraj_kljuc():
    return Fernet.generate_key()

# Kriptiranje teksta
def kriptiraj_tekst(tekst, kljuc):
    f = Fernet(kljuc)
    return f.encrypt(tekst.encode())

# Dekriptiranje teksta
def dekriptiraj_tekst(tekst, kljuc):
    f = Fernet(kljuc)
    return f.decrypt(tekst).decode()

def generiraj_barkod():
    tekst = unos_polje.get()
    tip_barkoda = vrsta_barkoda.get()

    # Provjera je li odabrana podržana vrsta barkoda
    if tip_barkoda.lower() not in ("ean13", "code128"):
        status_label.config(text="Nepodržana vrsta barkoda")
        return

    # Provjera je li unesen tekst za generiranje barkoda
    if not tekst:
        status_label.config(text="Unesite tekst za generiranje barkoda")
        return

    # Odabir klase barkoda ovisno o odabranom tipu
    try:
        kod = barcode.get_barcode_class(tip_barkoda.lower())
    except barcode.errors.BarcodeNotFoundError:
        status_label.config(text="Greška pri dohvaćanju klase barkoda")
        return

    # Kriptiranje teksta prije generiranja barkoda
    kljuc = generiraj_kljuc()
    kriptirani_tekst = kriptiraj_tekst(tekst, kljuc)

    # Generiranje barkoda i spremanje slike
    kod_instance = kod(kriptirani_tekst, writer=ImageWriter())
    img = kod_instance.render()

    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    if save_path:
        img.save(save_path)
        status_label.config(text="Barkod je uspješno spremljen u datoteku {}".format(save_path))

    # Prikazivanje ključa korisniku
    messagebox.showinfo("Ključ za dekriptiranje", f"Ključ: {kljuc.decode()}")

def generiraj_qr_kod():
    tekst = tekst_unos.get()

    if not tekst:
        status_label.config(text="Unesite tekst ili URL za generiranje QR koda")
        return

    # Kriptiranje teksta prije generiranja QR koda
    kljuc = generiraj_kljuc()
    kriptirani_tekst = kriptiraj_tekst(tekst, kljuc)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(kriptirani_tekst)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    if save_path:
        img.save(save_path)
        status_label.config(text=f"QR kod je uspješno spremljen u datoteku {save_path}")

    # Prikazivanje ključa korisniku
    messagebox.showinfo("Ključ za dekriptiranje", f"Ključ: {kljuc.decode()}")

# Stvaranje Tkinter aplikacije
root = tk.Tk()
root.title("Generator kriptiranih barkoda i QR kodova")

# Polje za unos teksta za barkod
barkod_label = tk.Label(root, text="Unesite tekst za generiranje barkoda:")
barkod_label.pack()
unos_polje = tk.Entry(root)
unos_polje.pack()

# Odabir vrste barkoda
vrsta_barkoda_label = tk.Label(root, text="Odaberite vrstu barkoda:")
vrsta_barkoda_label.pack()
vrsta_barkoda = tk.StringVar()
vrsta_barkoda.set("ean13")  # Postavljamo početnu vrijednost
vrste_barkoda_optionmenu = tk.OptionMenu(root, vrsta_barkoda, "ean13", "code128")
vrste_barkoda_optionmenu.pack()

# Gumb za generiranje barkoda
generiraj_barkod_gumb = tk.Button(root, text="Generiraj barkod", command=generiraj_barkod)
generiraj_barkod_gumb.pack()

# Polje za unos teksta za QR kod
qr_label = tk.Label(root, text="Unesite tekst ili URL za generiranje QR koda:")
qr_label.pack()
tekst_unos = tk.Entry(root)
tekst_unos.pack()

# Gumb za generiranje QR koda
generiraj_qr_gumb = tk.Button(root, text="Generiraj QR kod", command=generiraj_qr_kod)
generiraj_qr_gumb.pack()

# Statusna oznaka
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
