# 2) Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de 
#    personaje jugable. Partiendo de que la estadística base es 2, debes cumplir las siguientes condiciones:
# - El caballero tiene el doble de vida y defensa que un guerrero
# - El guerrero tiene el doble de ataque y alcance que un caballero
# - El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su
#   alcance
# - Muestra cómo quedan las propiedades de los tres personajes

caballero = {"vida":2, "ataque":2, "defensa":2, "alcance":2}
guerrero = {"vida":2, "ataque":2, "defensa":2, "alcance":2}
arquero = {"vida":2, "ataque":2, "defensa":2, "alcance":2}

caballero["vida"] = 2 * guerrero["vida"]
caballero["defensa"] = 2 * guerrero["defensa"]
guerrero["ataque"]= 2 * caballero["ataque"] 
guerrero["alcance"]= 2 * caballero["alcance"] 
arquero["vida"] = guerrero["vida"]
arquero["ataque"] = guerrero["ataque"]
arquero["defensa"] = guerrero["defensa"] / 2
arquero["alcance"] = guerrero["alcance"] * 2

print("Caballero:\t",caballero)
print("Guerrero:\t",guerrero)
print("Arquero:\t",arquero)