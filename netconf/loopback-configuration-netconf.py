from ncclient import manager 
m = manager.connect( 
 host="192.168.56.103", 
 port=830, 
 username="cisco", 
 password="cisco123!",
 hostkey_verify=False 
 )

netconf_loopback = """ 
<config> 
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"> 
 <interface> 
 <Loopback> 
 <name>11</name> 
 <description>Examen Transversal</description> 
 <ip> 
 <address> 
 <primary> 
 <address>11.11.11.11</address> 
 <mask>255.255.255.255</mask> 
 </primary> 
 </address> 
 </ip> 
 </Loopback> 
 </interface> 
</native> 
</config> 
""" 

netconf_reply = m.edit_config(target="running", config=netconf_loopback)
