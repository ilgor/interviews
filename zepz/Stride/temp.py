class Node:
    def __init__(self, data: int = None, next: 'Node' = None) -> None:
        self.data = data
        self.next = next

    def add(self, data) -> 'Node':
        new_node = Node(data)

        current_node = self

        while (current_node.next != None):
            current_node = current_node.next

        current_node.next = new_node
        return self

    def __repr__(self) -> str:
        current_node = self
        result = ''

        while current_node is not None:
            result += f'{current_node.data}'

            if current_node.next is not None:
                result += ' --> '

            current_node = current_node.next

        return result


l = Node(1)
l.add(2).add(3)

print(l)
