import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ds=pd.read_csv("town.csv")
# print(ds.shape) gives (812,46)

#total can be analyzed for imputations before male and female in this case, because this column has no zeros. It will be different for other columns. 
ds["Total - Persons"].to_csv("town.csv")
#checking columns for zeros that shouldn't exist, op is an aid to track which columns to correct
op=1
temp=ds["Total - Persons"]
#somehow searching for zero only works if you copy all the elements in data series onto a list, for temp, it indicated zero is present even when it is not.Hence the creation of temp1.

#creating copy of column
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])

#checking for zeros and replacing them if found with mean(except where zero is an accpetable value)
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0)
#mean of all numbers other than the zeros 
	size=len(temp1)
	mean=mean*(size/float(size-num))
#replacement
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
else:
	print("no zero here")
	op+=1


#repeating for all the relevant columns

temp=ds["Total - Males"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:	
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	meanm=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	mtotal=sum(temp1)
else:
	print("no zero here")
	op+=1
	mtotal=sum(temp1)
ds["Total - Males"]=temp1  #END
temp=ds["Total - Females"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	ftotal=sum(temp1)
else:
	print("no zero here")
	ftotal=sum(temp1)
	op+=1
ds["Total - Females"]=temp1  #END
temp=ds["Illiterate - Males"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	mtotal=sum(temp1)
else:
	print("no zero here")
	mtotal=sum(temp1)
	op+=1
ds["Illiterate - Males"]=temp1  #END
temp=ds["Illiterate - Females"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	ftotal=sum(temp1)
else:
	print("no zero here")
	ftotal=sum(temp1)
	op+=1
ds["Illiterate - Females"]=temp1  #END
temp=ds["Illiterate - Persons"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op) 
	size=len(temp1)
	tmean=(ftotal+mtotal)/size
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(tmean)
	op+=1
else:
	print("no zero here")

	op+=1
ds["Illiterate - Persons"]=temp1  #END
temp=ds["Literate - Males"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op,end= " ")
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	if num>0:
		print("VALID1",end=" ")
	else:
		print("WRONG", end=" ")
	size=len(temp1)
	if((size-num)>0):
		print("VALID")
	else:
		print("WRONG")
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	mtotal=sum(temp1)
else:
	print("no zero here")
	mtotal=sum(temp1)
	op+=1
ds["Literate - Males"]=temp1  #END
temp=ds["Literate - Females"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	ftotal=sum(temp1)
else:
	print("no zero here")
	ftotal=sum(temp1)
	op+=1
ds["Literate - Females"]=temp1  #END
temp=ds["Literate - Persons"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op) 
	size=len(temp1)
	tmean=(ftotal+mtotal)/size
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(tmean)
	op+=1
else:
	print("no zero here")

	op+=1
ds["Literate - Persons"]=temp1  #END
temp=ds["Educational Level - Literate without Educational Level Males"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	mtotal=sum(temp1)
else:
	print("no zero here")
	mtotal=sum(temp1)
	op+=1
ds["Educational Level - Literate without Educational Level Males"]=temp1  #END
temp=ds["Educational Level - Literate without Educational Level Females"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	ftotal=sum(temp1)
else:
	print("no zero here")
	ftotal=sum(temp1)
	op+=1
ds["Educational Level - Literate without Educational Level Females"]=temp1  #END
temp=ds["Educational Level - Literate without Educational Level Persons"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op) 
	size=len(temp1)
	tmean=(ftotal+mtotal)/size
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(tmean)
	op+=1
else:
	print("no zero here")

	op+=1
ds["Educational Level - Literate without Educational Level Persons"]=temp1  #END
temp=ds["Educational Level - Below Primary Males"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	mtotal=sum(temp1)
else:
	print("no zero here")
	mtotal=sum(temp1)
	op+=1
ds["Educational Level - Below Primary Males"]=temp1  #END
temp=ds["Educational Level - Below Primary Females"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	ftotal=sum(temp1)
else:
	print("no zero here")
	ftotal=sum(temp1)
	op+=1
ds["Educational Level - Below Primary Females"]=temp1  #END
temp=ds["Educational Level - Below Primary Persons"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op) 
	size=len(temp1)
	tmean=(ftotal+mtotal)/size
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(tmean)
	op+=1
else:
	print("no zero here")

	op+=1
ds["Educational Level - Below Primary Persons"]=temp1  #END
temp=ds["Educational Level - Primary Males"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	mtotal=sum(temp1)
else:
	print("no zero here")
	mtotal=sum(temp1)
	op+=1
ds["Educational Level - Primary Males"]=temp1  #END
temp=ds["Educational Level - Primary Females"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	ftotal=sum(temp1)
else:
	print("no zero here")
	ftotal=sum(temp1)
	op+=1
ds["Educational Level - Primary Females"]=temp1  #END
temp=ds["Educational Level - Primary Persons"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op) 
	size=len(temp1)
	tmean=(ftotal+mtotal)/size
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(tmean)
	op+=1
else:
	print("no zero here")
	op+=1
ds["Educational Level - Primary Persons"]=temp1  #END
temp=ds["Educational Level - Middle Males"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	mtotal=sum(temp1)
else:
	print("no zero here")
	mtotal=sum(temp1)
	op+=1
ds["Educational Level - Middle Males"]=temp1  #END
temp=ds["Educational Level - Middle Females"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	ftotal=sum(temp1)
else:
	print("no zero here")
	ftotal=sum(temp1)
	op+=1
ds["Educational Level - Middle Females"]=temp1  #END
temp=ds["Educational Level - Middle Persons"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op) 
	size=len(temp1)
	tmean=(ftotal+mtotal)/size
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(tmean)
	op+=1
else:
	print("no zero here")
	op+=1
ds["Educational Level - Middle Persons"]=temp1  #END
temp=ds["Educational Level - Matric/Secondary Males"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	mtotal=sum(temp1)
else:
	print("no zero here")
	mtotal=sum(temp1)
	op+=1
ds["Educational Level - Matric/Secondary Males"]=temp1  #END
temp=ds["Educational Level - Matric/Secondary Females"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	ftotal=sum(temp1)
else:
	print("no zero here")
	ftotal=sum(temp1)
	op+=1
ds["Educational Level - Matric/Secondary Females"]=temp1  #END
temp=ds["Educational Level - Matric/Secondary Persons"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op) 
	size=len(temp1)
	tmean=(ftotal+mtotal)/size
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(tmean)
	op+=1
else:
	print("no zero here")
	op+=1
ds["Educational Level - Matric/Secondary Persons"]=temp1  #END
temp=ds["Educational Level - Higher Secondary/Intermediate Pre-University/Senior Secondary Males"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	mtotal=sum(temp1)
else:
	print("no zero here")
	mtotal=sum(temp1)
	op+=1
ds["Educational Level - Higher Secondary/Intermediate Pre-University/Senior Secondary Males"]=temp1  #END
temp=ds["Educational Level - Higher Secondary/Intermediate Pre-University/Senior Secondary Females"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	ftotal=sum(temp1)
else:
	print("no zero here")
	ftotal=sum(temp1)
	op+=1
ds["Educational Level - Higher Secondary/Intermediate Pre-University/Senior Secondary Females"]=temp1  #END
temp=ds["Educational Level - Higher Secondary/Intermediate Pre-University/Senior Secondary Persons"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op) 
	size=len(temp1)
	tmean=(ftotal+mtotal)/size
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(tmean)
	op+=1
else:
	print("no zero here")
	op+=1
ds["Educational Level - Higher Secondary/Intermediate Pre-University/Senior Secondary Persons"]=temp1  #END
temp=ds["Educational Level - Non-technical Diploma or Certificate Not Equal to Degree Males"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	mtotal=sum(temp1)
else:
	print("no zero here")
	mtotal=sum(temp1)
	op+=1
ds["Educational Level - Non-technical Diploma or Certificate Not Equal to Degree Males"]=temp1  #END
temp=ds["Educational Level - Non-technical Diploma or Certificate Not Equal to Degree Females"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	ftotal=sum(temp1)
else:
	print("no zero here")
	ftotal=sum(temp1)
	op+=1
ds["Educational Level - Non-technical Diploma or Certificate Not Equal to Degree Females"]=temp1  #END
temp=ds["Educational Level - Non-technical Diploma or Certificate Not Equal to Degree Persons"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op) 
	size=len(temp1)
	tmean=(ftotal+mtotal)/size
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(tmean)
	op+=1
else:
	print("no zero here")
	op+=1
ds["Educational Level - Non-technical Diploma or Certificate Not Equal to Degree Persons"]=temp1  #END
temp=ds["Educational Level - Technical Diploma or Certificate Not Equal to Degree Males"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	mtotal=sum(temp1)
else:
	print("no zero here")
	mtotal=sum(temp1)
	op+=1
ds["Educational Level - Technical Diploma or Certificate Not Equal to Degree Males"]=temp1  #END
temp=ds["Educational Level - Technical Diploma or Certificate Not Equal to Degree Females"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	ftotal=sum(temp1)
else:
	print("no zero here")
	ftotal=sum(temp1)
	op+=1
ds["Educational Level - Technical Diploma or Certificate Not Equal to Degree Females"]=temp1  #END
temp=ds["Educational Level - Technical Diploma or Certificate Not Equal to Degree Persons"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op) 
	size=len(temp1)
	tmean=(ftotal+mtotal)/size
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(tmean)
	op+=1
else:
	print("no zero here")
	op+=1
ds["Educational Level - Technical Diploma or Certificate Not Equal to Degree Persons"]=temp1  #END
temp=ds["Educational Level - Graduate & Above Males"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	mtotal=sum(temp1)
else:
	print("no zero here")
	mtotal=sum(temp1)
	op+=1
ds["Educational Level - Graduate & Above Males"]=temp1  #END
temp=ds["Educational Level - Graduate & Above Females"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op)
	mean=sum(temp1)/len(temp1)
	num=temp1.count(0) 
	size=len(temp1)
	mean=mean*(size/float(size-num))
	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(mean)
	op+=1
	ftotal=sum(temp1)
else:
	print("no zero here")
	ftotal=sum(temp1)
	op+=1
ds["Educational Level - Graduate & Above Females"]=temp1  #END
temp=ds["Educational Level - Graduate & Above Persons"]
temp1=[]
for i in range(len(temp)):
	temp1.append(temp[i])
if 0 in temp1:
	print("do imputation here, in ",op) 
	size=len(temp1)
	tmean=(ftotal+mtotal)/size

	for j in range(size):
		if(temp1[j]==0):
			temp1[j]=int(tmean)
	op+=1
else:
	print("no zero here")
	op+=1
ds["Educational Level - Graduate & Above Persons"]=temp1  #END
ds.to_csv("town.csv")

