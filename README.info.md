# PRESA-PREDADOR
## ¿Qué es?

PRESA-PREDADOR es un código que permita llevar a cabo la simulación de las ecuaciones de Lotka-Volterra ambientado a un ecosistema donde conviven presas y predadores. El objetivo es poder analizar de qué manera se comportan las poblaciones de ambos en base a condiciones de entorno iniciales establecidas desde capacidades de terreno y tasas de supervivencia, de manera que ingresando cierta cantidad de cada población respectivamente se pueda interpretar graficamente qué pasa con ellos.

<img src="https://i.pinimg.com/originals/cc/4d/90/cc4d905bd67df4d2fc3747f010757e1d.jpg" width="100" height="100"><img src="http://todovector.com/vector/animales/terrestres/zorro/1.png" width="100" height="100">

**¿QUÉ PARAMETROS POSEE?**

La simulación insume los siguientes parametros iniciales:
-Cantidad de presas: definido de forma pre determinada en 2500 presas
-Cantidad de predadores: definido de forma predeterminada en 2 predadores
-Capacidad de terreno: definido para limitar la natalidad de presas en el ecosistema. Se considera que no existen agentes externos que pueden
formar parte de la tasa de mortalidad de las presas como condicion de entorno.
-Tasa de natalidad de presas: relacionado directamente a la capacidad del terreno y las condiciones establecidas por las ecuaciones de Lotka Volterra
-Tasa de supervivencia de predadores
-Diferencial de tiempo representativo sobre la unidad del tiempo a considerar (unidad: semana)
-Cantidad de encuentros

La transformación de la población se simula a través de un ciclo de tiempo, seteado por defecto en 500 (unidad: semanas)

**ALGORITMOS UTILIZADOS Y FLUJO DE TRABAJO**
Los algoritmos incorporados son:
- Un condicional While que analiza el estado de una variable 'run' que varía dependiendo de la toma de decisiones que el usuario lleve a cabo por consola luego de finalizar el primer modelado con las ecuaciones pre establecidas.
- Dentro del funcionamiento del While, tenemos incorporado el flujo de trabajo que el ecosistema manifiesta durante el curso de 500 semanas (loop manipulado con condicional For).

PRIMERAS INSTANCIAS :seedling:
Se define la capacidad actual de liebres que el ecosistema posee :rabbit:
Se generan los primeros calculos de los parámetros definidos y comienza a acumularse la cantidad de presas y predadores resultantes
Estos resultados son almacenados en dos array definidos previos al loop, respectivamente a presa y predador, a traves de un append
Al finalizar el loop de 500 semanas, dentro de estos arrays hemos podido obtener respectivamente a cada ciclo, las magnitudes poblacionales obtenidas en cada semana en función de los parametros calculados en cada uno de ellos
Ambos arrays comienzan a ser graficados :chart_with_downwards_trend:. Se lleva a cabo un diagrama poblacional para representar la poblacion de presas y predadores con el uso de matplotlib, librería especializada en la gráfica de datos contenidos en listas o arrays

DIAGRAMA DE FASE
El diagrama de Fase nos permite interpretar como fueron comportandose las poblaciones de ambas especies a lo largo del ciclo. Comenzando con una tendencia de 2500 presas y un rango cercano al 0 de predadores, manifestando un crecimiento de predadores y un decrecimiento de presas como las primeras variaciones, hasta llegar a un pico máximo de poblacion de predadores pero un mínimo de presas, por lo que predadores comienzan a morir por un determinado tiempo hasta que las presas pueden comenzar a aumentar en natalidad. Nuevamente comienza un comportamiento similar al anterior pero en menor escala, hasta demostrar una tendencia de comportamiento de un total de 500 presas para 25 predadores aproximadamente.

![image info](./src/phase-diagram.png)

DIAGRAMA DE POBLACION
Los diagramas de poblacion nos permite representar respectivamente como se comportaron ambos grupos poblacionales en función del tiempo, los picos crecientes, decrecientes y la tendencia a mantenerse. En este caso: podemos visualizar que las presas comenzaron un pico de 2500, y los predadores en su valor inicial de 2. Al comenzar el ciclo, las presas decrecen a su pico máximo y los predadores aumentan a su pico máximo. Esto genera que los predadores deban pasar hambre y morir para el proximo ciclo hasta que las presas puedan comenzar a nacer nuevamente y recomponer su natalidad, las oscilaciones comienzan a repetirse en menor escala hasta lograr la tendencia que el diagrama de fase demostraba.

![image info](./src/poblational-diagram.png)

**NUESTRO PATRÓN INICIAL**

La simulacion inicial está seteado en 2500 presas y 2 predadores, como únicos valores a modificar. Una vez representado la primer situacion, la aplicación consulta si desea manifestar otro esquema poblacional, en caso de ser positiva la respuesta del usuario se solicitan las cantidades de presas y predadores y comienza la nueva simulacion.

EJEMPLOS DE SIMULACIONES PROPIAS:
500 PRESAS 1 PREDADOR

![image info](./src/phase1-diagram.png)
![image info](./src/poblational1-diagram.png)

3000 PRESAS 30 PREDADORES

![image info](./src/phase2-diagram.png)
![image info](./src/poblational2-diagram.png)

Como podemos ver, el primer ejemplo extra simula una situacion parecida en el modelado del ecosistema pero en cambio, en el segundo caso las poblaciones sufren picos de mortalidad bruzcos constanemente y si bien se repite el patrón de comportamiento, no logra encontrar un punto equilibrado de natalidad/mortalidad de las especies puestas en prueba.
**¿CUANDO TERMINA?**
Finaliza por iteracción de consola cuando la simulación actual finalizó y el usuaro no desea cargar otro par poblacional.
