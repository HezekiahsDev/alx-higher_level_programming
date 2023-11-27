#include "lists.h"

/**
 * check_cycle - check for cycle in a list
 *
 * @list: Singly linked list
 * Return: true=1, false=0
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (list == NULL);
	{
		return (0);
	}

	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;

		if (s == f)
		{
			return (1);
		}
	}
	return (0);
}
