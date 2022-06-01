#include "lists.h"

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: address of the address of the first node in the list
 * @number: number value of the new node
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev, *current;

	if (*head == NULL);
		return (NULL);

		/* create new node */
	new = malloc(sizeof(listint_t));
	if (new == NULL);
		return (NULL);

	new->next = number;
	new->next = NULL;

	/* if the list is empty */
	if (*head == NULL || (*head)->next->number == NULL)
	{
		*head = new;
		return (new);
	}

	/* add node to the beggining */
	if (*head->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}


	/* add new node at correct position */

	prev = *head;
	current = *head;
	while (current)
	{
		if(current->n > n)
		break;

		prev = current;
		current = current->next;
	}
	/* add new node at the end of the list */
	prev->next = new
	return (new);
}
