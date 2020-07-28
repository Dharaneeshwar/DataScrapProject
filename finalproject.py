print('\t\tWELCOME TO MINI PROJECT MADE BY DHARANEESHWAR.P\n\n')
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
myURL = 'https://www.health.com/weight-loss/30-simple-diet-and-fitness-tips#diet-fitness-tips'
  #opening up the connection and grabbing the page
uClient = uReq(myURL)
 #reads all the HTML data from the webpage
page_html = uClient.read()
 #close the connection after reading the data
uClient.close()
 #storing the data using BeautifulSoup function, which is renamed as soup
 #parses the html
page_soup = soup(page_html,"html.parser")
# gets all the details of all the graphic card products

containers = page_soup.findAll("div",{"class":"caption margin-24-bottom"})
#print(len(containers))
#fo=open("scrapped_data.txt","w")
para_list=[]
fo=open('url no 1.txt','a') 
for container in containers:
    
    brand=container.text
    #print(brand,'\n')
    #fo=open('webscrap.txt','a') 
    para_list.append(brand)
    #fo.write(brand)
fo.writelines(str(para_list))
fo.close()

total_content=",".join(para_list)

words=total_content.split(' ')

count=0
print('Name of the Website is : www.health.com')
print('Words in url=',len(words))
word_to_be_checked1=input("Enter the word to which density is required in the first url")

import re

pattern= re.compile(word_to_be_checked1)
for word in words:
    match=pattern.match(word)
    if match:
        count+=1
    else:
        continue

print('number of words matched is ',count)
print('Density of the word \'',word_to_be_checked1,'\' you entered is ',count/len(words)*100,'%')
print('\n\n\n')
density1=count/len(words)*100
#-------------------------------------------------------------------------------------------------------------------------
myURL1 = 'https://healthservices.camden.rutgers.edu/topics_wellness'


  #opening up the connection and grabbing the page
uClient = uReq(myURL1)
 #reads all the HTML data from the webpage
page_html = uClient.read()
 #close the connection after reading the data
uClient.close()
 #storing the data using BeautifulSoup function, which is renamed as soup
 #parses the html
page_soup = soup(page_html,"html.parser")
# gets all the details of all the graphic card products
containers = page_soup.find("div",{"class":"field-item even"})
#print(len(containers))
para_list1=[]
para_list2=[]
fo=open('url no 2.txt','a') 
for i in containers.findAll('p'):
    #print(i.text,'\n\n')
    para_list1.append(i.text)
fo.writelines(str(para_list1))
for j in containers.findAll('ol'):
    #print(j.text,'\n')
    para_list2.append(j.text)
fo.writelines(str(para_list2))
fo.close()
para_list3=para_list1+para_list2
total_content=",".join(para_list3)
words2=total_content.split(' ')
count2=0
print('Name of the Website is : www.healthservices.com')
print('Words in url=',len(words2))
word_to_be_checked=input("Enter the word to which density is required in the second url")
import re
pattern= re.compile(word_to_be_checked)
for word in words2:
    match=pattern.match(word)
    if match:
        count2=count2+1
    else:
        continue


print('number of words matched is ',count2)
print('Density of the word \'',word_to_be_checked,'\' is ',count2/len(words2)*100,'%')
density2=count2/len(words2)*100
print('\n\n\n')
#----------------------------------------------------------------------------------------------------------
myURL2 = 'http://www.healthynudgez.com/general-health/10-ways-attract-positive-energy-life/'
  #opening up the connection and grabbing the page
uClient = uReq(myURL2)
 #reads all the HTML data from the webpage
page_html = uClient.read()
 #close the connection after reading the data
uClient.close()
 #storing the data using BeautifulSoup function, which is renamed as soup
 #parses the html
page_soup = soup(page_html,"html.parser")
containers = page_soup.find("div",{"class":"entry-content clearfix"})

para_list4=[]
fo=open('url no 3.txt','a') 


for i in containers.ol.li.findAll('ol'):
    para_list4.append(i.text)
fo.writelines(str(para_list4))
fo.close()
total_content=",".join(para_list4)
words3=total_content.split(' ')
count3=0
print('Name of the Website is : www.healthynudgez.com')
print('Words in url=',len(words3))
word_to_be_checked3=input("Enter the word to which density is required in the first url")
import re
pattern= re.compile(word_to_be_checked3)
for word in words3:
    match=pattern.match(word)
    if match:
        count3=count3+1
    else:
        continue
