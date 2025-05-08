# Agenda de tareas:
# Debe poder crear tareas y almancenarlas, debe mostrar las tareas creadas en forma de lista de
# prioridad, debe poder marcar como completada una tarea, modificarla, eliminarla, y tener el codigo abierto a agregar funciones que guarde la
# informacion luego de cerrarse con json. Tiene que tener un sistema de horario; inicio, fin.
import json
import os
from datetime import date, datetime, timedelta

global archive
archive = "X. Tests\Agenda de tareas\data.json"
with open(archive, "r") as f:
    global datos
    datos: list = json.load(f)
for idx, _ in enumerate(datos):
    global new_id
    new_id = idx
    new_id += 1

class Main():
    dict_options = {
        1:"inputs",
        2:"",
        # 3:"EliminarTarea",
        # 4:"VerTareas",
        # 5:"Cerrar"
        
    }
    
    def __init__ (self, title, subtitle, description, tarea, completed=False, due_date=None, priority=0 ):
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.task = tarea
        self.completed = completed
        self.due_date = due_date
        self.priority = priority
        self.created_at = str(datetime.now())
    
    def __str__(self):
        return f'Titulo:\n{self.title}\nSubtitulo:\n{self.subtitle}\nDescripción:{self.description}\nTarea:\n{self.task}\nCompletado````````````````:{self.completed}, "due_date":{self.due_date}, "priority":{self.priority}'
    def __repr__(self):
        return f'"Titulo" :{self.title}, "Subtitle": {self.subtitle}, "description":{self.description}, "Tarea":{self.task}, "Completed":{self.completed}, "due_date":{self.due_date}, "priority":{self.priority}'

    def inputs(self): #Esto es para administrar los inputs del usuario
        while True:
            try:
                self.title =input("Titulo: \n") 
                self.subtitle = input("Subtitulo:\n ")
                self.description = input("Descripcion: \n")
                self.due_date = int(input("Vencimiento (min):\n "))
                self.priority = int(input("Prioridad:\n "))
                return {
            "id": new_id,
            "task_title": self.title,
            "subtitle": self.subtitle,
            "description": self.description,
            "task": self.task,
            "due_date": self.due_date,
            "created_at": self.created_at,
            "completed": self.completed,
            "priority": self.priority,
        }
            except ValueError as e:
                input(f"Error {e}.\nEnter para continuar")
                continue

    def main_menu(self): # Aca se define el main menu de la agenda
        print("-Main Menu-\n")
        try:
            opcion = int(input(f"1. Crear tarea\n2. Ver tareas\n3. Cerrar\n--> "))
            if opcion in range(0,6):
                print("a")
                value= self.dict_options[opcion]
                new_task = getattr(Main, value)(Main)
                
        except ValueError as e:
            input(f"Error: {e}.\nEnter para continuar")

class CrearTarea(Main):

    def __init__(self, title, subtitle, description, tarea, completed=False, due_date=None, priority=0):
        super().__init__(title, subtitle, description, tarea, completed, due_date, priority)

    def nueva_tarea():
        nueva_tarea = datos[0]
        return nueva_tarea

    def construir(self):
        task: dict = {
            "id": id,
            "task_title": self.title,
            "subtitle": self.subtitle,
            "description": self.description,
            "task": self.task,
            "due_date": self.due_date,
            "created_at": self.created_at,
            "completed": self.completed,
            "priority": self.priority,
        }
        diccionario_tarea = CrearTarea.nueva_tarea()
        dict(diccionario_tarea).update(task)
        datos.append(diccionario_tarea)
        with open(archive, "w") as f:
            json.dump(datos, f, indent=4)
        print(f"Tarea guardada! Dirìgete a 'Ver Tareas' para verla.""")            

# tiempo_tarea = str(datetime.now() + timedelta(hours=2))
# Tarea = CrearTarea("Estudiar Programacion", "Estudio de POO y Backend",
#                     "Avanzar en los cursos al menos durante una hora",
#                     "hacer cosas",False, tiempo_tarea).construir()


class ModificarTarea(Main):
    def __init__(self, mod_id, title, subtitle, description, tarea, completed=False, due_date=None, priority=0):
        super().__init__(title, subtitle, description, tarea, completed, due_date, priority)
        self.mod_id = mod_id
        self.update_at = str(datetime.now())

    def Modify(self):
        task: dict = {
            "task_title": self.title,
            "subtitle": self.subtitle,
            "description": self.description,
            "task": self.task,
            "due_date": self.due_date,
            "updated_at": self.update_at,
            "completed": self.completed,
            "priority": self.priority,
        }
        
        tarea_objetivo = datos[self.mod_id]
        dict(tarea_objetivo).update(task)
        datos[self.mod_id] = tarea_objetivo

        with open(archive, "w") as f:
            json.dump(datos, f, indent=4)

class VerTareas(Main):
    def __init__(self, title, subtitle, description, tarea, completed=False, due_date=None, priority=0):
        super().__init__(title, subtitle, description, tarea, completed, due_date, priority)
    
    def mostrar(self):
        
        
VerTareas.mostrar(VerTareas)
