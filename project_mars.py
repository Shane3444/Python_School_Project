from tkinter import *
def clear(window):
    window.destroy()

def mars():

    window=Tk()
    window.geometry("650x600")
    window.configure(bg="black")
    window.title("Mars")

    bgimage=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\Un bg.png")
    bglabel=Label(window,image=bgimage).grid(rowspan=10,columnspan=10)

    Label(window,text="MARS",width=33,
          font=("Elephant",20),justify="center",borderwidth=2,relief="groove",highlightbackground="white",highlightcolor="white",
          bg="black",fg="white").grid(row=0,columnspan=2,column=0)
    image=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\mars.png")
    Label(window,image=image).grid(row=1,column=1)


    Label(window,text="""•VOLCANOES: Mars has some huge
    volcanoes,the biggest being
    Olympus Mons, which is also
    the biggest in the known solar
    system. Olympus Mons is about
    three times as high as Everest,
    and measures 600km across -
    about the same size as the
    state of Arizona.""",
          bg="black",width=30,justify="left",
          fg="white",
          font=("GillSansMTCondensed",10)).grid(row=1,column=0)

    Label(window,text="""•THE VALLES MARINERIS SYSTEM:
    A series of canyons extending
    3000km across the surface,
    compared to which Earth's Grand
    Canyon is but a speck.""",
          bg="black",width=30,justify="left",
          fg="white",
          font=("GillSansMTCondensed",10)).grid(row=2,column=0)

    Label(window,text="""•THE POLAR CAPS: Consisting of
    frozen water and frozen carbon
    dioxide.""",
          bg="black",width=30,
          fg="white",
          font=("GillSansMTCondensed",10),justify="left").grid(row=3,column=0)

    LF=LabelFrame(window,text="Spacecraft Details",font=("",10,"bold"),bg="black",width=200,height=200,
                  fg="white").grid(row=2,
                  column=1,rowspan=2, sticky='EWNS',
                  padx=5, pady=0, ipadx=5,
                  ipady=5)
    image1=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\Mars craft.png")

    L=Label(LF,image=image1).grid(row=2,column=1,pady=10)
    Label(LF,text="Name : SP-67-4-A\nTop Speed : 670,500,000 mph",fg="white",bg="black",font=("Impact",12)).grid(row=3,column=1)

    b1=Button(window,text="Continue",command=lambda:clear(window),font=("Impact",15),bg="grey",width=10).grid(row=4,column=1)
    window.mainloop()


