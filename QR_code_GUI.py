import tkinter as tk
from tkinter import filedialog
import qrcode

def generiraj_qr_kod():
    tekst = tekst_unos.get()
    naziv_datoteke = naziv_datoteke_unos.get()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(tekst)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    if save_path:
        img.save(save_path)
        status_label.config(text=f"QR kod je uspješno spremljen u datoteku {save_path}")

# Stvaranje Tkinter aplikacije
root = tk.Tk()
root.title("Generator QR koda")

# Polje za unos teksta
tekst_label = tk.Label(root, text="Unesite tekst koji želite pretvoriti u QR kod:")
tekst_label.pack()
tekst_unos = tk.Entry(root)
tekst_unos.pack()

# Polje za unos naziva datoteke
naziv_datoteke_label = tk.Label(root, text="Unesite naziv datoteke za spremanje QR koda:")
naziv_datoteke_label.pack()
naziv_datoteke_unos = tk.Entry(root)
naziv_datoteke_unos.pack()

# Gumb za generiranje QR koda
generiraj_gumb = tk.Button(root, text="Generiraj QR kod", command=generiraj_qr_kod)
generiraj_gumb.pack()

# Statusna oznaka
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
