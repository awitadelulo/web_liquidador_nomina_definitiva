# Proyecto Calculadora de liquidacion definitiva

## Elaborado por: 

- Marcello Maccanti
- Sebastian Buitrago Quintero

## Optimizado para web por: 
 
- Walter Bedoya Perez
- David lópez Rivera

## ¿Qué es y para qué es?

Puedes guardar en la base de datos todos tus empleados y cuando desees calcular el pago de su liquidacion lo podras hacer seleccionandolos por su id. 
El proyecto es una calculadora de liquidacion definitiva; se utiliza para calcular el pago de liquidación cuando empleado
sale de la empresa, por despido, renuncia, finalización de contrado, entre otros.

## ¿Qué necesitas para que funcione?

-Tener instalado Kivy:  `pip install kivy[base]`
-Tener instalado Flask: `pip install flask`
-Tener instalado psycopg2: `pip install psycopg2`

## ¿Cómo se usa?


1. Para correrlo en la web primero debes clonar el repositorio en tu computadora, abriendo el git bash y escribiendo  `git clone https://github.com/awitadelulo/web_liquidador_nomina_definitiva.git`
2. Despues debes editar el archivo SecretConfig que esta en src/controller, debes ingresar los datos de acceso de tu base de datos (dejando el PGPORT intacto).
3. Luego deberas pararte en el archivo escribiendo en git bash `cd web_liquidador_nomina_definitiva`
4. Ahora escribes `py app.py` en el git bash, esto te dara un link `Running on 'aqui estara el link que debes copiar y pegar en el buscador' `
5. Ya en la web podras usar la calculadora


