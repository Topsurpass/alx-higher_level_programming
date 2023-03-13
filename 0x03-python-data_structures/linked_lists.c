#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to the head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *copy;
	size_t i = 0;

	copy = h;

	while (copy != NULL)
	{
		printf("%d\n", copy->n);
		copy = copy->next;
		i++;
	}
	return (i);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new, *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		temp = *head;
		while (temp->next != NULL)
			temp = temp->next;
		temp->next = new;
	}
	return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *temp;

	while (head != NULL)
	{
		temp = head;
		head = head->next;
		free(temp);
	}
}

