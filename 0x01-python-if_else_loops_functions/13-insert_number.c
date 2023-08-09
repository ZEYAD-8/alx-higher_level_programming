#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - adds a number into a sorted linked list
 * @head: the head of the sorted linked list from lowest to highest
 * @number: the number to add
 * Return: the address of the new node containing the number
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *previous;
	listint_t *new;

	current = *head;
	previous = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (current != NULL && number > current->n)
		{
			previous = current;
			current = current->next;
		}
		new->next = current;
		previous->next = new;
		return (new);
	}
}
