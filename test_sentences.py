from Sentences import get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb
import pytest
def test_get_determiner():
    # 1. Test the single determiners.
    single_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_determiner(1)
    # Verify that the word returned from get_determiner is
    # one of the words in the single_determiners list.
    assert word in single_determiners
    # 2. Test the plural determiners.
    plural_determiners = ["some", "many"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(2)
    # Verify that the word returned from get_determiner
    # is one of the words in the plural_determiners list.
    assert word in plural_determiners
def test_get_noun():
    # 3. Test the single nouns.
    single_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_noun(1)
    # Verify that the word returned from get_determiner is
    # one of the words in the single_determiners list.
    assert word in single_nouns
    # 4. Test the plural nouns.
    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_noun(2)
    # Verify that the word returned from get_noun
    # is one of the words in the plural_nouns list.
    assert word in plural_nouns 

def test_get_prepositional_phrase():
    #This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        phrase = get_prepositional_phrase(1)
    # Verify that the returned phrase contains three different words.
        phrases = phrase.split(" ")
    assert len(phrases) == 3
    pytest.main(["-v", "--tb=no", "test_sentences.py"])