CC:=gcc
CFLAGS:= -c -Wall -g -O3

paralelisador:	main.o	funcao.o
	$(CC) main.o funcao.o -lpthread -o paralelizador

main.o:	main.c
	$(CC) $(CFLAGS) main.c

funcao.o:	funcao.c	funcao.h
	$(CC) $(CFLAGS) funcao.c

clean:
	rm -rf *.o
