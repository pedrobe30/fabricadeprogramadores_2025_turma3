from classes_01 import AnimaisMarinhos

sexo_final = AnimaisMarinhos.machoFemea()

marinho1 = AnimaisMarinhos('Baleia', 'Agua salgada', 10.21, sexo_final,  'Sim', False)
marinho2 = AnimaisMarinhos('Tubarão', "Água salgada", 6.65, sexo_final,  "Sim", True)
marinho3 = AnimaisMarinhos("Golfinho", "Água salgada", 1.83, sexo_final, "Sim", False)
marinho4 = AnimaisMarinhos("Jacaré", "Água Doce", 1.70, sexo_final, "Sim", False)
marinho5 = AnimaisMarinhos("Carangueijo", "Água Salgada", 0.80, sexo_final, "Não", False)
marinho6 = AnimaisMarinhos("Estrela do Mar", "Água Salgada", 0.20, sexo_final, "Não", True)
marinho7 = AnimaisMarinhos()
marinho8 = AnimaisMarinhos()
marinho9 = AnimaisMarinhos()
marinho10 = AnimaisMarinhos()
marinho11 = AnimaisMarinhos()
marinho12 = AnimaisMarinhos()
marinho13 = AnimaisMarinhos()
marinho14 = AnimaisMarinhos()
marinho15 = AnimaisMarinhos()
marinho16 = AnimaisMarinhos()
marinho17 = AnimaisMarinhos()
marinho18 = AnimaisMarinhos()
marinho19 = AnimaisMarinhos()
marinho20 = AnimaisMarinhos()

def genero():
 if sexo_final == 'femea':
     return print("Tenho gravidez")
 elif sexo_final == 'macho':
     return print("Não tenho gravidez")


marinho1.nadar()
marinho1.respirar_dentro_agua()
marinho1.alimentacao()
marinho1.agua()
genero()


print("--"*90)
sexo_final = AnimaisMarinhos.machoFemea()

marinho2.nadar()
marinho2.respirar_dentro_agua()
marinho2.alimentacao()
marinho2.agua()
genero()

print("--"*90)

marinho3.nadar()
marinho3.respirar_dentro_agua()
marinho3.alimentacao()
marinho3.agua()
genero()

print("--"*90)


