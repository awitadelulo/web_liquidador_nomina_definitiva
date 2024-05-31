from flask import Blueprint, render_template, request
import sys
import os
sys.path.append("src")
sys.path.append("Cl_liquidacion_definitiva/src")
import model.calculateLogic as calculateLogic
from model.calculateLogic import worker
from controller.controller_worker import ControllerWorker
ControllerWorker.EliminarTabla()
ControllerWorker.CreateTabla()

blueprint = Blueprint( "vista_usuario", __name__, "templates" )

import sys
sys.path.append("src")

@blueprint.route("/")
def Home():
   """
   Esta función maneja la ruta principal de la aplicación web.
   Cuando un usuario accede a la URL raíz ("/"), esta función se ejecuta 
   y devuelve el contenido de una página HTML específica llamada "menu_principal.html".
   """
   return render_template("menu_principal.html")

@blueprint.route( "/nuevo_empleado" )
def nuevo_empleado():
   """
   Esta función maneja la ruta "/nuevo_empleado" de la aplicación web.

   Cuando un usuario accede a la URL "/nuevo_empleado", esta función se ejecuta
   y devuelve el contenido de una página HTML específica llamada "nuevo_empleado.html"
   """
   return render_template("nuevo_empleado.html")

@blueprint.route("/crear_nuevo_empleado", methods=["POST"])
def crear_nuevo_empleado():
    """
    Esta función maneja la ruta "/crear_nuevo_empleado" de la aplicación web y 
    permite crear un nuevo empleado utilizando datos recibidos a través de un formulario POST.

    Cuando un usuario envía un formulario a la URL "/crear_nuevo_empleado", esta función
    se ejecuta y extrae los datos del formulario, crea una instancia de un objeto worker
    con esos datos y lo guarda en la base de datos.

    La función luego renderiza una página HTML específica llamada "trabajador.html",
    pasando el nuevo objeto trabajador y un mensaje de éxito a la plantilla.
    """
    # Extrae los datos del formulario enviados mediante POST
    id_empleado = request.form["id_empleado"]
    salario_base = request.form["salario_base"]
    meses_trabajados = request.form["meses_trabajados"]
    dias_vacaciones = request.form["dias_vacaciones"]
    horas_extras_diurnas = request.form["horas_extras_diurnas"]
    horas_extras_nocturnas = request.form["horas_extras_nocturnas"]
    dias_faltantes_contrato = request.form["dias_faltantes_contrato"]
    
    # Crea una instancia del objeto worker con los datos del formulario
    trabajador = worker(
        id=id_empleado,
        salary_base=salario_base,
        months_worked=meses_trabajados, 
        vacation_days=dias_vacaciones,
        hours_extra=horas_extras_diurnas,
        hours_extra_nigth=horas_extras_nocturnas,
        days_finish=dias_faltantes_contrato)
    
    ControllerWorker.Insertarworker(trabajador)
    mensaje = "Se ha ingresado con éxito el trabajador"
    return render_template("trabajador.html", trabajador=trabajador, mensaje=mensaje)


@blueprint.route( "/seleccionar_empleado" )
def seleccionar():
   '''
   Esta función maneja la ruta "/seleccionar_empleado" de la aplicación web.
   Cuando un usuario accede a la URL "/seleccionar_empleado", esta función se ejecuta
   y devuelve el contenido de una página HTML específica llamada "seleccionar_empleado.html".
   '''
   return render_template("seleccionar_empleado.html")

@blueprint.route("/mostrar_informacion_empleado", methods=['POST'])
def mostrar_informacion_empleado():
   '''
   Esta función maneja la ruta "/mostrar_informacion_empleado" de la aplicación web y
   permite mostrar la información de un empleado utilizando un ID recibido a través de un formulario POST.

   Cuando un usuario envía un formulario a la URL "/mostrar_informacion_empleado", esta función
   se ejecuta y extrae el ID del empleado del formulario, busca al empleado en la base de datos
   utilizando el controlador ControllerWorker, y luego renderiza una página HTML específica
   llamada "trabajador.html" pasando el objeto trabajador y un mensaje.
   '''
   id_empleado = request.form["id_empleado"]
   trabajador=ControllerWorker.BuscarWorkerId(id_empleado)
   mensaje="El empleado que buscaste es este"
   return render_template("trabajador.html", trabajador=trabajador, mensaje=mensaje)


