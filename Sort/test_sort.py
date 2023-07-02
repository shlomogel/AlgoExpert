import pytest
import random

@pytest.fixture
def random_length():
    return random.randint(0, 10)

@pytest.fixture(autouse=True, params=[1, 2, 3])
def random_array(request, random_length):
    random_list = [random.randint(-100, 100) for _ in range(random_length)]
    return random_list

def test_bubbleSort(random_array):
    sort_snap = sorted(random_array)
    for _ in random_array:
        for i in range(len(random_array) -1):
            if random_array[i] > random_array[i+1]:
                random_array[i],random_array[i+1] = random_array[i+1],random_array[i]
    assert random_array == sort_snap


def test_insertionSort(random_array):
    sort_snap = sorted(random_array)
    for i in range(1,len(random_array)):
        j = i
        while j > 0 and random_array[j] < random_array[j -1]:
            random_array[j], random_array[j-1] = random_array[j-1], random_array[j]
            j = j-1
    assert random_array == sort_snap


def test_selectionSort(random_array):
    sort_snap = sorted(random_array)
    for swap_inx in range(len(random_array)):
        selector = swap_inx
        for i in range(swap_inx, len(random_array)):
            if random_array[i] < random_array[selector]:
                selector = i
        random_array[swap_inx], random_array[selector] = random_array[selector], random_array[swap_inx]
    assert random_array == sort_snap


def test_quickSort(random_array):
    sort_snap = sorted(random_array) 
    random_array = quick_sort(random_array)
    assert random_array == sort_snap

def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    left = [n for n in array[1:] if n < pivot]
    right = [n for n in array[1:] if n >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)