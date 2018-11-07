from sys import argv
import io

def ler_arquivo (path):
	try:
		with open (path, 'r') as content_file:
			content = content_file.read().split('\n')
			content.pop()
			return content
	except Exception as e:
		print 'Erro ao abrir arquivo: ', e
		exit (1)

def ler_arquivo_utf (path):
	try:
		with io.open (path, encoding='utf-8') as content_file:
			content = content_file.read().split('\n')
			content.pop()
			return content
	except Exception as e:
		print 'Erro ao abrir arquivo: ', e
		exit (1)


# Cria mascara binaria de atributos utilizados.
def criar_mascara (atributos, at_utilizados):
	# Recebendo lista com todos os atributos.
	lista_atributos = ler_arquivo (atributos)
	# Recebendo lista com os atributos utilizados.
	lista_at_ut = ler_arquivo (at_utilizados)
	mascara = [0] * len (lista_atributos)
	cont = 0
	# Criando mascara de bit para identificar quais atributos
	# Serao levados.
	for a in lista_atributos:
		if a in lista_at_ut:
			mascara[cont] = 1
		cont += 1
	return mascara

def extrair_dados (mascara, arquivo_dados):
	dados = ler_arquivo (arquivo_dados)
	dados_finais = list()
	for linha in dados:
		tokens = linha.split (';')
		cont = 0
		temp = list ()
		# Extraindo os valores dos atributos.
		while cont < len (mascara):
			# Selecionando os atributos marcados.
			if (mascara[cont] == 1):
				att = tokens[cont].replace('\n','').replace ('\r','')
				try:
					temp.append (att)#.iencode ('ascii'))
				except Exception as e:
					print e
					pass
			cont += 1
		dados_finais.append (temp)
	return dados_finais

if __name__=='__main__':
	dados = extrair_dados (criar_mascara (argv[1], argv[2]), argv[3])
	cont = 0
	for l in dados:
		print l
