#include "lists.h"
/**
 * is_palindrome - check if a signly linked list is a palindrome
 * @head: the head
 *
 * Return: 0 if it is not a palidrome or 1 if it is.
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

}

void reverse(struct Node** head_ref)
{
	struct Node* prev = NULL;
	struct Node* current = *head_ref;
	struct Node* next;
	while (current != NULL) {
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head_ref = prev;
}
