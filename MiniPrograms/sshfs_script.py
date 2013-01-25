import os 

print "Would you like to mount (1) or unmount (2)?"
choice = int(raw_input("< "))
if choice == 1:
    os.system('sshfs james@server:/media/WII/Music/ ~/sshmusic/')
    os.system('echo "Mount Successful"')
elif choice == 2:
    os.system('fusermount -u ~/sshmusic/')
    os.system('echo "Unmount Successful"')
else:
    print "No valid entry."
