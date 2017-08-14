import subprocess
from datetime import datetime, timedelta

draw = [".aaaa..",
        "a.....a",
        "b.b...b",
        "..c....",
        ".......",
        "ccccc.c",
        ".......",
        "..ccccc",
        "d......",
        "..ddddd",
        ".......",
        "ddddddd",
        "c..c..c",
        "c.....c",
        ".......",
        ".......",
        ".......",
        ".......",
        ".......",
        "ccccccc",
        "b..b..b",
        "b.....b",
        ".......",
        "......b",
        "aaaaaaa",
        "......b",
        ".......",
        "bbbbbbb",
        "...c...",
        "ccccccc",
        ".......",
        ".......",
        ".......",
        ".......",
        ".......",
        "ccccccc",
        "...d..d",
        "....dd.",
        ".......",
        "ddddddd",
        "c......",
        "c......",
        ".......",
        "bb....b",
        "b..b..b",
        "a....aa",
        ".......",
        ".......",
        "......."]

def new_commit(letter, date_str):
    if letter=='a':
        intensity = 1
    elif letter=='b':
        intensity = 2
    elif letter=='c':
        intensity = 3
    elif letter=='d':
        intensity = 4
    else:
        intensity = 0

    for x in range(intensity):
        with open("foo.txt", "a") as f:
            f.write("new line\n")

        basecmd = ["git", "add", "."]
        subprocess.call(basecmd)

        # commit_date = date + timedelta(days=i)
        # date_str = commit_date.strftime("%Y-%m-%dT0:0:0")
        basecmd = "GIT_AUTHOR_DATE=" + date_str + " GIT_COMMITTER_DATE=" + date_str + " git " + "commit " + "-m " + "'" + date_str + "'"

        print(basecmd)
        output = subprocess.check_output(['bash','-c', basecmd])
        # print(output)



date = datetime(2017, 8, 13, 10, 00)
print(date)
i = 0
for line in draw:
    y = list(line)[::-1]
    print(y)
    for x in y:
        print(i)
        if x!='.':
            commit_date = date + timedelta(days=i)
            date_str = commit_date.strftime("%Y-%m-%dT0:0:0")
            new_commit(x, date_str)

        i +=1
