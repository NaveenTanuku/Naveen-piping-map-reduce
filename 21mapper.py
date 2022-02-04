# Case 2 - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split("    ")
  datalist=datalist[0].split(",")
  print(datalist)
  if (len(datalist) == 8) : 
    YEAR, MOVIE, GENRE, RATING,	DISTRIBUTOR,	TOTAL_YEAR,	TOTAL_IN_DOLLARS,TICKETS_SOLD = datalist

    # print intermediate key-value pairs to standard output
    print(GENRE,"\t",TICKETS_SOLD)

