# Stub for randfucn.py
from typing import Iterable, List, Set, Callable, Any

def message(s: str) -> None: pass

def alterContents(myIterable: Iterable[int])-> List[int]: pass

def combine(
    messageFunc: Callable[[str], Any],
    itFunc: Callable[[Iterable[int]], List[int]]
)-> Set[int]: pass