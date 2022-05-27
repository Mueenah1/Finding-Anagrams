# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from ntpath import join


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = 'l'.join(sorted(word.lower()))
    anagram = 'l'.join(sorted(anagram.lower()))
    if word == anagram:
        return True
    else:
        return False

solve = find_anagram('Hello', 'Check')
print(solve)
solve1 = find_anagram('Tap', 'Pat')
print(solve1)
solve2 = find_anagram('Bruise', 'Cruise')
print(solve2)
    

