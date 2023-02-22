import numpy as np
from numpy import var
from numpy import std
from statistics import mean, median
from statistics import mode

lista = np.genfromtxt('sales_info.csv', delimiter=',', skip_header=True)
lista=np.array(lista)

sale_16=lista[:,3:4]
sale_15=lista[:,2:3]
margin=lista[:,1:2]
volumen= lista[:,0:1]
milista=[]
for i in volumen:
    milista.append(i[0])
vol=np.array(milista)

list_marg=[]
for i in margin:
    list_marg.append(i[0])
l_marg=np.array(list_marg)

list15=[]
for i in sale_15:
    list15.append(i[0])
list15=np.array(list15)

list16=[]
for i in sale_16:
    list16.append(i[0])
list16=np.array(list16)

def media():
    m16=np.mean(list16)
    m15=np.mean(list15)
    m_marg=np.mean(list_marg)
    m_v=np.mean(vol)
    return m16,m15,m_marg,m_v
  
d16,d15,damar,davol=media()

def medina():
    mm16=np.median(list16)
    mm15=np.median(list15)
    mm_marg=np.median(list_marg)
    mm_v=np.median(vol)
    return mm16,mm15,mm_marg,mm_v

sal16,sal15,mag_med,vol_med=medina()

def moda():
    print(mode(list16))
    print(mode(list15))
    print(mode(list_marg))
    print(mode(vol))
moda()

def varia():
    va16=np.var(list16)
    va15=np.var(list15)
    vamg=np.var(list_marg)
    vav=np.var(vol)
    return va16,va15,vamg,vav
vas16,vas15,vamgi,vavl=varia()
print(vas16)

def est():
    est16=np.std(list16)
    est15=np.std(list15)
    est_mg=np.std(list_marg)
    est_vo=np.std(vol)

    return est16,est15,est_mg,est_vo

ests16,ests15,est_mgr,est_vol=est()
print(ests15)




 

