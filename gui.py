# A basic Gui built using the Tkinter library
import os
from datafetcher import FetchWeather 
from Tkinter import *
result=None
def call_for_parsing_():
	print query.get()
	data=query.get()
	result=FetchWeather(data).__execute__()
	
	if result!=None:
		print 'Results : \n',result
	else:
		print 'No results found'
top=Tk()
top.geometry('750x500')
top.title('Weather Application')
label=Label(top,text='Please enter the name of the city you want to get the weather details from: ',font='Verdana -16 bold')
label.pack()
query=Entry(top)
query.pack()
enter_button=Button(top,text='GO!',activebackground='red',activeforeground='blue',command=call_for_parsing_)
enter_button.pack()
new_label=Label(top,text='Result:',font='Roboto -12 bold italic')
new_label.pack()
result_text=Label(top,text=result)
result_text.pack()
mainloop()
