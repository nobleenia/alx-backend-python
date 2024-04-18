from typing import TypeVar, Mapping, Any, Union

# Define a TypeVar T, which can be any type or None
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[T, Any]:
    """
    Retrieves a value from a dictionary based on the provided key. If the key does not exist,
    returns a default value.

    Parameters:
    dct (Mapping): The dictionary from which to retrieve the value.
    key (Any): The key for which to look up the value.
    default (Union[T, None], optional): The default value to return if the key is not found. Defaults to None.

    Returns:
    Union[T, Any]: The value associated with the key if found; otherwise, the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
