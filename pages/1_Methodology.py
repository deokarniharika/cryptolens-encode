import streamlit as st

# Define the text with a background color using HTML and CSS
text_with_background = """
<div style="background-color: #f0f8ff; padding: 10px; border-radius: 5px;">
    <p style="color: black; font-size: 16px;">The list below includes list of different Python libraries and lists used.</p>
</div>
"""

# Display the text box in Streamlit
st.markdown(text_with_background, unsafe_allow_html=True)

st.divider()

st.markdown(" ##### Streamlit")
st.write("Streamlit is an open-source Python library used for building interactive web applications for data science and machine learning projects quickly and easily. It allows developers to turn Python scripts into web applications with minimal effort and is particularly popular among data scientists and analysts who want to create and share data-driven apps without needing extensive web development knowledge.")

st.markdown(" ##### Pandas")
st.write("Pandas is a powerful and popular open-source Python library primarily used for data manipulation and analysis. Built on top of the NumPy library, Pandas provides flexible data structures, especially designed to work with labeled data.")

st.markdown(" ##### NumPy")
st.write("NumPy (short for Numerical Python is a foundational Python library used for scientific computing. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.")

st.markdown(" ##### Seaborn")
st.write("Seaborn is a Python data visualization library based on Matplotlib, providing a high-level interface for drawing attractive and informative statistical graphics. Seaborn makes it easy to explore and understand complex data by enabling you to create aesthetically pleasing plots with minimal code. It’s particularly popular for statistical data visualization, as it works seamlessly with Pandas DataFrames and supports a wide variety of plot types commonly used in data analysis.")

st.markdown(" ##### Matplotlib")
st.write("Matplotlib is a fundamental data visualization library in Python, providing tools to create static, animated, and interactive plots. It's highly flexible, allowing users to customize every aspect of a plot, and serves as the underlying engine for other visualization libraries like Seaborn and Pandas plotting.") 

st.markdown(" ##### PLotly Express")
st.write("Plotly Express is a high-level interface for creating interactive plots with Plotly, a popular Python library for data visualization. It allows users to create a variety of visualizations easily and quickly with minimal code, making it an excellent choice for exploratory data analysis and presenting results in an interactive format.")

st.markdown(" ##### Psycopg2")
st.write("Psycopg2 is a popular PostgreSQL adapter for the Python programming language. It allows Python code to interact with PostgreSQL databases, enabling developers to execute SQL commands, manage database connections, and perform various database operations within their Python applications. Psycopg2 is known for its efficiency and is widely used in web applications, data analysis, and backend development.")

st.markdown(" ##### Networkx")
st.write("NetworkX is a Python library for the creation, manipulation, and study of complex networks (graphs). It provides tools to work with both undirected and directed graphs, enabling users to perform various operations and analyses on network structures. NetworkX is widely used in fields such as social network analysis, biological network modeling, and transportation systems.")

