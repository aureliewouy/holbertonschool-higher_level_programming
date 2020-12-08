#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the head of the list
 * @number: the number to insert
 *
 * Return: a listint_t
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while ((temp->next != NULL) && (temp->next->n < number))
	{
		temp = temp->next;
	}
	new->next = temp->next;
	temp->next = new;
	return (new);
}
