# -*- coding: utf-8 -*-

class Sınıf():
    sınıfNiteliği = "sınıf niteliği"
    
    def __init__(self):
        self.örnekNiteliği = "örnek niteliği"
        
    def örnekMetodu(self):
        print("örnek metodu")
        
    @classmethod
    def sınıfMetodu(cls):
        print("sınıf metodu")
        
    @staticmethod
    def statikMetot():
        print("statik metot")