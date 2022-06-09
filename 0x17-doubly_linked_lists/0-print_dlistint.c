#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * print_dlistint - prints the doubly linked lists
 * @h: pointer to the header in which previous is null
 * 
 * Return: the number of nodes 
 */

size_t print_dlistint(const dlistint_t *h)
{
    int count = 0;

    while (h != NULL)
    {
        printf("%d\n", h->n);
        count++;
        h = h->next;
    }
    return (count);  
}