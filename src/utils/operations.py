from typing import (Union, Optional)


def divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    try:
        return a / b
    except ZeroDivisionError:
        return None
