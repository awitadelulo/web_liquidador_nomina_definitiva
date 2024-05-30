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
   return render_template("menu_principal.html")

@blueprint.route( "/nuevo_empleado" )
def nuevo_empleado():
   return render_template("nuevo_empleado.html")

@blueprint.route("/crear_nuevo_empleado", methods=["POST"])

def crear_nuevo_empleado():
    id_empleado = request.form["id_empleado"]
    salario_base = request.form["salario_base"]
    meses_trabajados = request.form["meses_trabajados"]
    dias_vacaciones = request.form["dias_vacaciones"]
    horas_extras_diurnas = request.form["horas_extras_diurnas"]
    horas_extras_nocturnas = request.form["horas_extras_nocturnas"]
    dias_faltantes_contrato = request.form["dias_faltantes_contrato"]
   
    trabajador = worker(
        id=id_empleado,
        salary_base=salario_base,
        months_worked=meses_trabajados, 
        vacation_days=dias_vacaciones,
        hours_extra=horas_extras_diurnas,
        hours_extra_nigth=horas_extras_nocturnas,
        days_finish=dias_faltantes_contrato
    )
   
    ControllerWorker.Insertarworker(trabajador)
    mensaje="se ha ingresado con exito el trabajador"
    return render_template("trabajador.html", trabajador=trabajador, mensaje=mensaje)


@blueprint.route( "/seleccionar_empleado" )
def seleccionar():
   return render_template("seleccionar_empleado.html")

@blueprint.route("/mostrar_informacion_empleado", methods=['POST'])
def mostrar_informacion_empleado():
   id_empleado = request.form["id_empleado"]
   trabajador=ControllerWorker.BuscarWorkerId(id_empleado)
   mensaje="El empleado que buscaste es este"
   return render_template("trabajador.html", trabajador=trabajador, mensaje=mensaje)


@blueprint.route( "/eliminar_empleado" )
def eliminar():
   return render_template("eliminar_empleado.html")

@blueprint.route('/eliminar_trabajador_definitivo', methods=['POST'])
def eliminar_trabajador_definitivo():
   id_empleado = request.form["id_empleado"]
   ControllerWorker.EliminarWorker(id_empleado)
   return render_template("eliminar_definitivamente.html",numero_cedula=id_empleado)


@blueprint.route( "/modificar_empleado" )
def modificar():
   return render_template("modificar_empleado.html")

@blueprint.route("/modificar_empleado_tabla", methods=['POST'])
def modificar_empleado_tabla():
   id_empleado = request.form['id_empleado']
   nuevo_valor = request.form['nuevo_valor']
   atributo = request.form['atributo']
   ControllerWorker.modifacarWorker2(ID=id_empleado,Variable=atributo,valor=nuevo_valor)
   trabajador_modificado=ControllerWorker.BuscarWorkerId(id_empleado)
   mensaje="EL ususario fue modificado correctamente y ahora eston son los valores "
   return render_template("trabajador.html", trabajador=trabajador_modificado, mensaje=mensaje)

@blueprint.route("/ver_liquidacion", methods=['POST'])
def ver_liquidacion():
   id_empleado = request.form['id_empleado']
   trabajador=ControllerWorker.BuscarWorkerId(id_empleado)
   reultado=ControllerWorker.calculate_liquidacion_def(trabajador)
   mensaje="La catidad a pagar esta aca"
   return render_template("trabajador_liquidacion.html",trabajador=trabajador,mensaje=mensaje,liquidacion_total=reultado)

@blueprint.route( "/liquidacion_empleado" )
def liquidacion():
   return render_template("liquidacion_empleado.html")




