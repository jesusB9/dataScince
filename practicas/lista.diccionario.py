juego={
    "personajes":[
                    {"nombre":[{"nombre1":"Darsamat","apellido":"hernen"}],"tipo":"mago","level":23,"password":"320320"},
                    {"nombre":[{"nombre1":"JuanElGuerrero","apellido":"jimenez"}],"tipo":"guerrero","level":22,"password":"13213123"},
                    {"nombre":[{"nombre1":"juan","apellido":"perez"}],"tipo":"elfo","level":24,"password":"32323213"},
                 ],
    "paises":["japon","corea","australia"]
    }
def listas():
    for valor in juego["personajes"].values():
        for i in valor.values():
           print(i)
            
listas()
def usu():
     for i in range(len(juego["personajes"])):
      
            print(juego["personajes"][i]["nombre"])
            print(juego["paises"][i])

usu()





