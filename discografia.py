import pymongo
import json

client = pymongo.MongoClient("localhost", 27017)
db = client.discografia

albuns_list = [] #albuns_list irá armazenar todos os documentos com informações de albuns em formato string

# Criando as strings com informações dos albuns:
albuns_list.append(
    '{"nome" : "Somewhere Far Beyond", "dataLancamento" : "1992-05-30", "duracao" : "3328", "artista" : {"nome" : "Blind Guardian"}}'
)
albuns_list.append(
    '{"nome" : "Master of Puppets", "dataLancamento" : "1986-03-03", "duracao" : "3286", "artista": {"nome": "Metallica"}}'
)
albuns_list.append(
    '{"nome" : "...And Justice for All", "dataLancamento" : "1988-08-25", "duracao" : "3929", "artista": {"nome": "Metallica"}}'
)
albuns_list.append(
    '{"nome" : "Among the Living", "produtor" : "Eddie Kramer","artista": {"nome": "Metallica"}}'
)
albuns_list.append(
    '{"nome" : "Nevermind", "artista" : {"nome": "Nirvana"}, "estudioGravacao" : ["Sound City Studios", "Smart Studios (Madison)"], "dataLancamento" : "1992-01-11"}'
)
albuns_list.append(
    '{"nome" : "The Dark Side of The Moon", "artista" : {"nome":"Pink Floyd"}, "dataLancamento" : "1973-04-29"}'
)

# Transforma as instrings em documento JSON e depois insere na coleção 'albuns' do MongoDB
for item in albuns_list: 
    album = json.loads(item)
    db.albuns.insert(album)

artists_list = [] #artists_list irá armazenar todos os documentos com informações de artistas em formato string

# Criando as strings com informações dos artistas:
artists_list.append(
    '{"nome":"Metallica","origem":"Los Angeles","nacionalidade":"Estados Unidos"}'
)
artists_list.append(
    '{"nome":"Pink Floyd", "nacionalidade":"Reino Unido", "genero":"Rock Progressivo"}'
)
artists_list.append(
    '{"nome":"Nirvana", "nacionalidade":"Estados Unidos", "genero":"Grunge"}'
)
artists_list.append(
    '{"nome":"Blind Guardian", "nacionalidade":"Alemanha", "genero":"Power Metal", "origem":"Krefeld"}'
)

# Transforma as instrings em documento JSON e depois insere na coleção 'artistas' do MongoDB
for item in artists_list: 
    artist = json.loads(item)
    db.artistas.insert(artist)