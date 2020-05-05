#include "lists.h"
/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: pointer to the head
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
listint_t *ptr0;
listint_t *ptr1;
listint_t *ptr2;
ptr0 = NULL;
ptr2 = NULL;
ptr1 = *head;
if (*head == NULL)
return (1);
while (ptr1 != NULL)
{
ptr2 = ptr1->next;
ptr1->next = ptr0;
ptr0 = ptr1;
ptr1 = ptr2;
}
*head = ptr0;
while (ptr1  && ptr0)
{
if (ptr0->n == ptr1->n)
{
ptr0 = ptr0->next;
ptr1 = ptr1->next;
}
else
return (0);
}
if (ptr0 == NULL && ptr1 == NULL)
return (1);
return (1);
}
