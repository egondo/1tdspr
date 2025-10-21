def mostra_vice(campeao: str, paises: list):
    for vice in paises:
        if campeao != vice:
            print(f"1º {campeao} 2º{vice}")


times = ["Alemanha", "Argentina", "Bélgica", "Brasil", "Colômbia", "Costa Rica", "França", "Holanda"]

#mostra_vice('Alemanha', times)
#mostra_vice('Argentina', times)

for campeao in times:
    mostra_vice(campeao, times)
