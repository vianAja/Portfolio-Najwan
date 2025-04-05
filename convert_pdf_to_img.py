import fitz  # PyMuPDF
import os
# Buka file PDF

def main(full_path):
    # file_name = "Certificate Data Manipulation with Pandas - Part 1.pdf"
    # dir_path = "images/sertif/"
    # full_path = os.path.join(dir_path, file_name)
    doc = fitz.open(full_path)

    # Loop setiap halaman dan simpan sebagai gambar
    for i, page in enumerate(doc):
        pix = page.get_pixmap()  # Render halaman jadi gambar
        pix.save(f"{full_path}.png")  # Simpan sebagai PNG
        print(f'Conver Berhasil, silahkan cek di {full_path}')
