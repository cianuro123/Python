import glob
import os
import time
# Terminal color definitions


class fg:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[1;49;32m'
    YELLOW = '\033[33m'
    BLUE = '\033[0;49;34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[1;49;96m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
    BLUE_SUB = '\033[4;49;34m'
    CYAN_SUB = '\033[4;49;36m'
    YELLOW_SUB = '\033[4,49,33m'


class bg:
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'
    RESET = '\033[49m'


class stylesheet:
    BRIGHT = '\033[1m'
    DIM = '\033[2m'
    NORMAL = '\033[22m'
    RESET_ALL = '\033[0m'
    SUBRAYADO = '\033[4;49;97m'


estado = ''


class Personaje:
    def __init__(self, nombre, fuerza, armadura, velocidad, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.armadura = armadura
        self.velocidad = velocidad
        self.vida = vida
    personajes = {}

    def __str__(self):
        return f"{self.nombre}:\nVida: {self.vida}\nFuerza: {self.fuerza}\nArmadura: {self.armadura}\nVelocidad: {self.velocidad}"

    def __repr__(self):
        return f'Personaje("{self.nombre}", {self.vida}, {self.fuerza}, {self.armadura}, {self.velocidad})'

    def __add__(self, other):
        name = input(
            f"{fg.YELLOW}Escribe el nombre del nuevo personaje: {fg.RESET}")
        fuerza = round((self.fuerza * other.fuerza)/2)
        arm = round((self.armadura * other.armadura)/2)
        vel = round((self.velocidad * other.velocidad)/2)
        vida = round((self.vida * other.vida)/2)
        return Personaje(name, fuerza, arm, vel, vida)

    def error():
        input(f"{fg.RED}ERROR:\nHa ocurrido un error con los datos ingresados.{fg.RESET}{stylesheet.SUBRAYADO}Presiona Enter para volver al menu:{stylesheet.RESET_ALL} ")
        os.system("cls")
        return None

    def mostrarse(self):
        return print(f"{fg.MAGENTA}Nombre: {self.nombre}{fg.RESET}\nVida: {self.vida}❤️\nFuerza: {self.fuerza}💪\nArmadura: {self.armadura}🛡️\nVelocidad: {self.velocidad}💨\n")

    def fname(self, fst, snd):
        fst = list(str.lower(fst))
        snd = list(str.lower(snd))
        del fst[3:]
        del snd[3:]
        k = []
        fst = list(map(lambda i: k.extend(i), fst))
        snd = list(map(lambda i: k.extend(i), snd))
        k[0] = str.upper(k[0])
        return '◦'+''.join(k)

    def crear_pj():
        while True:
            pj_name = input(
                f"{fg.YELLOW}Escribe el nombre del nuevo personaje (X para salir): {fg.RESET}")
            Personaje.salir(pj_name)
            if pj_name in Personaje.personajes:
                input(
                    f"{fg.RED}ERROR: El nombre ingresado ya está registrado.\nPresiona Enter para reintentar: {fg.RESET}")
                continue
            pj_vida = int(
                input(f"{fg.YELLOW}Escriba el nivel de vida del personaje: {fg.RESET}"))
            pj_fuerza = int(
                input(f"{fg.YELLOW}Escriba el nivel de fuerza del personaje: {fg.RESET}"))
            pj_armor = int(
                input(f"{fg.YELLOW}Escriba el nivel de armadura del personaje: {fg.RESET}"))
            pj_vel = int(
                input(f"{fg.YELLOW}Escriba el nivel de velocidad del personaje: {fg.RESET}"))
            return Personaje(pj_name, pj_fuerza, pj_armor, pj_vel, pj_vida)

    def accion1():
        global estado
        estado = 'accion1'
        while True:
            os.system("cls")
            print(
                f"{fg.BLUE_SUB}🔵 CREACION DE PERSONAJE 🔵{stylesheet.RESET_ALL}\n")
            pj = Personaje.crear_pj()
            nombre_pj = pj.nombre
            Personaje.personajes.update(add_to_dict(nombre_pj, pj))
            print(f"{stylesheet.RESET_ALL}{fg.GREEN}El personaje se creó con éxito")
            respuesta = input(
                f"{fg.BLUE}Desea volver a crear un personaje? S/N: {fg.RESET}").strip().lower()
            if respuesta == 'n':
                sleeping()
                break
            elif respuesta != "s":
                print(Personaje.error())
                break

    def accion2():
        global estado
        estado = 'accion2'
        while True:
            os.system("cls")
            print(f"{fg.BLUE_SUB}🔵 FUSION 🔵{stylesheet.RESET_ALL}\n")
            count = 1
            for key, _ in Personaje.personajes.items():
                print(f"{count}. {key}")
            pj1 = input(
                f"{fg.YELLOW}Escriba nombre de un personaje (X para salir): {fg.RESET}")
            Personaje.salir(pj1)
            pj2 = input(
                f"{fg.YELLOW}Escriba el nombre de otro personaje: {fg.RESET}")
            if verificacion_doble(pj1, pj2, Personaje.personajes) == False:
                return getattr(Personaje, estado)()
            fusion = Personaje.personajes[pj1] + Personaje.personajes[pj2]
            fusion_nombre = fusion.nombre
            Personaje.personajes.update(add_to_dict(fusion_nombre, fusion))
            print(
                f"{fg.GREEN}La fusión ha sido exitosa!\nEl nuevo personaje se llama '{fusion_nombre}'")
            respuesta = input(
                f"{fg.BLUE}Desea volver a fusionar un personaje? S/N: {fg.RESET}").strip().lower()
            if respuesta == 'n':
                sleeping()
                break
            elif respuesta != "s":
                print(Personaje.error())
                break
    def salir(value):
        if value.lower() == "x":
                sleeping()
                return main()
        pass
    def accion3():
        global estado
        estado = 'accion3'
        os.system("cls")
        print(
            f"{fg.BLUE_SUB}🔵 MIS PERSONAJES 🔵{stylesheet.RESET_ALL}\n")
        for _, personaje in Personaje.personajes.items():
            personaje.mostrarse()
        input(f"{fg.MAGENTA}Estos son todos tus personajes y sus estadísticas!\n{fg.RESET}{stylesheet.SUBRAYADO}Escribe cualquier cosa para salir:{stylesheet.RESET_ALL} ")
        sleeping()

    def accion4():
        global estado
        estado = 'accion4'
        while True:
            os.system("cls")
            print(
                f"{fg.BLUE_SUB}🔵 ELIMINAR PERSONAJES 🔵{stylesheet.RESET_ALL}\n")
            count = 1
            for key, _ in Personaje.personajes.items():
                print(f"{count}. {key}")
                count += 1
            name_to_delete = input(
                f"{fg.YELLOW}Escribe el nombre de un personaje (X para salir): {fg.RESET}")
            Personaje.salir(name_to_delete)
            if name_to_delete not in Personaje.personajes.keys():
                input(
                    f"{fg.RED}El personaje ingresado no se encuentra registrado. Presiona Enter para reintentar: {fg.RESET}")
                return getattr(Personaje, estado)()
            respuesta = input(
                f"{fg.MAGENTA}¿Está seguro? '{name_to_delete}' Se eliminará para siempre {stylesheet.SUBRAYADO}¡eso es mucho tiempo!{stylesheet.RESET_ALL}{fg.MAGENTA} S/N:{stylesheet.RESET_ALL} ").strip().lower()

            if respuesta == "n":
                name_to_delete = ""
                sleeping()
                return getattr(Personaje, estado)()
            elif respuesta != "s":
                print(Personaje.error())
                name_to_delete = ""
                break

            del Personaje.personajes[name_to_delete]
            print(f"{fg.GREEN}EL personaje fue eliminado con éxito!")
            respuesta = input(
                f"{fg.BLUE}Desea volver a eliminar un personaje? S/N: {fg.RESET}").strip().lower()
            if respuesta == 'n':
                sleeping()
                return main()

    def accion5():
        global estado
        estado = "accion5"
        out_verify = input(f"{fg.YELLOW}Está seguro que quiere salir? S/N:{fg.RESET} ").lower().strip()
        if out_verify != "s" and out_verify != "n":
            print(f"{fg.RED}Ha ingresado una letra no válida. Por favor presiona 'S' para aceptar o 'N' para denegar.{fg.RESET}")
            getattr(Personaje,estado)()
        if out_verify == "s":
            os.system("cls")
            print(f"{fg.CYAN}gracia' loco")
            time.sleep(1.5)
            os.abort()
        else:
            sleeping()
            main()

def add_to_dict(name: str, dic: object):
    return {name: dic}


def verificacion_doble(pj1, pj2, personajes):
    if ((pj1 not in Personaje.personajes.keys()) and (pj2 not in Personaje.personajes.keys())):
        input(f"{fg.RED}ERROR: Debe ingresar nombres válidos{fg.RESET}\nPresiona Enter para continuar: ")
        return False


def sleeping():
    print(f"{fg.BLUE}Cargando")
    time.sleep(0.7)
    print("🔵")
    time.sleep(0.7)
    print("🔵")
    time.sleep(0.7)
    print("🔵"+stylesheet.RESET_ALL)
    time.sleep(0.9)
    os.system("cls")


dict_opciones = {
    1: "accion1",
    2: "accion2",
    3: "accion3",
    4: "accion4",
    5: "accion5"
}

value = 0
main_menu = f"{fg.CYAN_SUB}Menu Principal.{stylesheet.RESET_ALL}\n{fg.YELLOW}1. Crear personaje.\n2. Fusionar Personajes.\n3. Mostrar Personajes.\n4. Eliminar Personajes.\n5. Salir.{fg.CYAN}\n-->{stylesheet.RESET_ALL} "
print(f"{fg.CYAN_SUB}✦  ¡Comienza a fusionar tus personajes! ✦\n{fg.RESET}➔  Comienza creando tu primer personaje, escriba '1'.\n")


def main():
    global estado
    while True:
        try:
            value = (int(input(main_menu)))
            if int(value) not in dict_opciones.keys():
                input(f"{stylesheet.BRIGHT}{fg.RED}ERROR\nEl número no se encuentra dentro de las opciones (1,2,3,4)\nPresiona Enter para continuar: {stylesheet.RESET_ALL}")
                continue
            accion = dict_opciones[value]
            getattr(Personaje, accion)()
        except:
            Personaje.error()
            continue
main()
