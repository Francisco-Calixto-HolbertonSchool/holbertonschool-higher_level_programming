#include "lists.h"

/**
 * is_palindrome - entry point
 * @head: head
 * Return: 1 or 0
 */

int is_palindrome(listint_t **head)
{
  listint_t *temp, *aux, *half;
  int *a_1, *a_2, n, j, t, c, h;

  if (!*head || !head)
    return (1);
  aux = *head;
  for (n = 1; aux->next; n++)
    aux = aux->next;
  half = *head;
  for (h = 0; h < ((n + 1) / 2); h++)
    half = half->next;
  a_1 = malloc(sizeof(int) * (n / 2));
  if (!a_1)
    return (-1);
  a_2 = malloc(sizeof(int) * (n / 2));
  if (!a_2)
    return (-1);
  temp = *head;
  for (t = 0; t < (n / 2); t++)
    {
      a_1[t] = temp->n;
      temp = temp->next;
    }
  for (j = ((n / 2) - 1); j >= 0; j--)
    {
      a_2[j] = half->n;
      half = half->next;
    }
  for (c = 0; c < (n / 2); c++)
    {
      if (a_1[c] != a_2[c])
	{
	  free(a_1);
	  free(a_2);
	  return (0);
	}
    }
  free(a_1);
  free(a_2);
  return (1);
}
