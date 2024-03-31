# promedio de duracion
otros_min = 2.5
otros_max = 7
otros_promedio = 4
dalto = 1.5

#Duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5
#diferencias de duracion
dif_min = 100 - dalto / otros_min *100
dif_max = 100 - dalto *1000 // otros_max / 10
dif_promedio = 100 - dalto / otros_promedio *100

#calculando  el porcentaje de tiempo vacio
tiempo_vacio_promedio = 100 - otros_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto * 1000 // crudo_dalto / 10

print('-------------------')

#mostrando ejercicio A (diferencias de duracion)
print(f'El curso de Dalto dura un {dif_min}% menos que el mas rapido')
print(f'El curso de Dalto dura un {dif_max}% menos que el mas lento')
print(f'El curso de Dalto dura un {dif_promedio}% menos que el promedio')
print('-------------------')


#mostrando ejercicio B (porcentaje de tiempo vacío)
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio')
print('-------------------')
#mostrando la diferencia si los cursos duraran 10 horas
print(f'Ver 10 horas de este curso equivale a ver {otros_promedio * 100 // dalto / 10} horas de otros cursos')
print(f'Ver 10 horas de otros curso equivale a ver {dalto * 100 // otros_promedio / 10} horas de este curso')


