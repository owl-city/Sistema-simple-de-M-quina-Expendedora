# -*- coding: utf-8 -*-
def main():
        print("Códigos Disponibles:")
if __name__ == "__main__":
        main()
print("A1, A2, A3, A4, A5" '\n')

Boton=input("Elige un código: ")


MiTupla=("A1", "A2", "A3", "A4", "A5")
MiDiccionario={MiTupla[0]:"$6", MiTupla[1]:"$7.50", MiTupla[2]:"$8", MiTupla[3]:"$10", MiTupla[4]:"$11"}

if Boton == "A1":
        print(f"El precio es de: {MiDiccionario[Boton]}" '\n')
elif Boton == "A2":
        print(f"El precio es de: {MiDiccionario[Boton]}" '\n')
elif Boton == "A3":
        print(f"El precio es de: {MiDiccionario[Boton]}" '\n')
elif Boton == "A4":
        print(f"El precio es de: {MiDiccionario[Boton]}" '\n')
elif Boton == "A5":
        print(f"El precio es de: {MiDiccionario[Boton]}" '\n')
else:
        print("El código no existe, introduce un código válido")
        exit()                
        
Dinero=float(input("Introduce tu moneda: "))
if Dinero > 0:
        
        print(f"Ingresó ${Dinero}")
    
        if Boton == "A1":
                if Dinero  < 6 :
                        suma=(6-Dinero)
                        print (f"Le falta ${suma}")
                else:
                        suma=(Dinero-6)
                        print(f"Su cambio es de ${suma} pesos")

        elif Boton == "A2":
                if Dinero < 7.50:
                        suma=(7.50-Dinero)
                        print(f"Le falta ${suma}")
                else:
                        suma=(Dinero-7.50)
                        print(f"Su cambio es de ${suma} pesos")

        elif Boton == "A3":
                if Dinero < 8:
                        suma=(8-Dinero)
                        print(f"Le falta ${suma}")
                else:
                        suma=(Dinero-8)
                        print(f"Su cambio es de ${suma} pesos")
        elif Boton == "A4":
                if Dinero < 10:
                        suma=(10-Dinero)
                        print(f"Le falta ${suma}")
                else:
                        suma=(Dinero-10)
                        print(f"Su cambio es de ${suma} pesos")
        elif Boton == "A5":
                if Dinero < 11:
                        suma=(11-Dinero)
                        print(f"Le falta ${suma}")
                else:
                        suma=(Dinero-11)
                        print(f"Su cambio es de ${suma} pesos")
        else:
                print("Proporcine un código válido")
else:
        print("Tienes que elegir un número real")
