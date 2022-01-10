from tkinter import *
def tk_1():
      window = Tk()
      window.title('Beginners Test')
      count=0
      val1 = StringVar()
      val2 = StringVar()
      val3 = StringVar()
      val1.set(' ')
      val2.set(' ')
      val3.set(' ')
      value1,value2,value3=0,0,0
      Label(text='Beginners Test for Space Travel',font=('Copperplate Gothic Bold',18)).grid(row=0,column=0,padx=100,columnspan=10)
      Label(text='Before proceding any further, prepare for a beginners test to know if you are eligible for this adventure\nAnswer 1 out of these 3 questions correctly to procede ! -').grid(row=1,column=3)
      Label(text='Question No.1 : A Person not wearing a Space Suit explodes in Space ').grid(row=2,column=3)
      Radiobutton(text='True',variable=val1,value=0).grid(row=3,column=3)
      Radiobutton(text='False',variable=val1,value=1).grid(row=4,column=3)
      Label(text='Question No.2 : A fire in a space can only be put out using water ').grid(row=5,column=3)
      Radiobutton(text='True',variable=val2,value=0).grid(row=6,column=3)
      Radiobutton(text='False',variable=val2,value=1).grid(row=7,column=3)
      Label(text='Question No.3 : A special bag is used if a person feels like vomiting in space ').grid(row=8,column=3)
      Radiobutton(text='True',variable=val3,value=1).grid(row=9,column=3)
      Radiobutton(text='False',variable=val3,value=0).grid(row=10,column=3)
      def perf():
            count=0
            flag2=0
            value1 = val1.get()
            value2 = val1.get()
            value3 = val1.get()
            if int(value1) == 1:
                  count+=1
            if int(value2) == 1:
                  count+=1
            if int(value3) == 1:
                  count+=1
            window.destroy()
      if count >= 1:
            flag2=1
      Button(window,command=perf,text='Submit').grid(row=11,column=3)
      window.mainloop()

