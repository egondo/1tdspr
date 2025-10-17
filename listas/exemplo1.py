filmes = []
filmes.append("Snow White")
filmes.append("Cinderella")
filmes.append("The Beauty and the Beast")
filmes.append("The Lion King")
filmes.append("The Little Mermaid")
filmes.append("Lilo & Stitch")

for movie in filmes:
    print(movie)

print("=" * 80)

i = len(filmes) - 1
while i >= 0:
    print(filmes[i])
    i = i - 1

