from .models import ResultTeamMatch, ResultSingleMatch
from deportes.models import Faculty

class Result:
    
    def __init__(self, params) -> None:

        self.pos = params[0]
        self.name = params[1]
        self.gold = params[2]
        self.silver = params[3]
        self.bronze = params[4]
        self.points = params[5]

def get_results():
    result_team = ResultTeamMatch.objects.all()
    result_single = ResultSingleMatch.objects.all()
    points_for_positions = [30, 25, 20, 17, 15, 13, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    for faculty in Faculty.object.all:

        gold, silver, bronze, points = 0, 0, 0, 0

        for a in result_single.match.all:

            pass
        