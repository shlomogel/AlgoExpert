from  linked_list import Node, LinkedList
import pytest

@pytest.fixture(autouse=True, params=[[], [1,2,3]])
def test_list(request) -> LinkedList:
    return LinkedList(nodes=request.param)


@pytest.fixture
def new_node(request)->list:
    return request.param

@pytest.fixture(params=[1,2,3])
def insert_node_data(request):
    return request.param

@pytest.mark.parametrize('new_node', [1, 0], indirect=True)
def test_add_first(test_list: LinkedList, new_node):
    previous_head = test_list.head
    new_node = Node(data=new_node)

    test_list.add_first(new_node)

    assert test_list.head == new_node
    assert new_node.next == previous_head

@pytest.mark.parametrize('new_node', [4, 5])
def test_add_last(test_list: LinkedList, new_node):
    new_node = Node(data=new_node)

    test_list.add_last(new_node)
    for n in test_list:
        pass
    assert n.data == new_node.data
    assert new_node.next == None

@pytest.mark.parametrize('new_node, insert_node_data', [(11,1), (22,2), (33,3)])
def test_add_after(test_list: LinkedList, new_node, insert_node_data):
    if test_list.head is None:
        with pytest.raises(Exception) as exeption_info:
            assert str(exeption_info.value) == "Empty List"

    else:
        test_list.add_after(new_node=Node(new_node), after=insert_node_data)
        assert test_list.exists(node=Node(new_node))

@pytest.mark.parametrize('new_node, insert_node_data', [(11,1), (22,2), (33,3)])
def test_add_before(test_list: LinkedList, new_node, insert_node_data):
    if test_list.head is None:
        with pytest.raises(Exception) as exeption_info:
            assert str(exeption_info.value) == "Empty List"

    else:
        test_list.add_before(new_node=Node(new_node), before=insert_node_data)
        assert test_list.exists(node=Node(new_node))

def test_remove_node(test_list: LinkedList, insert_node_data):
    if test_list.head is None:
        with pytest.raises(Exception) as exeption_info:
            assert str(exeption_info.value) == "Empty List"

    else:
        test_list.remove_node(insert_node_data)
        assert not test_list.exists(node=Node(new_node))

