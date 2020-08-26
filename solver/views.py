from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import main
import re
# Create your views here.


def index(request):
    return render(request, 'solver/index.html')

#function that takes json stringified array and converts it into a sudoku representation.
def create_puzzle(data: str) -> list:
    string = data
    string = string.split(']')
    puzzle = []
    for rows in string:
        x = re.findall(r'[0-9]', rows)
        if len(x) == 9:
            puzzle.append(x)
    return puzzle

@csrf_exempt
def solve(request):
    if request.method == "POST":
        puzzle = request.POST['puzzle']
        puzzle = create_puzzle(puzzle)
        for i in range(9):
            for j in range(9):
                puzzle[i][j] = int(puzzle[i][j])
        main.solver(puzzle)
        print(puzzle)
        return JsonResponse(puzzle, safe=False)

