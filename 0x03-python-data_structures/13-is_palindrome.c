#include "lists.h"
/**
 * is_palindrome -  check if a singly linked is a palindrome
 * @head: pointer to the head
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
listint_t *tmp;
int len = 0, i = 0;
char buffer[5000];
if (*head == NULL)
return (1);
tmp = *head;
	while (tmp != NULL)
	{
		buffer[len] = tmp->n;
	 len++;
		tmp = tmp->next;
	}
len--;
while (i < len)
{
if (buffer[i] == buffer[len])
{
i++;
len--;
}
else
return (0);
}
return (1);
}
