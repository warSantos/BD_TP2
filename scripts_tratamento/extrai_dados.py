# argv[1]: Arquivo com todos os atributos.
# argv[2]: Arquivo com os atributos escolhidos.
# argv[3]: Arquivo com dados para triagem.
from sys import argv

def ler_arquivo (path):
	try:
		with open (path, 'r') as content_file:
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
	#lista_atributos.pop()
	# Recebendo lista com os atributos utilizados.
	lista_at_ut = ler_arquivo (at_utilizados)
	#lista_at_ut.pop ()
	tipos = list()
	mascara = [0] * len (lista_atributos)
	cont = 0
	# Criando mascara de bit para identificar quais atributos
	# Serao levados.
	for a in lista_atributos:
		if a in lista_at_ut:
			mascara[cont] = 1
			tipos.append (a.split()[1])
		cont += 1
	return mascara, tipos

def extrair_dados (mascara, arquivo_dados):
	dados = ler_arquivo (arquivo_dados)
	dados_finais = list()
	atributo_id = [0] * len (mascara)
	for linha in dados:
		tokens = linha.split (';')
		cont = 0
		temp = list ()
		# Extraindo os valores dos atributos.
		while cont < len (mascara):
			# Selecionando os atributos marcados.
			if (mascara[cont] == 1):
				att = tokens[cont].replace('\n','').replace ('\r','')
				temp.append (att)
			cont += 1
		dados_finais.append (temp)
	return dados_finais

def constroi_json (dados, arquivo_atributos, tipos, prefixo):
	att_ut = ler_arquivo (arquivo_atributos)
	ptw_file = open (prefixo+'.json', 'w')
	for participante in dados:
		tupla = '{'
		for att, valor, tipo in zip (att_ut, participante, tipos):
			# Se for uma string.
			v_utf = valor.decode ('iso-8859-1').encode ('utf8')
			if (tipo == '0'):
				tupla += '"' + att.split ()[0] + '": "' + v_utf + '", '
			# Se for float ou int.
			else:
				tupla += '"' + att.split ()[0] + '": ' + v_utf + ', '
		tupla = tupla[:-1]
		tupla = tupla[:-1]
		tupla += '}\n'
		ptw_file.write (tupla)

if __name__=='__main__':

	mascara, tipos = criar_mascara (argv[1], argv[2])
	# Recebendo dados triados.
	dados = extrair_dados (mascara, argv[3])
	# Criando o arquivo json no formato do mongo.
	constroi_json (dados, argv[2], tipos, argv[3])
