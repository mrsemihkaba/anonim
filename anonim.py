import os
import subprocess

def check_tool(tool_name, install_command):
    try:
        # Komutu çalıştırarak aracın yüklü olup olmadığını kontrol ediyoruz
        subprocess.check_output([tool_name, "--version"])
    except OSError:
        print(f"{tool_name} yüklü değil. Yükleniyor...")
        os.system(f"sudo apt install {install_command}")

def change_mac():
    interface = input("MAC adresini değiştirmek istediğiniz ağ arayüzünü girin: ")
    os.system(f"sudo macchanger -r {interface}")

def restore_mac():
    interface = input("Eski MAC adresine dönmek istediğiniz ağ arayüzünü girin: ")
    os.system(f"sudo macchanger -p {interface}")

def change_ip():
    os.system("sudo anonsurf start")

def restore_ip():
    os.system("sudo anonsurf stop")

def get_ip():
    os.system("curl ifconfig.me")

# Macchanger'ı kontrol edelim
check_tool("macchanger", "macchanger")

# Anonsurf'ü kontrol edelim
try:
    subprocess.check_output(["anonsurf", "--status"])
except OSError:
    print("Anonsurf yüklü değil. Yükleniyor...")
    # Anonsurf'ü GitHub adresinden indirip kurabilirsiniz
    os.system("git clone https://github.com/Und3rf10w/kali-anonsurf.git")
    os.chdir("kali-anonsurf")
    os.system("sudo ./installer.sh")

# Algoritma menüsü
while True:
    print("Anonim Menüsü:")
    print("1-) Mac adresini değiştir")
    print("2-) Eski mac adresine dön")
    print("3-) IP adresini değiştir")
    print("4-) Eski IP adresine dön")
    print("5-) Benim IP adresim ne")
    print("6-) Çıkış")

    choice = input("Bir seçenek seçin: ")

    if choice == "1":
        change_mac()
    elif choice == "2":
        restore_mac()
    elif choice == "3":
        change_ip()
    elif choice == "4":
        restore_ip()
    elif choice == "5":
        get_ip()
    elif choice == "6":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")
