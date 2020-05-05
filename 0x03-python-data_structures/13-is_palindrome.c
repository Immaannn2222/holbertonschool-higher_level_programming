#include "lists.h"
/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: pointer to the head
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
listint_t *tmp;
int i = 0, j = 0;
char *s = NULL;
if (*head == NULL)
return (1);
tmp = *head;
while (tmp != NULL)
{
s[i] = tmp->n;
i++;
tmp = tmp->next;
}
i--;
while (j < i)
{
if (s[j] == s[i])
{
j++;
i--;
}
else
return (0);
}
return (1);
}