from http.client import TEMPORARY_REDIRECT
from pathlib import Path
from time import sleep
from tkinter import ANCHOR, ttk,Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Frame
from tkinter.font import BOLD
from typing_extensions import Self
import uiFunctions as f 
import tkinter as tk1
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame


f.createDbs()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
aux_val = 0

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def canvas2Refresh():
    global canvas2
    canvas2.destroy()
    canvas2 = Canvas(window,bg = "#FFFFFF",height = 817,width = 1359-425,bd = 0, highlightthickness = 0,relief = "ridge")
    canvas2.place(x = 425, y = 0)
    return canvas2

def createSku():
    """
     Función del boton "crear nuevo sku" de la UI.
     Elimina canvas 2 y crea los campos necesarios en canvas2
     y permite la carga de un nuevo SKU
     """
    global entry_bg_1,entry_bg_2,entry_bg_3,entry_bg_4,entry_bg_5,entry_1,entry_2,entry_3,entry_4,entry_5,entry_image_1,entry_image_2,entry_image_3,entry_image_4,entry_image_5,button_image_6,button_image_1

    canvas2=canvas2Refresh()

    canvas2.create_text(528.0-425,35.0,anchor="nw",text="Codigo SKU",font=("K2D bold", 24 * -1))
    canvas2.create_text(460-425,168.0,anchor="nw",text="Nombre",fill="#7C7777",font=("K2D Bold", 24 * -1))
    canvas2.create_text(460.0-425,260.0,anchor="nw",text="Volumen",fill="#7C7777",font=("K2D Bold", 24 * -1))
    canvas2.create_text(460.0-425,355.0,anchor="nw",text="Precio",fill="#7C7777",font=("K2D Bold", 24 * -1))
    canvas2.create_text(460.0-425,449.0,anchor="nw",text="Peso",fill="#7C7777",font=("K2D Bold", 24 * -1))
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
    entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
    entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
    
    entry_bg_1 = canvas2.create_image(633.5-425,79.5,image=entry_image_1)
    entry_1 = Entry(canvas2,bd=0,bg="#d9d9d9",highlightthickness=0)# place  
    entry_1.place(x=520.0-400,y=65.0,width=170.0,height=30.0)   
    entry_bg_2 = canvas2.create_image(565.5-425,215.5,image=entry_image_2)
    entry_2 = Entry(canvas2,bd=0,bg="#d9d9d9",highlightthickness=0)
    entry_2.place(x=452.0-400,y=203.0,width=170.0,height=30.0)
    entry_3 = Entry(canvas2, bd=0,bg="#d9d9d9",highlightthickness=0)
    entry_3.place(x=452.0-400,y=293.0,width=170,height=30.0)
    entry_bg_3 = canvas2.create_image(565.5-425,306.5,image=entry_image_3)
    entry_bg_4 = canvas2.create_image(565.5-425,495.5,image=entry_image_4)
    entry_4 = Entry(canvas2, bd=0,bg="#d9d9d9",highlightthickness=0)
    entry_4.place(x=452.0-400,y=482.0,width=170.0,height=30.0)
    entry_bg_5 = canvas2.create_image(565.5-425,400.5,image=entry_image_5)
    entry_5 = Entry(canvas2,bd=0,bg="#d9d9d9",highlightthickness=0)
    entry_5.place(x=452.0-400,y=386.0,width=170.0,height=30.0)

    button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_6 = Button(canvas2,image=button_image_6,borderwidth=0,width=227.0,height=51.0,highlightthickness=0,command=sku_info,relief="flat")
    button_6.place(x=1102.0-425,y=739.0)

    
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_77 = Button(canvas2,image=button_image_1,borderwidth=0,width=227.0,height=51.0,highlightthickness=0,command=sku_info,relief="flat")
    button_77.place(x=-100,y=50.0)
    

def sku_info():
    global entry_1, entry_2, entry_3, entry_4, entry_5
    try:
        skuCodeGet = entry_1.get()
        skuNameGet = entry_2.get()
        skuVolumeGet = entry_3.get()
        skuWeightGet = entry_4.get()
        skuPriceGet = entry_5.get()
        print(skuCodeGet)
        canvas2Refresh()
        return f.create_sku(skuCodeGet,skuNameGet,skuWeightGet,skuVolumeGet,skuPriceGet)
    except Exception as e:
        print(e)
    
