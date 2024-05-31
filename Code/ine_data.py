import pandas as pd


# function to preprocess the files
def get_last_data(ine_file, ine_type='income'):
    variables = 'Indicadores de renta media' if ine_type == 'income' else 'Indicadores demográficos' \
        if ine_type == 'demo' else "error"
    if variables != 'error':
        ine_file = ine_file[['Secciones', variables, 'Periodo', 'Total']]
        ine_file = ine_file[ine_file['Secciones'].notnull()]
        ine_file['section'] = ine_file['Secciones'].apply(lambda x: str(x)[:10])
        ine_file.drop(['Secciones'],axis=1,inplace=True)
        # the table has data for a few years and we only need the last year
        last_data = ine_file['Periodo'].max()
        ine_file_last_data = ine_file[ine_file['Periodo'] == last_data]
        ine_file_last_data['Total'] = pd.to_numeric(ine_file_last_data['Total'], errors='coerce')
        pivot_ine_data = ine_file_last_data.pivot_table(
             index='section',
             columns=variables,
             values='Total'
        )
        return pivot_ine_data
    else:
        raise ValueError("The ine_type of data file is incorrect. Must be demo or income")


# function to get data for specific section
def get_section_data(pivot_data, section, printing=0):
    padded_section = str(section).zfill(10)
    section_data = pivot_data[pivot_data.index == padded_section]
    if printing == 1:
        for c in pivot_data.columns:
            print(f'The indicator: {c} for section {section} is {pivot_data[c].iloc[0]}')
    return section_data

