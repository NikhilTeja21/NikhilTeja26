from cProfile import label
from datetime import date
from turtle import home
from typing import Any, Tuple
from numpy import square, true_divide
from pyparsing import anyCloseTag
import streamlit as s
from streamlit_lottie import st_lottie
import requests
from PIL import Image

#Above modules should be imported for all the features to make your website adore.
#Import them in your command prompt from your python idle 
#Type "python install pip", then you can install all other modules using pip.
# "pip install __Module name__" for all the modules not for streamlit
#For streamlit lottie we have other commands, I'll soon provide all the commands to install them.


page_name = s.set_page_config(page_title="My Introduction",page_icon=":star2:",layout="wide",menu_items={}) #--Main settings for website name,layout,Icon,Menu.. etc.
s.title("Web Development")
s.header("Introduction")
"""
    - This is a Demo Website
    - Just for practising how website is developed
    - What are the in-builts and functions and graphical contents 
    - To learn the structure 
    - How to make my website good looking in future
"""
s.write("---------")
img1 = Image.open("F:\OneDrive\Pictures\Screenshots\img1.png")
#Provide path of an image that you want to add
with s.container() :
    image_column, text_column = s.columns(2)
    with image_column :
        s.image(img1,width=500)
    with text_column :
        s.write("Images can be inserted and can be resized")
s.time_input(label="Time",key="Key",help="This generates a ? mark at the topo right to know what we've prvided.",kwargs="WidgetKwargs") #--24 Hrs time format
s.balloons()  #--Creates something interesting stuff
s.bar_chart(data=[2,3,4,5,4.9,9.73,2.34,6.75],width=10,height=500)
#s.camera_input(label="Click a photo",key=3,on_change='600x200.png')
s.checkbox(label="I agree to the terms and conditions",value=False,help="Please read the above data properly") #--False makes checkbox is not checked, -True makes box Checked
""" 
    - A check box can be used to agreeing terms and conditions
    - The terms and conditions can be displayed by using help= and a ? will be displayed at the top then we can check the box
"""
s.button(label="Next",key=1,disabled=False)
#s.date_input(label="Enter your DOB : ",value=[21,8,2001],min_value=[1,1,1950],max_value=[1,1,2150])
s.color_picker(label="Pick a color : ",value="#00FFAA",key=1)
#s.plotly_chart(figure_or_data=[1,2,3,4,5,6],use_container_width=False,sharing="StreamLit")
s.code(body="print('Hey man.!')",language="python")
with s.container() :
    left, middle, right = s.columns(3)
    with left :
        s.number_input(label="Enter your Number : ",min_value=0,value=100000000,step=1)
    with middle :
        ""
    with right :
        s.file_uploader(label="Select a file to upload",type=[".png",".pdf",".jpeg",".ppt",".pptx","html"],accept_multiple_files=True,help="*File size should be less than 5MB")
        """
            - We can upload any files and we can also mention the files what kind we can upload
            - .png,.jpeg,.pdf..... etc
        """
# s.form(s.form_submit_button(label="Submit"))
s.__loader__
s.text_input(label="Enter text here...",value="",max_chars=10000,autocomplete="")
#s.graphviz_chart(figure_or_dot=Any,use_container_width=False) --Unhandled error
s.caption(body=Any,unsafe_allow_html=False)
s.line_chart(data=[12,32,43,9,26,14,21,18],width=200,height=500,use_container_width=True)
s._arrow_bar_chart(data=[27.32,15.85,49.32,26.21,14.26,26.18,37.26],width=200,height=500,use_container_width=True)
