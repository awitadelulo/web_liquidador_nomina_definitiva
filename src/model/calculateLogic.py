#clase de error para salario igual o menor que cero
class SalarybaseExcepction(Exception):
    def __init__(self):        
        super().__init__(f"el salario no puede ser igual o menor que 0")
#clase de error para cuando no tiene meses o dias trabajados 

class Months_workendExcepction(Exception):
    def __init__(self):       
        super().__init__(f"no tiene dias o meses trabajados")

class MisspelledException(Exception):
    def __init__(self):       
        super().__init__(f'no diligencio "si" o "no')

class error_llaveprimaria(Exception):
    pass

class not_exist(Exception):
    pass

class user_not_found(Exception):
    pass

class valor_actualizar_nopresente(Exception):
    pass

class worker:
    def __init__(self, id, salary_base, months_worked, vacation_days,hours_extra,hours_extra_nigth,days_finish):
        self.id= id
        self.salary_base = salary_base
        self.months_worked = months_worked
        self.vacation_day= vacation_days
        self.hours_extra= hours_extra
        self.hours_extra_nigth= hours_extra_nigth
        self.days_finish= days_finish

    def __str__(self) -> str:
        return f"id: {self.id} \nsalario base: {self.salary_base} \nmeses trabajados: {self.months_worked} \
            \ndias pendientes de vacasiones: {self.vacation_day} \nhoras extras: {self.hours_extra}\
            \nhoras extras nocturnas: {self.hours_extra_nigth} \ndias pendinetes para finalizar contrato: {self.days_finish}"

    def Isequal(self, dbneon):
        
        assert (self.id == dbneon.id)
        assert (self.salary_base == dbneon.salary_base)
        assert (self.months_worked == dbneon.months_worked)
        assert (self.vacation_day== dbneon.vacation_day)
        assert (self.hours_extra ==  dbneon.hours_extra)
        assert (self.hours_extra_nigth== dbneon.hours_extra_nigth)
        assert (self.days_finish == dbneon.days_finish)

    def primary_key(query):     
        if query is not None:
            raise error_llaveprimaria(f"Ya ingresaste este usuario: {query.id}")
        else: 
            pass
    
    def notexist(employer):
        if any(value is None for value in employer.__dict__.values()):
            raise not_exist("Falta un valor al crear la clase Employerinput")
    
    def trabajador_no_encontrado(query):
        if query is None:
            raise user_not_found("no se ha encontrado su busqueda")

    def valor_presente(atributo):
        lista_atributos= ["id","salary_base","months_worked", "vacation_day",
                            "hours_extra","hours_extra_nigth", 
                            "days_finish"]
        
        if atributo not in lista_atributos:
            raise valor_actualizar_nopresente("no se encuentra el valor para realizar el update") 


#clase para implementar la logica del programa
class Settlementcalculator:
    def __init__(self, salary_base, months_worked, changeable_variables):
        """
        self.salary_base = salario base
        self.months_worked = meses trabajados                                
        self.vacations_day= dias de vacacion
        self.hours_extra= horas extras
        self.hours_extra_nigth= horas extras nocturnas
        self.compensation_days= dias de compensacion
        self.total_days_months= Dias del mes, suponiendo 30        
        self.salary_day= salario de un dia
        self.hours_work = horas trabajadas
        self.value_hours_extra_max = valor de las horas extras con recargo del 75%
        self.value_hours_extra = valar de las horas extras de 25%
        self.Months_of_years= mese del año
        self.interest_rate_layoufffs = porcentaje de intereses de cesantias
        self.taxes_rate= porcentaje de impuestos
        """

        self.salary_base = salary_base
        self.months_worked = months_worked
        self.vacations_day= changeable_variables["vacation"]
        self.hours_extra= changeable_variables["hours_extra"]
        self.hours_extra_nigth= changeable_variables["hours_extra_nigth"]
        self.compensation_days= changeable_variables["days_finish"]
        self.total_days_months= 30        
        self.salary_day= (self.salary_base / self.total_days_months)
        self.hours_work = 8  
        self.value_hours_extra_noc = 1.75
        self.value_hours_extra = 1.25        
        self.Months_of_years= 12
        self.interest_rate_layoufffs = 0.12        
        self.taxes_rate= 0.2

        #llamado a errores
        self.Check_salariobase()
        self.Check_months_worked()

    #metodo que calcula las cesantias por despido
    def calculate_severance_pay(self):            
        if self.months_worked < 12:
            return 0
        return self.salary_base * self.months_worked
    

    #metodo que calcula los intereses de cesantias por despido
    def Calculate_severance_interest(self):
        return  self.calculate_severance_pay() * self.interest_rate_layoufffs

    #metodo que calcula prima de servicios
    def Calculate_bonus_services(self):        
        return self.salary_day /self.Months_of_years


    #metodo que calcula los dias de vacaciones
    def Calculate_vacation(self, vacation_days):
            return self.salary_day * vacation_days
        

    #metodo que calcula horas extras 
    def Calulate_extra_hours(self,extra,extra_nigth):
        extra_hours= extra * (self.salary_day/self.hours_work) * self.value_hours_extra    # Recargo del 25% para horas extras diurnas
        extra_hours_nigth= extra_nigth * (self.salary_day/self.hours_work) * self.value_hours_extra_noc    # Recargo del 75% para horas nocturnas
        return extra_hours + extra_hours_nigth
            

    def Calculate_compensation_dismissal(self,days_finish):
        return (self.salary_base / self.total_days_months) * days_finish     

    #metodo que calcula el salario bruro total
    def Calculate_gross_total(self):
        total = self.salary_base + self.calculate_severance_pay() + self.Calculate_severance_interest() + \
                self.Calculate_bonus_services() + self.Calculate_vacation(self.vacations_day) + \
                self.Calulate_extra_hours(self.hours_extra,self.hours_extra_nigth)  + self.Calculate_compensation_dismissal(self.compensation_days)                
        return total

    #metodo que calcula el impuesto
    def Calculate_taxes(self, groos_total):
        return groos_total * self.taxes_rate

    #metodo que calcula el total neto 
    def Calculate_net_total(self):
        gross_total= self.Calculate_gross_total()
        return gross_total - self.Calculate_taxes(gross_total)
    
    #metodo que lanza la excepcion de salario base igual o menor que cero 
    def Check_salariobase (self):
        if self.salary_base == 0:
            raise SalarybaseExcepction()
        
    #metodo que lanza la excepcion de dias no trabajados
    def Check_months_worked (self):
        if self.months_worked == 0:
            raise Months_workendExcepction()
        
    