from tkinter import *

def btn_clear():
    entry.delete(0,END)
    
def btn_click(item):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(item))
    
def btn_equal():
    expression=entry.get()
    entry.delete(0,END)
    result=str(eval(expression))
    entry.insert(0,str(result))

root=Tk()
root.title("CALCULATOR")

entry=Entry(root,width=50,font=('arial',10,'bold'))
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

clear=Button(root,text='C',padx=20,pady=10,command=lambda:btn_clear())
divide=Button(root,text='/',padx=20,pady=10,command=lambda:btn_click('/'))

seven=Button(root,text='7',font=('arial',10,'bold'),width=10,height=3,bd=0,bg="#dcdcdc",cursor="hand2",fg="black",command=lambda:btn_click('7'))
eight=Button(root,text='8',font=('arial',10,'bold'),width=10,height=3,bd=0,bg="#dcdcdc",cursor="hand2",fg="black",command=lambda:btn_click('8'))
nine=Button(root,text='9',font=('arial',10,'bold'),width=10,height=3,bd=0,bg="#dcdcdc",cursor="hand2",fg="black",command=lambda:btn_click('9'))
add=Button(root,text='+',font=('arial',10,'bold'),width=10,height=3,bd=0,bg="#dcdcdc",cursor="hand2",fg="black",command=lambda:btn_click('+'))

four=Button(root,text='4',font=('arial',10,'bold'),width=10,height=3,bd=0,bg="#dcdcdc",cursor="hand2",fg="black",command=lambda:btn_click('4'))
five=Button(root,text='5',font=('arial',10,'bold'),width=10,height=3,bd=0,bg="#dcdcdc",cursor="hand2",fg="black",command=lambda:btn_click('5'))
six=Button(root,text='6',font=('arial',10,'bold'),width=10,height=3,bd=0,bg="#dcdcdc",cursor="hand2",fg="black",command=lambda:btn_click('6'))
minus=Button(root,text='-',font=('arial',10,'bold'),width=10,height=3,bd=0,bg="#dcdcdc",cursor="hand2",fg="black",command=lambda:btn_click('-'))

one=Button(root,text='1',font=('arial',10,'bold'),width=10,height=3,bd=0,bg="#dcdcdc",cursor="hand2",fg="black",command=lambda:btn_click('1'))
two=Button(root,text='2',font=('arial',10,'bold'),width=10,height=3,bd=0,bg="#dcdcdc",cursor="hand2",fg="black",command=lambda:btn_click('2'))
three=Button(root,text='3',font=('arial',10,'bold'),width=10,height=3,bd=0,bg="#dcdcdc",cursor="hand2",fg="black",command=lambda:btn_click('3'))
multiply=Button(root,text='*',font=('arial',10,'bold'),width=10,height=3,bd=0,bg="#dcdcdc",cursor="hand2",fg="black",command=lambda:btn_click('*'))
zero=Button(root,text='0',font=('arial',10,'bold'),width=10,height=3,bd=0,bg="#dcdcdc",cursor="hand2",fg="black",command=lambda:btn_click('0'))

equal=Button(root,text='=',font=('arial',10,'bold'),width=10,height=3,bd=0,bg="#dcdcdc",cursor="hand2",fg="black",command=lambda:btn_equal())

clear.grid(row=1,column=0)
divide.grid(row=1,column=1)

seven.grid(row=2,column=0)
eight.grid(row=2,column=1)
nine.grid(row=2,column=2)
add.grid(row=2,column=3)

four.grid(row=3,column=0)
five.grid(row=3,column=1)
six.grid(row=3,column=2)
minus.grid(row=3,column=3)

one.grid(row=4,column=0)
two.grid(row=4,column=1)
three.grid(row=4,column=2)
multiply.grid(row=4,column=3)
zero.grid(row=5,column=0)
equal.grid(row=5,column=1,columnspan=2)

root.mainloop()