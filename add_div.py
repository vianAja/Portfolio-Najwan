from bs4 import BeautifulSoup
import convert_pdf_to_img
import json
import os
import re


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

def link_publisher(file):
    with open(file, 'r') as f:
        daftar_link_publisher = {}
        for data in f.readlines():
            certif_name, link_certif = data.rsplit(' - ', 1)
            daftar_link_publisher[certif_name] = link_certif.strip()
        return daftar_link_publisher

def main(filename):
    path_certificate = os.path.join('images', 'sertif')
    daftar_publisher = os.listdir(path_certificate)
    div_name = select_div()
    orig_prettify = BeautifulSoup.prettify
    r = re.compile(r'^(\s*)', re.MULTILINE)
    def prettify(self, encoding=None, formatter="minimal", indent_width=4):
        return r.sub(r'\1' * indent_width, orig_prettify(self, encoding, formatter))
    BeautifulSoup.prettify = prettify

    for publisher in daftar_publisher:
        full_path = os.path.join(path_certificate, publisher)
        
        daftar_certif = os.listdir(full_path)
        
        ## mengambil link publisher dari certif nya
        file_link_publisher = [daftar_certif.pop(i) for i,d in enumerate(daftar_certif) if 'link publisher' in d.lower()][0]
        daftar_link_publisher = link_publisher(os.path.join(full_path, file_link_publisher))
        
        with open(filename, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
        
        # Cari div target pertama yang ada
        global daftar_div
        daftar_div = soup.find_all("div", class_=div_name)
        
        ## Seleksi agar certificate tidak double, memastikan hanya certif baru yg di add
        for div in daftar_div:
            name_sertif = ' '.join(div.find('h1').text.replace('\n', '').split())
            certif_old = [
                sertif for sertif, _ in daftar_link_publisher.items() if name_sertif in sertif
            ]
            if certif_old:
                del daftar_link_publisher[certif_old[0]]
        
        print(json.dumps(daftar_link_publisher, indent=4))
        
        for certif, link in daftar_link_publisher.items():
            file = [d for d in daftar_certif if certif in d]
            if file:
                full_path_file = os.path.join(full_path, file[0])
                if file[0].endswith('.pdf'):
                    continue
                    convert_pdf_to_img.main(full_path_file)
                
                # Buat duplikat dari div target    h2_tag = daftar_div.find("h2")
                new_div = BeautifulSoup(str(daftar_div[-1]), "html.parser")  # Duplikasi elemen dengan kontennya
                judul_certificate = new_div.find("h1")
                publisher_tag = new_div.find("h3")
                tahun_terbit = new_div.find("p")
                link_publisher_tag = new_div.find("a")
                img_tag = new_div.find("img")
                
                if link_publisher_tag:
                    link_publisher_tag['href'] = link
                # Ganti src pada <img>
                if img_tag:
                    img_tag['src'] = full_path_file.replace('\\', '/')
                if tahun_terbit:
                    tahun_terbit.string = '2024 - 2025'
                if publisher_tag:
                    publisher_tag.string = f'By {publisher}'
                if judul_certificate:
                    judul_certificate.string = certif
                daftar_div[-1].insert_after(new_div)
                
                print(f"Berhasil menambahkan {certif}")
            else:
                print('tidak ada,', certif)
                print('Coba cek, apakah file Certificate nya ada')
        
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(soup.prettify(
                formatter='html'
            )))
    



if __name__ == "__main__":
    filename = 'about.html'
    main(filename)
    #add_div("about_copy.html", "item-certificate") 