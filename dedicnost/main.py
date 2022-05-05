class Zvieratko:
    def __init__(self,meno):
        self.meno = meno

    def jedz(self,jedlo):
        print(f"{self.meno}: {jedlo} mi chutna")


class Macka(Zvieratko):
    def zamnaukuj(self):
     print(f"{self.meno}: mnau!")

    def jedz(self,jedlo):
        super().jedz("Sunka")
        print(f"{self.meno}: {jedlo} mi nechuti")



#dedim od zvieratka jeho metody
class Pes(Zvieratko):
    def zastekaj(self):
        print(f"{self.meno}: Haf!")


macka = Macka("Micka")
pes = Pes("Falko")

#mozem pouzivat jedz ktore som definoval v tgriede Zvieratko
macka.jedz("Sunka")
macka.zamnaukuj()

pes.jedz("granulka")
pes.zastekaj()

# POLYMORFISMUS
zvieratka = [Macka("Naginy"), Pes("Azor")]

for zvieratko in zvieratka:
    zvieratko.jedz("Granulka")



#GENERALIZACIA







