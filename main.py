#import string

def get_book_text(path):
    '''
    opens the file at the given path and returns the text in the file
    
    path: string
    returns: string
    '''
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_word_cnt(text):
    '''
    accepts a string and returns the number of words in the given string

    text: string
    returns: int
    '''
    words = text.split()
    return len(words)

def get_letter_cnt(text):
    '''
    counts the occurances of each lowercase character in the given string

    text: string
    returns: dictionary
    '''
    lowered_text = text.lower()
    cnt_by_letter = {}
    for i in lowered_text:
        if i in cnt_by_letter:
            cnt_by_letter[i] += 1
        else:
            cnt_by_letter[i] = 1
    return cnt_by_letter

def get_cnt_by_char(dict):
    '''
    accepts a dictionary and sorts it by value

    dict: dictionary
    returns: list of dictionaries ordered by character count
    '''
    #make a list of dictionaries with each letter and its corresponding count
    letters = []
    for l in dict:
        if l.isalpha():
            letters.append({'letter': l, 'cnt': dict[l]})
    #get the value of cnt for each letter
    def sort_on(dict):
        return dict['cnt']
    #sort the list of dictionaries by the counts
    letters.sort(key=sort_on,reverse=True)
    return letters


def main():
    path = 'books/frankenstein.txt'
    text = get_book_text(path)
    print(text)
    word_cnt = get_word_cnt(text)
    letters_dict = get_letter_cnt(text)
    letters = get_cnt_by_char(letters_dict)
    print(f"--- Begin report of {path} ---")
    print(f"{word_cnt} words found in the document")
    print()
    for i in letters:
        print(f"There are {i['letter']} occurances of the letter {i['cnt']}")
    print("--- End report ---")


main()
