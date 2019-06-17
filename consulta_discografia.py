import pymongo
import json

client = pymongo.MongoClient("localhost", 27017)
db = client.discografia

print('\nOs álbuns de artistas americanos são:')

artistas_americanos = db.artistas.find({"nacionalidade":"Estados Unidos"})
for artista_americano in artistas_americanos:
    albuns_americanos = db.albuns.find({"artista":{"nome":artista_americano["nome"]}})
    for album in albuns_americanos:
        print('- '+album["nome"])