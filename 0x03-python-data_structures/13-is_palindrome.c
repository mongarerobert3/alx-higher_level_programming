#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * is_palindrome - check if number is palindrome
 * @head - pointer to a pointer of the first node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int arr[1024];
	int i, n = 0;
	listint_t *trav;

	if (head == NULL)
		return (0);

	/* copy the numbers to the aray */
	trav = *head;
	while (trav)
	{
		arr[n++] = trav->n;
		trav = trav->next;
	}

	 /* check palindrome */
	for (i = 0; i < n / 2; i++)
	{
		if (arr[i] != arr[n - i - 1])
			return (0);
	}
	return (1);
}
