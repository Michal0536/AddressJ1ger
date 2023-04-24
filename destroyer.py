import csv
import random
import string
import pyfiglet
import os

banner = pyfiglet.figlet_format('DESTROYER', font = "slant",width=900)

def menu():
    print(f"\n{banner}")
    print("[1] J1gowanie adresu\n[2] Tworzenie formatek do botow\n[3] Wyjdz")

    choice = int(input())
    if choice == 1:
        ulica_basic = input("Podaj ulice do j1gowania: ")
        nr_domu = input("Podaj nr domu/ nr mieszkania: ")
        user_ilosc = input("Podaj ilosc adresow do wygenerowania: ")
        j1g_adres("J1g",ulica_basic,user_ilosc,nr_domu)
        os.system('cls')
        print("Wygenerowano do pliku adresy.txt")
        menu()
    if choice == 2:
        print("Formatka:\n [1] BananaAIO\n [2] PanAIO")
        choice2 = int(input())
        if choice2 == 1:
            banana()
            os.system('cls')
            print("Wygenerowano do pliku banana.csv")
            menu()
        if choice2 == 2:
            pan_aio()
            os.system('cls')
            print("Wygenerowano do pliku panaio.csv")
            menu()
        else:
            menu()
    if choice == 3:
        quit()
    else:
        menu()


def j1g_adres(arg,ulica_basic,user_ilosc,nr_domu):
    open('adresy.txt','w').close()
    for ilosc in range(int(user_ilosc)):
        ulica_tab = []
        ulica_przedrostek = ['st','ST','STRAAT','straat','strat',f"{random.choice(string.ascii_letters)}Ul",f"{random.choice(string.ascii_letters)}Al",f"{random.choice(string.ascii_letters)}{random.choice(string.ascii_letters)}"]
        
        for s in ulica_basic.lower():
                ulica_tab.append(s)

        l_ulica = len(ulica_tab)-1
        if len(ulica_tab) > 6:
            starting = 4
        else:
            starting = 3

        r = random.randint(starting,int(l_ulica))
        if ulica_tab[r] == "a":
            ulica_tab[r] = "4"
        if ulica_tab[r] == "o":
            ulica_tab[r]="0"
        else:
            ulica_tab[r] = random.choice(string.ascii_letters)

        ulica = map(str,ulica_tab)
        ulica_size = ''.join(random.choice((str.upper, str.lower))(char) for char in ulica)
        ulica_przedrostek_size = ''.join(random.choice((str.upper, str.lower))(char) for char in random.choice(ulica_przedrostek))
        if arg == 'J1g': 
            with open("adresy.txt",'a') as f:
                f.write(f"{ulica_przedrostek_size}.{ulica_size} {nr_domu}\n")
                f.close()
        if arg == 'ret':    
            return (f"{ulica_przedrostek_size}.{ulica_size}")

def banana():
    hm = int(input("Ile pofili wygenerowac: "))
    header = ["PROFILE","ShippingCity","ShippingFirstname","ShippingLastname","ShippingStreet","ShippingAdditional","ShippingZip","SameBilling","BillingCity","BillingFirstname"	"BillingLastname","BillingStreet","BillingAdditional","BillingZip","PhoneNumber","Webhook"]
    with open('banana.csv', 'w', encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            f.close()
    try:
        print("Uzupelnij dane:")
        profile_name = input("Nazwa profilu: ")
        city= input("Miasto: ")
        name = input('Imie: ')
        surname = input('Nazwisko: ')
        ulica = input('Ulica: ')
        nr_domu = input('Nr domu/Nr mieszkania: ')
        nip = input('NIP: ')
        kod = input('Kod pocztowy: ')
        sameasBiling = input('Shipping same as biling (TRUE/FALSE): ')
        if sameasBiling == "TRUE":
            BillingCity = ""
            BillingFirstnameBillingLastname =""
            BillingStreet =""
            BillingAdditional=""
            BillingZip=""
        if sameasBiling == "FALSE":
            BillingCity = input("[Billing] Miasto: ")
            BillingFirstnameBillingLastname = input("[Billing] Imie i nazwsko: ")
            BillingStreet = input("[Billing] Ulica: ")
            BillingAdditional = input("[Billing] NIP: ")
            BillingZip = input("[Billing] Kod pocztowy: ")
        phone_number = input('Nr telefonu: ')
        webhook = input('Webhook: ')
        if not profile_name or not city or not name or not surname or not ulica or not nr_domu or not kod or not sameasBiling or not webhook or not phone_number:
            raise ValueError("empty string")
    except ValueError as e:
        print("\nNie uzupelniono wszystkich kolumn.Spróbuj jeszcze raz!\n")
        banana() 

    for i in range(hm):
        profile_name_1 = profile_name+str(i)
        adres = f"{j1g_adres('ret',ulica,hm,nr_domu)} {nr_domu}"
        data = [profile_name_1, city, name, surname, adres, nip,kod,sameasBiling,BillingCity,BillingFirstnameBillingLastname,BillingStreet,BillingAdditional,BillingZip,phone_number,webhook]
        with open('banana.csv', 'a', encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
            f.close()


def pan_aio():
    hm = int(input("Ile pofili wygenerowac: "))
    header = ["name","address","address2","city","postcode","email","country","region","cards","holder","numbercard","month","year","cvv","phone","profileName","webhook"]
    with open('panaio.csv', 'w', encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            f.close()
    try:
        print("Uzupelnij dane:")
        name = input('Imie i nazwisko: ')
        ulica = input('Ulica: ')
        nr_domu = input('Nr domu/Nr mieszkania: ')
        nip = input('NIP: ')
        city= input("Miasto: ")
        kod = input('Kod pocztowy: ')
        email = input("email: ")
        wojewodztwo = input("wojewodztwo: ")
        phone_number = input('Nr telefonu: ')
        profile_name = input("Nazwa profilu: ")
        webhook = input('Webhook: ')
        if not name or not ulica or not nr_domu or not city or not kod or not email or not wojewodztwo or not phone_number or not profile_name or not webhook:
            raise ValueError("Empty String")
    except ValueError as e:
        print("\nNie uzupelniono wszystkich kolumn.Spróbuj jeszcze raz!\n")
        pan_aio()
   
    for i in range(hm):
        profile_name_1 = profile_name+str(i)
        adres = f"{j1g_adres('ret',ulica,hm,nr_domu)} {nr_domu}"
        data = [name,adres,nip,city,kod,email,"PL",wojewodztwo,"VISA",name,"4123512361237123",'01','2022','123',phone_number,profile_name_1,webhook]
        with open('panaio.csv', 'a', encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
            f.close()
        

menu()