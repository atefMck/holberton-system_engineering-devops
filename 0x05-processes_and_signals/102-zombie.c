#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
* infinite_while - creates an infinite loop
*
* Return: always 0 (success)
*/
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}

/**
* main - creates five zombie processes
*
* Return: status
*/
int main(void)
{
pid_t p;
int i;
for (i = 0; i < 5; i++)
{
p = fork();
if (p < 0)
fprintf(stderr, "Zombie process not created\n");
else if (p == 0)
exit(0);
printf("Zombie process created, PID: %d\n", p);
}
infinite_while();
return (0);
}
