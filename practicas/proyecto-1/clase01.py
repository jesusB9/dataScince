from re import I


juego={
    "personajes":[
                    {"nombre":[{"nombre1":"Darsamat","apellido":"hernen"}],"tipo":"mago","level":23,"password":"320320"},
                    {"nombre":[{"nombre1":"JuanElGuerrero","apellido":"jimenez"}],"tipo":"guerrero","level":22,"password":"13213123"},
                    {"nombre":[{"nombre1":"juan","apellido":"perez"}],"tipo":"elfo","level":24,"password":"32323213"},
                 ],
    "paises":["japon","corea","australia"]
    }

def usuario():
    cont=0
    for i in range(len(juego["personajes"])):
      
            print(juego["personajes"][i]["nombre"][0]["nombre1"])
            print(juego["personajes"][i]["nombre"][0]["apellido"])
            print(juego["paises"][i])
          

     
usuario()

print(I)