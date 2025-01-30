"""Modifica el ejercicio de la práctica anterior para que el proceso se repita minetras el usuario introduzca
continuar (S/N).
Debes indicar el final del proceso, cuánto dinero recauda el Estado en concepto de IRPF, y en concepto de
SS, además de cuánto dinero invierte la empresa en total en la fuerza de trabajo. Muestra
una lista de sueldos netos con los nombres de los trabajadores."""

# def calcularSalarioParte2(sueldo):
#     irpf = sueldo * 0.12
#     ssl = sueldo * 0.528
#     return irpf, ssl, sueldo
#
# salir = True
# nombreTrabajadores = []
#
# while salir:
#     nombre = input("Ingresa el nombre: ")
#     nombreTrabajadores.append(nombre)
#     sueldo = float(input("Ingresa el sueldo bruto: "))
#     continuar = input("Continuar? [S/N]")
#     nombreTrabajadores.append(nombre)
#     if continuar == "S":
#         salir = True
#
#     else:
#         print(f"" + nombreTrabajadores)
#         salir = False

irpfRecaudado = 0
ssRecaudado = 0
inversionTotal = 0
nombresTrabajadores = []
sueldosTrabajadores = []
continuar = True

while continuar:
    nombre = input("Nombre del trabajador: ")
    sueldoBruto = float(input("Sueldo bruto: "))
    irpf = sueldoBruto * 0.12
    ss = sueldoBruto * 0.0520
    irpfRecaudado += irpf
    ssRecaudado += ss
    inversionTotal += sueldoBruto
    Descuento = irpf + ss
    sueldoNeto = sueldoBruto - Descuento
    nombresTrabajadores.append(nombre)
    sueldosTrabajadores.append(sueldoNeto)
    # if input("¿continuar? (s/n)".lower()) != "s"

    continuar = False

print(f"El estado recauda {irpfRecaudado} en IRPF. ")
print(f"El estado recauda {ssRecaudado} en SS. ")
print(f"La empresa ")



