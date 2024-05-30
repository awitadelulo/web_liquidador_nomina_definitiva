import psycopg2
#import SecretConfig

from model.calculateLogic import Settlementcalculator, SalarybaseExcepction, Months_workendExcepction, worker
from model.calculateLogic import worker as wolker
from model.calculateLogic import error_llaveprimaria
from SecretConfig import *
class ControllerWorker:

    def CreateTabla(): 
        try: 
            """ Crea la tabla de usuario en la BD """
            cursor = ControllerWorker.ObtenerCursor()

            cursor.execute("""create table worker (
                                id int primary key not null,
                                salary_base float not null,
                                months_worked int not null,
                                vacation_day int not null,
                                hours_extra int not null,
                                hours_extra_nigth int not null,
                                days_finish int not null
                                );""")
            cursor.connection.commit()
        except:
            pass

    def EliminarTabla():
        try:
            """ Borra la tabla de usuarios de la BD """
            cursor = ControllerWorker.ObtenerCursor()

            cursor.execute("""drop table worker""" )
            # Confirma los cambios realizados en la base de datos
            # Si no se llama, los cambios no quedan aplicados
            cursor.connection.commit()
        except:
            pass

    def EliminarWorker(id):
        """ Borra el trabajador de la BD """
        cursor = ControllerWorker.ObtenerCursor()

        cursor.execute(f"""
        DELETE FROM worker
        WHERE id= {id};
        """ )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()

    def modifacarWorker():
        """ modificar trabajador"""
        id= int(input("ingrese el id del trabajador: "))
        modificar= int(input("1. id \n2. salary_base	\n3. months_worked \n4.vacation_day \n5. hours_extras \
                            \n6. extra_hours_nigth \n7. days_finish \ningrese dato a modificar: "))
        valor= input("valor a ingresar: ")
        modificar= option(modificar)
        cursor = ControllerWorker.ObtenerCursor()
        cursor.execute(f"""
        UPDATE worker
        SET {modificar} = {valor}
        WHERE id = {id};
        """ )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()
    
    def modifacarWorker2(ID,Variable,valor):
        """ modificar trabajador"""
        cursor = ControllerWorker.ObtenerCursor()
        wolker.valor_presente(Variable)
        cursor.execute(f"""
        UPDATE worker
        SET {Variable} = {valor}
        WHERE id = {ID};
        """ )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()

    def Insertarworker( worker : worker ):
        """ Recibe un a instancia de la clase Usuario y la inserta en la tabla respectiva"""
        ControllerWorker.veri(worker)
        wolker.notexist(worker)
        cursor = ControllerWorker.ObtenerCursor()
        cursor.execute( f"""insert into worker (id, salary_base,months_worked, vacation_day,
                            hours_extra,hours_extra_nigth, 
                            days_finish) 
                        values ('{worker.id}', '{worker.salary_base}', '{worker.months_worked}',  
                            '{worker.vacation_day}', '{worker.hours_extra}',
                            '{worker.hours_extra_nigth}', '{worker.days_finish}')""" )
        cursor.connection.commit()
    
    def veri(persona):
        variables=ControllerWorker.BuscarWorkerId(persona.id)
        wolker.primary_key(variables)
    
        
    def BuscarWorkerId(id):
        """ Trae un usuario de la tabla de usuarios por la id """
        cursor = ControllerWorker.ObtenerCursor()
        cursor.execute(f"""select id, salary_base, months_worked, vacation_day,hours_extra,hours_extra_nigth, days_finish
        from worker where id = {id}""" )
        fila = cursor.fetchone()
        if fila is not None: 
            resultado = worker( id=fila[0], salary_base=fila[1], months_worked=fila[2], vacation_days=fila[3],
                                hours_extra=fila[4], hours_extra_nigth=fila[5], days_finish=fila[6] )
            return resultado
        else:
            return None

    def calculate_liquidacion_def(worker): 
        changeable_variables= {}
        changeable_variables["vacation"]= worker.vacation_day
        changeable_variables["hours_extra"]= worker.hours_extra
        changeable_variables["hours_extra_nigth"]= worker.hours_extra_nigth
        changeable_variables["days_finish"]= worker.days_finish
        try:
            settlement_calculator = Settlementcalculator(worker.salary_base, worker.months_worked,changeable_variables)
            net_total = settlement_calculator.Calculate_net_total()
            return net_total
        except SalarybaseExcepction as e:
            print(e)
        except Months_workendExcepction as a:
            print(a)


    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor


def option(modificar):
    if modificar == 1:
        modificar= "id"
    if modificar == 2:
        modificar= "salary_base"
    if modificar == 3:
        modificar= "months_worked"
    if modificar == 4:
        modificar= "vacation_day"
    if modificar == 5:
        modificar= "hours_extra" 
    if modificar == 6:
        modificar= "hours_extra_nigth"
    if modificar == 7:
        modificar= "days_finish"
    return modificar
