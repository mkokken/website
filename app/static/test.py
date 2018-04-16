import numpy as np
import cgi
form = cgi.FieldStorage()
area =  form.getvalue('area')

z = np.cos(area)
print(z)