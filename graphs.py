
def data_extract(s,b):
    import pandas as pd
    length = b*365
    dataset = pd.read_pickle('dataset_249')    
  
#    dataset = data.loc[data.STN ==s]

    sun_e = dataset.reset_index(drop=True).Q
    time_d  = dataset.reset_index(drop=True).YYYYMMDD
    
    sun_e_list = sun_e.tolist()
    time_list  = time_d.tolist()  
    
    start_point = len(sun_e_list)-length
    
    for i in range(length):
        sun_e_list[start_point + i] = float(sun_e_list[start_point + i])
        time_list[start_point + i] = float(time_list[start_point + i])
            
    return sun_e_list[start_point:]



def create_pie_chart(E,b):
    from nvd3 import pieChart
    import time 
    import numpy as np
    energieverbruik = E 
    b = b
    start = time.clock()
    day_mean_e = np.mean(data_extract(249,b))
    year_mean_kWh = day_mean_e*(365)/(24*10)
    
    besparingen = 0.2 * year_mean_kWh
    boiler = 0.45 * year_mean_kWh
    
    type = 'pieChart'
    chart = pieChart(name=type, color_category='category20', height=550, width=1000)
    xdata = ["Rest","Opbrengst uit panelen", "Besparingen", "Opbrengst uit zonneboilers"]
    ydata = [(energieverbruik-year_mean_kWh-besparingen - boiler), year_mean_kWh, besparingen, boiler]
    extra_serie = {"tooltip": {"y_start": "", "y_end": " J/cm<sup>2"}}
    chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
    chart.buildcontent()
    result = chart.htmlcontent
    tijd = start - time.clock()
    return result

def create_line_chart(b):
    from nvd3 import lineWithFocusChart
    import datetime 
    import time 

    year = 2000 +(18-b)
    start_time = int(time.mktime(datetime.datetime(year, 4, 1).timetuple()) * 1000) 


    type = "lineWithFocusChart" 
    chart = lineWithFocusChart(name=type, height=550, width=1000, 
                               color_category='category20b', x_is_date=True, 
                               x_axis_format="%d %b %Y", focus_enable=True) 
    ydata = data_extract(249,b)
    xdata = list(range(len(ydata))) 
    xdata = [start_time + x * 86400000 for x in xdata] 
    extra_serie = {"tooltip": {"y_start": "There was ", "y_end": " J/cm<sup>2"}, 
           "date_format": "%d %b %Y"} 
    chart.add_serie(name = 'Energie in J/cm<sup>2', y=ydata, x=xdata, extra=extra_serie)
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
    import time 
    start = time.clock()
    from nvd3 import lineChart
    import datetime


    year = 2000 +(18-b)
    start_time = int(time.mktime(datetime.datetime(year, 4, 1).timetuple()) * 1000) 
    type = "lineChart" 
    chart = lineChart(name=type, x_is_date=True, x_axis_format="%d %b %Y") 
    
    ydata = data_extract(249,b)

    xdata = list(range(len(ydata))) 
    xdata = [start_time + x * 86400000 for x in xdata] 
    kwargs1 = {'color': '#66b3ff'} 

    extra_serie = {"tooltip": {"y_start": "There was ", "y_end": " J/cm<sup>2"}} 
    chart.add_serie(y=ydata, x=xdata, name='Zonne-energie', extra=extra_serie, **kwargs1) 
    
    
    chart.buildhtml() 
    tijd = start - time.clock()    
    result = chart.htmlcontent

    
    return result


