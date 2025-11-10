from main import AVL, Node


def test_create_empty_tree():
    avl = AVL()
    assert avl.root is None
    assert avl.get_height() == 0
    assert avl.inorder() == []


def test_create_node():
    node = Node(10)
    assert node.key == 10
    assert node.left is None
    assert node.right is None
    assert node.height == 1


def test_insert_single_element():
    avl = AVL()
    avl.insert(10)
    assert avl.root.key == 10
    assert avl.get_height() == 1
    assert avl.inorder() == [10]


def test_insert_multiple_elements():
    avl = AVL()
    keys = [10, 20, 30, 40, 50]
    for key in keys:
        avl.insert(key)

    assert avl.inorder() == [10, 20, 30, 40, 50]
    assert avl.is_balanced()


def test_insert_maintains_balance():
    avl = AVL()
    for i in range(1, 8):
        avl.insert(i)
        assert avl.is_balanced(), f"Дерево не сбалансировано после вставки {i}"


def test_insert_duplicate():
    avl = AVL()
    avl.insert(10)
    avl.insert(20)
    avl.insert(10)

    assert avl.inorder() == [10, 20]


def test_insert_left_left_case():
    avl = AVL()
    avl.insert(30)
    avl.insert(20)
    avl.insert(10)

    assert avl.root.key == 20
    assert avl.root.left.key == 10
    assert avl.root.right.key == 30
    assert avl.is_balanced()


def test_insert_right_right_case():
    avl = AVL()
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)

    assert avl.root.key == 20
    assert avl.root.left.key == 10
    assert avl.root.right.key == 30
    assert avl.is_balanced()


def test_insert_left_right_case():
    avl = AVL()
    avl.insert(30)
    avl.insert(10)
    avl.insert(20)

    assert avl.root.key == 20
    assert avl.root.left.key == 10
    assert avl.root.right.key == 30
    assert avl.is_balanced()


def test_insert_right_left_case():
    avl = AVL()
    avl.insert(10)
    avl.insert(30)
    avl.insert(20)

    assert avl.root.key == 20
    assert avl.root.left.key == 10
    assert avl.root.right.key == 30
    assert avl.is_balanced()


# Тесты поиска
def test_search_existing_element():
    avl = AVL()
    keys = [10, 20, 30, 40, 50]
    for key in keys:
        avl.insert(key)

    for key in keys:
        assert avl.search(key)


def test_search_non_existing_element():
    avl = AVL()
    keys = [10, 20, 30]
    for key in keys:
        avl.insert(key)

    assert not avl.search(100)
    assert not avl.search(5)


def test_search_empty_tree():
    avl = AVL()
    assert not avl.search(10)


# Тесты удаления
def test_delete_leaf_node():
    avl = AVL()
    keys = [20, 10, 30]
    for key in keys:
        avl.insert(key)

    avl.delete(10)
    assert avl.inorder() == [20, 30]
    assert not avl.search(10)
    assert avl.is_balanced()


def test_delete_node_with_one_child():
    avl = AVL()
    keys = [20, 10, 30, 25]
    for key in keys:
        avl.insert(key)

    avl.delete(30)
    assert avl.inorder() == [10, 20, 25]
    assert avl.is_balanced()


def test_delete_node_with_two_children():
    avl = AVL()
    keys = [20, 10, 30, 5, 15, 25, 35]
    for key in keys:
        avl.insert(key)

    avl.delete(20)
    assert 20 not in avl.inorder()
    assert avl.is_balanced()


def test_delete_root():
    avl = AVL()
    keys = [20, 10, 30]
    for key in keys:
        avl.insert(key)

    avl.delete(20)
    assert avl.root.key in [10, 30]
    assert avl.is_balanced()


def test_delete_maintains_balance():
    avl = AVL()
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        avl.insert(key)

    avl.delete(10)
    assert avl.is_balanced()

    avl.delete(50)
    assert avl.is_balanced()


def test_delete_non_existing_element():
    avl = AVL()
    keys = [10, 20, 30]
    for key in keys:
        avl.insert(key)

    initial_inorder = avl.inorder()
    avl.delete(100)
    assert avl.inorder() == initial_inorder


def test_delete_from_empty_tree():
    avl = AVL()
    avl.delete(10)
    assert avl.root is None


def test_delete_all_elements():
    avl = AVL()
    keys = [10, 20, 30]
    for key in keys:
        avl.insert(key)

    for key in keys:
        avl.delete(key)

    assert avl.root is None
    assert avl.inorder() == []

def test_height_single_node():
    avl = AVL()
    avl.insert(10)
    assert avl.get_height() == 1


def test_height_multiple_nodes():
    avl = AVL()
    keys = [10, 20, 30, 40, 50]
    for key in keys:
        avl.insert(key)

    assert avl.get_height() <= 3


def test_balance_after_multiple_operations():
    avl = AVL()

    for i in range(1, 20):
        avl.insert(i)

    assert avl.is_balanced()

    for i in range(1, 10):
        avl.delete(i)

    assert avl.is_balanced()


def test_large_tree():
    avl = AVL()
    keys = list(range(1, 101))

    for key in keys:
        avl.insert(key)

    assert len(avl.inorder()) == 100
    assert avl.is_balanced()

    for key in keys:
        assert avl.search(key)


def test_random_operations():
    avl = AVL()

    avl.insert(50)
    avl.insert(25)
    avl.insert(75)
    avl.insert(10)
    avl.insert(30)
    avl.insert(60)
    avl.insert(80)

    assert avl.is_balanced()
    assert len(avl.inorder()) == 7

    avl.delete(25)
    assert avl.is_balanced()
    assert not avl.search(25)

    avl.delete(75)
    assert avl.is_balanced()
    assert not avl.search(75)

    for key in [50, 10, 30, 60, 80]:
        assert avl.search(key)
