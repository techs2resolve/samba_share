# Samba folder sharing program
import os


print(100 * "=")
print("Welcome to Folder Sharing Program")
print(100 * "=")

folder_name = input("Enter the folder name only:- ")
folder_location = input("Enter the folder full path you want to share:- ")
print(folder_location)

print("Making change is SMB config file please wait:- ")

f = open('/Users/sarfaraz/smb.conf','a')   # change the file location to /etc/samba/smb.conf
f.write('\n' + '[' + folder_name + ']')
f.write('\n' + '\t' +'comment = '+ folder_name)
f.write('\n' + '\t' +'path = '+ folder_location)
f.write('\n' + '\t' +'browseable = yes')
f.write('\n' + '\t' +'writeable = yes')
f.write('\n' + '\t' +'create mode = 0777')
f.write('\n' + '\t' +'directory mode = 0777')
f.write('\n' + '##########################')
f.write('\n')
f.close()

# Reading file from here
f = open('/Users/sarfaraz/smb.conf','r')
message = f.read()
print(message)
f.close()

###########

print("Changing the folder permission")

if os.path.exists(folder_location) == True:
    os.chmod(folder_location, 0o777)
else:
    os.mkdir(folder_location)
    os.chmod(folder_location, 0o777)

#################
print("Restarting the Samba service")
#smb_service = "sudo service smbd"
#os.system(smb_service)



