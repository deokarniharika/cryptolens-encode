import streamlit as st
import matplotlib.pyplot as plt
import psycopg2
import plotly.express as px

st.markdown("## Dashboard")

# Define your database connection parameters
connection = psycopg2.connect(
    host="34.77.163.253",  # CloudSQL instance IP
    port="5432",            # Default PostgreSQL port, update if different
    dbname="dojo_data",  # Replace with your database name
    user="i-can-only-read-gmx-data",        # Replace with your username
    password="house-football-checksum-11"     # Replace with your password
)

# Create a cursor to interact with the database
cursor = connection.cursor()

cursor.execute("SELECT * FROM hackathon_arbitrum_events LIMIT 10;")
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

query="""
SELECT 
    event_data ->> 'recipient' AS recipient,
    COUNT(*) AS swap_count,
    SUM(gas) AS total_gas,
    AVG(gas_price) AS avg_gas_price,
    MIN(block_timestamp) AS first_swap_time,
    MAX(block_timestamp) AS last_swap_time
FROM 
    hackathon_ethereum_events 
WHERE 
    event_name='Swap' AND
    block_timestamp BETWEEN '2024-07-01' AND '2024-07-31'
GROUP BY
    recipient
ORDER BY
    swap_count DESC
LIMIT 100000;
"""
df_r = pd.read_sql(query, connection)
df_r.head(5)

query='''
SELECT event_name, COUNT(*) AS count
FROM hackathon_ethereum_events
GROUP BY event_name;
'''
df_eth_eventnames = pd.read_sql(query, connection)
df_eth_eventnames.head(5)

threshold = 6000

above_threshold = df_eth_eventnames[df_eth_eventnames['count'] >= threshold]
below_threshold = df_eth_eventnames[df_eth_eventnames['count'] < threshold]

other_row = pd.DataFrame([['Other', below_threshold['count'].sum()]], columns=['event_name', 'count'])

# Combine the above-threshold rows with the new "Other" row
df_eth_eventnames = pd.concat([above_threshold, other_row], ignore_index=True)

fig = px.pie(df_eth_eventnames, values=df_eth_eventnames['count'], names=df_eth_eventnames['event_name'], title="Distribution of event names for Ethereum")
# Plot!
st.plotly_chart(fig, use_container_width=True)

#--------------------------------

query ='''
SELECT 
    CASE 
        WHEN event_name IN ('EventLog1', 'EventLog2') 
        THEN event_data ->> 'eventName'
        ELSE event_name
    END AS event_name,
    COUNT(*) AS count
FROM hackathon_arbitrum_events
GROUP BY 
    CASE 
        WHEN event_name IN ('EventLog1', 'EventLog2') 
        THEN event_data ->> 'eventName'
        ELSE event_name
    END;
'''

df_arb = pd.read_sql(query, connection)
df_arb.head(5)

threshold = 100000

# Separate rows above and below the threshold
above_threshold = df_arb[df_arb['count'] >= threshold]
below_threshold = df_arb[df_arb['count'] < threshold]

# Summing the counts below the threshold
other_row = pd.DataFrame([['Other', below_threshold['count'].sum()]], columns=['event_name', 'count'])

df_arb = pd.concat([above_threshold, other_row], ignore_index=True)

fig = px.pie(df_arb, values=df_arb.iloc[:,1], names=df_arb.iloc[:,0], title="Distribution of event names for Arbitrum")

# Plot!
st.plotly_chart(fig, use_container_width=True)

#--------------------------------

st.write("  ")
st.write(" ")
st.write(" ")
st.write(" ")

st.write(f"**Cumulative total over time- difference between burn and mint.**")
query='''
SELECT event_name, block_timestamp, event_data -> 'amount0' AS amount0, event_data -> 'amount1' AS amount1
FROM hackathon_ethereum_events
WHERE event_name IN ('Burn', 'Mint');
'''
df_mb = pd.read_sql(query, connection)
df_mb.head(5)

filtered_df = df_mb[(df_mb['amount0'] == 0) | (df_mb['amount1'] == 0)]

# Create a new column 'total_amount' which is the sum of amount0 and amount1
filtered_df['total_amount'] = filtered_df['amount0'] + filtered_df['amount1']
filtered_df = filtered_df.drop(['amount0','amount1'],axis=1)
filtered_df.head(5)

filtered_df['total_amount'] = filtered_df.apply(lambda x: x['total_amount'] if x['event_name'] == 'Mint' else -x['total_amount'], axis=1)
filtered_df.head(5)

import pandas as pd
import streamlit as st

# Assuming `filtered_df` is already defined and processed as per your code

# Step 1: Convert block_timestamp to datetime
filtered_df['block_timestamp'] = pd.to_datetime(filtered_df['block_timestamp'])

# Step 2: Sort DataFrame by block_timestamp
filtered_df = filtered_df.sort_values('block_timestamp')

# Step 3: Calculate cumulative sum of total_amount as float
# Check for large values and convert to float if necessary
filtered_df['total_amount'] = filtered_df['total_amount'].astype(float)
filtered_df['cumulative_amount'] = filtered_df['total_amount'].cumsum()

# Step 4: Plot cumulative total amount over time using Streamlit's line_chart
st.line_chart(filtered_df.set_index('block_timestamp')['cumulative_amount'])

#--------------------------------
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

st.write(f"**Cumulative total over time- difference between borrow and repay.**")

# Assuming `connection` is already established
query = '''
SELECT event_name, block_timestamp, event_data ->> 'amount' AS amount
FROM hackathon_ethereum_events
WHERE event_name IN ('Borrow', 'Repay');
'''
# Step 1: Read data from SQL query
df_bore = pd.read_sql(query, connection)

# Step 2: Convert amount to numeric, coerce errors to NaN
df_bore['amount'] = pd.to_numeric(df_bore['amount'], errors='coerce')

# Step 3: Transform amounts based on event name
df_bore['amount'] = df_bore.apply(lambda x: x['amount'] if x['event_name'] == 'Repay' else -x['amount'], axis=1)

# Step 4: Convert block_timestamp to datetime
df_bore['block_timestamp'] = pd.to_datetime(df_bore['block_timestamp'])

# Step 5: Sort DataFrame by block_timestamp
df_bore = df_bore.sort_values('block_timestamp')

# Step 6: Calculate cumulative sum of amount
df_bore['cumulative_amount'] = df_bore['amount'].cumsum()

# Step 7: Plot cumulative total amount over time using Streamlit's line_chart
st.line_chart(df_bore.set_index('block_timestamp')['cumulative_amount'])

#--------------------------------