@blueprint.route( "/eliminar_empleado" )
def eliminar():
   '''
   Esta función maneja la ruta "/eliminar_empleado" de la aplicación web.
   Cuando un usuario accede a la URL "/eliminar_empleado", esta función se ejecuta
   y devuelve el contenido de una página HTML específica llamada "eliminar_empleado.html".
   '''
   return render_template("eliminar_empleado.html")

@blueprint.route('/eliminar_trabajador_definitivo', methods=['POST'])
def eliminar_trabajador_definitivo():
   '''
   Esta función maneja la ruta "/eliminar_trabajador_definitivo" de la aplicación web y permite eliminar 
   de manera definitiva a un trabajador utilizando un ID recibido a través de un formulario POST.
   Cuando un usuario envía un formulario a la URL "/eliminar_trabajador_definitivo", esta función se ejecuta y extrae el ID del empleado del formulario. Luego, 
   utiliza el controlador ControllerWorker para eliminar definitivamente al trabajador de la base de datos.
   Después de eliminar al trabajador, se renderiza una página HTML específica llamada "eliminar_definitivamente.html",
    pasando el ID del empleado eliminado como parámetro.
   '''
   id_empleado = request.form["id_empleado"]
   ControllerWorker.EliminarWorker(id_empleado)
   return render_template("eliminar_definitivamente.html",numero_cedula=id_empleado)


@blueprint.route( "/modificar_empleado" )
def modificar():
   '''
   Esta función maneja la ruta "/modificar_empleado" de la aplicación web.
   Cuando un usuario accede a la URL "/modificar_empleado", esta función se ejecuta
   y devuelve el contenido de una página HTML específica llamada "modificar_empleado.html".
   '''
   return render_template("modificar_empleado.html")

@blueprint.route("/modificar_empleado_tabla", methods=['POST'])
def modificar_empleado_tabla():
   '''
    Esta función maneja la ruta "/modificar_empleado_tabla" de la aplicación web y permite modificar 
    los atributos de un empleado utilizando datos recibidos a través de un formulario POST.
    Cuando un usuario envía un formulario a la URL "/modificar_empleado_tabla", 
    esta función se ejecuta y extrae el ID del empleado, el nuevo valor y el atributo a modificar del formulario. 
    Luego utiliza el controlador ControllerWorker para modificar el atributo del empleado en la base de datos.
    Después de modificar el empleado, se busca nuevamente en la base de datos y se renderiza una página HTML específica llamada 
    "trabajador.html", pasando el objeto trabajador modificado y un mensaje.
   '''
   id_empleado = request.form['id_empleado']
   nuevo_valor = request.form['nuevo_valor']
   atributo = request.form['atributo']
   ControllerWorker.modifacarWorker2(ID=id_empleado,Variable=atributo,valor=nuevo_valor)
   trabajador_modificado=ControllerWorker.BuscarWorkerId(id_empleado)
   mensaje="EL ususario fue modificado correctamente y ahora eston son los valores "
   return render_template("trabajador.html", trabajador=trabajador_modificado, mensaje=mensaje)

@blueprint.route("/ver_liquidacion", methods=['POST'])
def ver_liquidacion():
   '''
   Esta función maneja la ruta "/ver_liquidacion" de la aplicación web y permite calcular y mostrar la liquidación 
   de un trabajador utilizando datos recibidos a través de un formulario POST.
   Cuando un usuario envía un formulario a la URL "/ver_liquidacion", 
   esta función se ejecuta y extrae el ID del empleado del formulario. Luego, utiliza el controlador 
   ControllerWorker para buscar al trabajador en la base de datos y calcular la liquidación.
   Después de calcular la liquidación, se renderiza una página HTML específica llamada "trabajador_liquidacion.html", 
   pasando el objeto trabajador, un mensaje y el resultado de la liquidación.
   '''
   id_empleado = request.form['id_empleado']
   trabajador=ControllerWorker.BuscarWorkerId(id_empleado)
   reultado=ControllerWorker.calculate_liquidacion_def(trabajador)
   mensaje="La catidad a pagar esta aca"
   return render_template("trabajador_liquidacion.html",trabajador=trabajador,mensaje=mensaje,liquidacion_total=reultado)

@blueprint.route( "/liquidacion_empleado" )
def liquidacion():
   '''
   Esta función maneja la ruta "/liquidacion_empleado" de la aplicación web.
   Cuando un usuario accede a la URL "/liquidacion_empleado", esta función se ejecuta
   y devuelve el contenido de una página HTML específica llamada "liquidacion_empleado.html".
   '''
   return render_template("liquidacion_empleado.html")




