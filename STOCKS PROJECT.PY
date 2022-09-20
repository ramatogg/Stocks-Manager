# FUNCIONES BASICAS: añadir sku, eliminar sku, consulta de sku, operar sku + - , log sku (modif en sql) , usuario q modifico
# atributos de un SKU:  nombre. volumen peso, precio, fecha vencimiento?,
#
#
import openpyxl as xl
import tkinter as tk

window = tk.Tk()

availableProducts = {}
path=r"C:\Users\agust\OneDrive\Escritorio\Stock-Manager\sku.xlsx"
print(path)
skuManagerxls=xl.load_workbook(path)
ws1 = skuManagerxls.worksheets[0]

class skuProduct(object):
    def __init__(self, name, volume, weight, price,qty=0):
        self.vol = volume
        self.weight = weight
        self.price = price
        self.name = name
        self.qty = qty

    def getVol(self):
        return self.vol

    def getPrice(self):
        return self.price

    def getWeight(self):
        return self.weight

    def getName(self):
        return self.name
    
    def getQty(self):
        return self.qty

    def ingresoStock(self,qty):    
        self.qty+=qty
        return self.qty

    def egresoStock(self,qty):    
        self.qty-=qty
        return self.qty
        
def crearNuevoSKU():
    name=input(f"ingresa el nombre del SKU \n")
    volume=input(f"ingresa el volumen del SKU \n")
    weight=input(f"ingresa el peso del SKU \n")
    price=input(f"ingresa el precio del SKU \n")
    sku=skuProduct(name,volume,weight,price)
    availableProducts[sku.name] = sku
    ws1.cell(1,1).value = name
    skuManagerxls.save(path)
    return main()


def eliminarSKU():
    name=input(f"ingresa el nombre del SKU a eliminar\n")
    try:
        availableProducts.pop(name)
    except:
        print("el SKU no existe.\n")
    return main()
    
def operarQty():
    operacion=input(f"Tipo de Operacion : 1 Ingreso - 2 Egreso\n")
    if not operacion in ["1","2"]: return main()

    skuName=input(f"Sku ? \n")
    if not skuName in availableProducts.keys(): return main()
    try:
        cantidad=int(input(f"Cantidad ? \n"))
    except:
        print("no pusiste una cantidad valida. por favor proba de nuevo \n")
        return operarQty
    if operacion == "1":
        print(f"se agrego al stock. cantidad nueva:{availableProducts[skuName].ingresoStock(cantidad)} \n")
    elif operacion == "2":
        print(f"se resto al stock. cantidad nueva:{availableProducts[skuName].egresoStock(cantidad)} \n")
    else:
        print("Opcion incorrecta \n")
        probar=input("opción incorrecta! queres probar de nuevo? si/no \n")
        if probar=="si":
            return operarQty()
    return main()    


def main():
    greeting = tk.Label(text="STOCK MANAGER \n Acciones disponibles \n1 - Ingresar SKU \n 2 - Eliminar SKU \n 3 - Operar Cantidad \n 4 - Consulta SKU \n")
    greeting.pack()
    x = int(input("Seleccionar ACCION: \n"))
    if x == 1:
        crearNuevoSKU()
    elif x == 2:
        eliminarSKU()
    elif x == 3:
        operarQty()
#    elif x == 4:
#       consultaSKU()
    else:
       print("Opcion incorrecta")
       return main() 

main()

