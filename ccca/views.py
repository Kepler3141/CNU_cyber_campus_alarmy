from django.shortcuts import render
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common import db
import time


# def index(request):
#     return render(request, 'ccca/ccca.html')


def main(request):
    # testdata = db.dataBase

    now = time
    testdata = now.strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'ccca/main.html', {'testdata': testdata})


def notifications(request):
    return render(request, 'ccca/notifications.html')


def assignments(request):
    return render(request, 'ccca/assignments.html')


def materials(request):
    return render(request, 'ccca/materials.html')