grid = [1,0,0,1]

for index,data in enumerate(grid):
    print(index,data)


def make_readable(seconds):
    if seconds == 0:
        return "00:00:00"
    else:
        hh = seconds // 3600
        mm = seconds // 60
        ss = seconds 


