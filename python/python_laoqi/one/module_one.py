########################################
#模块编写
########################################

class Book:
    '''
    '''
    lang = 'learn python with laoqi'

    def __init__(self, author):
        self.author = author

    def get_name(self):
        return self.author
    
def new_book():
    return "12345"


if __name__ == "__main__":
    python = Book('laoqi')
    author_name = python.get_name()
    print(author_name)
    published = new_book()
    print(published)
