#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: the head address of the linked list
 * Return: 1 if it's a palindrome, else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *c = *head;
	int t[2048], i = 0, j = 0;

	if (*head)
	{
		while (c)
		{
			t[i] = c->n;
			c = c->next;
			i++;
		}

		while (j < i / 2)
		{
			if (t[j] == t[i - j - 1])
				j++;
			else
				return (0);
		}
	}
	return (1);
}
