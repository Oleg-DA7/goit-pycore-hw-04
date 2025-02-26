# Завдання 1

import pandas as pd 
import numpy as np

def total_salary(path):
    try:
        df_salary = pd.read_csv(path, delimiter = ",", header = None, names = ['name', 'sum'])
    except FileNotFoundError:
        print(f'Can`t find file {path}')
        return None, None
    except IOError:
        print(f'An error occurred while reading the file {path}')
        return None, None

    if df_salary.empty:
        print(f'Please check the file {path}, it is missing data or invalid format.')
        return None, None
    elif np.isnan(df_salary['sum'][0]) or len(df_salary.columns) != 2:
        print(f'Invalid format file {path}')
        return None, None
    else: 
        return df_salary['sum'].sum(), df_salary['sum'].mean()


total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


# Завдання 2

def get_cats_info(path):
    result = []
    try:
        df_cats = pd.read_csv(path, delimiter=",", header = None, names = ['id', 'name', 'age'])
    except FileNotFoundError:
        print(f'Can`t find file {path}')
        return None
    except IOError:
        print(f'An error occurred while reading the file {path}')
        return None

    if df_cats.empty:
        print(f'Please check the file {path}, it is missing data or invalid format.')
        return None
    elif np.isnan(df_cats['age'][0]) or len(df_cats.columns) != 3:
        print(f'Invalid format file {path}')
        return None
    else: 
        for i, r in df_cats.iterrows():
            result.append({'id': f'{r['id']}', 'name': f'{r['name']}', 'age': f'{r['age']}'})
        return result

cats_info = get_cats_info("cats.txt")
print(cats_info)



