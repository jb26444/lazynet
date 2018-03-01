def SERVICE_INSTANCE:
    CLIENT_VLAN = input('VLAN Number: ')
    CLIENT_VRF = input('descrition: ')
    text_file.write('interface ' + INTERFACE)
    text_file.write('\nservice instance ' + CLIENT_VLAN + ' ethernet')
    text_file.write('\ndescription cust: ' + CLIENT_VRF)
    text_file.write('\nencapsulation dot1q ' + CLIENT_VLAN)
    text_file.write('\nrewrite ingress tag pop 1 symmetric')
    text_file.write('\nbridge-domain ' + CLIENT_VLAN)
    text_file.write('\n!')

INTERFACE = input('Interface name aka Gig1/0: ')
CLIENT_VLAN = input('VLAN Number: ')
CLIENT_VRF = input('descrition: ')
text_file = open("service_instancev3.txt", "w")
text_file.write('interface ' + INTERFACE)
text_file.write('\nservice instance ' + CLIENT_VLAN + ' ethernet')
text_file.write('\ndescription cust: ' + CLIENT_VRF)
text_file.write('\nencapsulation dot1q ' + CLIENT_VLAN)
text_file.write('\nrewrite ingress tag pop 1 symmetric')
text_file.write('\nbridge-domain ' + CLIENT_VLAN)
text_file.write('\n!')
NewService = input('NewServiceInstaneceVLAN or q: ')
if CLIENT_VLAN1 != q:
    def SERVICE_INSTANCE
else:
    text_file.close()

