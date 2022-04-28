
#KT1
#Martin Pettai
#28.04
#IT21
fail='oda_uus.txt'

def odavise(fail):
    parimad_visked=[]
    parim_vise = 0
    with open(fail, 'r', encoding="utf-8") as minu_fail:
        for rida in minu_fail:
            pnimi,enimi,vise1,vise2,vise3=rida.split(" ")   #splittisin read
            
            visked=vise1,vise2,vise3
            for vise in visked:
                if float(vise)>float(parim_vise): # parim vise
                    parim_vise=vise
                    parim_viskaja=enimi+" "+pnimi
                    parimad_visked.append(parim_vise)
                    

            vastus=print(pnimi,enimi,parim_vise)
    print("Võitja: "+parim_viskaja+" | "+parim_vise)


odavise(fail)