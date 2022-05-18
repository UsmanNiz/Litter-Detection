import os
from random import shuffle
import shutil

list1 = os.listdir("Data")
listOfText= []

for value in list1:
    if "txt" in value and "class" not in value:
        listOfText.append(value)

shuffle(listOfText)

lengthOfTxt = len(listOfText)

trainListOfTxt = listOfText[:int(lengthOfTxt*0.8)]
valListOfTxt = listOfText[int(lengthOfTxt*0.8):]

for val in trainListOfTxt:
    shutil.copy("Data/" + (val),"Dataset/labels/train")
    shutil.copy(("Data/" + (val.split(".")[0] +".jpg")), "Dataset/images/train" )
for val in valListOfTxt:
    shutil.copy("Data/" + (val),"Dataset/labels/val")
    shutil.copy(("Data/" + (val.split(".")[0] +".jpg")), "Dataset/images/val" )

# os.mkdir("")

# print(len(trainListOfTxt), "  ", len(valListOfTxt))
# print( len(listOfText),len(list1),listOfText)

# print(list1)