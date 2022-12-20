from django.shortcuts import render;
def wishes(request):
	return render(request,'FirstApp/wishes.html')


def hello(request):
	return render(request,'FirstApp/hello.html')



# {{templ-tag-vars}}
import datetime;
import time;


def datetimefunction(request):
	date1 = datetime.datetime.now();
	print(date1)
	date2 = time.ctime();
	dict1 = {"server_datetime": date1, "server_datetime2": date2}
	return render(request, 'FirstApp/datetime.html', context=dict1)

import datetime
def wishes2(request):
    date1=datetime.datetime.now()
    msg1='Hello User/Client...GOOD';
    hr=int(date1.strftime('%H'));
    if hr<12:
        msg1+=' Morning!!'
    elif hr<16:
        msg1+=' Afternoon!!'
    elif hr<20:
        msg1+=' Evening!!'
    else:
        msg1='Hello User/Client...Very Good Night!!'
    dict1={'date1':date1,'msg1':msg1}
    return render(request,'FirstApp/wishes2.html',context=dict1);




