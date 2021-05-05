# PRESA-PREDADOR
## ¿Qué es?

PRESA-PREDADOR es un código que permita llevar a cabo la simulación de las ecuaciones de Lotka-Volterra ambientado a un ecosistema donde conviven presas y predadores. El objetivo es poder analizar de qué manera se comportan las poblaciones de ambos en base a condiciones de entorno iniciales establecidas desde capacidades de terreno y tasas de supervivencia, de manera que ingresando cierta cantidad de cada población respectivamente se pueda interpretar graficamente qué pasa con ellos.

<img src="https://i.pinimg.com/originals/cc/4d/90/cc4d905bd67df4d2fc3747f010757e1d.jpg" width="100" height="100">
VS
<img src="http://todovector.com/vector/animales/terrestres/zorro/1.png" width="100" height="100">

**¿QUÉ PARAMETROS POSEE?**

La simulación insume los siguientes parametros iniciales:
-Cantidad de presas
-Cantidad de predadores
-Capacidad de terreno para limitar la natalidad de presas en el ecosistema
-Tasa de natalidad de presas
-Tasa de supervivencia de predadores
-Diferencial de tiempo representativo sobre la unidad del tiempo a considerar (unidad: semana)
-Cantidad de encuentros

La transformación de la población se simula a través de un ciclo de tiempo, seteado por defecto en 500 (unidad: semanas)

**¿DE QUÉ MANERA ESTÁ REPRESENTADO EL COMPORTAMIENTO DEL ECOSISTEMA?**
El comportamiento se representa a través de dos diagramas fundamentales:
- Diagrama de fase con la información de presas y predadores para visualizar los cambios que posee nuestro esquema poblacional en función de las condiciones dadas.
- Diagrama poblacional con la cantidad de presas y Predadores para poder visualizar la supervivencia de ambas especies en función del tiempo.

**NUESTRO PATRÓN INICIAL**

La simulacion inicial está seteado en 2500 presas y 2 predadores, como únicos valores a modificar. Una vez representado la primer situacion, la aplicación consulta si desea manifestar otro esquema poblacional, en caso de ser positiva la respuesta del usuario se solicitan las cantidades de presas y predadores y comienza la nueva simulacion.

**¿CUANDO TERMINA?**
Finaliza por iteracción de consola cuando la simulación actual finalizó y el usuaro no desea cargar otro par poblacional.
