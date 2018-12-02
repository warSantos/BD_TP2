#include "funcao.h"

char **get_paths (char *file, int *qtde_paths){
	
	FILE *leitor = fopen (file, "r");
	char path[SIZE_PATH];
	if (leitor == NULL){
		printf ("Arquivo %s não econtrado.\n", file);
		return NULL;
	}
	int qtde_lines = 0;
	while (fscanf(leitor, "%s", path)!=EOF){
		qtde_lines++;
	}
	fclose (leitor);
	char **paths = malloc (sizeof(char *) * qtde_lines);
	int cont;
	for (cont = 0; cont < qtde_lines; cont++){
		paths[cont] = malloc(SIZE_PATH);
	}
	leitor = fopen (file, "r");
	cont = 0;
	while (cont < qtde_lines){

		fscanf(leitor, "%s", paths[cont]);
		//printf ("%s\n", paths[cont]);
		cont++;
	}
	fclose (leitor);
	*qtde_paths = qtde_lines;
	return paths;
}

void run_command (void *file){
	
	char comando[2000];
	char *pypath = "python2 ../scripts_tratamento/extrai_dados.py ../metadados/todos_att_tipos.txt ../metadados/utilizados_att_tipos.txt ";
	sprintf (comando, "%s%s\n", pypath, (char *)file);
	system(comando);
	printf (comando, "\n");
	sprintf (comando, "done: %s", (char *)file);
	pthread_mutex_lock(&protect_num_thread);
	num_thread--;
	flush_disk("files_done.log", comando);
	pthread_mutex_unlock(&protect_num_thread);
	//pthread_exit((void *)NULL);
}

void flush_disk (char *file, char *data){
	
	FILE *ptw_file = fopen (file, "a");
	if (ptw_file == NULL){
		printf("Nao foi possivel abrir o arquivo %s.\n", file);
		return;
	}
	fprintf(ptw_file, "%s\n", data);
  	fclose (ptw_file);	
}

void function_test (void *file){
	
	//sleep (1);
	//printf("%s\n", (char *)file);
	pthread_mutex_lock(&protect_num_thread);
	num_thread--;
	//printf ("num_thread: %d\n", num_thread);
	pthread_mutex_unlock(&protect_num_thread);
	//pthread_exit((void *)NULL);
}


