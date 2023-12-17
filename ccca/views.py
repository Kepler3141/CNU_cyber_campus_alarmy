from django.shortcuts import render

# def index(request):
#     return render(request, 'ccca/ccca.html')


def main(request):
    return render(request, 'ccca/main.html')


def notifications(request):
    return render(request, 'ccca/notifications.html')


def assignments(request):
    return render(request, 'ccca/assignments.html')


def materials(request):
    return render(request, 'ccca/materials.html')