#include "lists.h"
/**
 * insert_node - adds a number into a sorted linked list
 * @head: the head of the sorted linked list
 * @number: the number to add
 * Return: the address of the new node containing the number
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *previous;
	listint_t *new;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	else
	{
		while (current->next != NULL)
		{
			if (number > current->n)
			{
				previous = current;
				current = current->next;
				continue;
			}
			new->next = current;
			previous->next = new;
			return (new);
		}
		current->next = new;
		return (new);
	}
}
