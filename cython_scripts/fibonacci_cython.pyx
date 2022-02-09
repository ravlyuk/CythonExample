import cython

cpdef long test(long n, int repeat):
    cdef long i
    cdef long j
    cdef long f1 = 1
    cdef long f2 = 1
    for i in range(repeat):
        f1 = f2 = 1
        for j in range(n - 2):
            f1, f2 = f2, f1 + f2
    return f2
