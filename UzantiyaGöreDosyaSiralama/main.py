import os
def duzenle():
    klasor = input("Düzenlenecek Klasör: ")#düzenlenmesi istenilen dosyanın tam yolu
    dosyalar = [] #dosyalar burada depolanacak
    uzantilar = [] #uzantilar burada depolanacak
    def list_dir():
        for dosya in os.listdir(klasor):
            if os.path.isdir(os.path.join(klasor,dosya)): #dosyamız klasör mü
                continue
            if dosya.startswith("."): #dosyamız gizli klasör mü
                continue
            else:
                dosyalar.append(dosya)
    list_dir()
    #uzantıları alma
    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1]
        if uzanti in uzantilar: #uzantı daha önce eklendi mi onu kontrol ettiğim nokta
            continue
        else:
            uzantilar.append(uzanti)
    for uzanti in uzantilar:  #klasörlerler bu döngü ile oluşturuluyor
        if os.path.isdir(os.path.join(klasor,uzanti)):
            continue
        else:
            os.mkdir(os.path.join(klasor,uzanti))
    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1]
        os.rename(os.path.join(klasor,dosya),os.path.join(klasor,uzanti,dosya))
duzenle()
