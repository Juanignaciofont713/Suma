import time

def despertar():
    print("Despertarse")
    time.sleep(2)  # Simula el tiempo que lleva despertarse

def estirarse():
    print("Estirarse un poco para empezar el dia con energia")
    time.sleep(2)  # Simula el tiempo que lleva estirarse

def lavarse():
    print("Lavarse la cara y cepilllarse los dientes")
    time.sleep(4)  # Simula el tiempo que lleva lavarse y cepillarse

def vestirse():
    print("Vestirse")
    time.sleep(4)  # Simula el tiempo que lleva vestirse

def desayuno():
    print("Preparar desayuno & desayunar.")
    time.sleep(5)  # Simula el tiempo que lleva preparar la bebida

def iniciar_dia():
    despertar()
    estirarse()
    lavarse()
    vestirse()
    desayuno()
    print("¡Listo para comenzar el dia!")

# Ejecutar el algoritmo
iniciar_dia()