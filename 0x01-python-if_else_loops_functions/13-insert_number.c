#include "lists.h"
/**
 * insert_node - insert a number
 * @head: list head
 * @number: number to stor
 * return:pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *runner;
	listint_t *new;

	runner = *head;

	new = mlloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new-> = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return(new);
	}
	while(runner->next != NULL)
	{
		if ((runner->next)->n >= number)
		{
			new->next = runner->next;
			runner->next = new;
			return(new);
		}
		runner = runner->next;
	}
	new->next = NULL;
	runner->next = new;
	return(new);
}
