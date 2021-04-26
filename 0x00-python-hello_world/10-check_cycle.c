#include "lists.h"

/**
 * check_cycle - check if linked list is looped
 * @list: list node to analyse from
 * Return: 0 if not looped, 1 vice versa
 */

int check_cycle(listint_t *list)
{
  listint_t *slow, *fast;

  slow = list;
  fast = list;
  while (slow && fast && fast->next)
    {
      slow = slow->next;
      fast = fast->next->next;
      if (slow == fast)
	return(1);
    }
  return(0);
}
