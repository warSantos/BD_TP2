#include "funcao.h"

int main (int argc, char **argv){
	
	// recebendo o caminho dos aruqivos a serem processados.
	int qtde_paths;
	char **paths = get_paths (argv[1], &qtde_paths);
	
	// Disparando threads.
	pthread_mutex_init(&protect_num_thread, NULL);
	num_thread = 0;
	next_path = 0;
	pthread_t tid[qtde_paths];
	while (next_path < qtde_paths){
		// se a variável num_thread não estiver sendo usada.
		pthread_mutex_lock(&protect_num_thread);
		// se o numero de thread estiver igual ao de cores, então durma.
		if (num_thread == CORES){
			pthread_mutex_unlock(&protect_num_thread);
			sleep(5);
		}else{// se o número de threads estiver inferior ao de cores, crie mais uma.	
			num_thread++;
//printf("%d - %d\n", next_path + 1, qtde_paths);
			pthread_mutex_unlock(&protect_num_thread);
			pthread_create (&(tid[next_path]), NULL, (void *)&run_command, (void *)paths[next_path]);
			next_path++;
		}
	}
	// Esperando o término das threads.
	printf ("Término de disignação dos arqivos.\n");
	int cont;
	for (cont = 0; cont < qtde_paths; cont++){
		pthread_join(tid[cont], NULL);
	}
	pthread_mutex_destroy(&protect_num_thread);
	return 0;
}
