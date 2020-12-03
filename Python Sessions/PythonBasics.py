#PYTHON LESSONS - LAB1

# print something on the screen
print("PYTHON LESSONS - LAB1")

#Variable declaration and handling
iFirstNumber = 20
iSecondNumber = 13
iSum = iFirstNumber + iSecondNumber
iDifference = iFirstNumber - iSecondNumber
iMultiplication = iFirstNumber*iSecondNumber
divide1 = iFirstNumber//iSecondNumber #Result is a digit
divide2 = iFirstNumber/float(iSecondNumber) #Result is a float
print(divide1)
print(divide2)
type(iSum)

#different ways of printing in Python
print("The addition result is : " + str(iSum))
print("result of the sum is : %d" %(iSum))
print("result of %d and %d is: %d" %(iFirstNumber,iSecondNumber,iSum))
print("result of sum is: {0}, the difference is {1} and the multiplication is {2}".format(iSum,iDifference,iMultiplication))
print(f"the result of the sum is {iSum} , the difference is {iDifference} and the multiplication is {iMultiplication}")
print("this is what I call: \n a new line")

#Python useful methods
'nitesh'.upper()
'nitesh'.replace('e','i')
str_text= "Hello there! My name is Nitesh!!"
str_text_modified= str_text.replace("e","_")
print(str_text_modified)
str_text_modified_new = str_text.replace("e","_")\
                                .replace("i", "*")\
                                .replace("N", "r")
print(str_text_modified_new)

#Importing a library and usind a function from imported library in Python
import re
re.sub('[aeiou]', '_', 'Nitesh Dabas - You are amazing!!')

#For loop in Python
for num in range(0,1000, 1):
  if(num%10==0) and num !=0:
    print(num)

#Loop over letters of strings - trim and strip
for letter in str_text.replace(" ", "" ):
  print(letter)

#Defining and calling a function in Python
def writing_name(student_name):
  print("my name is : " + str(student_name))
writing_name("Nitesh")

import os
#get current working directory
current_dir = os.getcwd()
#list of files in the directory(relative directory)
all_files_1 = os.listdir(current_dir)
all_files_2 = os.listdir()
print(all_files_1)
print(all_files_2)

assert all_files_1 == all_files_2 #Equality test

#to browse a directory and list down all python files
my_list = []
all_files = os.scandir(current_dir) 
print(all_files)
#Scandir generates an iterator and hence needs a for loop to iterate over
for entry in all_files:
  if entry.path.endswith(".py"):
    my_list.append(entry.path) 
  print(entry.name)
  print(entry.path)
  print(my_list)

#import glob2
#all_files_3 = glob2.glob("/*/*/*/*.py", include_hidden=True)
#print(all_files_3)
#new_regexp = os.path.join(current_dir, '*.py')
#print(new_regexp)

import wget
#Import dataset IRIS
iris_link = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/bezdekIris.data"
#ddl_iris = wget.download(iris_link)
#!wget https://archive.ics.uci.edu/ml/machine-learning-databases/iris/bezdekIris.data

#To install the library
#Run command "pip  install wget" in terminal
import pandas as pd
#df = pd.read_csv(iris_link)
df = pd.read_csv(iris_link, header=None, names=["Sepal.Length", "Sepal.Width","Petal.Length","Petal.Width","Species"], sep=",")
print(df.head())

#importing and loading datasets
from sklearn import datasets
iris = datasets.load_iris()
#print(iris)

print(iris["target_names"])

#function which returns a subset of dataset IRIS
import numpy as np
def dataset_to_frame(dataset):
  framed_set = pd.DataFrame(data=np.c_[dataset.data, dataset.target],\
                               columns= dataset.feature_names + ["target"]) #list(dataset.target.keys())[0]
  #at this point we have 5 column dataframe but the frame column has values from 0 to 2
  keys = list(range(len(dataset.target_names)))
  values = dataset.target_names
  #mapping numbers to class names objectives{0: setosa, 1:versicolor ,2: virginica}
  mapping_disctionary = dict(zip(keys,values))
  framed_set = framed_set.replace({"target": mapping_disctionary})
  return(framed_set) 
res = dataset_to_frame(iris)
print(res.head())

#Last column gets the length of classes names
#About Map funtions in python
#Create a new column that applies the function lambda to each elements of the column
res["target_length"] = res["target"].apply(lambda x: len(x))
print(res.head())
