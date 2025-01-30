""""Vas a capturar el nombre de una persona y el sueldo bruto que va a cobrar. Debes
calcular el sueldo neto de dicha persona. Se le descuenta como IRPF un 12% y en
concepto de Seguridad social 5,28%. Mostrar un mensaje: EL sueldo neto de
XXXXXX es XXXXXX euros


#OTRO SCRIPT

Modifica el ejercicio de la práctica anterior para que el proceso se repita minetras el sueldo
de la persona sea positivo. Debes indicar al final del proceso, cuánto dinero recaida el
Estado en concepto de IRPF y Seguridad Social. Y cuánto dinero paga la empresa por
todos sus trabajdores antes de applicar los impuestos."""

nombre = input("Ingresa tu nombre: ")
sueldo = float(input("Ingresa tu sueldo bruto: "))
IRPF = sueldo * 0.12
SS = sueldo * 0.0528
descuento = IRPF + SS
sueldoNeto = sueldo - descuento
print("El sueldo neto de: " + nombre + " es: ", sueldoNeto)







