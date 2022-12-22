
import random
from customtkinter import *
from os import _exit


title = "Math"
h1 = 50
w1 = 200
h  = (3*h1)+40
w = w1+20

class AppWindow():
    def __init__(self) -> None:
        self.window = CTk()
        self.window.geometry(f"{w}x{h}")
        self.window.minsize(w, h)
        self.window.maxsize(w, h)
        self.window.title(title)
        # self.window.iconbitmap("icon.ico")
        set_appearance_mode("dark")
        set_default_color_theme("blue") 
        self.allow = []
        self.addon = 0
        self.subon = 0
        self.mulon = 0
        self.divon = 0
        self.l1 = 0
        self.l2 = 100
        self.r = 3
        self.wintype = 1
        self.settingframe = CTkFrame(self.window)
        self.maxf = CTkFrame(self.settingframe)
        self.minf = CTkFrame(self.settingframe)
        self.dicf = CTkFrame(self.settingframe)
        self.maxl = CTkLabel(self.maxf, text = "Max",  height=40, width=(w1/3)-1, fg_color=None)
        self.minl = CTkLabel(self.minf, text = "Min",  height=40, width=(w1/3)-1, fg_color=None)
        self.dicl = CTkLabel(self.dicf, text = "Round",  height=40, width=(w1/3)-1, fg_color=None)
        self.max = CTkEntry(self.maxf,  height=40, width=(w1/3)-1, fg_color=None)
        self.min = CTkEntry(self.minf,  height=40, width=(w1/3)-1, fg_color=None)
        self.dic = CTkEntry(self.dicf,  height=40, width=(w1/3)-1, fg_color=None)
        self.cbut = CTkButton(self.settingframe, text = "Save", command=self.limitdone)
        self.cbut.pack()
        self.max.pack()
        self.min.pack()
        self.dic.pack()
        self.maxl.pack()
        self.minl.pack()
        self.dicl.pack()
        self.maxf.pack(side = LEFT, padx = 2, pady = 2)
        self.minf.pack(side = LEFT, padx = 2, pady = 2)
        self.dicf.pack(side = LEFT, padx = 2, pady = 2)
        self.main = CTkFrame(self.window)
        self.windowframe = CTkFrame(self.main)
        self.cbut = CTkButton(self.windowframe, text = "Settings", command=self.limitcheck)
        self.cbut.pack()
        self.add = CTkButton(self.windowframe, text = "+", command=self.addc, height=40, width=40, fg_color=None)
        self.sub = CTkButton(self.windowframe, text = "-", command=self.subc, height=40, width=40, fg_color=None)
        self.mul = CTkButton(self.windowframe, text = "*", command=self.mulc, height=40, width=40, fg_color=None)
        self.div = CTkButton(self.windowframe, text = "/", command=self.divc, height=40, width=40, fg_color=None)
        self.add.pack(side = LEFT, padx = 2, pady = 2)
        self.sub.pack(side = LEFT, padx = 2, pady = 2)
        self.mul.pack(side = LEFT, padx = 2, pady = 2)
        self.div.pack(side = LEFT, padx = 2, pady = 2)
        self.windowframe.pack()
        self.sum = CTkLabel(self.main, text = "", height=h1, width=w1,text_font=("Courier", 25))
        self.sum.pack()
        self.answer = CTkEntry(self.main, height=h1, width=w1,text_font=("Courier", 15))
        self.answer.pack()
        self.warn = CTkLabel(self.window, text = "")
        self.main.pack(side = TOP)
        self.warn.pack()
        self.selection(1)
        self.selection(2)
        self.selection(3)
        self.selection(4)
        print(self.allow)
        self.window.bind('<Return>', self.enterevent)     
        self.window.bind('s', self.limitcheck)    
        self.window.bind('r', self.getsum)  
        self.window.bind('q', self.end) 
        self.window.bind('h', self.help)  
        self.window.bind('=', self.help)   
        self.window.bind('+', self.addc)
        self.window.bind('-', self.subc)
        self.window.bind('*', self.mulc)
        self.window.bind('/', self.divc)
        self.window.bind('<space>', self.addsub)
        self.getsum(None)

    def limitcheck(self, event=None):
        self.max.delete(0, END)
        self.min.delete(0, END)
        self.dic.delete(0, END)
        self.max.insert(0,self.l1)
        self.min.insert(0,self.l2)
        self.dic.insert(0,self.r)
        self.warn.pack_forget()
        self.main.pack_forget()
        self.settingframe.pack()
        self.warn.pack()
        self.wintype = 0
        self.max.focus()

    def limitdone(self):
        try:
            self.r = int(self.dic.get())
            self.l1 = int(self.max.get())
            self.l2 = int(self.min.get())
            self.warn.pack_forget()
            self.settingframe.pack_forget()
            self.main.pack()
            self.warn.pack()
            self.getsum()
            self.wintype = 1
        except:
            self.warn.configure(text="Value Error")


    def addc(self, event=None):
        
        if self.addon == 1:
            self.addon = 0
            self.add.configure(fg_color = "black")
        else:
            self.addon = 1
            self.add.configure(fg_color = "green")
        self.allowcheck()

    def subc(self, event=None):
        
        if self.subon == 1:
            self.subon = 0
            self.sub.configure(fg_color = "black")
        else:
            self.subon = 1
            self.sub.configure(fg_color = "green")
        self.allowcheck()

    def mulc(self, event=None):
        
        if self.mulon == 1:
            self.mulon = 0
            self.mul.configure(fg_color = "black")
        else:
            self.mulon = 1
            self.mul.configure(fg_color = "green")
        self.allowcheck()

    def divc(self, event=None):
        
        if self.divon == 1:
            self.divon = 0
            self.div.configure(fg_color = "black")
        else:
            self.divon = 1
            self.div.configure(fg_color = "green")
        self.allowcheck()

    def addsub(self, event):
        self.entry = str(self.answer.get()).replace(" ","")
        if "-" in self.entry:
            self.final = self.entry.replace("-","")
        else:
            self.final = "-"+self.entry
        
        self.answer.delete(0,END)
        self.answer.insert(0,self.final)
        

    def enterevent(self, event=None):
        if self.wintype == 1:
            self.check()
        else:
            self.limitdone()

    def selection(self, event=None):
        
        if event == 1:
            if self.addon == 1:
                self.addon = 0
                self.add.configure(fg_color = "black")
            else:
                self.addon = 1
                self.add.configure(fg_color = "green")
        if event == 2:
            if self.subon == 1:
                self.subon = 0
                self.sub.configure(fg_color = "black")
            else:
                self.subon = 1
                self.sub.configure(fg_color = "green")
        if event == 3:
            if self.mulon == 1:
                self.mulon = 0
                self.mul.configure(fg_color = "black")
            else:
                self.mulon = 1
                self.mul.configure(fg_color = "green")
        if event == 4:
            if self.divon == 1:
                self.divon = 0
                self.div.configure(fg_color = "black")
            else:
                self.divon = 1
                self.div.configure(fg_color = "green")

        self.allowcheck()

    def allowcheck(self):
        
        self.allow.clear()
        if self.addon == 1:
            self.allow.append(1)
        if self.subon == 1:
            self.allow.append(2)
        if self.mulon == 1:
            self.allow.append(3)
        if self.divon == 1:
            self.allow.append(4)

        self.getsum()

    def help(self,event):
        
        self.answer.delete(0,END)
        self.answer.insert(0,self.real)

    def getsum(self, event=None):
        
        if len(self.allow) != 0:
            self.warn.configure(text = "")
            self.answer.delete(0,END)
            self.sumtype = random.choice(self.allow)
            self.first = random.randint(self.l1,self.l2)
            self.second = random.randint(self.l1,self.l2)
            if self.sumtype == 1:
                self.real = self.first + self.second
                self.sumtext = f"{self.first} + {self.second}"
            elif self.sumtype == 2:
                self.real = self.first - self.second
                self.sumtext = f"{self.first} - {self.second}"
            elif self.sumtype == 3:
                self.real = self.first * self.second
                self.sumtext = f"{self.first} * {self.second}"
            elif self.sumtype == 4:
                if self.second == 0:
                    if len(self.allow) == 1:
                        self.sumtext= "Error"
                        self.real = ""
                        self.answer.delete(0,END)
                        self.warn.configure(text = "")
                    else:
                        self.getsum()
                else:
                    self.sumtext = f"{self.first} / {self.second}"
                    self.real = round(self.first / self.second, self.r)
                    if self.first // self.second == self.first / self.second:
                        self.real = self.first // self.second
                    
            self.sum.configure(text = self.sumtext)
            self.answer.focus()
        else:
            self.sum.configure(text = "Select")
            self.real = ""
            self.answer.delete(0,END)
            self.warn.configure(text = "")

    def check(self, event=None):
        
        self.entry = str(self.answer.get())
        self.final = self.entry.replace(" ", "")
        if self.final == str(self.real):
            self.getsum(None)
        else:
            if len(self.allow) != 0:
                self.warn.configure(text = "Wrong Answer")

    def end(self, event=None):
        
        self.window.destroy()
        _exit(0)



if __name__ == "__main__":
    app = AppWindow()
    app.window.mainloop()