"""
Uzrakstiet programmu Python, 
kas pieņem veselu skaitli (n) un 
aprēķina n + nn + nnn vērtību.
"""

#ja piem. 2  tad izdrukaas 2+22+222 kopaa 246

a=input("ievadi ciparu; ")
aa=str(a)+str(a)
aaa=str(a)+str(a)+str(a)
summa=int(a)+int(aa)+int(aaa)

print(summa)