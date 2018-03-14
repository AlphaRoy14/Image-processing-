from motion_detection2 import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool ,ColumnDataSource

#columndatasource is a satndardisied way to provode datat to a bokeh data plot, some functions need
#this instead of dataframes

df['start_string']=df['start'].dt.strftime('%y-%m-%d %H-%M-%S')
df['end_string']=df['end'].dt.strftime('%y-%m-%d %H-%M-%S')


hover=HoverTool(tooltips=[("start","@start_string"),("end","@end_string")])

#@start_string is a decorator


cds=ColumnDataSource(df)
p=figure(width=700,height=400,x_axis_type="datetime",title="Motion detector graph")
p.yaxis.minor_tick_line_color=None #to remove the precission lines in the scale 
# p.ygrid.grid_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1
q=p.quad(left='start',right='end',bottom=0,top=1, color='red',source=cds)
p.add_tools(hover)
output_file('graph.html')

show(p)
