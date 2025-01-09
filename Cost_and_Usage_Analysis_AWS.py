import boto3
import mysql.connector
from datetime import datetime, timedelta

# AWS Client
ce_client = boto3.client(
    'ce', 
    region_name='us-east-1',
    aws_access_key_id='AKIA32XTIHSBEQR#####',
    aws_secret_access_key='/dNzBX97/o4otAzJHyJkc9zTk5rDTp08AjR#####'
)

# Define start and end dates
start_date = datetime.strptime('2024-01-01', '%Y-%m-%d')
end_date = datetime.utcnow()

# Initialize an empty list to store all data
all_data = []

# Iterate over date ranges in chunks of 3 months
chunk_start_date = start_date
while chunk_start_date < end_date:
    chunk_end_date = min(chunk_start_date + timedelta(days=90), end_date)
    print(f"Fetching data from {chunk_start_date.strftime('%Y-%m-%d')} to {chunk_end_date.strftime('%Y-%m-%d')}")

    # Fetch data for the current chunk
    response = ce_client.get_cost_and_usage(
        TimePeriod={
            'Start': chunk_start_date.strftime('%Y-%m-%d'),
            'End': chunk_end_date.strftime('%Y-%m-%d')
        },
        Granularity='DAILY',
        Metrics=['BlendedCost', 'UnblendedCost', 'UsageQuantity'],
        GroupBy=[
            {'Type': 'DIMENSION', 'Key': 'SERVICE'}
        ]
    )

    # Parse and append data
    for result in response['ResultsByTime']:
        for group in result['Groups']:
            row = {
                'report_date': result['TimePeriod']['Start'],
                'service': group['Keys'][0],
                'blended_cost': float(group['Metrics']['BlendedCost']['Amount']),
                'unblended_cost': float(group['Metrics']['UnblendedCost']['Amount']),
                'usage_quantity': float(group['Metrics']['UsageQuantity']['Amount']),
            }
            all_data.append(row)

    # Move to the next chunk
    chunk_start_date = chunk_end_date

# Connect to MySQL and insert data
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='@Prath91##',
    database='aws_cost_data'
)
cursor = connection.cursor()

insert_query = """
    INSERT INTO aws_cost_usage (
        report_date, service, blended_cost, unblended_cost, 
        usage_quantity
    )
    VALUES (%s, %s, %s, %s, %s)
"""
cursor.execute("TRUNCATE TABLE aws_cost_usage")

for row in all_data:
    cursor.execute(insert_query, (
        row['report_date'], row['service'], row['blended_cost'], 
        row['unblended_cost'], row['usage_quantity']
    ))

connection.commit()
print(f"{cursor.rowcount} rows inserted into MySQL.")

cursor.close()
connection.close()
