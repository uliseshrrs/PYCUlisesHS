SUE = float (input("INGRESA EL SUELDO DEL TRABAJADOR:"))
if SUE < 1000 :
    AUM = SUE * 0.15
    NSUE = SUE + AUM
    print(f"EL AUMENTO DEL TRABAJADOR ES DE : {AUM} $ Y SU NUEVO SUELDO ES  :{NSUE} $")

if SUE > 1000:
    print("FIN DEL PROGRAMA")
