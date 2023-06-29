color_codes = {
'red': '\033[0;31m',
'yellow': '\033[0;33m',
'reset': '\033[0m'
}

def app():
    """Inicializa la app y abre el menu."""
print('Auto Seguro App')
print('Selecciona Y/n para continuar')
print(color_codes['red'] + 'Y: Si' + color_codes['reset'])
print(color_codes['yellow'] + 'n: No' + color_codes['reset'])
entry = input('')

if entry == 'Y':
    menu()

if entry == 'n':
    return

def menu():
    """Menu con las opciones."""
keep_process = True
while keep_process:
    print('Menu de operaciones')
    print('1: Grabar')
    print('2: Buscar')
    print('3: Imprimir certificados')
    print('4: Salir')

    entry = int(input())

    if entry == 4:
        keep_process = False

def save():
# Your implementation here
    return

def search():
# Your implementation here
    return

def print_certificates():
# Your implementation here
    return

app() # Inicializa la app