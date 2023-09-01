import pandas as pd
import os
import calendar
import logging

def process_dataset_by_year_by_month(pathfile):
    """
    Generates a directory structure organized by year and generates 
    CSV files of orders within each folder, one per month.

    Args:
        path (str): The path to the input CSV file.

    Returns:
        None
    """
    if not os.path.exists(pathfile):
        raise FileNotFoundError(f"The file {pathfile} doesn't exist")
    
    df = pd.read_csv(pathfile)

    df['Order Date'] = pd.to_datetime(df['Order Date'], format="%m/%d/%Y")

    df = df.sort_values(by=['Order Date'])

    df['Year'] = df['Order Date'].dt.strftime('%Y')

    max_year = int(df['Year'].max())
    min_year = int(df['Year'].min())

    processed_folder = os.path.exists('orders')

    if not processed_folder:
        os.makedirs('orders', exist_ok=True)

    for year in range(min_year, max_year+1):
        output_folder = os.path.join('orders', str(year))
        os.makedirs(output_folder, exist_ok=True)
        df_year = df[(df['Order Date'] >= f'{year}-01-01') & (df['Order Date'] <= f'{year}-12-31')]
        for month in range(1, 13):
            df_month = df_year[df_year['Order Date'].dt.month == month]
            month_name = calendar.month_name[month]
            df_month.to_csv(f'orders/{year}/{month_name}_{str(year)[2:]}.csv', index=False)