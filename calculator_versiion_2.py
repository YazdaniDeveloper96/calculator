#programed by Mz96
#-------------------------------------------reqirments
from tkinter import *
#--------------------------------------optional module
import os 
os.system('cls')
#------------------------------------creating functions
class Calculator:
    def __init__(self) -> None:
        self.self.root=Tk()
        self.myentry_1=Entry(self.root,borderwidth=5,width=35)
        self.self.root.title("Calculator (Ver1)")
        self.self.root.resizable(width=False,height=False)
        #---------------------------------------------------
        self.label_1=Label(self.root,text="cacio",fg="#000000",padx=10,pady=5)
        #-----------------------------------------------number button making
        self.button_1=Button(self.root,text=1,width=4,padx=20,pady=10)
        self.button_2=Button(self.root,text=2,width=4,padx=20,pady=10)
        self.button_3=Button(self.root,text=3,width=4,padx=20,pady=10)
        self.button_4=Button(self.root,text=4,width=4,padx=20,pady=10)
        self.button_5=Button(self.root,text=5,width=4,padx=20,pady=10)
        self.button_6=Button(self.root,text=6,width=4,padx=20,pady=10)
        self.button_7=Button(self.root,text=7,width=4,padx=20,pady=10)
        self.button_8=Button(self.root,text=8,width=4,padx=20,pady=10)
        self.button_9=Button(self.root,text=9,width=4,padx=20,pady=10)
        self.button_0=Button(self.root,text=0,width=4,padx=20,pady=10)
        #---------------------------------------------- +/-/'/'/*/clear button making
        self.button_clear=Button(self.root,text="clear",width=4,padx=20,pady=10)
        self.button_equal=Button(self.root,text="=",width=4,padx=20,pady=10)
        self.button_plus=Button(self.root,text='+',width=4,padx=20,pady=10)
        self.button_minus=Button(self.root,text='-',width=4,padx=20,pady=10)
        self.button_divide=Button(self.root,text='/',width=4,padx=20,pady=10)
        self.button_times=Button(self.root,text='*',width=4,padx=20,pady=10)
        self.myentry_1.grid(row=0,column=0,columnspan=3,padx=5,pady=5)
        #-----------------------------------------------number box griding
        self.button_1.grid(row=1,column=0)
        self.button_2.grid(row=1,column=1)
        self.button_3.grid(row=1,column=2)
        self.button_4.grid(row=2,column=0)
        self.button_5.grid(row=2,column=1)
        self.button_6.grid(row=2,column=2)
        self.button_7.grid(row=3,column=0)
        self.button_8.grid(row=3,column=1)
        self.button_9.grid(row=3,column=2)
        self.button_0.grid(row=4,column=0)
        #----------------------------------------------clear/= box griding
        self.button_clear.grid(row=4,column=1)
        self.button_equal.grid(row=4,column=2)
        #--------------------------------------------- +/-/*/'/'/ box griding
        self.button_plus.grid(row=1,column=3)
        self.button_minus.grid(row=2,column=3)
        self.button_times.grid(row=3,column=3)
        self.button_divide.grid(row=4,column=3)
        #----------------------------------------------entry box griding
        self.label_1.grid(row=0,column=3)
        #--------------------------------------------- +/-/*/'/'//=/clear/ binding
        self.button_clear.bind("<Button>",self.clear())
        self.button_plus.bind("<Button>",self.plus())
        self.button_minus.bind("<Button>",self.minus())
        self.button_times.bind("<Button>",self.times())
        self.button_divide.bind("<Button>",self.divide())
        self.button_equal.bind("<Button>",self.equal())
        #----------------------------------------------number clicking binding
        self.button_1.bind("<Button>",lambda x :self.buttom_click(1))
        self.button_2.bind("<Button>",lambda x :self.buttom_click(2))
        self.button_3.bind("<Button>",lambda x :self.buttom_click(3))
        self.button_4.bind("<Button>",lambda x :self.buttom_click(4))
        self.button_5.bind("<Button>",lambda x :self.buttom_click(5))
        self.button_6.bind("<Button>",lambda x :self.buttom_click(6))
        self.button_7.bind("<Button>",lambda x :self.buttom_click(7))
        self.button_8.bind("<Button>",lambda x :self.buttom_click(8))
        self.button_9.bind("<Button>",lambda x :self.buttom_click(9))
        self.button_0.bind("<Button>",lambda x :self.buttom_click(0))
        #----------------------------------------------------optional functions
        self.button_0.bind("<Enter>",self.func0)
        self.button_0.bind("<Leave>",self.func00)
        self.button_1.bind("<Enter>",self.func1)
        self.button_1.bind("<Leave>",self.func11)
        self.button_2.bind("<Enter>",self.func2)
        self.button_2.bind("<Leave>",self.func22)
        self.button_3.bind("<Enter>",self.func3)
        self.button_3.bind("<Leave>",self.func33)
        self.button_4.bind("<Enter>",self.func4)
        self.button_4.bind("<Leave>",self.func44)
        self.button_5.bind("<Enter>",self.func5)
        self.button_5.bind("<Leave>",self.func55)
        self.button_6.bind("<Enter>",self.func6)
        self.button_6.bind("<Leave>",self.func66)
        self.button_7.bind("<Enter>",self.func7)
        self.button_7.bind("<Leave>",self.func77)
        self.button_8.bind("<Enter>",self.func8)
        self.button_8.bind("<Leave>",self.func88)
        self.button_9.bind("<Enter>",self.func9)
        self.button_9.bind("<Leave>",self.func99)
        #------------------------------------------------
        self.button_plus=self.button_plus.bind("<Enter>",self.funcp)
        self.button_minus=self.button_minus.bind("<Leave>",self.funcm1)
        self.button_times=self.button_times.bind("<Enter>",self.funct)
        self.button_times=self.button_times.bind("<Leave>",self.funct1)
        self.button_divide=self.button_divide.bind("<Enter>",self.funcd)
        self.button_divide=self.button_divide.bind("<Leave>",self.funcd1)
        self.button_clear=self.button_clear.bind("<Enter>",self.funcc)
        self.button_clear=self.button_clear.bind("<Leave>",self.funcc1)
        self.button_equal=self.button_equal.bind("<Enter>",self.funce)
        self.button_equal=self.button_equal.bind("<Leave>",self.funce1)
        self.self.root.mainloop()
        
    def buttom_click(self,number):
        current_number=self.myentry_1.get()
        self.myentry_1.delete(0,END)
        self.myentry_1.insert(0,str(current_number)+str(number))
    #-------------plus(+)
    n1=0
    sign=" "  
    def plus(self,event):
        self.label_1.config(text="plus")
        global n1
        global sign
        first_number=int(self.myentry_1.get())
        n1=first_number
        sign="plus"
        self.myentry_1.delete(0,END)
        # print(n1)
    #-------------minus(-)
    def minus(self,number):
        self.label_1.config(text="minus")
        global n1
        global sign
        first_number=int(self.myentry_1.get())
        n1=first_number
        sign="minus"
        self.myentry_1.delete(0,END)
        # print(n1)
    #-------------times (*)
    def times(self,number):
        self.label_1.config(text="times")
        global n1
        global sign
        first_number=int(self.myentry_1.get())
        n1=first_number
        sign="times"
        self.myentry_1.delete(0,END)
        # print(n1)
    #-------------divide (/)
    def divide(self,number):
        self.label_1.config(text="divide")
        global n1
        global sign
        first_number=int(self.myentry_1.get())
        n1=first_number
        sign="divide"
        self.myentry_1.delete(0,END)
        # print(n1)
    #------------- equal (=)
    def equal(self,number):
        self.label_1.config(text="equal")
        global sign
        global n1
        secend_number=self.myentry_1.get()
        self.myentry_1.delete(0,END)
        if sign=="plus":
            self.myentry_1.insert(0,n1+int(secend_number))
        elif sign=="minus":
            self.myentry_1.insert(0,n1-int(secend_number))
        elif sign=="times":
            self.myentry_1.insert(0,n1*int(secend_number))
        else:
            self.myentry_1.insert(0,n1/int(secend_number))
        sign=""
    #--------------------------------------------------------------clear
    def clear(self,event):  
        self.label_1.config(text="clear")
        self.myentry_1.delete(0,END)
    #----------------------------------------------------------- enter & leave ravadid
    def func0(self,event):
        self.button_0.config(bg="#F18F01",fg="#ffffff")
    def func00(self,event):
        self.button_0.config(bg="#f0f0f0",fg="#000000")
    def func1(self,event):
        self.button_1.config(bg="#F18F01",fg="#ffffff")
    def func11(self,event):
        self.button_1.config(bg="#f0f0f0",fg="#000000")
    def func2(self,event):
        self.button_2.config(bg="#F18F01",fg="#ffffff")
    def func22(self,event):
        self.button_2.config(bg="#f0f0f0",fg="#000000")
    def func3(self,event):
        self.button_3.config(bg="#F18F01",fg="#ffffff")
    def func33(self,event):
        self.button_3.config(bg="#f0f0f0",fg="#000000")
    def func4(self,event):
        self.button_4.config(bg="#F18F01",fg="#ffffff")
    def func44(self,event):
        self.button_4.config(bg="#f0f0f0",fg="#000000")
    def func5(self,event):
        self.button_5.config(bg="#F18F01",fg="#ffffff")
    def func55(self,event):
        self.button_5.config(bg="#f0f0f0",fg="#000000")
    def func6(self,event):
        self.button_6.config(bg="#F18F01",fg="#ffffff")
    def func66(self,event):
        self.button_6.config(bg="#f0f0f0",fg="#000000")
    def func7(self,event):
        self.button_7.config(bg="#F18F01",fg="#ffffff")
    def func77(self,event):
        self.button_7.config(bg="#f0f0f0",fg="#000000")
    def func8(self,event):
        self.button_8.config(bg="#F18F01",fg="#ffffff")
    def func88(self,event):
        self.button_8.config(bg="#f0f0f0",fg="#000000")
    def func9(self,event):
        self.button_9.config(bg="#F18F01",fg="#000000")
    def func99(self,event):
        self.button_9.config(bg="#f0f0f0",fg="#000000")
    #------------------------------------------------------------- + / - / * / "/" / clear / equal    enter & leave ravadid
    def funcp(self,event):
        self.button_plus.config(bg="#F18F01",fg="#000000")
    def funcp1(self,event):
        self.button_plus.config(bg="#f0f0f0",fg="#000000")
    def funcm(self,event):
        self.button_minus.config(bg="#F18F01",fg="#000000")
    def funcm1(self,event):
        self.button_minus.config(bg="#f0f0f0",fg="#000000")
    def funct(self,event):
        self.button_times.config(bg="#F18F01",fg="#000000")
    def funct1(self,event):
        self.button_times.config(bg="#f0f0f0",fg="#000000")
    def funcd(self,event):
        self.button_divide.config(bg="#F18F01",fg="#000000")
    def funcd1(self,event):
        self.button_divide.config(bg="#f0f0f0",fg="#000000")
    def funce(self,event):
        self.button_equal.config(bg="#F18F01",fg="#000000")
    def funce1(self,event):
        self.button_equal.config(bg="#f0f0f0",fg="#000000")
    def funcc(self,event):
        self.button_clear.config(bg="#F18F01",fg="#000000")
    def funcc1(self,event):
        self.button_clear.config(bg="#f0f0f0",fg="#000000")
    #-------------------------------------------------body of calculator
    