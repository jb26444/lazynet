#
#
# add your configurations in a list format
#
#host_conf = ['show license usage', 'show version', 'show modul', 'show inventory', 'show module fex',]
#host_conf_1 = ['sh run | inc ntp','sh ntp status','sh run | inc tacacs']
host_conf = open ("conf.txt").readlines() 
