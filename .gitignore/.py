# -*- coding: utf-8 -*-
import time
import datetime
from datetime import timedelta


vd_min = [10, 10, 10, 10]
vd = [10, 10, 10, 10]
tc = [0,0,0,0,0,0,0,0,0,0,0,0]

plano = [[vd[0],"00000000", vd[1],"00000000", vd[2],"00000000", vd[3],"00000000"],
         [vd[0],"00000000", vd[1],"00000000", vd[2],"00000000", vd[3],"00000000"],
         [vd[0],"00000000", vd[1],"00000000", vd[2],"00000000", vd[3],"00000000"],
         [vd[0],"00000000", vd[1],"00000000", vd[2],"00000000", vd[3],"00000000"],
         [vd[0],"00000000", vd[1],"00000000", vd[2],"00000000", vd[3],"00000000"],
         [vd[0],"00000000", vd[1],"00000000", vd[2],"00000000", vd[3],"00000000"],
         [vd[0],"00000000", vd[1],"00000000", vd[2],"00000000", vd[3],"00000000"],
         [vd[0],"00000000", vd[1],"00000000", vd[2],"00000000", vd[3],"00000000"],
         [vd[0],"00000000", vd[1],"00000000", vd[2],"00000000", vd[3],"00000000"],
         [vd[0],"00000000", vd[1],"00000000", vd[2],"00000000", vd[3],"00000000"],
         [vd[0],"00000000", vd[1],"00000000", vd[2],"00000000", vd[3],"00000000"],
         [vd[0],"00000000", vd[1],"00000000", vd[2],"00000000", vd[3],"00000000"],
         [vd[0],"00000000", vd[1],"00000000", vd[2],"00000000", vd[3],"00000000"],
         [vd[0],"00000000", vd[1],"00000000", vd[2],"00000000", vd[3],"00000000"],
         [vd[0],"00000000", vd[1],"00000000", vd[2],"00000000", vd[3],"00000000"]]
         

am = [3, 3, 3, 3, 3, 3, 3, 3]
       

file=open("data.txt", "r")

with file as arq:
    for line in arq:
        try:
            n_plans, n_est, n_fas, n_troc = line.split("  ")
        except:
            continue
    file.close()




#-----------------------------------------------------------------------------------
# Leitura dos estágios e fases e planos (data.txt)

with open("data.txt") as arq:
    count = 0
    for line in arq:
        try:
            t1, stat1, t2, stat2, t3, stat3, t4, stat4 = line.split(" ")
        except:
            continue
        plano[count] = int(t1), stat1, int(t2), stat2, int(t3), stat3, int(t4), stat4
        nr_planos = count + 1
        count +=1
            
#------------------------------------------------------------------------------------         
# Leitura do Cronograma: (data.txt)


def crono():

    dia_sem = datetime.datetime.today().weekday()
    now = datetime.datetime.now().replace(microsecond=0, second=0)
    atual = now.time()
    

    with open("data.txt") as arq:

        ant = "00:00"
        pla = "0"
        pl = "0"
   
        for line in arq:
            try:
                ds, hr, pl = line.split("-") # dia da semana, hora/min, plano
                   
            except:
                continue
        
            inst = datetime.datetime.strptime(hr, '%H:%M')
            inst = inst.time()
            inst2 = datetime.datetime.strptime(ant, '%H:%M')
            inst2 = inst2.time()
           
            if int(dia_sem) == int(ds):
                if atual >= inst2 and atual < inst:
                    print ("plano atual %s" %pla)
                    break
                
            ant = hr
            pla = pl

        pl = pla
        global pl
     
#--------------------------------------------------------------------------------------  


def ciclo(p): 
    
    print ("estágio 1 plano %d") % int(p)
    for tpo in range(0, plano[p][0]):
        print (tpo)
        time.sleep(1)

    print ("estágio 2 plano %d") % int(p)
    for tpo in range(0, plano[p][2]):
        print (tpo)
        time.sleep(1)
        
    print ("estágio 3 plano %d") % int(p)
    for tpo in range(0, plano[p][4]):
        print (tpo)
        time.sleep(1)
        
    print ("estágio 4 plano %d") % int(p)   
    for tpo in range(0, plano[p][6]):
        print (tpo)
        time.sleep(1)

           

        
while True:
    
      crono()  
      ciclo(int(pl))
    











    
