__author__ = 'ortus'

sn = input("Input Social Security Number, AAA-GG-SSSS").strip()

def inp(a):
    try:
        area, group, serial = a.split('-')
        t = area, group, serial
        q = t[0]+'-'+t[1]+'-'+t[2]
        if len(t) == 3:
            if t[2] == '':
                print("Not a valid SS number!")
                return None
            elif '666' in t[0]:
                print("Not a valid SS number!")
                return None
            elif len(t[0]) != 3:
                print("Not a valid SS number!")
                return None
            elif len(t[1]) != 2:
                print("Not a valid SS number!")
                return None
            elif len(t[2]) != 4:
                print("Not a valid SS number!")
                return None
            elif '000' in t[0]:
                print("Not a valid SS number!")
                return None
            elif '00' in t[1]:
                print("Not a valid SS number!")
                return None
            elif '0000' in t[2]:
                print("Not a valid SS number!")
                return None
            elif area + group + serial == '078' + '05' + '1120':
                print("Not a valid SS number!")
                return None
        area = int(area)
        group = int(group)
        serial = int(serial)
        if 900 <= area <= 999:
            print("Not a valid SS Number!")
            return None
        else:
            print(q)

    except ValueError:
        print("Not a valid SS number!")
        return None

def ss():
    ss = inp(sn)
    while ss is None:
        ss = inp(sn)
        #return

ss()
