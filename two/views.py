from django.shortcuts import render

def about(request):
    return render(request, 'two/about.html')  # استخدم علامات الاقتباس بشكل صحيح
