class PointsForPlace:
    @staticmethod
    def get_points_for_place(place):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return 0
        if place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return 0
        points = 101 - place
        return points

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return 0
        points = meters * 0.5
        return points

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, meters, place):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return total
