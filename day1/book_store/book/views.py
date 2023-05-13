from django.shortcuts import redirect, render



books_list=[
   {
        'index': 0,
        'id': 1,
        'name': 'book-1',
        'author': "Yousef",
        'description': "Learning Learnin gJSfffjk dfjdklg jkdgjdkgjdkgjd kgjdkgjdglk jdgkljfjfjejekgjekgjekgjekgjgekjgekLearningJSfffjkdfjdklgjkdgjdkgjdkgjdkgjdkgjdglkjdgkljfjfjejekgjekgjekgjekgjgekjgekLearningJSfffjkdfjdklgjkdgjdkgjdkgjdkgjdkgjdglkjdgkljfjfjejekgjekgjekgjekgjgekjgek",
    },
    {
        'index': 1,
        'id': 2,
        'name': 'book-2',
        'author': "Ahmed",
        'description': "Learning LearningJS fffjkdfjd klgjkdgjdkgjdkgjdkgjd kgjdglkjdgk ljfj fjejekgjekgjekgjekgjgekjgek",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'book-3',
        'author': "Ali",
        'description': "LearningJS fffjk dfjdklgjkdg jdkgjdkgjd kgjdkgjdglkjdgkl jfjfjejekg jekgjekgjekgjgekjgek",
    },
]




def get_book(book_id):
    for book in books_list:
        if book["id"] == book_id:
            return book
    return None



      
    
   

# Create your views here.
def book_index(request):
   
   return render(request,"all_books.html",context={"books":books_list})

def book_details(request,**kwargs):
   book_id=kwargs.get("bid")
   book=get_book(book_id)
   print(book_id)  
   return render(request,"book_details.html",context=book)



def book_delete(request, **kwargs):
    book_id=kwargs.get("bid")
    book=get_book(book_id)
    if books_list:
        books_list.remove(book)
    return redirect('book:book-index')   

def book_update(request, **kwargs):
    book_id=kwargs.get("bid")
    book=get_book(book_id)
    for b in books_list:
        if b == book:
            b['name'] = f"Update {book['name']}"
            
    return redirect('book:book-index') 


def book_create(request):
    return render(request,"create_book.html")




def add_book(request):
    if request.method=="POST":
        #& why if I decalre size outside it can not see it?
        size=len(books_list)+1
        print(request.POST)
        new_book={
            "id":size,
            "name":request.POST['name'],
            "author":request.POST['author'],
            "description":request.POST['description']
            }
        books_list.append(new_book)
        size+=1
    return redirect('book:book-index')  



