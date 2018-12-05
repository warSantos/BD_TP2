#argv[1]: arquivos com tuplas no formato JSON.
from sys import argv, exit
import pymongo, yaml

def ler_arquivo (path):
	lista = list()
	try:
		with open (path, 'r') as content_file:
			content = content_file.read().split('\n')
			content.pop()
			for t in content:
				lista.append (yaml.load (t))
			return lista
			#return content
	except Exception as e:
		print 'Erro ao abrir arquivo: ', e
		exit (1)

def inserir_dados (arquivos_json):
	# Carregando JSON
	tuplas = ler_arquivo (arquivos_json)
	# Conectando ao MongoDB
	cliente = pymongo.MongoClient ("mongodb://localhost:27017/")
	banco = cliente["enem"]
	# Inserindo dados no banco.
	colecao = banco["enem_participant"]
	retorno = colecao.insert_many (tuplas)

if __name__=='__main__':
	inserir_dados (argv[1])
