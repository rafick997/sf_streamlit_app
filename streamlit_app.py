
import streamlit
import pandas
streamlit.title("Parents cooking dinner")
streamlit.header("Dinner menu")
streamlit.text("Item 1")
streamlit.text("Item 2")
streamlit.text("Item 3")
streamlit.text("Enjoy!")


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some items:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
