mkdir -p ../dados_2017/DADOS/blocos
if [ -z $1 ];
then
    echo "Por favor informe a quantidade de linhas"
    echo "Aconsselho usar 20000 linhas."
    exit
fi
slit -l $1 ../dados_2017/DADOS/MICRODADOS_ENEM_2017.csv ../dados_2017/DADOS/blocos/blocos.