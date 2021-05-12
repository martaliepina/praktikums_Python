""" 
Uzrakstiet programmu, kas ielasa vienu vārdu 
un izvada uz ekrāna sveicienu sekojošā formātā:
"Labdien, vards, pimrdienā!"
Ja ievadīts nav jūsu vards, tiek izdrukāts teksts - Uzredzēšanos!
Pārbaudiet programmas darbību ar dažādiem ievaddatiem.
"""

vards=input("ievadi vārdu:  ")

if vards=="Marta":
    print("Labdien, "+vards+", pirmdienā!")
else:
    print("Uzredzēšanos")

