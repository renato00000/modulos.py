from calculos import es_surfeable,alerta_vientos_peligroso,obtener_temperatura_limite_traje,mostrar_advertencia_marejada
from pantalla import mostrar_titulo,titulo_menu

def menu():
    mostrar_titulo()
    altura_ola = float(input("ingrese la altura de las olas en metros: "))
    viento = int(input("ingrese la velocida del viento en nudos: "))
    while True:
        titulo_menu()
        print(f"OLA ingresada: {altura_ola} metros | viento: {viento} nudos")
        print("[1] ¿es surfeable hoy?")
        print("[2] evaluar peligro de viento")
        print("[3] consultar limite de temperatura")
        print("[4] ver aviso de la armada")
        print("[5] actualizar datos")
        print("[6] SALIR")
        opcion = int(input("\nseleccione una opcion: "))
        if opcion ==1:
            apto = es_surfeable(altura_ola) 
            if apto:
                print("\nExelentes ola para el surf")
            else:
                print("\nel mar esta muy tranquilo")
        elif opcion == 2:
            alerta_vientos_peligroso(viento)
        elif opcion == 3:
            temperatura_critica = obtener_temperatura_limite_traje()
            print(f"\nrecuerda: bajo los {temperatura_critica}°C es obligatorio usar el traje 4/3mm")
        elif opcion == 4:
            mostrar_advertencia_marejada()
        elif opcion == 5:
            altura_ola = float(input("\ningresa la nueva altura de las olas en metros"))
            viento = int(input("ingresa la nueva velocidad del viento"))
            print("[INFO] datos actualizados")
        elif opcion == 6:
            print("\nsaliendo del sistema.........")
            break
        else:
            print("\ncOpcion no valida")
if __name__=="__main__":
    menu()       