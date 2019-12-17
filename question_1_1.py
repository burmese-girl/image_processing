import os
import glob

mypath = os.path.dirname(os.path.abspath(__file__))

os.chdir( mypath+'/Question1/Dataset/')

result = glob.glob('*.csv' ) # find csv files Dataset
result2 = glob.glob('RankC/*.csv' ) # find csv files Dataset/RankC

count=len(result) + len(result2) # total count under Dataset/RankC and Dataset

# print ('"'+str(count)+'"'+ " is a number")
print ("CSV File Count: ",count ," files")
