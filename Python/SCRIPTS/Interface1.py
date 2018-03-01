ans=True
while ans:
    print ("""
    1.Gig
    2.Fa
    3.TenGig
    4.Exit/Quit
    """)
    ans=input("What would you like to do?")
    if ans=="1": 
      interface=Gig 
    elif ans=="2":
      interface=Fa
    elif ans=="3":
      interface=TenGig
    elif ans=="4":
      print("\n Goodbye") 
    elif ans !="":
      print("\n Not Valid Choice Try again")
interfacenumber = input('interface name aka 1/1: ')
vlan = input ('vlan number - sepeated by columm 10,12,13: ')
text_file = open("Output.txt", "w")
text_file.write('interface ' + interface + interfacenumber)
text_file.write('\nNo shutdown')
text_file.write('\nswitchport mode trunk')
text_file.write('\nswitchport trunk access vlan ' + vlan)
text_file.close()