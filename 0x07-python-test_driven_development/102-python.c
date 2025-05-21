#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p)
{
    printf("[.] string object info\n");

    // Check if the object is a string
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    // Check if the string is compact ASCII
    if (PyUnicode_IS_COMPACT_ASCII(p))
    {
        printf("  type: compact ascii\n");
    }
    else
    {
        printf("  type: compact unicode object\n");
    }

    // Get the length of the string
    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    printf("  length: %ld\n", length);

    // Convert the Python string to a UTF-8 C string
    const char *value = PyUnicode_AsUTF8(p);
    printf("  value: %s\n", value);
}
