from tkinter import *
from tkinter import messagebox
import json
import time
import vlc
import random



mzk=vlc.MediaPlayer("C:/Users\KAAN/Downloads/muzik.mp3")
mzk.play()

pencere = Tk()
pencere.geometry("800x500")
pencere.title("StajUygulama")
with open('sorucevap.txt',encoding='utf-8') as f:
    cek = json.load(f)
q = (cek['sorular'])
secenekler = (cek['secenekler'])
a = (cek['cevaplar'])

z=zip(q,secenekler,a)
l=list(z)
random.shuffle(l)
q,secenekler,a=zip(*l)

class Sinav:
    def __init__(self):
        self.sn = 0
        self.sorular = self.soru(self.sn)
        self.verilencevap = IntVar()
        self.secenekler = self.radiobtns()
        self.gorunum(self.sn)
        self.buttons()
        self.dogru = 0

    def soru(self, sn):
        baslik = Label(pencere, text="Kim Stajyer Olmak İster ?", width=50, bg="blue", fg="white", font=("times", 20, "bold"))
        baslik.place(x=0, y=5)
        sn = Label(pencere, text=q[sn], width=60, font=("times", 16, "bold"), anchor="w")
        sn.place(x=10, y=100)
        return sn

    def radiobtns(self):
        dgr = 0
        b = []
        yp = 150
        while dgr < 4:
            btn = Radiobutton(pencere, text=" ", variable=self.verilencevap, value=dgr + 1, font=("times", 14,"bold"))
            b.append(btn)
            btn.place(x=10, y=yp)
            dgr += 1
            yp += 40
        return b

    def gorunum(self, sn):
        dgr = 0
        self.verilencevap.set(0)
        self.sorular['text'] = q[sn]
        for scnk in secenekler[sn]:
              self.secenekler[dgr]['text'] = scnk
              dgr += 1

    def buttons(self):
        devambuton = Button(pencere, text="Sonraki",command=self.devambuton, width=10,bg="green",fg="white",font=("times",16,"bold"))
        devambuton.place(x=200,y=380)
        cikisbutton = Button(pencere, text="Çıkış",command=pencere.destroy,width=10,bg="red",fg="white", font=("times",16,"bold"))
        cikisbutton.place(x=380,y=380)

    def cevapkontrol(self, sn):
        if self.verilencevap.get() == a[sn]:
             return True
        
    def devambuton(self):
        if self.cevapkontrol(self.sn):
            self.dogru += 1
        self.sn += 1
        if self.sn == 10:
            self.sonuc_gorunum()
        else:
            self.gorunum(self.sn)       
        

    def sonuc_gorunum(self):
        skor = int(self.dogru / 10 * 100)
        sonuc = "Başarı Oranınız: " + "%" + str(skor)
        wc = 10 - self.dogru
        dogru = "Doğru Cevap Sayısı: " + str(self.dogru)
        yanlis = "Yanlış Cevap Sayısı: " + str(wc)
        messagebox.showinfo("Sonuç", "\n".join([sonuc, dogru, yanlis]))



sinav=Sinav()
pencere.mainloop()
