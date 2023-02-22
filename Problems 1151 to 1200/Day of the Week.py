class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        date = datetime.datetime(year, month, day)


        return date.strftime('%A')
