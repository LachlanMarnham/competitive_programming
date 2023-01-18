class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def add_node_to_list(linked_list, node):
    linked_list.insert_node(node.data)
    return node.next


def merge_lists(head1, head2):
    list_3 = SinglyLinkedList()
    node_1, node_2 = head1, head2
    while True:
        if node_1 is not None:
            if node_2 is not None:
                if node_1.data < node_2.data:
                    node_1 = add_node_to_list(list_3, node_1)
                else:
                    node_2 = add_node_to_list(list_3, node_2)
            else:
                node_1 = add_node_to_list(list_3, node_1)
        elif node_2 is not None:
            node_2 = add_node_to_list(list_3, node_2)
        else:
            break
    return list_3.head
