import matplotlib.pyplot as plt

#CONDICIONES INICIALES DE POBLACION
presa = 2500
predador = 2

#PARAMETROS LIEBRES-ZORROS
tasa_presa = 0.08
tasa_predador = 0.2
capacidad_terreno = 1500
dt = 1

total_presa = []
total_predador = []
run = True

initial_presa = presa
initial_predador = predador

while run == True:
    for i in range(500):
        cap_actual = capacidad_terreno - presa
        incremental_presa = (cap_actual/capacidad_terreno)*tasa_presa*presa
        dis_predador = tasa_predador * predador
        cantidad_encuentros = presa * predador
        presa = presa + dt * (incremental_presa - 0.002 * cantidad_encuentros)
        predador = predador + dt * (0.0004 * cantidad_encuentros - dis_predador)
        total_presa.append(presa)
        total_predador.append(predador)

    plt.plot(total_presa, total_predador)
    plt.ylabel('Poblacion Predadores')
    plt.xlabel('Poblacion Presas')
    plt.title('MODELACION CANTIDAD PRESA: {} PREDADOR: {}'.format(initial_presa, initial_predador))
    plt.show()

    plt.plot(total_presa, label='Presa')
    plt.ylabel('Poblacion Presas')
    plt.xlabel('Semanas')
    plt.legend(loc='upper right', bbox_to_anchor=(0.5, 0.6, 0.5, 0.5))

    plt.twinx()

    plt.plot(total_predador, label='Predador', color='red')
    plt.ylabel('Poblacion Predadores')
    plt.xlabel('Semanas')
    plt.legend(loc='upper right', bbox_to_anchor=(0.3, 0.6, 0.5, 0.5))

    plt.grid()
    plt.show()

    opc = input(str("¿Desea hacer otra prueba? Y/N\n"))
    if opc == 'Y':
        presa = int(input("Ingrese la cantidad de presas a modelar\n"))
        predador = int(input("Ingrese la cantidad de predadores a modelar\n"))
        initial_presa = presa
        initial_predador = predador
        run = True
    else:
        run = False
