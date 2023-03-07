#include "lists.h"
/**
 * insert_node - insert anumber into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: number to be inserted in singly linked list
 *
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *temp = NULL;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		(*head)->next = NULL;
		return (new);
	}
	if ((*head)->next == NULL)
	{
		if (new->n < (*head)->n)
		{
			new->next = *head;
			*head = new;
		}
		else
			(*head)->next = new;
		return (new);
	}
	temp = *head;
	while (temp->next != NULL)
	{
		if (new->n < temp->n)
		{
			new->next = temp;
			*head = new;
			return (new);
		}
		if (((new->n > temp->n) && (new->n < (temp->next)->n)) ||
				(new->n == temp->n))
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		temp = temp->next;
	}
	temp->next = new;
	return (new);
}
