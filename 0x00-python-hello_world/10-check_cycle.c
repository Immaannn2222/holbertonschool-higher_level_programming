#include "lists.h"
/**
 * check_cycle - checks if a list contains a  cycle or no
 * @list: a pointer to the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
listint_t *fir = list, *sec = list;
while (list && sec && sec->next)
{
fir = fir->next;
sec = sec->next->next;
if (fir == sec)
return (1);
}
return (0);
}
