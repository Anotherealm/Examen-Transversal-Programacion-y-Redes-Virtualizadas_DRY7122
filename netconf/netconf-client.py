from ncclient import manager 
m = manager.connect( 
 host="192.168.56.103", 
 port=830, 
 username="cisco", 
 password="cisco123!",
 hostkey_verify=False 
 )

netconf_hostname = """ 
<config> 
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"> 
 <hostname>PARDO-RIVAS</hostname> 
 </native> 
</config> 
"""

netconf_reply = m.edit_config(target="running", config=netconf_hostname)

