from netmiko import ConnectHandler

# Datos del dispositivo Cisco
device = {
    'device_type': 'cisco_xe',
    'host': '192.168.56.103',      
    'username': 'cisco',
    'password': 'cisco123!',
}

# Lista de comandos a ejecutar
commands = {
    "Estado de interfaces IPv4 (show ip interface brief)": "show ip interface brief",
    "Archivo de configuración (show running-config)": "show running-config",
    "Versión del sistema (show version)": "show version",
}

try:
    print("Conectando al dispositivo...")
    connection = ConnectHandler(**device)
    connection.enable()

    for title, cmd in commands.items():
        print(f"\n {title}")
        print("-" * len(title))
        output = connection.send_command(cmd)
        print(output)

    connection.disconnect()
    print("\n Conexión finalizada exitosamente.")

except Exception as e:
    print(f" Error al conectar o ejecutar comandos: {e}")
