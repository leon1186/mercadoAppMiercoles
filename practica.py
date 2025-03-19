nombres=[]
cantidad =int(input("ingresa cuantos nombres quieres ingresar: \n"))

for i in range(cantidad ):
    nombre=input(f'in grese el nombre {i}: \n')
    nombres.append(nombre)

print(f'los nombres ingresados son {nombres}')    

