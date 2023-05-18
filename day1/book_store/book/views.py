from django.shortcuts import redirect, render
from .models import Book
from .forms import BookForm



# books_list=[
#    {
#         'index': 0,
#         'id': 1,
#         'name': 'book-1',
#         'author': "Yousef",
#         'description': "Learning Learnin gJSfffjk dfjdklg jkdgjdkgjdkgjd kgjdkgjdglk jdgkljfjfjejekgjekgjekgjekgjgekjgekLearningJSfffjkdfjdklgjkdgjdkgjdkgjdkgjdkgjdglkjdgkljfjfjejekgjekgjekgjekgjgekjgekLearningJSfffjkdfjdklgjkdgjdkgjdkgjdkgjdkgjdglkjdgkljfjfjejekgjekgjekgjekgjgekjgek",
#     },
#     {
#         'index': 1,
#         'id': 2,
#         'name': 'book-2',
#         'author': "Ahmed",
#         'description': "Learning LearningJS fffjkdfjd klgjkdgjdkgjdkgjdkgjd kgjdglkjdgk ljfj fjejekgjekgjekgjekgjgekjgek",
#     },
#     {
#         'index': 2,
#         'id': 3,
#         'name': 'book-3',
#         'author': "Ali",
#         'description': "LearningJS fffjk dfjdklgjkdg jdkgjdkgjd kgjdkgjdglkjdgkl jfjfjejekg jekgjekgjekgjgekjgek",
#     },
# ]




# def get_book(book_id):
#     for book in books_list:
#         if book["id"] == book_id:
#             return book
#     return None



      
    
   

# Create your views here.
def book_index(request):
   books=Book.objects.all()
   return render(request,"all_books.html",context={"books":books})

def book_details(request,bid):
   book=Book.objects.get(pk=bid)
   return render(request,"book_details.html",context={"book":book})



def book_delete(request, bid):
    book=Book.objects.get(pk=bid).delete()
    return redirect('book:book-index')   

def book_update(request, bid):
    book = Book.objects.get(pk=bid)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book:book-details", bid=book.id)
    return render(request, 'update_book.html', context={
        'form': form, 
        'book': book
    })

def book_create(request):
    form = BookForm()
    return render(request, 'create_book.html', context={
        'form': form
    })





def add_book(request):
    
        #& why if I decalre size outside it can not see it?
        # size=len(books_list)+1
        # print(request.POST)
        # new_book={
        #     "id":size,
        #     "name":request.POST['name'],
        #     "author":request.POST['author'],
        #     "description":request.POST['description']
        #     }
        # books_list.append(new_book)
        # size+=1
    form = BookForm()
    if request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("book:book-index")




