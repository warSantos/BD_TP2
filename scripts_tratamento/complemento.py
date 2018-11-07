from sys import argv

def get_file (path):
	with open (path, 'r') as content_file:
		content = content_file.read().split('\n')
		return content

complemento = set(get_file (argv[1])) - set(get_file (argv[2]))

for f in complemento:
	print f
