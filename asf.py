tarifaAnual = 10000

edad = int(input())
print("¿Usted trabaja?")
print("1- Si")
print("2- No")
trabajo = int(input())
print("Edad: ", edad, ", Trabajo: ", trabajo)
if edad > 18 and trabajo == 1 :
    print("Usted paga el 100% de la tarifa") 
    print("Monto a abonar: ", tarifaAnual, "$")
elif edad < 18 and trabajo == 1  :
    descuento = (tarifaAnual * 5) / 100
    tarifaFinal = tarifaAnual - descuento
    print("Usted paga el 95% de la tarifa")
    print("Monto a abonar: ", tarifaFinal, "$")
elif edad > 18 and trabajo == 2 :
    descuento = (tarifaAnual * 25) / 100
    tarifaFinal = tarifaAnual - descuento
    print("Usted paga el 75% de la tarifa")
    print("Monto a abonar: ", tarifaFinal, "$")
elif edad < 18 and trabajo == 2 :
    descuento = (tarifaAnual * 50) / 100
    tarifaFinal = tarifaAnual - descuento
    print("Usted paga el 50% de la tarifa")
    print("Monto a abonar: ", tarifaFinal, "$")
    print("gracias locaso")
              