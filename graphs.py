
def data_extract(s,b):
    import pandas as pd
    length = b*365
    data = pd.read_pickle('testfile')    
    var  = str(s)
    var_name = 'set_' + var
    dataset = data.loc[data.STN ==s]

    sun_e = dataset.reset_index(drop=True).Q
    time  = dataset.reset_index(drop=True).YYYYMMDD
    
    sun_e_list = sun_e.tolist()
    time_list  = time.tolist()
    
    for i in range(len(sun_e_list)):
        sun_e_list[i] = float(sun_e_list[i])
        time_list[i] = float(time_list[i])
    
    return sun_e_list[-length:]



def create_pie_chart(E,b):
    from nvd3 import pieChart
    import numpy as np
    energieverbruik = E 
    b = b 
    opbrengst = np.mean(data_extract(249,b))*365 
    type = 'pieChart'
    chart = pieChart(name=type, color_category='category10', height=550, width=1000)
    xdata = ["Rest","Opbrengst uit panelen"]
    ydata = [(energieverbruik-opbrengst), opbrengst]
    extra_serie = {"tooltip": {"y_start": "", "y_end": " Joules"}}
    chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
    chart.buildcontent()
    result = chart.htmlcontent
    
    return result

def create_line_chart(a,b):
    from nvd3 import lineWithFocusChart
    import random 
    import datetime 
    import time 
    mult = a
    year = 2000 +(18-b)
    start_time = int(time.mktime(datetime.datetime(year, 4, 1).timetuple()) * 1000) 
    nb_element = 100 

    test = True
    
    if test:
        type = "lineWithFocusChart" 
        chart = lineWithFocusChart(name=type, height=550, width=1000, 
                                   color_category='category20b', x_is_date=True, 
                                   x_axis_format="%d %b %Y", focus_enable=True) 
        ydata = data_extract(249,b)
        xdata = list(range(len(ydata))) 
        xdata = [start_time + x * 86400000 for x in xdata] 
        extra_serie = {"tooltip": {"y_start": "There was ", "y_end": " j/cm2"}, 
               "date_format": "%d %b %Y"} 
        chart.add_serie(name = 'Energie', y=ydata, x=xdata, extra=extra_serie)
        chart.buildhtml()
        result = chart.htmlcontent

        
    else: 
        type = "lineWithFocusChart" 
        chart = lineWithFocusChart(name=type, height=550, width=1000, 
                                   color_category='category20b', x_is_date=True, 
                                   x_axis_format="%d %b %Y %H", focus_enable=True) 
        #chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n") 

        
         
        xdata = list(range(nb_element)) 
        xdata = [start_time + x * 1000000000 for x in xdata] 
        ydata = [i + random.randint(-10, 10) for i in range(nb_element)] 
        
    
        
         
        ydata2 = [x * 2*mult for x in ydata] 
        ydata3 = [x * (3+mult) for x in ydata] 
        ydata4 = [x * 4*mult for x in ydata] 
        
        extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"}, 
                       "date_format": "%d %b %Y %H:%M:%S %p"} 
        # extra_serie = None 
        #chart.add_serie(name="serie 1", y=ydata, x=xdata, extra=extra_serie) 
        #chart.add_serie(name="serie 2", y=ydata2, x=xdata, extra=extra_serie) 
        #chart.add_serie(name="serie 3", y=ydata3, x=xdata, extra=extra_serie) 
        chart.add_serie(name="serie 4", y=ydata4, x=xdata, extra=extra_serie) 
        
         
        chart.buildhtml()
        result = chart.htmlcontent
    
    return result

def create_area_chart():
    from nvd3 import stackedAreaChart
    
    type = 'stackedAreaChart'
    chart = stackedAreaChart(name=type, height=550, width=1000) 
    
    xdata = [100, 101, 102, 103, 104, 105, 106] 
    ydata = [6, 11, 12, 7, 11, 10, 11] 
    ydata2 = [8, 20, 16, 12, 20, 28, 28] 
    
     
    extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " min"}} 
    chart.add_serie(name="Serie 1", y=ydata, x=xdata, extra=extra_serie) 
    chart.add_serie(name="Serie 2", y=ydata2, x=xdata, extra=extra_serie) 
    
    chart.buildhtml() 
    
    result = chart.htmlcontent
    
    return result

def create_line_chart2(b):
    from nvd3 import lineChart
    import random 
    import datetime 
    import time 

    year = 2000 +(18-b)
    start_time = int(time.mktime(datetime.datetime(year, 4, 1).timetuple()) * 1000) 
    type = "lineChart" 
    chart = lineChart(name=type, x_is_date=True, x_axis_format="%d %b %Y") 
    
    ydata = data_extract(249,b)
    xdata = list(range(len(ydata))) 
    xdata = [start_time + x * 86400000 for x in xdata] 
    kwargs1 = {'color': '#66b3ff'} 

    extra_serie = {"tooltip": {"y_start": "There was ", "y_end": " j/cm2"}} 
    chart.add_serie(y=ydata, x=xdata, name='Zonne-energie', extra=extra_serie, **kwargs1) 

    
    chart.buildhtml() 
    
    result = chart.htmlcontent
    
    return result 


