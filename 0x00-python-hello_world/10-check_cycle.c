#include "lists.h"

/**
 * check_cycle - Check if a singly list has a cycle in it or loop
 * @head: Pointer to head of list
 *
 * Return: 1 (if there's a cycle) and 0 (if there's no cycle)
 */

int check_cycle(listint_t *head)
{
	listint_t *prev, *fwrd;

	if (head == NULL)
		return (0);

	prev = fwrd = head;

	while (1)
	{
		if (fwrd->next != NULL && fwrd->next->next != NULL)
		{
			fwrd = fwrd->next->next;
			prev = prev->next;
			if (prev == fwrd)
				return (1);
		}
		else
			return (0);

	}
}
