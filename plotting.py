from motion_detection2 import df
from bokeh.plotting import figure, show, output_file

p=figure(width=700,height=400,x_axis_type="datetime",title="Motion detector graph")
p.yaxis.minor_tick_line_color=None #to remove the precission lines in the scale 
# p.ygrid.grid_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1
q=p.quad(left=df['start'],right=df['end'],bottom=0,top=1, color='red')
output_file('graph.html')
show(p)
