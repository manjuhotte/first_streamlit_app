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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)



