total_altura_mujeres = 0
total_altura_varones = 0
total_edad = 0
cantidad_mujeres = 0
cantidad_varones = 0
cantidad_participantes = 0

while True:
    altura = float(input("Ingrese la altura en cm (valor negativo para terminar): "))
    if altura < 0:
        break  
    
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (F/M): ").strip().upper()

    total_edad += edad
    cantidad_participantes += 1

    if sexo == 'F':
        total_altura_mujeres += altura
        cantidad_mujeres += 1
    elif sexo == 'M':
        total_altura_varones += altura
        cantidad_varones += 1
    else:
        print("Sexo no válido. Intente nuevamente.")

promedio_altura_mujeres = total_altura_mujeres / cantidad_mujeres if cantidad_mujeres > 0 else 0
promedio_altura_varones = total_altura_varones / cantidad_varones if cantidad_varones > 0 else 0
promedio_edad = total_edad / cantidad_participantes if cantidad_participantes > 0 else 0

print("\nResultados:")
print(f"Promedio de altura de las mujeres: {promedio_altura_mujeres:.2f} cm")
print(f"Promedio de altura de los varones: {promedio_altura_varones:.2f} cm")
print(f"Promedio de edad de los participantes: {promedio_edad:.2f} años")
