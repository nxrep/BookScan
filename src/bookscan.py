# BookScan Experiment - 2024 - Analyses ENG books in PDF format
from pypdf import PdfReader

VERSION="1.0.0"

def bookscan(file: str):

    print(f"Bookscan {VERSION} - Counts most used word")
    words={}
    print("Analysing book..")
    reader = PdfReader(file)

    pagesTotal=len(reader.pages)
    for currentPage in range(pagesTotal):
        page = reader.pages[currentPage]
        # extract page text and clean up for analysis
        pageText = page.extract_text()
        pageText=pageText.lower()
        removeList=["\n","?","!",".",",",";",":","“","”"]
        for char in removeList:
            pageText=pageText.replace(char,"")

        pageWords=pageText.split(" ")

        print(f"Page {currentPage}, found {len(pageWords)} words..")
        for word in pageWords:
            if word in words:
                words[word]+=1
            else: 
                if word:
                    words[word]=1

    # clean up and sort based on value

    # remove articles
    removeList=["the","a","an"]
    for article in removeList:
        if article in words:
            words.pop(article)

    # remove conjuctions
    removeList=["for","and","nor","but","or","yet","so"]
    for conjuction in removeList:
        if conjuction in words:
            words.pop(conjuction)

    # sort dict based on occurrences
    wordsSorted=dict(sorted(words.items(),key=lambda x:x[1], reverse=True))

    # output report
    print(f"\nBOOKSCAN REPORT FOR: {file.rsplit("/")[-1]}")

    print(f"Total pages: {pagesTotal}")
    wordsTotal=len(wordsSorted)
    print(f"Total unique words found (excluding articles, conjuctions and punctuation): {wordsTotal}")

    print("Most found words, larger than 2 characters:") # and more than 9 occurrences
    for word in wordsSorted:
        if len(word)>2 and wordsSorted[word]>9:
            print(f" word: {word} - found: {wordsSorted[word]} time(s)")

    if input("Display all found words? [Y]es/[N]o: ").lower()=="y":
        print("All words found.")
        print(wordsSorted)


if __name__ == "__main__":
    bookscan("../books/Dickens_Carol.pdf")
