import unittest
import sys
sys.path.append("src")
import model.calculateLogic as calculateLogic
from model.calculateLogic import Settlementcalculator, SalarybaseExcepction, Months_workendExcepction


"""
self.salary_base = salario base
self.months_worked = meses trabajados
self.annual_layoffs = cesantias anuales
self.interest_layoffs = intereses de cesantias
self.bonus_services = prima de servicios
self.vacation_days = dias de vacaciones
self.extra_hours = horas extras
self.night_charges = cargos nocturnos
self.compensation_dismissal = indemnizacion por despido
"""


class CalculTest(unittest.TestCase):
    
    # Caso de prueba 1: Empleado que renuncia voluntariamente después de 6 meses de trabajo
    def test_1(self):
        base_salary = 5000000
        months_worked = 6
        variables= {}
        annual_layoffs= 8.33
        interest_layoffs= 12 
        bonus_services= 8.33 
        variables["vacation"]= 10 
        variables["extra_hours"]= 5 
        variables["extra_hours_nigth"]= 2 
        variables["days_finish"]= 0
        expected_liquidation= 5506944
        

        result = Settlementcalculator(base_salary, months_worked,variables)
    
        valor_neto = round(result.Calculate_net_total(),0)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)


    # Caso de prueba 2: Empleado despedido sin justa causa después de 12 meses de trabajo
    def test_2(self):
        base_salary = 6000000
        months_worked = 12
        annual_layoffs= 8.33
        interest_layoffs= 12 
        bonus_services= 8.33 
        variables= {}
        variables["vacation"]= 15
        variables["extra_hours"]= 8 
        variables["extra_hours_nigth"]= 3 
        variables["days_finish"]= 36
        expected_liquidation= 77790333

        result = Settlementcalculator(base_salary, months_worked,variables)

        valor_neto = round(result.Calculate_net_total(),0)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)
        

    # Caso de prueba 3: Empleado con contrato a plazo fijo que finaliza después de 8 meses
    def test_3(self):
        base_salary = 5500000
        months_worked = 8
        annual_layoffs= 8.33
        interest_layoffs= 12 
        bonus_services= 8.33 
        variables= {}
        variables["vacation"]= 12
        variables["extra_hours"]= 10
        variables["extra_hours_nigth"]= 4 
        variables["days_finish"]= 0
        expected_liquidation= 6529722
        
        result = Settlementcalculator(base_salary, months_worked,variables)

        valor_neto = round(result.Calculate_net_total(),0)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)
    
    # Caso de prueba 4: Empleado con horas extras y recargos nocturnos
    def test_4(self):
        base_salary = 6000000
        months_worked = 10
        annual_layoffs = 8.33
        interest_layoffs = 12 
        bonus_services = 8.33         
        variables= {}
        variables["vacation"]= 20
        variables["extra_hours"]= 15
        variables["extra_hours_nigth"]= 5 
        variables["days_finish"]= 0
        expected_liquidation = 8563333

        result = Settlementcalculator(base_salary, months_worked,variables)

        valor_neto = round(result.Calculate_net_total(),0)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)

    # Caso de prueba 5: Empleado con indemnización por despido
    def test_5(self):
        base_salary = 7000000
        months_worked = 24
        annual_layoffs = 8.33
        interest_layoffs = 12 
        bonus_services = 8.33 
        variables= {}
        variables["vacation"]= 30
        variables["extra_hours"]= 12
        variables["extra_hours_nigth"]= 4 
        variables["days_finish"]= 20
        expected_liquidation = 165990222

        result = Settlementcalculator(base_salary, months_worked,variables)

        valor_neto = round(result.Calculate_net_total(),0)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)
    
    # Caso de prueba 6: Empleado con salario base y sin beneficios adicionales
    def test_6(self):
        base_salary = 4500000
        months_worked = 9
        annual_layoffs = 8.33
        interest_layoffs = 12 
        bonus_services = 8.33 
        variables= {}
        variables["vacation"]= 15
        variables["extra_hours"]= 0 
        variables["extra_hours_nigth"]= 0 
        variables["days_finish"]= 0
        expected_liquidation = 5410000

        result = Settlementcalculator(base_salary, months_worked,variables)

        valor_neto = round(result.Calculate_net_total(),0)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)

    # Caso de prueba 7: Empleado con indemnización por despido y sin otros beneficios adicionales
    def test_7(self):
        base_salary = 5000000
        months_worked = 12
        annual_layoffs = 8.33
        interest_layoffs = 12 
        bonus_services = 8.33 
        variables= {}
        variables["vacation"]= 20
        variables["extra_hours"]= 0
        variables["extra_hours_nigth"]= 0 
        variables["days_finish"]= 20
        expected_liquidation = 63104444

        result = Settlementcalculator(base_salary, months_worked,variables)

        valor_neto = round(result.Calculate_net_total(),0)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)

    # Caso de prueba 8: Empleado con todos los beneficios posibles
    def test_8(self):
        base_salary = 5500000
        months_worked = 18
        annual_layoffs = 8.33
        interest_layoffs = 12 
        bonus_services = 8.33 
        variables= {}
        variables["vacation"]= 25
        variables["extra_hours"]= 10
        variables["extra_hours_nigth"]= 3 
        variables["days_finish"]= 45
        expected_liquidation = 103708306

        result = Settlementcalculator(base_salary, months_worked,variables)

        valor_neto = round(result.Calculate_net_total(),0)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)



    # Caso de prueba 9:Contrato de trabajo a término indefinido sin cesantías
    def test_9(self):
        base_salary=6000000
        months_worked=24
        annual_layoffs=0
        interest_layoffs=12
        bonus_services=8.33
        variables= {}
        variables["vacation"]= 15
        variables["extra_hours"]= 8
        variables["extra_hours_nigth"]= 3 
        variables["days_finish"]= 0
        expected_liquidation = 136542333

        result = Settlementcalculator(base_salary, months_worked,variables)

        valor_neto = round(result.Calculate_net_total(),0)

        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)

    # Caso de prueba 10: salario base 0
    def test_10(self):
        base_salary= 0
        months_worked=24
        annual_layoffs=0
        interest_layoffs=12
        bonus_services= 0        
        variables= {}
        variables["vacation"]= 15
        variables["extra_hours"]= 10
        variables["extra_hours_nigth"]= 3 
        variables["days_finish"]= 0
        

        self.assertRaises(SalarybaseExcepction, Settlementcalculator,base_salary, months_worked,variables)
        
    # Caso de prueba 11: ningun dia trabajado
    def test_11(self):
        base_salary= 600000
        months_worked=0
        annual_layoffs=0
        interest_layoffs=12
        bonus_services= 0       
        variables= {}
        variables["vacation"]= 10
        variables["extra_hours"]= 8
        variables["extra_hours_nigth"]= 3 
        variables["days_finish"]= 0
        
        self.assertRaises(Months_workendExcepction, Settlementcalculator,base_salary, months_worked,variables)
        
    # Caso de prueba 12:
    def test_12(self):
        base_salary= 600000
        months_worked=0
        annual_layoffs=0
        interest_layoffs=12
        bonus_services= 0       
        variables= {}
        variables["vacation"]= 15
        variables["extra_hours"]= 8
        variables["extra_hours_nigth"]= 3 
        variables["days_finish"]= 0
        

        self.assertRaises(Months_workendExcepction, Settlementcalculator,base_salary, months_worked,variables)

    # Caso de prueba 13: Empleado con salario base y beneficios retenidos durante disputa legal
    def test_13(self):
        base_salary = 6000000
        months_worked = 24
        annual_layoffs = 8.33
        interest_layoffs = 12 
        bonus_services = 8.33 
        variables= {}
        variables["vacation"]= 15
        variables["extra_hours"]= 8
        variables["extra_hours_nigth"]= 3 
        variables["days_finish"]= 0        
        expected_liquidation= 136542333
        
        result = Settlementcalculator(base_salary, months_worked,variables)

        valor_neto = round(result.Calculate_net_total(),0)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)
    
    def test_14(self):
        base_salary= 1000000
        months_worked= 12
        annual_layoffs= 8.33
        interest_layoffs= 11
        bonus_services= 8.33
        variables= {}
        variables["vacation"]= 12
        variables["extra_hours"]= 7
        variables["extra_hours_nigth"]= 3 
        variables["days_finish"]= 0
        
        result=Settlementcalculator(base_salary, months_worked,variables)
        
    def test_15(self):
        base_salary= 2000000
        months_worked= 22
        annual_layoffs= 8.33
        interest_layoffs= 11
        bonus_services= 8.33
        variables= {}
        variables["vacation"]= 15
        variables["extra_hours"]= 9
        variables["extra_hours_nigth"]= 3 
        variables["days_finish"]= 0
        
        result=Settlementcalculator(base_salary, months_worked,variables)


    def test_16(self):
        base_salary= 8000000
        months_worked= 48
        annual_layoffs= 8.33
        interest_layoffs= 11
        bonus_services= 8.33
        variables= {}
        variables["vacation"]= 48
        variables["extra_hours"]= 30
        variables["extra_hours_nigth"]= 5
        variables["days_finish"]= 0
        
        result=Settlementcalculator(base_salary, months_worked,variables)

    def test_17(self):
        base_salary= 900000
        months_worked= 6
        annual_layoffs= 8.33
        interest_layoffs= 11
        bonus_services= 8.33
        variables= {}
        variables["vacation"]= 0
        variables["extra_hours"]= 30
        variables["extra_hours_nigth"]= 8 
        variables["days_finish"]= 0
        
        result=Settlementcalculator(base_salary, months_worked,variables)
    
    
    def test_18(self):
        base_salary= 1000000
        months_worked= 10
        annual_layoffs= 8.33
        interest_layoffs= 11
        bonus_services= 8.33
        variables= {}
        variables["vacation"]= 7
        variables["extra_hours"]= 10
        variables["extra_hours_nigth"]= 3
        variables["days_finish"]= 0
        
        result=Settlementcalculator(base_salary, months_worked,variables)


    def test_19(self):
        base_salary= 5000000
        months_worked= 24
        annual_layoffs= 8.33
        interest_layoffs= 11
        bonus_services= 8.33
        variables= {}
        variables["vacation"]= 30
        variables["extra_hours"]= 15
        variables["extra_hours_nigth"]= 3 
        variables["days_finish"]= 0
        
        result=Settlementcalculator(base_salary, months_worked,variables)


    def test_20(self):
        base_salary= 850000
        months_worked= 3
        annual_layoffs= 8.33
        interest_layoffs= 11
        bonus_services= 8.33
        variables= {}
        variables["vacation"]= 0
        variables["extra_hours"]= 8
        variables["extra_hours_nigth"]= 5
        variables["days_finish"]= 0
        
        result=Settlementcalculator(base_salary, months_worked,variables)
               

#Esto es para realizar las pruebas unitarias
if __name__ == '__main__':
    unittest.main()