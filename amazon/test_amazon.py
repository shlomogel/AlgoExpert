"""

Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:
* Given "abcabcbb", the answer is "abc", which the length is 3.
* Given "bbbbb", the answer is "b", with the length of 1.
* Given "pwwkew", the answer is "wke", with the length of 3. 

"""
import pytest

@pytest.mark.parametrize('my_str, expacted', [("abcabcbb",3), ("bbbbb",1), ("pwwkew",3)])
def test_largest_str(my_str, expacted):
    left = 0
    largest = 0
    sub_letters = set()
    for right in range(len(my_str)):
        while my_str[right] in sub_letters:
            sub_letters.remove(my_str[left])
            left+=1
        sub_letters.add(my_str[right])
        largest = max(right-left + 1, largest)
    
    assert largest == expacted
