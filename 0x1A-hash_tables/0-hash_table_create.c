#include "hash_tables.h"
/**
 * hash_table_create - Creates a hash table
 * @size: Size of hash Table array
 *
 * Return: pointer to the hash table
*/
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *table;
	hash_node_t *bucket;


	table = malloc(sizeof(hash_table_t));
	if (table == NULL)
	{
		return (NULL);
	}

	bucket = malloc(sizeof(hash_node_t) * size);
	if (bucket == NULL)
	{
		free(table);
		return (NULL);
	}
	table->size = size;
	table->array = &bucket;
	return (table);
}
