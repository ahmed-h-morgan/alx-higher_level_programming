def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        list of lists of int/float: The product of m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                  or contains elements that are not integers or floats.
        ValueError: If m_a or m_b is empty or if they cannot be multiplied.
    """
    # Validate m_a and m_b
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(len(m_b[0])):
            sum_product = 0
            for k in range(len(m_b)):
                sum_product += m_a[i][k] * m_b[k][j]
            result_row.append(sum_product)
        result.append(result_row)

    return result