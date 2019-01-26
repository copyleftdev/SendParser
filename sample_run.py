from utils.parser import LogParser as lp

d = lp(dbname="sample3")

with open("samplelog") as logout:
    for line in logout:
        if "clearMem" in line:
            pass
        else:
            d.parser(line)


print(len(d.get_failed_jobs()))
print(len(d.get_successful_jobs()))
