# Discografia_MongoDB_Python
Exercício de criação e pesquisa em um banco de dados NoSQL usando Mongo DB e Python

O repositório tem dois arquivos.
O primeiro, "discografia.py", conecta o MongoDB e cria duas Collections no Database "discografia": "albuns" e "artistas"
O segundo arquivo, "consulta_discrografia.py", consulta a Collection "artistas" atrás dos artistas com o atributo "nacionalidade":"Estados Unidos".
A partir do resultado dessa consulta, a Collection "albuns" é consultada e retorna os albuns desses artistas.
O atributo "nome" de cada álbum é exibido na tela.
