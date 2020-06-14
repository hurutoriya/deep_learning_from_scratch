"""
    [summary] Chapter 2. 
    > poetry run python chap2.py 
"""

import numpy as np


def AND_nobias(x1: int, x2: int) -> int:
    """
    [summary] AND operator wituout bias term

    Args:
        x1 (int): 1st input for AND
        x2 (int): 2nd input for AND

    Returns:
        int: result of AND operator
    """

    (w1, w2, theta) = (0.5, 0.5, 0.7)
    tmp = w1 * x1 + w2 * x2
    if tmp <= theta:
        return 0
    else:
        return 1


def AND(x1: int, x2: int) -> int:
    """
    [summary] AND operator using bias term

    Args:
        x1 (int): 1st input for AND
        x2 (int): 2nd input for AND

    Returns:
        int: result of AND operator
    """

    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    # bias works as thetresold
    if tmp <= 0:
        return 0
    else:
        return 1


def NAND(x1: int, x2: int) -> int:
    """
    [summary] NAND Operator

    Args:
        x1 (int): 1st input 
        x2 (int): 2md input

    Returns:
        int: output of NAND
    """

    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1: int, x2: int) -> int:
    """
    [summary] OR Operator

    Args:
        x1 (int): 1st input
        x2 (int): 2nd input

    Returns:
        int: output of OR operator
    """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.1
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def XOR(x1: int, x2: int) -> int:
    """
    [summary] XOR operator

    Args:
        x1 (int): 1st input
        x2 (int): 2nd input

    Returns:
        int: output of XOR
    """
    return AND(NAND(x1, x2), OR(x1, x2))


if __name__ == "__main__":
    # check AND operator
    assert AND(0, 0) == 0
    assert AND(0, 1) == 0
    assert AND(1, 0) == 0
    assert AND(1, 1) == 1

    # check NAND operator
    assert NAND(0, 0) == 1
    assert NAND(0, 1) == 1
    assert NAND(1, 0) == 1
    assert NAND(1, 1) == 0

    # check OR operator
    assert OR(0, 0) == 0
    assert OR(0, 1) == 1
    assert OR(1, 0) == 1
    assert OR(1, 1) == 1

    # check XOR operator
    assert XOR(0, 0) == 0
    assert XOR(0, 1) == 1
    assert XOR(1, 0) == 1
    assert XOR(1, 1) == 0
