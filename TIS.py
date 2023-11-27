( #-*- coding: utf-8 -*-
import os

def menu():

    print(""" 
▄▄▄█████▓      ██▓       ██████      
▓  ██▒ ▓▒     ▓██▒     ▒██    ▒      
▒ ▓██░ ▒░     ▒██▒     ░ ▓██▄        
░ ▓██▓ ░      ░██░       ▒   ██▒     
  ▒██▒ ░  ██▓ ░██░ ██▓ ▒██████▒▒ ██▓ 
  ▒ ░░    ▒▓▒ ░▓   ▒▓▒ ▒ ▒▓▒ ▒ ░ ▒▓▒ 
    ░     ░▒   ▒ ░ ░▒  ░ ░▒  ░ ░ ░▒  
  ░       ░    ▒ ░ ░   ░  ░  ░   ░   
           ░   ░    ░        ░    ░  
           ░        ░             ░  
           
           			@MEYİTZADE
           				2023
========================================
TERMUX ARAÇ YÜKLEYİCİ
----
SADECE TERMUX İÇİN! 😁😁
---- ✨-HOŞ GELDİNİZ-✨ ----
==========================================
00. Android'i bir Hack Makinesin'e dönüştürün.
------------------------------------------
---- GEREKLİ ARAÇLAR ----
1. KURULACAK Nmap 
2. KURULACAK Hydra
3. KURULACAK SQLMap
4. KURULACAK Metasploit
5. KURULACAK ngrok
6. KURULACAK Kali Nethunter
7. KURULACAK angryFuzzer
8. KURULACAK Red_Hawk
9. KURULACAK Weeman
10.KURULACAK IPGeoLocation
11.KURULACAK Cupp
12.KURULACAK Instagram Bruteforcer 
13.KURULACAK Twitter Bruteforcer   
14.KURULACAK Ubuntu
15.KURULACAK Fedora
16.KURULACAK viSQL
17.KURULACAK Hash-Buster
18.KURULACAK D-TECT
19.KURULACAK routersploit
------------------------------------------
99. ÇIKIŞ
==========================================
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "00":
        print("================================")
        print("Bunlar yüklenecek: nmap, hydra, sqlmap, metasploit, ngrok, \nangryFuzzer, red_hawk, weeman, \nIPGeoLocation, cupp, instahack, TwitterSniper, Hash-Buster, D-TECT, routersploit and viSQL with one click.")
        print("----------------")
        hm = input("[?] Devam etmek istiyor musun? (y/n): ")
        print("================================")
        if hm == "y":
            print("========================================================")
            print("[+] Lütfen androidinizi bırakın ve toilet indirin...")
            print("Çünkü bu uzun zaman alacak.")
            print("========================================================")
            os.system("pkg update")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y python2")
            os.system("pkg install -y wget")
            os.sysetm("pkg install -y nmap")
            os.system("plg install -y hydra ")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg install wget")
            os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
            os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
            os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
            os.system("cd /data/data/com.termux/files/home && bundle install")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
            os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
            os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home && pip2 install requests")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y php")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y python2")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
            os.system("cd /data/data/com.termux/files/home && cd weeman")
            os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
            os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
            os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y nano")
            os.system("pip install requests")
            os.system("pip install beautifulsoup4")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pip install mechanicalsoup")
            os.system("pkg install -y nano")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            os.system("clear")
            print("========================================")
            print("[+] Tatmin edici kurulum 3:)")
            print("[+] Mutlu Hacking <3")
            print("========================================")
        else:
            rmenu = input("[?]  Devam etmek istiyor musun? (y/n): ")
            if rmenu == "n":
                menu()
            else:
                break
    if what == "1":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y nmap")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] nmap doğru şekilde kuruldu :)")
        print("[+] Başlatmak için 'nmap' yazın.")
        print("====================================")
        rmenu = input("[?]  Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y hydra")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Hydra doğru kurulumu :)")
        print("[+] 'Hydra' Yaz Başlat.")
        print("====================================")
        rmenu = input("[?]  Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "3":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SQLMap doğru şekilde kuruldu :)")
        print("[+] Başlatmak için 'python2 sqlmap.py' yazın.")
        print("====================================")
        rmenu = input("[?]  Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "4":
        os.system("pkg install -y wget")
        os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home && bundle install")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Metasploit doğru kurulum :)")
        print("[+] Başlatmak için 'msfconsole' yazın.")
        print("====================================")
        rmenu = input("[?]  Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "5":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] ngrok doğru kurulum yapılmadı :)")
        print("[+]'./ngrok http 80' gösterdiğim gibi baştaki klasörü aç.")
        print("====================================")
        rmenu = input("[?]  Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "6":
        os.system("pkg update -y")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
        os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Nethunter doğru şekilde kuruldu :)")
        print("[+] Nethunter-In-Termux'u kullanın ve başlamak için './kalinethunter' yazın.")
        print("====================================")
        rmenu = input("[?]  Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "7":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
        os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
        os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home && pip2 install requests")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] AngryFuzzer doğru şekilde kuruldu :)")
        print("[+] AngryFuzzer'ı her yere yerleştirin\nbaşlatmak için 'python2 AngryFuzzer.py' dosyasını çalıştırın.")
        print("====================================")
        rmenu = input("[?]  Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "8":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y php")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] RED_HAWK doğru şekilde kuruldu :)")
        print("[+] RED_HAWK klasörünü açın ve başlatmak\niçin 'php rhawk.php' dosyasını açın.")
        print("====================================")
        rmenu = input("[?]  Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "9":
        os.system("pkg update -y")
        os.system("pkg install -y python2")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
        os.system("cd /data/data/com.termux/files/home && cd weeman")
        os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] weeman doğru kurulum :)")
        print("[+] weeman klasörünün tamamını açın ve\nbaşlatmak için 'python2 weeman.py' dosyasını çalıştırın.")
        print("====================================")
        rmenu = input("[?]  Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "10":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
        os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
        os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] IPGeoLocation doğru şekilde kuruldu :)")
        print("[+] IPGeoLocation klasörünü açın ve başlatmak\niçin 'python ipgeolocation.py' dosyasını çalıştırın.")
        print("====================================")
        rmenu = input("[?]  Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "11":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
        print("====================================")
        print("[+] cupp Doğru kurulum :)")
        print("[+] Cupp klasörünün tüm klasörünü açın ve\nbaşlatmak için 'python cupp3.py' dosyasını çalıştırın.")
        print("====================================")
        rmenu = input("[?] Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "12":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y nano")
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
        print("====================================")
        print("[+] instahack Doğru Kurulumu :)")
        print("[+] Instahack klasörünü açın ve başlatmak\niçin 'python hackinsta.py' dosyasını açın.")
        print("====================================")
        rmenu = input("[?] Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "13":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pip install mechanicalsoup")
        os.system("pkg install -y nano")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
        print("====================================")
        print("[+] TwitterSniper doğru şekilde kuruldu :)")
        print("[+] TwitterSniper'ın tüm klasörünü açın ve başlatmak\niçin 'python TwitterSniper.py' dosyasını açın.")
        print("====================================")
        rmenu = input("[?]  Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "14":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
        os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
        print("====================================")
        print("[+] Ubuntu  doğru şekilde kuruldu :)")
        print("[+] ve termux-ubuntu klasörünü başlatın\nve başlatmak için './start.sh' dosyasını açın.")
        print("====================================")
        rmenu = input("[?] Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "15":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y wget")
        os.system("apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
        print("====================================")
        print("[+] Fedora doğru şekilde kuruldu :)")
        print("[+] Başlatmak için 'sh termux-fedora.sh f26_arm64'\nveya 'sh termux-fedora.sh f26_arm' komutunu kullanın.")
        print("====================================")
        rmenu = input("[?] Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "16":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
        print("====================================")
        print("[+] viSQL doğru şekilde kuruldu :)")
        print("[+] viSQL klasörünü bulun ve başlatmak\niçin 'python2 viSQL.py --help' dosyasını açın.")
        print("====================================")
        rmenu = input("[?] Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "17":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
        print("====================================")
        print("[+] Hash-Buster doğru şekilde kuruldu :)")
        print("[+] Hash-Buster klasörünün tamamını açın ve\nbaşlatmak için 'python2 hash.py' dosyasını çalıştırın.")
        print("====================================")
        rmenu = input("[?] Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "18":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
        print("====================================")
        print("[+] D-TECT doğru şekilde kuruldu :)")
        print("[+] tüm Hash-Buster klasörünü açın ve başlatmak\niçin 'python2 hash.py' dosyasını çalıştırın.")
        print("====================================")
        rmenu = input("[?]  Devam etmek istiyor musun? (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            print("====================================")
            print("[+] Routersploit kurulumu doğru :)")
            print("[+] Routersploit klasörünün tamamını açın\nve başlatmak için 'python2 rsf.py' dosyasını açın.")
            print("====================================")
            rmenu = input("[?] Devam etmek istiyor musun? (y/n): ")
            if rmenu == "n":
                menu()
            else:
                break
    elif what == "99":
        print("Sağlıklı günler dilerim 🤝.")
        print("Kod yazmak sabır işidir. Sabredersen yaratmanın zevkini alırsın.😈")
        break
)
