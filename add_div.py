from bs4 import BeautifulSoup
import os
import re



def add_div(filename, div_name, url_img, link_publisher, tahun):
    # Formatting Indent file HTML
    orig_prettify = BeautifulSoup.prettify
    r = re.compile(r'^(\s*)', re.MULTILINE)
    def prettify(self, encoding=None, formatter="minimal", indent_width=4):
        return r.sub(r'\1' * indent_width, orig_prettify(self, encoding, formatter))
    BeautifulSoup.prettify = prettify

    # Buka file index.html
    with open(filename, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Cari div target pertama yang ada
    target_div = soup.find_all("div", class_=div_name)
    print(target_div)
    if target_div:
        # Buat duplikat dari div target    h2_tag = target_div.find("h2")
        new_div = BeautifulSoup(str(target_div[-1]), "html.parser")  # Duplikasi elemen dengan kontennya
        h3_tag = new_div.find("h3")
        p_tag = new_div.find("p")
        a_tag = new_div.find("a")
        img_tag = new_div.find("img")
        
        if a_tag:
            a_tag['hre'] = link_publisher
        # Ganti src pada <img>
        if img_tag:
            img_tag['src'] = url_img
        if p_tag:
            p_tag.string = tahun
        if h3_tag:
            h3_tag.string = filename.split(' ', 1)[-1]

        # Masukkan duplikasi setelah div yang ditemukan
        target_div[-1].insert_after(new_div)
        
        # Simpan kembali ke file index.html
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(soup.prettify(
                formatter='html'
            )))
        

        print("Div baru berhasil ditambahkan tepat setelah div sebelumnya!")
    else:
        print("Div tidak ditemukan.")


def select_div():
    while True:
        print('/n================================================')
        print('Pilih Func')
        print('================================================')
        print('1. Update Certificate')
        print('2. Update Project')
        print('================================================\n')
        try:
            option = int(input('  => '))
            if option == 1: return "item-certificate"
            elif option == 2: return 'belum ada'
        except Exception as e:
            print('Error:', e)

def main(filename):
    path_certificate = os.path.join('images', 'sertif')
    daftar_publisher = os.listdir(path_certificate)
    div_name = select_div()
    
    for publisher in daftar_publisher:
        full_path = os.path.join(path_certificate, publisher)
        
        daftar_certif = os.listdir(full_path)
        link_publisher = [daftar_certif.pop(i) for i,d in enumerate(daftar_certif) if 'link publisher' in d.lower()]
        with open(filename, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
        
        # Cari div target pertama yang ada
        daftar_div = soup.find_all("div", class_=div_name)
        
        
        daftar_certif_new = []
        for div in daftar_div:
            
        daftar_certif_new = [
            [certif for certif in daftar_certif if div.find('h1').text in certif] for div in daftar_div
        ]
        
        
        
        daftar_certif_new = [d.find('h1').text for d in daftar_div]
        print('certif baru yg berlum di tambah\n', daftar_certif_new)

if __name__ == "__main__":
    filename = 'about_copy.html'
    main(filename)
    #add_div("about_copy.html", "item-certificate") 