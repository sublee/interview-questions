def count_islands(world, x, y):
    h = len(world)
    w = len(world[0])

    count = 0
    touched = set()
    for j in range(0, h):
        for i in range(0, w):
            if world[j][i] != 0:
                count += 1
                mark_world(world, i, j, touched)

    return count


def mark_world(world, x, y, touched):
    queue = []

    def enqueue(x, y):
        if not in_boundary(world, x, y):
            return
        if (x, y) in touched:
            return
        queue.append((x, y))
        touched.add((x, y))

    enqueue(x, y)
    while queue:
        i, j = queue.pop(0)
        if world[j][i] != 0:
            world[j][i] = 0
            enqueue(i - 1, j)
            enqueue(i + 1, j)
            enqueue(i, j - 1)
            enqueue(i, j + 1)


def in_boundary(world, x, y):
    h = len(world)
    w = len(world[0])

    return (0 <= x < w) and (0 <= y < h)


def test_1():
    world = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 1],
    ]
    assert count_islands(world, 0, 0) == 2


def test_2():
    world = [
        [1, 1, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 0],
    ]
    assert count_islands(world, 0, 0) == 5


def test_3():
    world = [
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
    ]
    assert count_islands(world, 0, 0) == 2
