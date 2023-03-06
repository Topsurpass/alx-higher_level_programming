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

	prev = fwrd = head;

	while (prev != NULL && fwrd != NULL)
	{
		prev = prev->next;
		fwrd = fwrd->next->next;

		if (prev == fwrd)
			return (1);
	}
	return (0);
}
