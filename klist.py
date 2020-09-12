# -*- coding: utf-8 -*-

class Sorgu():
    def __init__(self,değer=None,sıra=None):
        self.liste = [("111111111","greenberg","sana gül bahçesi","metis"),
                      ("222222222","evren","postmodern kız sevdim","ithaki"),
                      ("333333333","nietzsche","buyurdu zerdüşt","cem")]
        
        if not değer and not sıra:
            l = self.liste
        else:
            l = [li for li in self.liste if değer == li[sıra]]
        for i in l:
            print(*i,sep=", ")
    
    @classmethod
    def isbnden(cls,isbn):
        cls(isbn,0)
    
    @classmethod
    def yazardan(cls,yazar):
        cls(yazar,1)
        
    @classmethod
    def eserden(cls,eser):
        cls(eser,2)
        
    @classmethod
    def yayınevinden(cls,yayınevi):
        cls(yayınevi,3)





