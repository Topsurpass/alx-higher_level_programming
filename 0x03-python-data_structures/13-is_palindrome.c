#include "lists.h"

/**
 * listint_size - get the length of the singly linked list
 * @h: the head node of the linked list
 *
 * Return: the length of the singly linked list
 */
int listint_size(const listint_t *h)
{
	const listint_t *current;
	int count = 0;

	current = h;

	while (current != NULL)
	{
		current = current->next;
		count++;
	}
	return (count);
}
/**
 * compare_arr - compare 2 arrays of int to check if the same
 * @arr1: the first array
 * @arr2: the second array
 * @len: length of arr1
 *
 * Return: 0 if not the same and 1 if the same
 */
int compare_arr(int *arr1, int *arr2, int len)
{
	int i, equal;

	equal = 1;

	for (i = 0; i < len; i++)
	{
		if (arr1[i] != arr2[i])
		{
			equal = 0;
			break;
		}
	}
	return (equal);
}

/**
 * is_palindrome - check if linked list is palidrome
 * @head: head node of the linked list
 *
 * Return: 0 if not a palindrome and 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i, j, arr1[10240], arr2[10240], len;

	/* if linked list is empty */
	if (*head == NULL)
		return (1);
	/* if linked list does not exist */
	if (head == NULL)
		return (0);

	len = listint_size(*head);
	current = *head;

	/* loop through the linked list and save each value of n in an array */
	i = 0;
	while (current != NULL)
	{
		arr1[i] = current->n;
		current = current->next;
		i++;
	}
	/* loop through the arr1 from the end and save in arr2 */
	for (j = 0; j < len; j++)
		arr2[j] = arr1[len - 1 - j];
	return (compare_arr(arr1, arr2, len));
}