def checkSKUs():
    global canvas2
    canvas2Refresh()
    f.cur.execute("SELECT * FROM skuinfo")
    rows = f.cur.fetchall()
    tree = ttk.Treeview(canvas2, column=(1,2,3,4,5),height=26, selectmode="extended", show='headings')
    tree.column(1,width=135);    tree.heading("#1", text="ID")
    tree.column(2);    tree.heading("#2", text="Nombre")
    tree.column(3);    tree.heading("#3", text="Volumen")
    tree.column(4);    tree.heading("#4", text="Precio")
    tree.column(5);    tree.heading("#5", text="Peso")
    style=ttk.Style()
    style.theme_use("default")
    style.configure("Treeview",font=100,background="#D9D9D9",foreground="black",rowheight=30,fieldbackground="white")
    style.configure("Treeview.Heading",background="#FFFFFF",font=200,rowheight=70) 
    tree.pack(expand=1)
    for row in rows:
        tree.insert("",tk1.END,values=row)
    
def ModifySKU():
    global entry_bg_1,entry_bg_2,entry_bg_3,entry_bg_4,entry_bg_5,entry_1,entry_2,entry_3,button_image_9,entry_4,entry_5,entry_image_1,entry_image_2,entry_image_3,entry_image_4,entry_image_5,button_image_6
    canvas2 = canvas2Refresh()
   
    canvas2.create_text(528.0-425,35.0,anchor="nw",text="Codigo SKU",font=("K2D bold", 24 * -1))
    

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
    entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
    entry_bg_1 = canvas2.create_image(633.5-425,79.5,image=entry_image_1)
    entry_1 = Entry(canvas2,bd=0,bg="#d9d9d9",highlightthickness=0)
    entry_1.place(x=520.0-400,y=65.0,width=170.0,height=30.0)

    
    button_image_9 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_9 = Button(canvas2,image=button_image_9,borderwidth=0,width=227.0,height=51.0,highlightthickness=0,command=stockModification,relief="flat")
    button_9.place(x=1102.0-625,y=45)

def checkStocks():
    
    global entry_bg_1,entry_bg_2,entry_bg_3,entry_bg_4,entry_bg_5,entry_1,entry_2,entry_3,button_image_11,entry_4,entry_5,entry_image_1,entry_image_2,entry_image_3,entry_image_4,entry_image_5,button_image_11
    canvas2 = canvas2Refresh()
    canvas2.create_text(528.0-425,35.0,anchor="nw",text="Codigo SKU",font=("K2D bold", 24 * -1))
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
    entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
    entry_bg_1 = canvas2.create_image(633.5-425,79.5,image=entry_image_1)
    entry_1 = Entry(canvas2,bd=0,bg="#d9d9d9",highlightthickness=0)
    entry_1.place(x=520.0-400,y=65.0,width=170.0,height=30.0)
    button_image_11 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_11 = Button(canvas2,image=button_image_11,borderwidth=0,width=227.0,height=51.0,highlightthickness=0,command=stockView,relief="flat")
    button_11.place(x=1102.0-625,y=45)

