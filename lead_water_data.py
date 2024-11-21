import pandas as pd

lead_water_df = pd.read_csv('lead_water.csv')

def __get_street_name__(address):
    text_attributes = []

    attributes = address.split(' ')

    for attr in attributes:
        if attr and not attr.isdigit():
            text_attributes.append(attr)

    if len(text_attributes) < 2:
        return ''

    return ' '.join(text_attributes)

def has_lead_water(address):
    street_name = __get_street_name__(address)

    if street_name and lead_water_df['Street Name'].str.contains(street_name.upper()).any():
        return True
    return False
