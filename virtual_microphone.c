#include <Python.h>

static PyObject* add(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }
    return PyLong_FromLong(a + b);
}

static PyMethodDef SimpleMethods[] = {
    {"add",  add, METH_VARARGS, "Add two numbers"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef simplemodule = {
    PyModuleDef_HEAD_INIT,
    "simple",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    SimpleMethods
};

PyMODINIT_FUNC PyInit_simple(void) {
    return PyModule_Create(&simplemodule);
}