def stockView():
    global entry_bg_1,entry_bg_2,label_2,label_3,label_4,label_5,entry_bg_3,entry_bg_4,entry_bg_5,entry_1,entry_2,entry_3,button_image_9,entry_4,entry_5,entry_image_1,entry_image_2,entry_image_3,entry_image_4,entry_image_5,button_image_6
    skuCodeGet = entry_1.get()
    f.cur.execute("SELECT * FROM skuinfo where skuid='"+str(skuCodeGet)+"' ")
    skudata = f.cur.fetchone()
    print(skudata)

    canvas2.create_text(460-425,168.0,anchor="nw",text="Nombre",fill="#7C7777",font=("K2D Bold", 24 * -1))
    canvas2.create_text(460.0-425,260.0,anchor="nw",text="Peso",fill="#7C7777",font=("K2D Bold", 24 * -1))
    canvas2.create_text(600,168.0,anchor="nw",text="Volumen",fill="#7C7777",font=("K2D Bold", 24 * -1))
    canvas2.create_text(600,260.0,anchor="nw",text="Precio",fill="#7C7777",font=("K2D Bold", 24 * -1))
    
    entry_bg_2 = canvas2.create_image(140.5,215.5,image=entry_image_2)
    entry_bg_3 = canvas2.create_image(140.5,306.5,image=entry_image_3)
    entry_bg_4 = canvas2.create_image(700,306.5,image=entry_image_4)
    entry_bg_5 = canvas2.create_image(700,215.5,image=entry_image_4)


    label_2 = Label(canvas2,text= skudata[2],bd=0,bg="#d9d9d9",highlightthickness=0)
    label_2.place(x=52,y=203.0,width=170.0,height=30.0)
    label_3 = Label(canvas2,text= skudata[3],bd=0,bg="#d9d9d9",highlightthickness=0)
    label_3.place(x=52,y=293.0,width=170,height=30.0)
    label_4 = Label(canvas2,text= skudata[5],bd=0,bg="#d9d9d9",highlightthickness=0)
    label_4.place(x=617.5,y=293.0,width=170,height=30.0)
    label_5 = Label(canvas2,text= skudata[4],bd=0,bg="#d9d9d9",highlightthickness=0)
    label_5.place(x=617.5,y=203.0,width=170,height=30.0)
    
    f.cur.execute("SELECT * FROM stockinfo where skuid='"+str(skuCodeGet)+"' order by date desc")
    rows = f.cur.fetchall()
    f.cur.execute("SELECT count(date) FROM stockinfo")
    quantityRows = f.cur.fetchone()
    tree = ttk.Treeview(canvas2, column=(1,2,3,4,5),height=quantityRows[0],  show='headings')
    tree.column(1,width=135);    tree.heading("#1", text="SKU ID")
    tree.column(2);    tree.heading("#2", text="Stock inicial")
    tree.column(3);    tree.heading("#3", text="Variación")
    tree.column(4);    tree.heading("#4", text="Stock Final")
    tree.column(5);    tree.heading("#5", text="Fecha")
    style=ttk.Style()
    style.theme_use("default")
    style.configure("Treeview",font=100,background="#D9D9D9",foreground="black",rowheight=30,fieldbackground="white")
    style.configure("Treeview.Heading",background="#FFFFFF",font=200,rowheight=70) 
    tree.pack(side = "bottom", pady=385)
    for row in rows:
        tree.insert("",tk1.END,values=row)
    

def stockModification():
    global entry_bg_1,entry_bg_2,entry_bg_3,entry_bg_4,entry_bg_5,entry_1,entry_2,entry_3,button_image_9,entry_4,entry_5,entry_image_1,entry_image_2,entry_image_3,entry_image_4,entry_image_5,button_image_6
    
    canvas2.create_text(460-425,168.0,anchor="nw",text="Nombre",fill="#7C7777",font=("K2D Bold", 24 * -1))
    canvas2.create_text(460.0-425,260.0,anchor="nw",text="Stock Actual",fill="#7C7777",font=("K2D Bold", 24 * -1))
    canvas2.create_text(460.0-425,355.0,anchor="nw",text="Variación de stock",fill="#7C7777",font=("K2D Bold", 24 * -1))
    skuCodeGet = entry_1.get()
    skuName,Stock0 = f.skuQuery(skuCodeGet)
    entry_bg_2 = canvas2.create_image(565.5-425,215.5,image=entry_image_2)
    label_2 = Label(canvas2,text= skuName,bd=0,bg="#d9d9d9",highlightthickness=0)
    label_2.place(x=452.0-400,y=203.0,width=170.0,height=30.0)
    label_3 = Label(canvas2,text= Stock0,bd=0,bg="#d9d9d9",highlightthickness=0)
    label_3.place(x=452.0-400,y=293.0,width=170,height=30.0)
    entry_bg_3 = canvas2.create_image(565.5-425,306.5,image=entry_image_3)
    entry_bg_4 = canvas2.create_image(565.5-425,400.5,image=entry_image_4)
    entry_4 = Entry(canvas2, bd=0,bg="#d9d9d9",highlightthickness=0)
    entry_4.place(x=452.0-400,y=386,width=170.0,height=30.0)
    
    button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_6 = Button(canvas2,image=button_image_6,borderwidth=0,width=227.0,height=51.0,highlightthickness=0,command=stockIncrease
    ,relief="flat")
    button_6.place(x=1102.0-425,y=739.0)
    
