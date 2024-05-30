# importar clases de logica del programa
import sys
sys.path.append("src")
import model.calculateLogic as calculateLogic
from model.calculateLogic import Settlementcalculator, SalarybaseExcepction, Months_workendExcepction

#importamos modulos de la libreria kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


#clase para la interfaz
class LiquidationApp(App):
    def build(self):

        """
        label_salary_base: label para el salario base
        label_month_work: label para los meses trabajaddos
        label_vacation: label para los dias restamtes de vacaciones
        label_extra_hours: label para las horas extras
        label_extra_hours_nigth: label para las horas extras nocturnas
        label_days_finish: label para los dias restantes de terminacion de contrato
        """
        
        #Creamos un layout 
        layout = GridLayout(cols=2, spacing=10, padding=20)

        # Etiquetas y campos de entrada
        label_Salary_base= Crear_Label(layout, 'ingrese salario base:')
        self.salary_input = TextInput(multiline=False)
        layout.add_widget(self.salary_input)

        label_month_work= Crear_Label(layout, 'Ingrese meses trabajados:')
        self.month_work_input = TextInput(multiline=False)
        layout.add_widget(self.month_work_input)
        
        label_vacation= Crear_Label(layout, 'ingrese dias restantes de vacaciones:')
        self.vacation_input = TextInput(multiline=False)
        layout.add_widget(self.vacation_input)

        label_extra_hours= Crear_Label(layout, 'Ingrese horas extras realizadas:') 
        self.extra_hours_input = TextInput(multiline=False)
        layout.add_widget(self.extra_hours_input)

        label_extra_hours_nigth= Crear_Label(layout, 'Ingrese horas extras nocturnas realizadas :')
        self.extra_nigth_input = TextInput(multiline=False)
        layout.add_widget(self.extra_nigth_input)

        label_days_finish= Crear_Label(layout, 'Ingrese dias rastantes para finalizar contrato:')
        self.days_finish_input = TextInput(multiline=False)
        layout.add_widget(self.days_finish_input)

        
        # Botón de cálculo
        self.calculate_button = Button(text='Calcular Liquidación')
        self.calculate_button.bind(on_press= self.calculate)
        layout.add_widget(self.calculate_button)

        # Resultado
        self.result_label = Label(text='')
        layout.add_widget(self.result_label)
        
        return layout
    
    #funcion que calcula liquidacion
    def calculate(self, instance):        
        #llamada a la funcion de crear variables de liquidacion
        variables_result =variables(self.vacation_input,self.extra_hours_input,self.extra_nigth_input,self.days_finish_input)

        #llamada a la funcion para calular liquidacion
        liquidation= Settlementcalculator(int(self.salary_input.text), int(self.month_work_input.text),variables_result)
        liquidation_result= liquidation.Calculate_net_total()

        #resultado del calulo
        self.result_label.text = f'Liquidación Definitiva: ${round(liquidation_result,0):.2f}'
        

#creacion de label
def Crear_Label(layout, text_quiz):
    layout.add_widget(Label(text= text_quiz))
    return

#creacion de diccionario de variables de liquidacion
def variables(vacation,extra_hours, extra_hours_nigth, days_finish):
    ingreso_variables= {}
    ingreso_variables["vacation"]= int(vacation.text) 
    ingreso_variables["extra_hours"]= int(extra_hours.text)
    ingreso_variables["extra_hours_nigth"]= int(extra_hours_nigth.text)
    ingreso_variables["days_finish"]= int(days_finish.text)
    return ingreso_variables


#comando de inicializacion
if __name__ == '__main__':
    LiquidationApp().run()