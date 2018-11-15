# Executar o paralelisador.

Dentro do diretório raiz do projeto.

make && make clean

cd paralelizador/ 
./paralelizador conjuntos.txt

# Inserir jsons na base de dados.

Dentro do diretório raiz do projeto.

cd scripts_tratamento/

python insere_dados.py  dados_2017/DADOS/conjuntos/[ARQUIVO].json

# Inserir multiplos arquivos de uma so vez na base.

Dentro do diretório raiz do projeto.

cd scripts_tratamento/

ls ../dados_2017/DADOS/conjuntos/part.*.json > conjuntos.txt

cat conjuntos.txt | xargs -n 1 -P 3 python insere_dados.py

-P 3: Número de processo rodando ao mesmo tempo.
