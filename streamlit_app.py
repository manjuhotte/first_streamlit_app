import streamlit


streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Menu')
streamlit.text('Idli vada')
streamlit.text('Dosai')
streamlit.text('Ricebath')


streamlit.header('Breakfast Menu 2')
streamlit.text('Omega3 and blueberrry oat meal')
streamlit.text('kale, spinach and rocket smotthie')
streamlit.text('Hard boiled egg')

streamlit.header('Breakfast Favorites')
streamlit.text('🥙Omega3 and blueberrry oat meal')
streamlit.text('🧀kale, spinach and rocket smotthie')
streamlit.text('🍗Hard boiled egg')

streamlit.header('🍧🥧Build your own best fruit smoothies')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)



