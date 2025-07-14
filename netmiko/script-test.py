from netmiko import ConnectHandler

# Datos del dispositivo Cisco
cisco_CSR1000v = {
    'device_type': 'cisco_xe',  
    'host': '192.168.56.103',
    'username': 'cisco',
    'password': 'cisco123!',
    }

try:
    # Establecer conexión
    print("Conectando al dispositivo...")
    net_connect = ConnectHandler(**cisco_CSR1000v)

    # Entrar a modo privilegiado (enable)
    net_connect.enable()

    # Comandos de configuración (modo config)
    config_commands = [
        'interface GigabitEthernet1',
        'description Configurado con Netmiko',
        'no shutdown',
    ]
    print("Aplicando configuración...")
    output_config = net_connect.send_config_set(config_commands)
    print(output_config)

    # Comandos de verificación (modo exec)
    print("Verificando estado de la interfaz...")
    output_verify = net_connect.send_command('show interface GigabitEthernet0/1 description')
    print(output_verify)

    # Cerrar conexión
    net_connect.disconnect()
    print("Conexión cerrada.")

except Exception as e:
    print(f"Error: {e}")
