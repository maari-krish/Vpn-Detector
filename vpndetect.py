from termcolor import colored
import requests
import webbrowser

print(colored('''
><<         ><<><<<<<<<  ><<<     ><<  
 ><<       ><< ><<    ><<>< ><<   ><<  
  ><<     ><<  ><<    ><<><< ><<  ><<  
   ><<   ><<   ><<<<<<<  ><<  ><< ><<  
    ><< ><<    ><<       ><<   >< ><<  
     ><<<<     ><<       ><<    >< <<  
      ><<      ><<       ><<      ><<  

><<<<<    ><<<<<<<<><<< ><<<<<<><<<<<<<<    ><<   ><<< ><<<<<<    ><<<<      ><<<<<<<    
><<   ><< ><<           ><<    ><<       ><<   ><<     ><<      ><<    ><<   ><<    ><<  
><<    ><<><<           ><<    ><<      ><<            ><<    ><<        >< <><<    ><<  
><<    ><<><<<<<<       ><<    ><<<<<<  ><<            ><<    ><<        >< <>< ><<      
><<    ><<><<           ><<    ><<      ><<            ><<    ><<        >< <><<  ><<    
><<   ><< ><<           ><<    ><<       ><<   ><<     ><<      ><<     ><<  ><<    ><<  
><<<<<    ><<<<<<<<     ><<    ><<<<<<<<   ><<<<       ><<        ><<<<      ><<      ><<      
\n''',"blue"))
print(colored("ミ★ 𝒞☯𝒹𝑒𝒹 𝐵𝓎 𝑀𝒶𝒶𝓇𝒾-𝒦𝓇𝒾𝓈𝒽 ★彡 \n","red"))
print(colored("[+] Detect VPN...\n","blue"))
vpn = input(colored("[+] Enter The Target IP Address : ","magenta"))
print("\n")
print("VPN Detect results for",vpn)
print("-------------------------------------------------------------------------------------")
print("\n")
key="4655b4f97a4148fe84d46ca2bfdee047"
api = "https://vpnapi.io/api/"+vpn+"?key="+key+""
response=requests.get(api)
data=response.json()
ip = data["ip"]
vpn = data["security"]["vpn"]
proxy = data["security"]["proxy"]
tor = data["security"]["tor"]
city = data["location"]["city"]
region = data["location"]["region"]
country = data["location"]["country"]
continent = data["location"]["continent"]
region_code = data["location"]["region_code"]
country_code = data["location"]["country_code"]
continent_code = data["location"]["continent_code"]
latitude = data["location"]["latitude"]
longitude = data["location"]["longitude"]
time_zone = data["location"]["time_zone"]
locale_code = data["location"]["locale_code"]
metro_code = data["location"]["metro_code"]
is_in_european_union = data["location"]["is_in_european_union"]
network = data["network"]["network"]
autonomous_system_number = data["network"]["autonomous_system_number"]
autonomous_system_organization = data["network"]["autonomous_system_organization"]
print(colored(f"[+] IP: {ip}","red"))
print(colored(f"[+] VPN: {vpn}","red"))
print(colored(f"[+] Proxy: {proxy}","red"))
print(colored(f"[+] TOR: {tor}","red"))
print(colored(f"[+] City: {city}","red"))
print(colored(f"[+] Region: {region}","red"))
print(colored(f"[+] Country: {country}","red"))
print(colored(f"[+] Continent: {continent}","red"))
print(colored(f"[+] Region code: {region_code}","red"))
print(colored(f"[+] Country code: {country_code}","red"))
print(colored(f"[+] Continent code: {continent_code}","red"))
print(colored(f"[+] Latitude: {latitude}","red"))
print(colored(f"[+] Longitude: {longitude}","red"))
print(colored(f"[+] Time Zone: {time_zone}","red"))
print(colored(f"[+] Locale Code: {locale_code}","red"))
print(colored(f"[+] Metro Code: {metro_code}","red"))
print(colored(f"[+] Is In European Union: {is_in_european_union}","red"))
print(colored(f"[+] Network: {network}","red"))
print(colored(f"[+] Autonomous System Number: {autonomous_system_number}","red"))
print(colored(f"[+] Autonomous System Organization: {autonomous_system_organization}","red"))
print('')
if data["security"]["vpn"] == True:
    print(colored("This IP Address Using Vpn","green"))
else:
    print(colored("This IP Address Doesn't Using Vpn","green"))
    print('')
if data["security"]["proxy"] == True:
    print(colored("This IP Address Using Proxy","red"))
else:
    print(colored("This IP Address Doesn't Using Proxy","red"))
    print('')
if data["security"]["tor"] == True:
    print(colored("This IP Address Using TOR","blue"))
else:
    print(colored("This IP Address Doesn't Using TOR","blue"))
    print('')
if data["location"]["latitude"] and data["location"]["longitude"]:
    lats = data["location"]["latitude"]
    lons = data["location"]["longitude"]
maps_url = "https://maps.google.com/maps?q=%s,+%s" % (lats, lons)
openWeb = input(colored("Do You Want To Open GPS location in web broser? (Y/N) ","green"))
if openWeb.upper() == 'Y':
    webbrowser.open(maps_url, new=2)
else:
    pass

