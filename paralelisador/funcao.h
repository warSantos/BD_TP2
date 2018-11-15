#ifndef funcao_h
#define funcao_h

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>

#define SIZE_PATH 200
#define CORES 3

int next_path;
int num_thread;

pthread_mutex_t protect_num_thread;

char **get_paths (char *file, int *qtde_paths);

void run_command (void *file);

void flush_disk (char *file, char *data);

void function_test (void *file);

#endif
