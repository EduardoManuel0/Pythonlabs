from collections import deque
from typing import Any


class Stack:
    """A stack (LIFO) data structure based on list."""  # «стек»

    def __init__(self):
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        """Add an element to the top of the stack."""
        self._data.append(item)

    def pop(self) -> Any:
        """Removes the top element of the stack and returns it."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Any | None:
        """Returns the top element without removing it. Returns None if the stack is empty."""
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, otherwise False."""
        return len(self._data) == 0

    def __len__(self) -> int:
        """The number of elements in the stack."""
        return len(self._data)


class Queue:
    """A FIFO data structure based on collections.deque."""  # «очередь»

    def __init__(self):
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Add an item to the end of the queue."""
        self._data.append(item)

    def dequeue(self) -> Any:
        """
        Removes the left element from the front of the queue and returns it.
        \nIf the queue is empty, returns IndexError exception.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self) -> Any | None:
        """Returns the first element without removing it. Returns None if the queue is empty."""
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """Returns True if the queue is empty."""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Number of elements in the queue."""
        return len(self._data)


# --------------------------------------------------------------#
# ---------------------------TESTING----------------------------#
# --------------------------------------------------------------#


if __name__ == "__main__":
    # ----------------------LIFO---------------------------------#
    stack = Stack()
    print("\n===================================================================")
    print(f"1. Stack created: {stack}")
    print("===================================================================")

    print(f"   Empty? {stack.is_empty()}, Length: {len(stack)}, Top: {stack.peek()}")

    elements = [15, 30, 5, "Author", ["David", "Laurindo"]]
    for elem in elements:
        # Executing LIFO
        stack.push(elem)  # Adding new elements to the top of the list
        print(f"2. Added {elem}: {stack}")  # Showing added element
        print(f"   Upper: {stack.peek()}, Length: {len(stack)}")  # Element on the Top

    print(f"\n   Empty? {stack.is_empty()}, Length: {len(stack)}, Top: {stack.peek()}")

    print("\n3. Extract (LIFO order):")
    while not stack.is_empty():  # Extrating elements from the top of the list
        item = stack.pop()  # Extration
        print(f"   Extracted: {item}, Remaining: {len(stack)}, Top: {stack.peek()}")

    print(f"\n4. Result: {stack}, Empty? {stack.is_empty()}")

    # ----------------------FIFO---------------------------------#
    q = Queue()

    # FIFO Initialization
    print("\n===================================================================")
    print(f"1. Queue created: {q}")
    print("===================================================================")
    print(f"\n   Empty? {q.is_empty()}, Length: {len(q)}, First: {q.peek()}")

    # Adding elements
    elements = ["first", "second", "third", 1, 2, 3]
    for element in elements:
        q.enqueue(element)
        print(f"2. Added {element}: {q}")
        print(f"   Last in: {q.peek()}, Length: {len(q)}")

    # Extracting elements
    print("\n3. Extract (FIFO order):")
    while not q.is_empty():
        item = q.dequeue()
        print(f"   Extracted: {item}, Remaining: {len(q)}, First: {q.peek()}")

    # Result
    print(f"\n4. Result: {q}, Empty? {q.is_empty()}")