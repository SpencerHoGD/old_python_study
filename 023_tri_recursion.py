def tri_recursion(k):
    """learn recursion from w3c
    https://www.w3schools.com/python/python_functions.asp
    """
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("Recursion Example Results:")
tri_recursion(6)
