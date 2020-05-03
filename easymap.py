import os

os.system("clear")
print("Coded BY c0rrect")
print("Programın çalışması için root olmanız gerekiyor. Sudo su yapıp çalıştırınız.")
print("----------------------------------------------------------------------------")
ipalma = input("Ip adresini öğrenmek istediğiniz site: ")
os.system("clear")
os.system("ping "+ipalma)
cevap = input("Ip adresini kopyaladıysanız 'evet' yazınız: ")
if(cevap=='evet'):
    os.system("clear")
    ip = input("Hefef sitenin ip adresini giriniz: ")
    os.system("nmap -sS -sV "+ip)
    print("--------------------------------------")
    print("       Turk Hack Team <3")

else:
    cevap2 = input("Lütfen IP adresini kopyalayınız.      Kopyaladıysanız 'evet' yazınız: ")
    if(cevap=='evet'):
        os.system("clear")
        ip = input("Hefef sitenin ip adresini giriniz: ")
        os.system("nmap -sS -sV "+ip)
        print("--------------------------------------")
        print("       Turk Hack Team <3")
