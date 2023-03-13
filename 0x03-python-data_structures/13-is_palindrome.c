#include "lists.h"

/**
 * is_palindrome - check if singly linked list is a palindrome
 * @head: pointer to head of singly linked list
 *
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;

	temp = *head;
	int len = 0, i = 0;
	int data[12000];

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);

	while (temp != NULL)
	{
		temp = temp->next;
		len += 1;
	}
	if (len == 1)
		return (1);

	temp = *head;
	/* loop linked list and add its value in an array */
	while (temp)
	{
		data[i++] = temp->n;
		temp = temp->next;
	}
	/* loop d array and compare 1st half of the arr length to 2nd half */
	for (i = 0; i <= (len / 2); i++)
	{
		if (data[i] != data[len - i - 1])
			return (0);
	}
	return (1);
}
