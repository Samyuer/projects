# we'll import the list/data from data.py and sort/clean them

# from data import (whatever the list/data you pick is)

from data import phone_book 
search = input("whom is it you're looking for? ")
def tab_search(phone_book,search):

    for i in phone_book:
        if i.upper or i.lower == search:
            print("found "+search+ " their number is ", phone_book.get(search))
            return 0
        elif i not in phone_book:
            print("")
#tab_search(phone_book,search)


from data import class_
c_search =input("which class is it you're looking for? ")
def class_search(class_,search):

    for i in class_:
        if i.upper or i.lower == c_search:
            print("found "+c_search+ " your class is ", class_.get(c_search))
            return 0
        else:
            print("notfound")
            return 1
        
        
#class_search(class_,c_search)

from data import listOfNames
def search_list(listOfNames):

    serach = input("who are you looking for? ")
    for i in listOfNames:
        if i == serach:
            print("found "+serach)
            return 0
        else:
            print("not found")
            return 1
        
#search_list(listOfNames)
