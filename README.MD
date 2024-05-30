# Proyecto Calculadora de liquidacion definitiva

## Elaborado por: 

Marcello Maccanti
Sebastian Buitrago Quintero


## ¿Qué es y para qué es?

El proyecto es una calculadora de liquidacion definitiva; se utiliza para calcular el pago de liquidación cuando empleado
sale de la empresa, por despido, renuncia, finalización de contrado, entre otros.

## ¿Cómo funcionar?

En esta etapa del proyecto el codigo tiene una interfaz en la que solo se necesita clonar el proyecto para corrrerlo y se utiliza con el comando src/console_basic/interfaz.py

Y una interfaz por consola, para corrrerlo se utiliza con el comando src/console/interfaz.py. 

para correr las pruebas unitarias se utiliza el comando tests\liquidacionTest.py

librerias a tener en cuenta: kivy, unittest, sys.
La libreria kivy nos proporciona los medios para crear una interfaz amigable con el usuario.

La libreria unittest nos permite correr las prubas unitarias; y la libreria sys nos permite importar clases de otras carpetas

El codigo lanza una serie de preguntas necesarias para ejecutar las operaciones por consola; el cuales tiene, salario base, dias de vacaciones,
cesantias, entre otras.

## ¿Cómo está hecho?

El proyecto esta organizado en carpetas donde encontramos .vscode, src, tests y el archivo de README... 
utilizamos las librerias de unittest, sys.

-Dentro de las carpeta .vscode encontramos el archivo tipo json, el cual contiene un arcvicho json 

-Dentro de las carpeta src encontramos un archivo __init__ y 2 carpetas las cuales son: console el cual contiene los archivos interfaz.py, console_kivy.py y __init__, tambien otra carpeta llamada settlement el cual contiene los archivos calculateLogic y __init__. 

Dentro de las carpeta tests encontramos los archivos __init__ y liquidacionTest.

## Entradas
self.salary_base = salario base
self.months_worked = meses trabajados
self.vacation_days = dias de vacaciones
self.extra_hours = horas extras
self.night_charges = cargos nocturnos
self.compensation_dismissal = compensacion de despido


# CL_liquidacion_definitiva
