from os import stat
import statistics
import pandas as pd
from pandas.io.parsers import read_table
data = pd.read_csv("StudentsPerformance.csv")

math = data["math score"].tolist()
read = data["reading score"].tolist()
write = data["writing score"].tolist()

result = []

mathmean = statistics.mean(math)
readmean = statistics.mean(read)
writemean = statistics.mean(write)

mathmode = statistics.mode(math)
readmode = statistics.mode(read)
writemode = statistics.mode(write)

mathmedian = statistics.median(math)
readmedian= statistics.median(read)
writemedian = statistics.median(write)

print("The mean, mode and median of math is {}, {} and {}".format(mathmean, mathmode, mathmedian))
print("The mean, mode and median of read is {}, {} and {}".format(readmean, readmode, readmedian))
print("The mean, mode and median of write is {}, {} and {}".format(writemean, writemode, writemedian))

mathdev = statistics.stdev(math)
readdev = statistics.stdev(read)
writedev = statistics.stdev(write)

math_firstdeviation_start, math_firstdeviation_end = mathmean - mathdev, mathmean + mathdev
math_seconddeviation_start, math_seconddeviation_end = mathmean - (2*mathdev), mathmean + (2*mathdev)
math_thirddeviation_start, math_thirddeviation_end = mathmean - (3*mathdev), mathmean + (3*mathdev)

read_firstdeviation_start, read_firstdeviation_end = readmean - readdev, readmean + readdev
read_seconddeviation_start, read_seconddeviation_end = readmean - (2*readdev), readmean + (2*readdev)
read_thirddeviation_start, read_thirddeviation_end = readmean - (3*readdev), readmean + (3*readdev)

write_firstdeviation_start, write_firstdeviation_end = writemean - writedev, writemean + writedev
write_seconddeviation_start, write_seconddeviation_end = writemean - (2*writedev), writemean + (2*writedev)
write_thirddeviation_start, write_thirddeviation_end = writemean - (3*writedev), writemean + (3*writedev)

math_list1 = [result for result in math if result > math_firstdeviation_start and result < math_firstdeviation_end]
math_list2 = [result for result in math if result > math_seconddeviation_start and result < math_seconddeviation_end]
math_list3 = [result for result in math if result > math_thirddeviation_start and result < math_thirddeviation_end]

read_list1 = [result for result in read if result > read_firstdeviation_start and result < read_firstdeviation_end]
read_list2 = [result for result in read if result > read_seconddeviation_start and result < read_seconddeviation_end]
read_list3 = [result for result in read if result > read_thirddeviation_start and result < read_thirddeviation_end]

write_list1 = [result for result in write if result > write_firstdeviation_start and result < write_firstdeviation_end]
write_list2 = [result for result in write if result > write_seconddeviation_start and result < write_seconddeviation_end]
write_list3 = [result for result in write if result > write_thirddeviation_start and result < write_thirddeviation_end]



