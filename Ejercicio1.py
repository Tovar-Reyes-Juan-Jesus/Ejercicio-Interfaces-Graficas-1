from tkinter import *
from tkinter import ttk

raiz = Tk() #creamos la ventana raiz
raiz.geometry("600x450") #definir el tamaño de la ventana
raiz.title("Ejercicio 1")
raiz.config(bg="gray74") #cambiar el fondo de la ventana.

#creamos los frames necesarios para poder usar tanto el metodo grid y pack a la vez.
frame = Frame(raiz, relief="raised",bg="gray74")
frame.grid(column=0,row=0)
#frame.pack(expand=True,fill="both")
#frame.config(border=2)

frame2 = Frame(raiz, relief="raised",bg="gray74",height=20) #con colocar el "Frame" sin acompañante hace que sea posible usar el "bg" y el "bd" entre otras funciones
frame2.grid(column=0,row=1)

#frame2.pack(fill="both",expand=True,padx=40)

frame3 = ttk.Frame(raiz, relief="raised",height=120,width=120,padding="13 12 65 13")
frame3.grid(column=0,row=2)
#frame3.pack(expand=True,fill="both")

frame4 = ttk.Frame(raiz,padding="13 20 240 20", relief="raised",width=100,height=100)
frame4.grid(column=0,row=3)
#frame4.pack(expand=True,fill="both")

frame5 = ttk.Frame(raiz,padding="13 12 100 13", relief="raised")
frame5.grid(column=0,row=4)
#frame5.pack(expand=True,fill="both")

frame6 = ttk.Frame(raiz,padding="130 12 420 113", relief="raised",width=30,height=10)
frame6.grid(column=0,row=5)
frame6
#frame6.pack(expand=True,fill="both")
#Frame 1
#se crean los tabs

style = ttk.Style()#para poder cambiar el color a las tabs asi como tamaño
style.theme_use("default")
style.configure("TNotebook.Tab",background="#00aae4",padding=[41, 30])
style.map("TNotebook.Tab",background=[("selected","#00aae4")])
#settings = {"TNotebook.Tab": {"configure": {"padding": [40, 20],
#                                            "background": "#00aae4"
#                                            },
#                                "map":{"background": [("selected","#00aae4"),
#                                                      ("active","#00aae4")],
#                                        "foreground": [("selected", "#ffffff"),
#                                                        ("active", "#000000")]
#                                                        }
#                                                        }
#                                                        }
#
#style.theme_create("mi_estilo",parent="alt",settings=settings)
#style.theme_use("mi_estilo")

notebook = ttk.Notebook(frame,width=10, height=4)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
tab4 = Frame(notebook)
tab5 = Frame(notebook)

notebook.add(tab1,text="Add")
notebook.add(tab2,text="Delete")
notebook.add(tab3,text="Search")
notebook.add(tab4,text="Services")
notebook.add(tab5,text="Help")

notebook.grid()
#notebook.pack(expand=True,fill="both") #expande y fill es el espacio de x y y.




#Frame 2
#ttk.Label(frame2,text="").grid(column=0,row=0,columnspan=2)

#Frame 3
Nombre = StringVar()
Apellido = StringVar()
Dia = StringVar()
Mes = StringVar()
Año = StringVar()
Pais = StringVar()

ttk.Label(frame3, text="    ").grid(column=0,row=0,sticky=W)
ttk.Label(frame3, text="First Name: ").grid(column=1,row=0,sticky=W)
Nameentry = ttk.Entry(frame3, width=30,textvariable=Nombre)
Nameentry.grid(column=2, row=0)
ttk.Label(frame3,text="   Last Name: ").grid(column=3, row=0, sticky=W)
ApellidoEntry = ttk.Entry(frame3,width=30,textvariable=Apellido)
ApellidoEntry.grid(column=4,row=0)
ttk.Label(frame3, text="      ").grid(column=0,row=1,sticky=W, columnspan=2)
ttk.Label(frame3, text="Birth Date: ").grid(column=1,row=2)
Diaentry = ttk.Entry(frame3,width=1,textvariable=Dia)
Diaentry.grid(column=2, row=2,sticky=W)
Diaentry.place(x=80, y=40)
Mesentry = ttk.Entry(frame3,width=1,textvariable=Mes)
Mesentry.grid(column=2, row=2,sticky=W)
Mesentry.place(x=100, y=40)
Añoentry = ttk.Entry(frame3,width=4,textvariable=Año)
Añoentry.grid(column=2, row=2,sticky=W)
Añoentry.place(x=120,y=40)
ttk.Label(frame3,text="Country: ").grid(column=3,row=2)
Paisentry = ttk.Entry(frame3,width=20,textvariable=Pais)
Paisentry.grid(column=3,row=2)
Paisentry.place(x=340,y=40)

#Frame 4
Credito = StringVar()

ttk.Label(frame4, text="    ").grid(column=0,row=0,sticky=W)
ttk.Label(frame4, text="Credit Card(if any): ").grid(column=1,row=0,sticky=W)
creditoentry = ttk.Entry(frame4,width=18,textvariable=Credito)
creditoentry.grid(column=2,row=0,sticky=W)
ttk.Label(frame4, text="    ").grid(column=0,row=1,columnspan=2)
ttk.Label(frame4,text="Credit Card Type(if any): ").grid(column=1,row=2,sticky=W)

Marca = StringVar()
Visa = ttk.Radiobutton(frame4,text="Visa",variable=Marca,value=Marca,compound="left").grid(column=2,row=2,sticky=W)
Mastercard = ttk.Radiobutton(frame4,text="MasterCard",variable=Marca,compound="center").grid(column=3,row=2,sticky=E)

#Frame 5
ttk.Label(frame5, text="    ").grid(column=0,row=0,sticky=W)
ttk.Label(frame5, text="RoomType: ").grid(column=1,row=0,sticky=W)

Room = StringVar()
Room2 = StringVar()
Room3 = StringVar()
Normal = ttk.Radiobutton(frame5,text="Normal",variable=Room,value=Room,compound="center").grid(column=2,row=0,sticky=W)
Familiar = ttk.Radiobutton(frame5,text="Familiar",variable=Room,value=Room2,compound="center").grid(column=2,row=1,sticky=W)
Special = ttk.Radiobutton(frame5,text="Special",variable=Room,value=Room3,compound="center").grid(column=2,row=2,sticky=W)

ttk.Label(frame5, text="                                                              ").grid(column=3,row=0,sticky=W)
ttk.Label(frame5, text="Total Staying Time(days): ").grid(column=4,row=0,sticky=W)
dias = StringVar()
diasentry = ttk.Entry(frame5,width=2,textvariable=dias)
diasentry.grid(column=5,row=0,sticky=W)

#Frame 6


ttk.Label(frame6,text="   ",width=7).grid(column=0,row=0,columnspan=2)
boton = ttk.Button(frame6,text="Submit")
boton.grid(column=2,row=0)
boton.place(x=130,y=10)
#prueba= ttk.Button(frame6,text="hola")
#prueba.grid(column=3,row=0)


raiz.mainloop() #esto es para que se ejecuta el main
