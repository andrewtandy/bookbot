def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    return report(text)

def report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")
    print("")

    characters = count_charas(text)
    letters = characters.keys()
    report_info = []

    for i in letters:
        if i.isalpha():
            new_dict = {
                "letter":i,
                "count":characters[i]
            }

            report_info.append(new_dict)
    
    report_info.sort(reverse=True, key=sort_on)
    
    for i in range(len(report_info)):
        print(f"The '{report_info[i]['letter']}' character was found {report_info[i]['count']} times")
    
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]


def count_charas(text):
    lowered_string = text.lower()
    chara_count = {}

    for character in lowered_string:
        if character in chara_count:
            chara_count[character] += 1
        else:
            chara_count[character] = 1

    return chara_count

def count_words(text):
    words = text.split()
    return len(words)

def read_book(path):
    with open(path) as f:
        return f.read()



main()