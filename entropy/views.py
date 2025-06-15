from django.shortcuts import render, redirect
from .models import Submission

def home(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Submission.objects.create(content=content)
            return redirect('home')

    submissions = Submission.objects.order_by('-created_at')[:10]
    return render(request, 'home.html', {
        'submissions': submissions
    })
