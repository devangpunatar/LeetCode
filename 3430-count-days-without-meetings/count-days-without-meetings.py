class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x: x[0])

        res = [meetings[0]]

        for start, end in meetings[1:]:
            last_end = res[-1][1]
            if start <= last_end:
                res[-1][1] = max(last_end, end)
            else:
                res.append([start, end])

        print(res)
        s, e = res[0][0], res[0][1]
        output = s - 1

        for start, end in res[1:]:
            if start > e:
                output += start - e - 1
            elif start <= e:
                continue
            e = end

        output += days - res[-1][1]

        return output