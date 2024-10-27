import pandas as pd
import streamlit as st
import plotly.express as px

#set page size
st.set_page_config(layout="wide")

#add a disclaimer
agree = st.checkbox('I agree to the terms and conditions') 
st.write('Agreement status:', agree)

# dashboard title
st.title('Air Passengers Dashboard')

#import data
df = pd.read_csv('airpassengers.csv')

#sought to create a combined bar plot to showcase another way to view the data
#fig = px.bar(airpassengers.csv, x='month', y='#passengers')
#fig.show()

st.dataframe(df)

#the attempt is to look at these three things desiring to be tracked as a stakeholder
#which year had the highest # of passengersoverall
#which month or months had the highest # of passengers overall
#which consecutive months had drops in passengers flying

# Rename columns
df = df.rename(column={'Month': 'Year-Month',})

print(df)

st.header()

# Save DataFrame to new CSV (attempting to edit data to be more readable)
df.to_csv('modified_file.csv', index=False)

# Splitting the 'Month' column based on 'Month and year'
df[['Year', 'Month']] = df['Month'].str.split('_', expand=True)

month = df["Month"].unique()

#offering the option to select a month to view individual data (experiment)
month_selected = st.selectbox("Select Month", month)

#wanting to show only the selected month data
selected_month_df = df[df["month"]] == month_selected

#create dataframe with sum of passengers based on year
df_summed = selected_month_df.groupby("month").agg({"#passengers":"sum"})


#explaning metrics and wanting to calculate total passengers per year (experiment)
col1.metric("Total Passengers", df_summed["#passengers"])

# creating a Sub Header for emblishment
st.subheader("Main figures", divider='purple')
col1 = st.columns(1)

# Ensure date column is datetime format (experiment)
df['month'] = pd.to_datetime(df['month'])

# Split data by year (experiment)
data_by_year = {year: df[df['month'].dt.year == year] for year in df['month'].dt.year.unique()}

# Display the data for each year (experiment)
for year, data in data_by_year.items():
    print(f"pd.read_csv('airpassengers.csv') for {year}:\n{pd.read_csv('airpassengers.csv')}\n")

#creating data to get a sum of total passengers for each year (experiment)
# Step 1: Calculate the sum total of values for each category
# Group by 'month' and sum the '#passengers' column
sum_df = df.groupby('month', as_index=False)['value'].sum()

# Step 2: Rename the columns if necessary for clarity
sum_df.columns = ['month', 'total passengers']

# Step 3: Display the new DataFrame
print(sum_df)



