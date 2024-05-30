import unittest
from unittest.mock import MagicMock
import sys
import os
sys.path.append("src")
sys.path.append("Cl_liquidacion_definitiva/src")
import model.calculateLogic as calculateLogic
from model.calculateLogic import worker
from controller.controller_worker import ControllerWorker
from  model.calculateLogic import error_llaveprimaria

class TestWorkerController(unittest.TestCase):
    def setUpClass():
        # Llamar a la clase COntrolador para que cree la tabla
        ControllerWorker.EliminarTabla()
        ControllerWorker.CreateTabla()
    
    
    def test_insertemployer(self):
        trabajador=worker(id=2020, salary_base=1600000, months_worked=50, vacation_days=40,
                          hours_extra=40,hours_extra_nigth=10,days_finish=20)
        ControllerWorker.Insertarworker(trabajador)
        findemployer= ControllerWorker.BuscarWorkerId(trabajador.id)
        findemployer.Isequal(trabajador)

    def testupdateworkers(self):
        trabajador=worker(id=20, salary_base=1600000, months_worked=50, vacation_days=40,
                          hours_extra=40,hours_extra_nigth=10,days_finish=20)
        ControllerWorker.Insertarworker(trabajador)
        #ControllerWorker.modifacarWorker()
        KEYUPDATE="months_worked"
        VALUEUPDATE=40
        # Actualizar el valor del atributo correspondiente utilizando getattr
        setattr(trabajador, KEYUPDATE, VALUEUPDATE)
        ControllerWorker.modifacarWorker2(trabajador.id, KEYUPDATE, VALUEUPDATE)
        findemployer=ControllerWorker.BuscarWorkerId(trabajador.id)
        findemployer.Isequal(trabajador)
    
    def testdeleteworkers(self):
        trabajador=worker(id=90, salary_base=1600000, months_worked=50, vacation_days=40,
                          hours_extra=40,hours_extra_nigth=10,days_finish=20)
        ControllerWorker.Insertarworker(trabajador)
        ControllerWorker.EliminarWorker(trabajador.id)
        findemployer=ControllerWorker.BuscarWorkerId(trabajador.id)
        self.assertIsNone(findemployer)
    
    def testpage(self):
        trabajador=worker(id=160, salary_base=5000000, months_worked=6, vacation_days=10,
                          hours_extra=5,hours_extra_nigth=2,days_finish=0)
        ControllerWorker.Insertarworker(trabajador)
        liquidacion_programa = ControllerWorker.calculate_liquidacion_def(trabajador)
        liquidacion_programa = round(liquidacion_programa, 0)
        expected_liquidation = 5506944
        self.assertAlmostEqual(liquidacion_programa, expected_liquidation, delta=1)
 
    def test_error_llave_primaria(self):
        trabajador1 = worker(id=400, salary_base=5000000, months_worked=6, vacation_days=10,
                             hours_extra=5, hours_extra_nigth=0, days_finish=0)
        ControllerWorker.Insertarworker(trabajador1)

        trabajador2= worker(id=400, salary_base=5000000, months_worked=6, vacation_days=10,
                             hours_extra=5, hours_extra_nigth=0, days_finish=0)
        self.assertRaises(calculateLogic.error_llaveprimaria, ControllerWorker.Insertarworker ,trabajador2)

    def test_fault_data(self):
        trabajador= worker(id=20000, salary_base=None, months_worked=6, vacation_days=10,
                             hours_extra=5, hours_extra_nigth=0, days_finish=0)
        self.assertRaises(calculateLogic.not_exist, ControllerWorker.Insertarworker ,trabajador)

    def test_not_found(self):
        id="30303030303"
        findemployer=ControllerWorker.BuscarWorkerId(id)
        self.assertRaises(calculateLogic.user_not_found, worker.trabajador_no_encontrado , findemployer)
    
    def test_notupdate(self):
        trabajador= worker(id=2000, salary_base=1600000, months_worked=50, vacation_days=40,
                          hours_extra=40,hours_extra_nigth=10,days_finish=20)
        ControllerWorker.Insertarworker(trabajador)
        self.assertRaises(calculateLogic.valor_actualizar_nopresente, ControllerWorker.modifacarWorker2 , trabajador.id,"hour",340000)

        
    


        
    

    


        
        """trabajador2 = worker(id=321, salary_base=5000000, months_worked=6, vacation_days=10,
                             hours_extra=5, hours_extra_nigth=2, days_finish=0)
        ControllerWorker.Insertarworker(trabajador2)"""



if __name__ == "__main__":
    unittest.main()
