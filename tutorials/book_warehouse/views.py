from django.shortcuts import render


def warehouse_home(request):
    
    return render(request, 'book_warehouse/index.html', {})