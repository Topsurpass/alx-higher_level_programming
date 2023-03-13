#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, idx;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (idx = 0; idx < size; idx++)
	{
		printf("Element %ld: %s\n",
		       idx,
		       (PY_TYPE(PyList_GetItem(p, idx)))->tp_name);
	}
}
