import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def get_tesla_facilities():
    start_url = "https://en.wikipedia.org/wiki/Tesla,_Inc."

    # Download the HTML from start_url
    downloaded_html = requests.get(start_url)

    # Parse the HTML with BeautifulSoup and create a soup object
    soup = BeautifulSoup(downloaded_html.text)

    # Select table.wikitable
    full_table = soup.select('table.wikitable tbody')[0]
    # print(full_table)

    # Extract the table column headings
    # End result: A list with all the column headings

    regex = re.compile('_\[\w\]')

    table_head = full_table.select('tr th')
    table_columns = []
    for element in table_head:
        column_label = element.get_text(separator=" ", strip=True)  # replace breaks with space
        column_label = column_label.replace(" ", "_")
        column_label = regex.sub('', column_label)  # strip off words within []
        table_columns.append(column_label)
    # print(table_columns)

    # Extract the table data (rows)
    # End result: A multi-dimensional list containing a list for each row

    table_rows = full_table.select('tr')[1:]
    # print(table_rows)

    table_data = []
    for element in table_rows:
        row_data = element.select('td')
        row_list = [item.text.strip() for item in row_data]
        table_data.append(row_list)
    # print(table_data)

    # Create a Pandas DataFrame

    df = pd.DataFrame(table_data, columns=table_columns)
    return df


if __name__ == '__main__':
    tesla_facilities = get_tesla_facilities()
    print(tesla_facilities)

