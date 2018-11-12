# argv[1]: Arquivo com todos os atributos.
# argv[2]: Arquivo com os atributos escolhidos.
# argv[3]: Arquivo com dados para triagem.
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
	utfex = 0
	linhas_ex = 0
	atributo_id = [0] * len (mascara)
	for linha in dados:
		tokens = linha.split (';')
		cont = 0
		temp = list ()
		excecao = False
		# Extraindo os valores dos atributos.
		while cont < len (mascara):
			# Selecionando os atributos marcados.
			if (mascara[cont] == 1):
				try:
					att = tokens[cont].replace('\n','').replace ('\r','').encode ('ascii')
					temp.append (att)#.iencode ('ascii'))
				except Exception as e:
					excecao = True
					utfex += 1
					atributo_id[cont] += 1
					#break
			cont += 1
		# Se nao ocorrerem excecoes.
		if (not excecao):
			dados_finais.append (temp)
		else:
			linhas_ex += 1
	return dados_finais, utfex, linhas_ex, atributo_id

if __name__=='__main__':
	dados, utfex, linhas_ex, att = extrair_dados (criar_mascara (argv[1], argv[2]), argv[3])
	cont = 0
	print 'Qtde de excecoes: ', utfex
	print 'Qtde de linhas excedidas: ', linhas_ex
	j = 0
	for i in att:
		print 'Atributo: ', j, ' - ', i
		j += 1