print('number of words matched is ',count3)
print('Density of the word \'',word_to_be_checked3,'\' you entered is ',count3/len(words3)*100,'%')
density3=count3/len(words3)*100

#------------------------------------------------------------------------------------------------------------------------------------
if density1>density2 and density1>density3:
	if density2>density3:
		rank1='First'
		rank2='Second'
		rank3='Third'
	else:
		rank1='First'
		rank2='Third'
		rank3='Second'
elif density2>density1 and density2>density3:
	if density1>density3:
		rank1='second'
		rank2='First'
		rank3='Third'
	else:
		rank1='Third'
		rank2='First'
		rank3='Second'
elif density3>density2 and density3>density1:
	if density2>density1:
		rank1='Third'
		rank2='Second'
		rank3='First'
	else:
		rank1='Second'
		rank2='Third'
		rank3='First'
#----------------------------------------------------------------------------------------------------------------------------------------------
import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('PROJECT WORK  with CHARTS.xlsx')
bold = workbook.add_format({'bold': True})

worksheet1 = workbook.add_worksheet()
worksheet1.write('A1','Project done by DHARANEESHWAR.P',bold)
worksheet1.write('A3','Website name:',bold)
worksheet1.write('B3','www.health.com')
worksheet1.write('A5','Total number of words:',bold)
worksheet1.write('B5',len(words))
worksheet1.write('A4','Word selected',bold)
worksheet1.write('B4',word_to_be_checked1)
worksheet1.write('A6','No of matching words',bold)
worksheet1.write('B6',count)
worksheet1.write('A7','Density of the word',bold)
worksheet1.write('B7',density1)
worksheet1.write('A9','RANK of DENSITY',bold)
worksheet1.write('B9',rank1)
chart=workbook.add_chart({'type':'bar'})
chart1 = workbook.add_chart({'type': 'pie'})
chart1.add_series({
    'name': 'Pie Chart',
    'categories': '=Sheet1!$A$5:$A$6',
    'values':     '=Sheet1!$B$5:$B$6',
})
worksheet1.insert_chart('D4', chart1, {'x_offset': 25, 'y_offset': 10})

worksheet2 = workbook.add_worksheet()
worksheet2.write('A3','Website name:',bold)
worksheet2.write('B3','www.healthservices.com')
worksheet2.write('A5','Total number of words:',bold)
worksheet2.write('B5',len(words2))
worksheet2.write('A4','Word selected',bold)
worksheet2.write('B4',word_to_be_checked)
worksheet2.write('A6','No of matching words',bold)
worksheet2.write('B6',count)
worksheet2.write('A7','Density of the word',bold)
worksheet2.write('B7',density2)
worksheet2.write('A9','RANK of DENSITY',bold)
worksheet2.write('B9',rank2)
chart2 = workbook.add_chart({'type': 'pie'})
chart2.add_series({
    'name': 'Pie chart',
    'categories': '=Sheet2!$A$5:$A$6',
    'values':     '=Sheet2!$B$5:$B$6',
})
worksheet2.insert_chart('D4', chart2, {'x_offset': 25, 'y_offset': 10})
worksheet3 = workbook.add_worksheet()
worksheet3.write('A3','Website name:',bold)
worksheet3.write('B3','www.healthnudgez.com')
worksheet3.write('A5','Total number of words:',bold)
worksheet3.write('B5',len(words3))
worksheet3.write('A4','Word selected',bold)
worksheet3.write('B4',word_to_be_checked3)
worksheet3.write('A6','No of matching words',bold)
worksheet3.write('B6',count3)
worksheet3.write('A7','Density of the word',bold)
worksheet3.write('B7',density3)
worksheet3.write('A9','RANK of DENSITY',bold)
worksheet3.write('B9',rank3)
chart3 = workbook.add_chart({'type': 'pie'})
chart3.add_series({
    'name': 'Pie chart',
    'categories': '=Sheet3!$A$5:$A$6',
    'values':     '=Sheet3!$B$5:$B$6',
})
worksheet3.insert_chart('D4', chart3, {'x_offset': 25, 'y_offset': 10})
workbook.close()

print('Pasting scraped data into files.....\n')
print('Creating Excel Worksheets......\n')
print('Saving required documents....\n')
print('Go to CODE location to view the rendered documents and reports\n')
print('THANKS FOR USING THE SERVICE')
