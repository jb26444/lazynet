interface = input('interface name aka Gig1/1: ')
vlan = input ('vlan number - sepeated by columm 10,12,13: ')
text_file = open("Output.txt", "w")
text_file.write('interface ' + interface)
text_file.write('\nNo shutdown')
text_file.write('\nswitchport mode trunk')
text_file.write('\nswitchport trunk access vlan ' + vlan)
text_file.close()