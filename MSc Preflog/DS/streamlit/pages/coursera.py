# import streamlit as st
# import pandas as pd

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'San Francisco', 'Los Angeles']
# }

# df = pd.DataFrame(data)

# st.table(df)

# import streamlit as st
# import pandas as pd

# st.title("Upload and Display CSV File")

# uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# if uploaded_file is not None:
#     # Read the CSV file
#     df = pd.read_csv(uploaded_file)
    
#     # Display the dataframe
#     st.write("Data from the CSV file:")
#     st.dataframe(df)
# else:
#     st.write("Please upload a CSV file to see its contents.")

# import streamlit as st
# import pandas as pd

# st.title("Load CSV from File Path")

# # Let user input the file path (or hardcode it)
# file_path = st.text_input("Enter the CSV file path", "/home/student/msc-74/vs/coursera_courses.csv")

# try:
#     df = pd.read_csv(file_path)
#     st.write("Data loaded successfully:")
#     st.dataframe(df)
# except FileNotFoundError:
#     st.error("File not found. Please check the path and try again.")
# except Exception as e:
#     st.error(f"Error loading file: {e}")

# import streamlit as st
# import pandas as pd

# st.set_page_config(layout="wide")
# st.title("CSV with Auto Serial Number")

# file_path = "/home/student/msc-74/vs/coursera_courses.csv"

# try:
#     # Load CSV
#     df = pd.read_csv(file_path)
    
#     # Reset index and add sr.no starting from 1
#     df = df.reset_index(drop=True)
#     df.insert(0, "sr.no", df.index + 1)
    
#     # Display dataframe
#     st.dataframe(df, width=1200, height=800)

# except FileNotFoundError:
#     st.error("File not found at: " + file_path)
# except Exception as e:
#     st.error(f"Error: {e}")


import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("CSV Table with Serial Number")

file_path = "/home/student/msc-74/vs/coursera_courses.csv"

try:
    df = pd.read_csv(file_path)
    df = df.reset_index(drop=True)  # reset index to 0,1,2...
    df.insert(0, "sr.no", df.index + 1)  # add serial number starting at 1

    st.success("CSV loaded successfully!")
    st.dataframe(df, width=1200, height=800)

except FileNotFoundError:
    st.error("File not found. Please check the file path.")
except Exception as e:
    st.error(f"An error occurred: {e}")
