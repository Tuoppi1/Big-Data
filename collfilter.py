import pandas as pd
from scipy.spatial.distance import pdist, squareform


df = pd.read_csv("lastfm-matrix-germany.csv",delimiter=",",encoding="latin")
df.set_index('user', inplace=True)
df = df.loc[(df).any(1), (df!=0).any(0)]

# Comparing Artists / columns
artists = squareform(pdist(df.T, "cosine"))
columnList = list(df)
ArtistSimList = []

# lists for task objective 4
MichaelJackson = []
Madonna = []
Scooter = []

currentArtist = 0

for lista in artists:
    if currentArtist > 284:
        break
    ArtistSimList.append((1,"templateArtist1","templateArtist2"))
    for i in range(0,len(lista)-1):
        usedbandList = []
        # catching data for task obejtive 4
        if columnList[currentArtist] == "michael jackson":
            MichaelJackson.append((lista[i],columnList[currentArtist],columnList[i]))
        if columnList[currentArtist] == "madonna":
            Madonna.append((lista[i],columnList[currentArtist],columnList[i]))
        if columnList[currentArtist] == "scooter":
            Scooter.append((lista[i],columnList[currentArtist],columnList[i]))
            
        if float(ArtistSimList[currentArtist][0]) > float(lista[i]) and float(lista[i]) < 1 \
        and ArtistSimList[currentArtist][2] not in usedbandList and float(lista[i]) > 0:
            # If the distance value is smaller than the previus value, it gets replaced
            stringi = (lista[i],columnList[currentArtist],columnList[i])
            ArtistSimList[currentArtist] = stringi
            usedbandList.append(stringi[2])
    currentArtist += 1

for i in ArtistSimList:
    print(i)

# Comparing Users / rows
df = pd.read_csv("lastfm-matrix-germany.csv",encoding="latin")
users = squareform(pdist(df.T, "cosine"))
rowList = list(df["user"])
userSimList = []
currentUser = 0

for lista in users:
    userSimList.append((1,"templateUser1","templateUser2"))
    for i in range(0,len(lista)):
        usedUserList = []
        if float(userSimList[currentUser][0]) > float(lista[i]) and float(lista[i]) < 1 \
        and userSimList[currentUser][2] not in usedUserList and float(lista[i]) > 0:
            stringi = (lista[i],rowList[currentUser],rowList[i])
            userSimList[currentUser] = stringi
            usedUserList.append(stringi[2])
    currentUser+=1
    
for i in userSimList:
    print(i)

print(*sorted(MichaelJackson)[1:][:10],sep="\n")
print()
print(*sorted(Madonna)[1:][:10],sep="\n")
print()
print(*sorted(Scooter)[1:][:10],sep="\n")   
