def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_counted(text)
    number_of_characters(text)
    print("--- End report ---")



def get_book_text(path):
    with open(path) as f:
        print("--- Begin report of books/frankenstein.txt ---")
        return f.read()

def words_counted(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    print(f"{count} words found in the document")
    return count

def number_of_characters(text):
    character_and_number_list = []
    character_and_number = {}
    lowered_string = text.lower()

    for char in lowered_string:
        if char in character_and_number:
            character_and_number[char] += 1
        else:
            character_and_number[char] = 1

    for char, count in character_and_number.items():
        new_dict = {"char": char, "num": count}
        character_and_number_list.append(new_dict)

    for item in character_and_number_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
        
    return character_and_number_list
        

    


main()