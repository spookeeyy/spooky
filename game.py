from random import randint

elusid = 10
münte = 0
võidukogus = 150
oht = False

while elusid > 0:
    print("Jalutasid metsas ja nägid ", end="")
    kedaMida = randint(1, 4)
    
    if oht:
        print("ohtu", end="")
        print(", ja kaotasid kaks elu.")
        elusid -= 2
        oht = False
        print("Sul on jäänud " + str(elusid) + " elu.")
    
    elif kedaMida == 1:
        print("seent", end="")
        if randint(1, 3) == 1:
            print(", mis kahjuks oli mürgine, kaotasid ühe elu.")
            elusid -= 1
            print("Sul on jäänud " + str(elusid) + " elu.")
        else:
            print(", mis oli söödav seen ja sai selle müügist ühe sendi.")
            münte += 1
    
    elif kedaMida == 2:
        print("karu", end="")
        if randint(1, 3) == 1:
            print(", kes oli kahjuks vihane ja kaotasid ühe elu.")
            elusid -= 1
            print("Sul on jäänud " + str(elusid) + " elu.")
        else:
            print(", kes oli rõõmus ning andis sulle 5 senti.")
            münte += 5
    
    elif kedaMida == 3:
        print("kuldmünti, ja sa said selle endale.")
        münte += 1
        
    else:
        print("aarekirstu, ja leidsid sealt 10 münti.")
        münte += 10
    
    if münte >= võidukogus:
        print("Sa kogusid piisavalt kuldmünte ja võitsid mängu!")
        break
    
    if randint(1, 10) == 1:
        print("Sattusid ohtu!")
        oht = True
    
    print("Nüüd on sul " + str(münte) + " kuldmünti.")
    input("Jätkamiseks vajuta enterit.")

if münte < võidukogus:
    print("Sa kaotasid kõik elud. Mäng on läbi.")