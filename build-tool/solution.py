class Node(object):

    def __init__(self, name):
        self.name = name
        self.is_leaf = False
        self.children = {}


def build(paths):
    head = Node('')
    for path in paths:
        node = head
        for name in path.split('/')[1:]:
            if name in node.children:
                node = node.children[name]
            else:
                child = Node(name)
                node.children[name] = child
                node = child
        node.is_leaf = True

    return head


def traverse(node, prev=[], depth=0):
    if node.is_leaf:
        yield '/'.join(prev + [node.name])
    else:
        for key, child in node.children.items():
            for x in traverse(child, prev + [node.name], depth + 1):
                yield x


def test_traverse():
    paths = [
        '/a/b/c',
        '/a/b/d',
        '/a/b',
        '/c',
        '/c',
    ]

    result = list(traverse(build(paths)))
    assert result == ['/a/b', '/c']
