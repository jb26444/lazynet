INTERFACE = input ('Interface name aka Gig1/0: ')
CLIENT_VLAN = input ('VLAN Number: ')
CLIENT_VRF = input ('descrition: ')
CLIENT_VLAN1 = input ('VLAN Number1: ')
CLIENT_VRF1 = input ('descrition1: ')
text_file = open("service_instancev2.txt", "w")
text_file.write('interface ' + INTERFACE )
text_file.write('\nservice instance ' + CLIENT_VLAN + ' ethernet')
text_file.write('\ndescription cust: ' + CLIENT_VRF)
text_file.write('\nencapsulation dot1q ' + CLIENT_VLAN)
text_file.write('\nrewrite ingress tag pop 1 symmetric')
text_file.write('\nbridge-domain ' + CLIENT_VLAN)
text_file.write('\n!')
text_file.write('\nservice instance ' + CLIENT_VLAN1 + ' ethernet')
text_file.write('\ndescription cust: ' + CLIENT_VRF1)
text_file.write('\nencapsulation dot1q ' + CLIENT_VLAN1)
text_file.write('\nrewrite ingress tag pop 1 symmetric')
text_file.write('\nbridge-domain ' + CLIENT_VLAN1)
text_file.write('\n!')
text_file.close()
