from Tkinter import*

def bosish(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)
def tozalash():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

cal = Tk()
cal.title("Calculator")
operator=""
text_Input =StringVar()

txtDisplay = Entry(cal,font=("arial",20, 'bold') , textvariable=text_Input,
                   bd=30, insertwidth=4, bg="powder blue",justify='right').grid(columnspan=4)
btn7=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20, 'bold'),
            text="7", bg="powder blue",command=lambda:bosish(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20, 'bold'),
            text="8", bg="powder blue",command=lambda:bosish(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20, 'bold'),
            text="9", bg="powder blue",command=lambda:bosish(9)).grid(row=1,column=2)
qosh=Button(cal,padx=16,pady=16,bd=8,fg="black", font=("arial",20, 'bold'),
            text="+", bg="powder blue",command=lambda:bosish("+")).grid(row=1,column=3)

btn4=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20, 'bold'),
            text="4", bg="powder blue",command=lambda:bosish(4)).grid(row=2,column=0)
btn5=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20, 'bold'),
            text="5", bg="powder blue",command=lambda:bosish(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20, 'bold'),
            text="6", bg="powder blue",command=lambda:bosish(6)).grid(row=2,column=2)
arifme=Button(cal,padx=16,pady=16,bd=8, fg="black",font=("arial",20, 'bold'),
            text="-", bg="powder blue",command=lambda:bosish("-")).grid(row=2,column=3)

btn3=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20, 'bold'),
            text="3", bg="powder blue",command=lambda:bosish(3)).grid(row=3,column=0)
btn2=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20, 'bold'),
            text="2", bg="powder blue",command=lambda:bosish(2)).grid(row=3,column=1)
btn1=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20, 'bold'),
            text="1", bg="powder blue",command=lambda:bosish(1)).grid(row=3,column=2)
kopaytir=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20, 'bold'),
            text="*", bg="powder blue",command=lambda:bosish("*")).grid(row=3,column=3)

btn0=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20, 'bold'),
            text="0", bg="powder blue",command=lambda:bosish(0)).grid(row=4,column=0)
bol=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20, 'bold'),
            text="/", bg="powder blue",command=lambda:bosish("/")).grid(row=4,column=1)
tenglik=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20, 'bold'),
            text="=", bg="powder blue",command=btnEqualsInput).grid(row=4,column=2)
tozala=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20, 'bold'),
            text="C", bg="powder blue",command= tozalash).grid(row=4,column=3)
cal.mainloop()
