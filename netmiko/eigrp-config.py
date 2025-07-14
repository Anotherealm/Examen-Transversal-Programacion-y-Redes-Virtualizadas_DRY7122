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
        'ipv6 unicast-routing', # Habilitar IPv6
        'interface Loopback10', # Ingresar a interface Loopback10
        'ip address 10.10.10.10 255.255.255.255', # Configuracion IPv4
        'ipv6 address 2001:DB8:1::1/64', # Configuracion IPv6
        'no shutdown',
        'ipv6 eigrp Examen-Pardo-Rivas',
	'exit',

	'router eigrp Examen-Pardo-Rivas',
	'address-family ipv4 unicast autonomous-system 99',
	'network 10.10.10.10 0.0.0.0',
	'af-interface Loopback10',
	'passive-interface',
	'exit',
	'no shutdown',
	'exit',

	'address-family ipv6 unicast autonomous-system 99',
	'af-interface Loopback10',
	'passive-interface',
	'exit',
	'no shutdown',
	'end',
    ]
    print("Aplicando configuración...")
    output_config = net_connect.send_config_set(config_commands)

    # Comandos de verificación (modo exec)
    output_verify = net_connect.send_command('show running-config | section eigrp')
    print(output_verify)

    # Cerrar conexión
    net_connect.disconnect()
    print("Conexión cerrada.")

except Exception as e:
    print(f"Error: {e}")
