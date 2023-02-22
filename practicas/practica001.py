import numpy as np



lista = np.genfromtxt('sales_info.csv', delimiter=',', skip_header=True)
lista=np.array(lista)

sale_16=lista[:,3:4]
sale_15=lista[:,2:3]
margin=lista[:,1:2]
volumen= lista[:,0:1]
milista=[]
for i in volumen:
    milista.append(i[0])
milista=np.array(milista)
vol=milista

list_marg=[]
for i in margin:
    list_marg.append(i[0])
list_marg=np.array(list_marg)

list15=[]
for i in sale_15:
    list15.append(i[0])
list15=np.array(list15)

list16=[]
for i in sale_16:
    list16.append(i[0])
list16=np.array(list16)

def medias():
    m16=np.mean(list16)
    m15=np.mean(list15)
    m_marg=np.mean(list_marg)
    m_v=np.mean(vol)
    return m16,m15,m_marg,m_v   
m16,m15,m_marg,m_v=medias()

print(m16)












