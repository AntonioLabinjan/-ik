import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
import barcode
from barcode.writer import ImageWriter


def generiraj_barkod():
  tekst = unos_polje.get()
  tip_barkoda = vrsta_barkoda.get()

  if tip_barkoda.lower() not in ("ean13", "code128"):
    status_label.config(text="Nepodržani tip barkoda")
    return

  if not tekst:
    status_label.config(text="Unesite tekst za generiranje barkoda")
    return

  try:
    kod = barcode.get_barcode_class(tip_barkoda.lower())
  except barcode.errors.BarcodeNotFoundError:
    status_label.config(text="Greška pri dohvaćanju klase barkoda")
    return

  kod_instance = kod(tekst, writer=ImageWriter())
  img = kod_instance.render()

  save_path = filedialog.asksaveasfilename(defaultextension=".png")
  if save_path:
    img.save(save_path)
    status_label.config(
      text="Barkod je uspješno spremljen u datoteku {}".format(save_path))


def generiraj_qr_kod():
  tekst = tekst_unos.get()

  if not tekst:
    status_label.config(text="Unesite tekst ili URL za generiranje QR koda")
    return

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
    status_label.config(
      text=f"QR kod je uspješno spremljen u datoteku {save_path}")


root = tk.Tk()
root.title("Generiranje barkoda i QR kodova")

barkod_label = tk.Label(root, text="Unesite tekst za generiranje barkoda:")
barkod_label.pack()
unos_polje = tk.Entry(root)
unos_polje.pack()

vrsta_barkoda_label = tk.Label(root, text="Odaberite vrstu barkoda:")
vrsta_barkoda_label.pack()
vrsta_barkoda = tk.StringVar()
vrsta_barkoda.set("ean13")
vrste_barkoda_optionmenu = tk.OptionMenu(root, vrsta_barkoda, "ean13",
                                         "code128")
vrste_barkoda_optionmenu.pack()

generiraj_barkod_gumb = tk.Button(root,
                                  text="Generiraj barkod",
                                  command=generiraj_barkod)
generiraj_barkod_gumb.pack()

qr_label = tk.Label(root, text="Unesite tekst ili URL za generiranje QR koda:")
qr_label.pack()
tekst_unos = tk.Entry(root)
tekst_unos.pack()

generiraj_qr_gumb = tk.Button(root,
                              text="Generiraj QR kod",
                              command=generiraj_qr_kod)
generiraj_qr_gumb.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
