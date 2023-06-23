


def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel= ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    count= {}
    for char in phrase:
        if char in vowel:
            count[char]= count.get(char,0)+1
    return count    
            