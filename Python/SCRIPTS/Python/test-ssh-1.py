import paramiko
import time

def disable_paging(remote_conn):
    '''Disable paging on a Cisco router'''

    remote_conn.send("terminal length 0\n")
    time.sleep(1)

    # Clear the buffer on the screen
    output = remote_conn.recv(1000)

    return output


if __name__ == '__main__':


    # VARIABLES THAT NEED CHANGED
    ip = '172.37.1.10'
    username = 'admin'
    password = 'cisco'

    # Create instance of SSHClient object
    conn = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    conn.set_missing_host_key_policy(
         paramiko.AutoAddPolicy())

    # initiate SSH connection
    conn.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
    print "SSH connection established to %s" % ip

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = conn.invoke_shell()
    print "Interactive SSH session established"

    # Strip the initial router prompt
    output = remote_conn.recv(1000)

    # See what we have
    print output

    # Turn off paging
    disable_paging(remote_conn)

    # Now let's try to send the router a command
    remote_conn.send("\n")
    remote_conn.send("show configuration\n")
    remote_conn.send("\n")
   

    # Wait for the command to complete
    time.sleep(4)
    
    output = remote_conn.recv(50000)
    print output
