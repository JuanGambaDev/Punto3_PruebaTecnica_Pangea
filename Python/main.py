import os

productos = []

def mostrar_menu_principal():
    #Mostramos un menu que guie al usuario en el proceso
    os.system('clear') #Limpiamos la consola. para OS Windows es encesario usar "cls"
    print("---------------------------------------------")
    print("                    MENÚ                     ")
    print("---------------------------------------------")
    print("[1]Agregar producto a la lista.")
    print("[2]Calcular IVA sobre productos de la lista.")
    print("[3]Salir.")
    print("")
    #Solicitamos opcion al usuario
    opcion = input("*Selecciona su opción: ")
    #comprobamos la opcion que eligio el usuario para enviarlo a una determinada funcion
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        solicitar_iva()
    elif opcion == "3":
        print("--> Fin")
        print("")
        # Salir de la aplicación
        exit()

def agregar_producto():
  os.system('clear') #Limpiamos la consola. para OS Windows es encesario usar "cls"
  inventario = False
  while inventario == False:
    nombre_producto = ""
    while len(nombre_producto)!=10:
      nombre_producto = input("Ingrese producto: ")
      if(len(nombre_producto)>10):
        print("tienes que introducir 10 caracteres")
      else:
        precio = int(input("ingrese precio del producto: "))
        producto = [nombre_producto, precio]
        productos.append(producto)
        if producto in productos:
            inventario = True
            print("Producto registrado de forma exitosa!")
            print(productos)
            opc = input("¿Desea realizar un nuevo registro? [y]Si [n]No: ")
            if opc == "y":
                inventario = False
            else:
                inventario = True
                mostrar_menu_principal()
        else:
            print("Error en registro. Por favor intente de nuevo")

def solicitar_iva():
  os.system('clear') #Limpiamos la consola. para OS Windows es encesario usar "cls"
  calcular = False
  while calcular == False:
    iva = ""
    while iva == "":
      iva = int(input("Ingrese un porcentaje de IVA. Valores permitidos(0-35): "))
      if iva > 35:
        print("ingere un valor valido.")
      else:
        for producto in productos:
          nombre, precio = producto
          valor_iva = iva * precio / 100
          productos[productos.index(producto)] = [nombre,valor_iva]
          calcular = True
        print("El valor del IVA de cada producto es: ", productos)
        opc = input("¿Desea realizar un nuevo cálculo? [y]Si [n]No: ")
        if opc == "y":
            calcular = False
        else:
            calcular = True
            mostrar_menu_principal()

def init():
  mostrar_menu_principal()
  
if __name__ == "__main__":
    init()