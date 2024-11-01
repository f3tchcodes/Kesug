### DISCLAIMER
`By using this program, you acknowledge that you do so at your own risk. The developer is not responsible for any loss, damage, or harm to files, data, systems, or any legal issues, including political matters, that may arise as a result of using this software. You agree to take full responsibility for any consequences arising from its use.`

> **NOTE I WOULD LIKE TO ENSURE THAT I MYSELF HAVE NOT USED THIS SOFTWARE AT ALL, AND I RECOMMEND YOU THE SAME. THIS SOFTWARE IS PURELY FOR EDUCATIONAL PURPOSES AND CHECKING OUT THE INNER WORKINGS OF A RANSOMWARE**

### Introduction
Hi, I'm `f3tch`. About a year ago I was super bored, so I decided to write a **ransomware**. I didn't have sufficient knowledge in C++ so I decided to go with **Python**.

*Pictures?? Nahh I'm too lazy to add them. And I do not want to run the program again.*

### How to setup
1. **Clone** the repository
2. **DOWNLOAD ALL LIBRARY REQUIREMENTS!** I'm too lazy to make the requirement file atm so you'd have to open the code and look through yourself which libraries you'd have to install
3. Move **htdocs** contents to xampp htdocs folder or your website
4. Create a **datbase** using **KesugDBStructure**. I don't remember how we had to do it but I suppose you just have to post the files to phpmyadmin
5. Enter your **webhook** in Kesug.py
6. I suppose that's it but I think there is some information in Kesug.py file like the website, wallet address etc so change that according to your needs
7. **Send** to the victim!

### Functionalites
```
- Fetches all drive letters and file paths.
- Encrypts all files using Fernet.
- Opens the program every time windows is booted.
- Takes a picture through integrated/dedicated camera and sends to a Discord webhook.
```

### How to decode
The key to decode is stored in the database you made. The victim is supposed to go to the website provided and enter their **discord** and **key ID**. Using which you contact them, confirm the payment, and hand over the decryption key.

### Bugs
*Alright if you review the code you can find out the key easily*, I suppose using a **network sniffer** like **wireshark** should do the job. I'm aware it's a huge bug but that's the first ever ransomware/hacking application I've written so just let it slide haha.

Also, I haven't run this program in like a year, and I don't want to. I've already reinstalled my windows several times using this as I wasn't using virtual machine at the time of testing *for some reason I don't remember*. As I was saying I do **NOT** remember if there are any errors, or my data being leaked. You'd have to sort that out yourself. 

### Credits
> Discord: f3tch

> Instagram: f3tch.hassan
