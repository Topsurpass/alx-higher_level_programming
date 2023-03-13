#include <Python.h>

/**
 * print_python_list_info - function that prints some basic
 * info about Python lists
 * @p: the python object list
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, idx;
	PyListObject *list;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (idx = 0; idx < size; idx++)
	{
		list = (PyListObject *)p;
		printf("Element %ld: %s\n",
				idx, Py_TYPE(list->ob_item[idx])->tp_name);
	}
}
