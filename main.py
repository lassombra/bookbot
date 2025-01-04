def main():
    results = {}
    with open('./books/frankenstein.txt', 'r') as file:
        results = readbook(file.read())
    output(results)

def output(results):
    chars, wordcount = results
    print('Word count:', wordcount)
    #create a list of tuples from the dictionary
    chars = [(char, count) for char, count in chars.items()]
    #sort the list by the count descending
    chars.sort(key=lambda x: x[1], reverse=True)
    for char, count in chars:
        print(f"The character {char} appears {count} times")

def readbook(book):
    chars = {}
    wordcount = len(book.split())
    for char in book:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return (chars, wordcount)

main()