from django.shortcuts import render
import common.db as db


# def index(request):
#     return render(request, 'ccca/ccca.html')


def main(request):
    testdata = db.dataBase['data']
    return render(request, 'ccca/main.html', {'testdata': testdata})


def notifications(request):
    return render(request, 'ccca/notifications.html')


def assignments(request):
    return render(request, 'ccca/assignments.html')


def materials(request):
    return render(request, 'ccca/materials.html')