def stockIncrease():
    global canvas2
    skuCodeGet = entry_1.get()
    skuDeltaStockGet = entry_4.get()
    f.increase_stock(skuCodeGet,skuDeltaStockGet,aux_val)
    canvas2=canvas2Refresh()

    
def stock_info():
    global entry_1, entry_2, entry_3, entry_4, entry_5
    try:
        skuCodeGet = entry_1.get()
        deltaStockGet = entry_2.get()
        print(skuCodeGet)
        canvas2Refresh()
        return f.increase_stock(skuCodeGet,deltaStockGet)
    except Exception as e:
        print(e)

def EgresoStock():
    global aux_val
    aux_val = -1
    ModifySKU()

def IngresoStock():
    global aux_val
    aux_val = 1
    ModifySKU()

def skuPlot():
    global entry_bg_1,entry_bg_2,entry_bg_3,entry_bg_4,entry_bg_5,entry_1,entry_2,entry_3,button_image_9,entry_4,entry_5,entry_image_1,entry_image_2,entry_image_3,entry_image_4,entry_image_5,button_image_6
    canvas2 = canvas2Refresh()

    f.cur.execute("select DATE(date) AS date, sum(stock1) stock from stockinfo group by 1 order by 1 asc")
    data=f.cur.fetchall()
    print(data)
    date=[]
    stock=[]
    for n in data:
        print(type(n[0]))
        date.append(n[0].strftime("%d/%m"))
        stock.append(n[1])

    data12 = {'Date': date,
         'Stock final': stock
        }
    print(date,stock)
    df1 = DataFrame(data12,columns=['Date','Stock final'])
    print (df1)

    
    
    figure1 = plt.Figure(figsize=(10,8), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, canvas2)
    bar1.get_tk_widget().pack()
    df1 = df1[['Date','Stock final']].groupby('Date').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Variación de stocks diario')


window = Tk()
window.geometry("1359x800")
window.configure(bg = "#8E8D8D")
window.title("Stock Manager")

canvas = Canvas(window,bg = "#3A7FF6",height = 817,width = 425,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)  
canvas2 = Canvas(window,bg = "#FFFFFF",height = 817,width = 1359-425,bd = 0,highlightthickness = 0,relief = "ridge")
canvas2.place(x = 425, y = 0)
canvas.create_text(6.0,770.0,anchor="nw",text="RG",fill="#000000",font=("Kosugi Regular", 20 * -1))
canvas2.create_text(460-425,168.0,anchor="nw",text="Bienvenido!",fill="#7C7777",font=("K2D Bold", 50 * -1))

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=createSku,relief="flat")
button_1.place(x=99.0,y=142.0,width=227.0,height=51.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=IngresoStock,relief="flat")
button_2.place(x=99.0,y=233.0,width=227.0,height=51.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=EgresoStock ,relief="flat")
button_3.place(x=99.0,y=324.0,width=227.0,height=51.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4,borderwidth=0,highlightthickness=0,command=checkSKUs,relief="flat")
button_4.place(x=99.0,y=415.0,width=227.0,height=51.0)
button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(image=button_image_5,borderwidth=0,highlightthickness=0,command=lambda: print("button_5 clicked"),relief="flat")
button_5.place(x=99.0, y=506.0, width=227.0, height=51.0)
button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
button_7 = Button(image=button_image_7,borderwidth=0,highlightthickness=0,command=checkStocks,relief="flat")
button_7.place(x=99.0,y=597.0,width=227.0,height=51.0)
button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
button_8 = Button(image=button_image_8,borderwidth=0,highlightthickness=0,command=skuPlot,relief="flat")
button_8.place(x=99.0,y=688.0,width=227.0,height=51.0)

canvas.create_text(64.0,37.0,anchor="nw",text="    Stock  Manager",fill="#2B2B2B",font=("K2D Bold", 32 * -1))

window.resizable(False, False)
window.mainloop()
