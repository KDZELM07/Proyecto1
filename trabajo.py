nombre=input("escriba su nombre: ")
edad=int(input("escriba su edad: "))

if(edad>=18):
    permiso="puede conducir"
    mayor=True
else:
    permiso="no puede conducir"
    mayor=False

licencia=bool(int(input("digite 1 si tiene licencia, 0 si no tiene: ")))  
   
if (licencia==1 and mayor==True):
   print(f"señor/señora {nombre}, usted puede conducir")
else:
    print(f"señor/señora {nombre}, usted no puede conducir")
