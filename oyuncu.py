# -*- coding: utf-8 -*-

import sys
import random
import time

class Oyuncu():
    def __init__(self,isim,can=5,enerji=100):
        self.isim=isim
        self.darbe=0
        self.can=can
        self.enerji=enerji
        
    def mevcutDurumuGörüntüle(self):
        print("darbe:",self.darbe)
        print("can:",self.can)
        print("enerji:",self.enerji)
        
    def saldır(self,rakip):
        print("Bir saldırı gerçekleştirdiniz.")
        print("saldırı sürüyor bekleyiniz.")
        
        for i in range(10):
            time.sleep(.3)
            print(".",end="",flush=True)
            
        sonuç = self.saldırıSonucunuHesapla()
        
        if sonuç == 0:
            print("\nSONUÇ:Kazanan taraf yok.")
        if sonuç == 1:
            print("\nSONUÇ:Rakibinizi darbelediniz.")
            self.darbele(rakip)
        if sonuç == 2:
            print("\nSONUÇ:Rakibinizden darbe aldınız.")
            self.darbele(self)
        
    def saldırıSonucunuHesapla(self):
        return random.randint(0,2)
    
    def kaç(self):
        print("Kaçılıyor...")
        for i in range(10):
            time.sleep(0.3)
            print("\n",flush=True)
        
        print("Rakibiniz sizi yakaladı.")
        
    def darbele(self,darbelenen):
        darbelenen.darbe += 1
        darbelenen.enerji -= 1
        if (darbelenen.darbe % 5) == 0:
            darbelenen.can -= 1
        if darbelenen.can < 1:
            darbelenen.enerji = 0
            print("{} oyunu kazandı.".format(self.isim))
            self.oyundanÇık()
    
    def oyundanÇık(self):
        print("Oyundan çıkılıyor...")
        sys.exit()
        
######################################
        
# Oyuncular
siz = Oyuncu("Ahmet")
rakip = Oyuncu("Mehmet")

# Oyun başlangıcı
while True:
    print("Şu anda rakibinizle karşı karşıyasınız.",
          "Yapmak istediğiniz hamle:",
          "Saldır: s",
          "Kaç:  k",
          "Çık:  q",sep="\n")
    
    hamle = input("\n> ")
    if hamle == "s":
        siz.saldır(rakip)
        
        print("Rakibinizin durumu.")
        rakip.mevcutDurumuGörüntüle()
        
        print("Sizin durumunuz.")
        siz.mevcutDurumuGörüntüle()
        
    if hamle == "k":
        siz.kaç()
        
    if hamle == "q":
        siz.oyundanÇık()