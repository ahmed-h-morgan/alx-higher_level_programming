import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy
    
    Args:
        m_a: First matrix (list of lists)
        m_b: Second matrix (list of lists)
    
    Returns:
        The resulting matrix as a numpy array
    
    Raises:
        ValueError: If matrices cannot be multiplied
        TypeError: If inputs are not valid matrices
    """
    try:
        result = np.matmul(m_a, m_b)
        return result
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
    except Exception as e:
        raise TypeError(str(e)) from e
