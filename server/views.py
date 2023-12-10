from re import compile
from json import loads
from server.models import Book
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.request import Request
from server.serializers import BookSerializer
from rest_framework.decorators import api_view
from django.db import DatabaseError, OperationalError
from django.core.exceptions import ObjectDoesNotExist

@api_view(["GET", "POST"])
def bookCreateReadAPIView(
    request: Request
) -> JsonResponse:
    """
    View for creating a book and listing all books.

    :param request (rest_framework.request.Request): The HTTP request object.
    :return (django.http.JsonResponse): The JSON response containing the result of the operation.
    """

    try:
        if request.method == "GET":
            books = Book.objects.all()
            serializer = BookSerializer(books, many = True)
            return JsonResponse({
                "status": "success",
                "info": "Books fetched successfully",
                "data": serializer.data
            }, status = 200)
        
        if request.method == "POST":
            try:
                data = loads(request.body)

                if bool(compile(r'^\d{4}-\d{2}-\d{2}$').match(data["publicationDate"])) == False:
                    return JsonResponse({
                        "status": "error",
                        "info": f"Date should be YYYY-MM-DD format",
                    }, status = 400)
                
                serializer = BookSerializer(data = data)

                if serializer.is_valid():
                    serializer.save()   
                    return JsonResponse({
                        "status": "success",
                        "info": "Book added successfully",
                        "data": serializer.data
                    }, status = 201)
                
                else:
                    # Raising an error if the request payload is invalid.
                    raise serializers.ValidationError(
                        detail = '; '.join('; '.join(f"{error} for {name}" for error in errors) for name, errors in serializer.errors.items())
                    )
                
            except serializers.ValidationError as e:
                # Handling the error due to an invalid request payload.
                return JsonResponse({
                    "status": "error",
                    "info": e.detail[0]
                }, status = 400)
            
    except (OperationalError, DatabaseError) as e:
        # Handling an error in case of a database connection issue.
        return JsonResponse({
            "status": "error",
            "info": "Database connection error",
        }, status = 500)
    
    except Exception as e:
        # Handling an unknown error; advise users to try again later.
        return JsonResponse({
            "info": "An unknown error occurred, please try again later",
            "status": "error"
        }, status = 500)
    
@api_view(["PUT"])
def bookUpdateAPIView(
    request: Request, 
    bookId: int
) -> JsonResponse:
    """
    View for creating a book and listing all books.

    :param request (rest_framework.request.Request): The HTTP request object.
    :param bookId (int): The bookId of the book which needs to be updated.
    :return (django.http.JsonResponse): The JSON response containing the result of the operation.
    """

    try:
        if request.method == "PUT":
            try:
                data = loads(request.body)

                if bool(compile(r'^\d{4}-\d{2}-\d{2}$').match(data["publicationDate"])) == False:
                    return JsonResponse({
                        "status": "error",
                        "info": f"Date should be YYYY-MM-DD format",
                    }, status = 400)
                
                book = Book.objects.get(bookId = bookId)
                serializer = BookSerializer(book, data = data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({
                        "status": "success",
                        "info": "Book details updated successfully",
                        "data": serializer.data
                    }, status = 200)
                
                else:
                    raise serializers.ValidationError(
                        detail = '; '.join('; '.join(f"{error} for {name}" for error in errors) for name, errors in serializer.errors.items())
                    )
            
            except ObjectDoesNotExist:
                # Handling an error when the book that needs to be updated is not found in the database.
                return JsonResponse({
                    "status": "error",
                    "info": f"Book with bookId {bookId} not found",
                }, status = 404)
            
            except serializers.ValidationError as e:
                 # Handling the error due to an invalid request payload.
                return JsonResponse({
                    "status": "error",
                    "info": e.detail[0]
                }, status = 400)
            
    except (OperationalError, DatabaseError) as e:
        # Handling an error in case of a database connection issue.
        return JsonResponse({
            "status": "error",
            "info": "Database connection error",
        }, status = 500)
    
    except Exception as e:
        # Handling an unknown error; advise users to try again later.
        return JsonResponse({
            "info": "An unknown error occurred, please try again later",
            "status": "error"
        }, status = 500)
