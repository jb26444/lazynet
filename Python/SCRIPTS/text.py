interface = input('interface name aka Gig1/1: ')
text_file = open("Output.txt", "w")
text_file.write('interface ' + interface + '\nNo shutdown')
text_file.close()