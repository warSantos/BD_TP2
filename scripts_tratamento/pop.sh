ls ../dados_2017/DADOS/blocos/blocos.*.json | xargs -n 1 -P 2 python insere_dados.py
#ls ../dados_2017/DADOS/blocos/blocos.*.json | head -n 2 | xargs -n 1 -P 2 python insere_dados.py
