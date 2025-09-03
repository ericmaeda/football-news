from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406423181',
        'name': 'Erico Putra Bani Mahendra',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
