#include "lists.h"

/**
 * check_cycle - check if list is cycle
 * @list: pointer to header of list
 * Return: return 0 if not or 1 if it is
 */

int check_cycle(listint_t *list)
{

	listint_t *p_check = list;
	listint_t *n_check = list;

	if (!list)
		return (0);
	while (p_check && n_check && n_check->next)
	{
		p_check = p_check->next;
		n_check = n_check->next->next;
		if (p_check == n_check)
			return (1);
	}
	return (0);
}
