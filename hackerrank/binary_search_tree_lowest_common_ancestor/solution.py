class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def get_anscestors(root, v):
    anscestors = [root]
    node = root
    while True:
        # If v1 is a descendent of v2, then v2 is the LCA.
        # This isn't usually what anscestor means, but ok...
        anscestors.append(node)
        if v == node.info:
            break
        if v > node.info:
            node = node.right
        else:
            node = node.left
    return anscestors


def lca(root, v1, v2):
    v1_anscestors = get_anscestors(root, v1)
    v2_anscestors = get_anscestors(root, v2)

    # We created each list of anscestors by appending
    # (to the right). Therefore, the LCA will be the last
    # item in v1_ancestors which is common to both, so
    # we traverse the list backwards.
    for node in reversed(v1_anscestors):
        if node in v2_anscestors:
            return node
