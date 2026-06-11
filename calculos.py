#funcion con parametros y con retorno
def es_surfeable(altura):
    return altura >= 1.5
#funcion
def convertir_a_centimetros(altura_metros):
    return altura_metros * 100

#funcion con paramertros y sin retorno
def alerta_vientos_peligroso(nudos_viento):
    if nudos_viento > 20:
        print("\n[ALERTA CRITICA] Viento peligroso,peligro de corriente")
    else:
        print("\ncondiciones de viento dentro del limite")
    
#funcion sin parametros y con retorno

def obtener_temperatura_limite_traje():
    temperatura_limite = 13
    return temperatura_limite

#funcion sin parametros y sin retorno
def mostrar_advertencia_marejada():
    print("\n------------------------------------------")
    print("   AVISO DE LA ARMADA: MAREJADAS ACTIVAS  ")
    print("------------------------------------------")