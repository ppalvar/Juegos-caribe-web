from django.shortcuts import render
from .models import ResultTeamMatch, ResultSingleMatch
from .results import Result

def positions_list(request):
    result_team = ResultTeamMatch.objects.all()
    result_single = ResultSingleMatch.objects.all()


    results = [
        Result((1,'Cuervos', 3, 0, 2, 18)),
        Result((2,'Aguilas', 0, 0, 2, 3)),
        Result((3,'Flex', 1, 0, 1, 12)),
        Result((4,'Serpientes', 2, 0, 2, 23)),
        Result((5,'Leones', 7, 5, 2, 43)),
        Result((6,'Los Tixxas', 2, 4, 2, 20)),
    ]

    return render(request,
        'medallero/medallero.html',
        {'results': results})