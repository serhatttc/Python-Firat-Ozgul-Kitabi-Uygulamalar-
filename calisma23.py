# -*- coding: utf-8 -*-
#                             -----  NESNE TABANLI PROGRAMLAMA  ---(DEVAMI)---

#              ----  Tkinter  ----

#            ---- Prosedürel Bir Örnek  ----
#import tkinter
#pencere = tkinter.Tk()
#pencere.mainloop()
# bu programı yazarak grafik arayüzüne geçiş yapmış olduk.
# gördüğümüz gibi ilk başta sınıfları kullanmadık.İlk etapta Tkinter'i daha
# iyi anlayabilme için prosedürel bir yaklaşımı benimseyeceğiz.

# yukarıda öncelikle modülü içe aktardık ve modülün adını kullanarak
# tkinter modülü içindeki Tk() sınıfını örnekledik.
# oluşturduğumuz pencereyi görünür hale getirmek için de mainloop() metodunu kullandık.

import tkinter as tk # tkinter yazması uzun diye tk olarak modülü içe aktardık.
pencere = tk.Tk()# Tk() adlı sınıfı örnekledik.pencereyi oluşturmuş olduk.
# Tkinter'le oluşturulan boş bir pencere ön tanımlı olarak 200 piksel genişliğe 
# ve 200 piksel yüksekliğe sahip olacaktır.
# ama istersek Tk() sınıfının geometry() metodunu kullanarak pencereyi ayarlayabiliriz.
pencere.geometry("200x70")
pencere.mainloop()
# penceremizi görünür hale getirdik.
# şimdi bu pencereye etiket ve düğme ekleyelim
etiket = tk.Label(text="Selam dünya")
etiket.pack()

düğme = tk.Button(text="tamam",command=pencere.destroy)
# burda üzerinde tamam yazan tıklandığında pencereyi kapatan bir düğme oluşturduk.
# destory() metodunu verdiğimizde pencereye kapatma sinyali göderecektir.
# yalnız bunu kullanırken () kullanmadık eğer () kullanmsaydık düğmenin üzerinde
# geldiğimiz gibi düğmeye basmadan ekran kapanacaktı.
düğme.pack()

pencere.mainloop()

# Label() ve Button() adlı iki sınıf daha kullandık.
# Label() sınıfı etiketler,Button() düğmeler oluşturmamızı sağlar.
# pack() metodunu etiket ve düğmeleri pencere üzerine yerleştirmek için kullanıyoruz.
# text parametresi etiket veya düğmede ne yazacağını söyler.

# prosedürel programlamada sıra çok önemlidir.Kodlar sırasına göre yazılır.
#%% mesela bir örnek yapalım.

import tkinter as tk # modülü içe aktardık.

pencere = tk.Tk() # Tk() sınıfı yardımıyla penceremizi oluşturduk.  

def çıkış():  # çıkış adlı bir fonk. tanımladık.
    etiket["text"] = "elveda dünya"
    düğme["text"] = "bekleyin"
    düğme["state"] = "disabled"
    pencere.after(2000,pencere.destroy)

etiket = tk.Label(text="Selam dünya")# etiketimizi oluştuduk.
etiket.pack()

düğme = tk.Button(text="çık",command=çıkış)# düğmemizi oluşturduk.
düğme.pack()
# 'X' düğmesine basıldığında pencere kapanmadan önce çıkış() fonk. çalışması 
# için aşağıdaki kodu yazıyoruz.
pencere.protocol("WM_DELETE_WİNDOW",çıkış)
pencere.mainloop()# penceremizi görünür hale getiriyoruz.

#%%           ----  Sınıflı Bir Örnek  ----

# şimdi yularıdaki kodları nesne tabanlı olarak yazalım.

import tkinter as tk # modülü tk adıyla içe aktarıyoruz.

class Pencere(tk.Tk): # Pencere() adlı sınıfımızı tanımlamaya başlıyoruz.Tk() sınıfını miras aldık.
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WİNDOW",self.çıkış)
        
        self.etiket = tk.Label(text="merhaba dünya")
        self.etiket.pack()
        
        self.düğme = tk.Button(text="çık",command=self.çıkış)
        self.düğme.pack()
        
    def çıkış(self):
        self.etiket["text"] = "elveda dünya"
        self.düğme["text"] = "bekleyin"
        self.düğme["state"] = "disabled"
        self.after(2000,pencere.destroy)
        
pencere = Pencere()
pencere.mainloop()

#%%          ----  Çoklu Miras Alma  ----

# Python'da bir sınıf aynı anda birden fazla sınıfı miras alabilir.

class Sınıf(tabanSınıf1,tabanSınıf2,tabanSınıf3):
    pass

#%%       ----  Dahil Etme  ----
    
# bir sınıfın içindeki nitelik ve metotları başka bir sınıfın içinde kullanmanın
# tek yolu miras alma değildir.Dahil etme(composition) yönteminide kullanabiliriz.

class Pencere(tk.Tk): 
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WİNDOW",self.çıkış)
        
        self.etiket = tk.Label(text="merhaba dünya")
        self.etiket.pack()
        
        self.düğme = tk.Button(text="çık",command=self.çıkış)
        self.düğme.pack()
        
    def çıkış(self):
        self.etiket["text"] = "elveda dünya"
        self.düğme["text"] = "bekleyin"
        self.düğme["state"] = "disabled"
        self.after(2000,pencere.destroy)
        
pencere = Pencere()
pencere.mainloop()

# uygulama penceremiz tk.Tk() sınıfının doğrudan bir türevidir.Bu yüzden onu miras alıyoruz.
# Label() ve Button() sınıfları ise bu uygulamanın bir parçasıdır.Bu da dahil etmektir.













