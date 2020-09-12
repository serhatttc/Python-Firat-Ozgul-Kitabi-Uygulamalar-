# -*- coding: utf-8 -*-

class Çalışan(): # öncelikle sınıfı tanımlıyoruz.
    _personel = [] # personel adlı sınıf niteliği ekliyoruz.
    
    def __init__(self,isim):
        self._isim = isim# isim parametresini sınıfın başka bölgelerinde de kullanmak için yaptık.
        self._personelEkle()
        
    def personelEkle(self):
        self._personel.append(self._isim)
        print("{} adlı kişi personele eklendi.".format(self._isim))
        
    @classmethod    
    def personeliGoruntule(cls):
        print("Personel Listesi : ")
        for kisi in cls._personel:
            print(kisi)
            
    @property
    def isim(self):
        return self._isim
    
    @isim.setter
    def isim(self,yeniİsim):
        kişi = self._personel.index(self._isim)
        self._personel[kişi] = yeniİsim
        print("yeni isim :",yeniİsim)