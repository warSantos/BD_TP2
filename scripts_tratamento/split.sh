mkdir -p ../dados_2017/DADOS/blocos
if [ -z $1 ];
then
	echo "Por favor informe a quantidade de linhas que devem ter cada bloco."
	echo "Aconselho usar 20000 linhas."
	exit
fi
split -l  $1 ../dados_2017/DADOS/MICRODADOS_ENEM_2017.csv ../dados_2017/DADOS/blocos/blocos.
