from typing import Any, Optional, Iterator


class Node:
    """Singly linked list node."""

    def __init__(self, value: Any, next: Optional["Node"] = None):
        self.value = value 
        self.next = next

    def __repr__(self) -> str:
        """A string representation of the node as [value]."""
        return f"[{self.value}]"


class SinglyLinkedList:
    """Singly linked list."""

    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None  # to speed up append
        self._size: int = 0

    def append(self, value: Any) -> None:
        """Add an element to the end of a list in O(1) time using tail."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            assert (
                self.tail is not None
            )  # Type checker: tail is not None when head is not None
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, value: Any) -> None:
        """Add an element to the beginning of a list in O(1)."""
        new_node = Node(value, next=self.head)
        self.head = new_node

        # If the list was empty, update tail
        if self.tail is None:
            self.tail = new_node

        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        """Insert an element at index idx."""
        # Checking the index correctness
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size}]")

        # Insert at the beginning
        if idx == 0:
            self.prepend(value)
            return

        # Вставка в конец
        if idx == self._size:
            self.append(value)
            return

        # Middle insert
        assert (
            self.head is not None
        )  # Type checker: head is not None when inserting in middle
        current = self.head
        for _ in range(idx - 1):
            assert (
                current.next is not None
            )  # Type checker: current.next is not None during traversal
            current = current.next

        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1

    def remove(self, value: Any) -> bool:
        """Removes the first occurrence of value. Returns True if the element was removed."""
        if self.head is None:
            return False

        # Delete from the beginning
        if self.head.value == value:
            self.head = self.head.next
            # If the list becomes empty, update tail
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True

        # Finding an element to delete
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                # Delete the element
                current.next = current.next.next
                # If the last element was deleted, update tail
                if current.next is None:
                    self.tail = current
                self._size -= 1
                return True
            current = current.next

        return False

    def remove_at(self, idx: int) -> Any:
        """Removes the element at index idx and return its value."""
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size - 1}]")

        assert self._size > 0  # Type checker: size > 0 means head is not None
        assert self.head is not None  # Type checker: head is not None when size > 0

        # Deletation from the beginning
        if idx == 0:
            value = self.head.value
            self.head = self.head.next
            # If the list becomes empty, update tail
            if self.head is None:
                self.tail = None
            self._size -= 1
            return value

        # Removal from the middle or end
        current = self.head
        for _ in range(idx - 1):
            assert (
                current.next is not None
            )  # Type checker: current.next is not None during traversal
            current = current.next

        assert (
            current.next is not None
        )  # Type checker: current.next is not None for removal
        value = current.next.value
        current.next = current.next.next

        # If the last element was deleted, update tail
        if current.next is None:
            self.tail = current

        self._size -= 1
        return value

    def __iter__(self) -> Iterator[Any]:
        """An iterator over the values ​​in a list (from head to tail)."""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        """The number of elements in the list."""
        return self._size

    def __repr__(self) -> str:
        """String representation of the list in constructor format."""
        values = list(self)
        return f"SinglyLinkedList({values})"

    def visualize(self) -> str:
        """A nice visual representation of the list: [A] -> [B] -> [C] -> None"""
        if self.head is None:
            return "None"

        result_parts = []
        current = self.head

        while current is not None:
            result_parts.append(f"{current}")  # используем __repr__ Node
            current = current.next

        result_parts.append("None")
        return " -> ".join(result_parts)

    def __str__(self) -> str:
        """String representation with nice visualization of relationships."""
        return self.visualize()


if __name__ == "__main__":
    lst = SinglyLinkedList()

    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(f"\nAfter append: {lst}")
    print(f"Nice output: {str(lst)}")

    lst.prepend(0)
    print(f"\nAfter prepend: {lst}")
    print(f"Nice output: {str(lst)}")

    lst.insert(2, 1.5)
    print(f"\nAfter insert(2, 1.5): {lst}")
    print(f"Nice output: {str(lst)}")

    lst.remove(1.5)
    print(f"\nAfter remove(1.5): {lst}")
    print(f"Nice output: {str(lst)}")

    removed = lst.remove_at(1)
    print(f"\nУдалён элемент: {removed}")
    print(f"После remove_at(1): {lst}")
    print(f"Красивый вывод: {str(lst)}")

    letters = SinglyLinkedList()
    letters.append("A")
    letters.append("B")
    letters.append("C")
    print(f"\nСписок букв: {str(letters)}")  # List of letters