import wmi
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from Tkinter import *


def doNothing():
    print("ok, doing nothing")

def GetNicConfigs():
    # Obtain network adaptors configurations
    return wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=False)

def OptionMenuItemSelected(selectedItem):
    #TODO: ?
    print("test")


def GetNicInfo(nicDesc):
    # Hämtar info om valt nätverkskort
    logging.debug('Getting info from selected adapter')
    nicIndexFound = False

    for nic in nic_configs:
        if nicDesc == nic.Description:
            print "Index: " + str(nic.Index)
            nicIndexFound = True

    if not nicIndexFound: 
        print "Index: N/A"
    #print ip
    
    print userEntryIPfirstOctet.get()

   
root = Tk()
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(600, 400))

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
# First dropdown menu
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New project...", command=doNothing)
subMenu.add_command(label="New", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

# Second dropdown menu
editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)


# Optionmenu with all available adapters
selectedNicOptionMenu = StringVar(root)
selectedNicOptionMenu.set("Adapters") # default value

nic_configs = GetNicConfigs()
nicDesclist = []
for nic in nic_configs:
    nicDesclist.append(nic.Description)

nicOptionMenu = OptionMenu(root, selectedNicOptionMenu, *nicDesclist,command=OptionMenuItemSelected)
nicOptionMenu.pack()

# Get info button
nicReqInfoButton = Button(root, text="Get index of nic", command=lambda: GetNicInfo(selectedNicOptionMenu.get()))
nicReqInfoButton.pack()

userEntryIPfirstOctet = Entry(root, width=5)
userEntryIPfirstOctet.pack()
userEntryIPsecondOctet = Entry(root, width=5)
userEntryIPsecondOctet.pack()
userEntryIPthirdOctet = Entry(root, width=5)
userEntryIPthirdOctet.pack()
userEntryIPfourthOctet = Entry(root, width=5)
userEntryIPfourthOctet.pack()





# IP address, subnetmask and gateway values should be unicode objects
#ip = str(userEntryIPfirstOctet.get()) + '.' +  userEntryIPsecondOctet.get() + '.' + userEntryIPthirdOctet.get() + '.' + userEntryIPfourthOctet.get()
ip = userEntryIPfirstOctet.get()

#ip = u'192.168.0.11'
subnetmask = u'255.255.255.0'
gateway = u'192.168.0.1'


# Set IP address, subnetmask and default gateway
# Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
#nic.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
#nic.SetGateways(DefaultIPGateway=[gateway])




def main():
    logger.info('Starting main')
    root.mainloop()


if __name__ == '__main__':
    main()