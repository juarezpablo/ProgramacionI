#Alumno: Juan Pablo Juarez
#Comision: 00 

#La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes para la cocina de Industrias Wayne. 
#Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
#preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
#1-PESO: (entre 10 y 100 kilos)
#2-PRECIO POR KILO: (mayor a 0 [cero]).
#3-TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
#Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto. 
# o si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.
#A-El importe total a pagar, BRUTO sin descuento.
#B-El importe total a pagar con descuento (Solo si corresponde).
#C-Informar el tipo de alimento más caro.
#D-El promedio de precio por kilo en total.
importe_total_bruto = 0
acumulador_kilos_total = 0
precio_mayor = 0
contador_vueltas = 0
acumulador_precio_por_kilo = 0

while(True):
    while(True):
        peso = int(input("Ingrese peso 'Entre 10 y 100 kilos':  "))
        if(peso>=10 and peso <=100):
            acumulador_kilos_total += peso
            break
    precio_por_kilo = int(input("Ingrese precio por kilo:  "))
    while(precio_por_kilo<1):
           precio_por_kilo = int(input("Ingrese precio por kilo:  ")) 
    while(True):
        tipo_alimento = input("Ingrese tipo 'v':vegetal, 'a':animal, 'm':mezcla   ")
        if(tipo_alimento == "v" or tipo_alimento == "a" or tipo_alimento == "m"):
            break

    importe = precio_por_kilo * peso        
    importe_total_bruto += importe
    #C-Informar el tipo de alimento más caro.
    if(precio_por_kilo>precio_mayor):
        precio_mayor = precio_por_kilo
        tipo_alimento_mayor_precio = tipo_alimento
    #D-El promedio de precio por kilo en total.
    contador_vueltas+=1
    acumulador_precio_por_kilo+=precio_por_kilo

    respuesta = input("Desea Salir S/N ?")
    if(respuesta == "S" or respuesta == "s"):
        break

if(acumulador_kilos_total>100 and acumulador_kilos_total<300):
    descuento = 15
elif(acumulador_kilos_total>300):
    descuento = 25
else:
    descuento = 0

importe_total_con_descuento = importe_total_bruto - (importe_total_bruto * (descuento/100))
promedio_total_precio_por_kilo = acumulador_precio_por_kilo/contador_vueltas

print("A) El importe bruto es: $",importe_total_bruto)
if(descuento!=0):
    print("B) El importe total con descuento es: $",importe_total_con_descuento)
if(tipo_alimento_mayor_precio == "v"):    
    print("C)El tipo de alimento mas caro es: Vegetal")
elif(tipo_alimento_mayor_precio == "a"):
    print("C)El tipo de alimento mas caro es: Animal")
else:
    print("C)El tipo de alimento mas caro es: Mezcla")        
print("El promedio total de precio por kilo es: $",promedio_total_precio_por_kilo)