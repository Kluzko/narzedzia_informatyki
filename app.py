import streamlit as st
import pandas as pd
import plotly.express as px

# Ladowanie danych 
@st.cache_data
def load_data(file_path):
    sheet_names = pd.ExcelFile(file_path).sheet_names
    return {name: pd.read_excel(file_path, sheet_name=name) for name in sheet_names}

# Czyszczenie 
def process_data(sheet_df):
    age_data = sheet_df.iloc[10:29, 0].apply(lambda x: x.strip().replace('lat', '').replace('lata', '').replace('a', ''))
    df_age = pd.DataFrame(columns=age_data)
    df_age.loc[0] = sheet_df.iloc[10:29, 1].values

    disease_columns = sheet_df.iloc[5, 2:21].values
    df_disease = pd.DataFrame(columns=disease_columns)
    df_disease.loc[0] = sheet_df.iloc[9, 2:21].values

    return df_age, df_disease

# Tworzenie wykresu schodkowego
def create_bar_chart(data, title):
    data_transposed = data.T
    data_transposed.columns = ['Count']
    fig = px.bar(data_transposed, x=data_transposed.index, y='Count')
    fig.update_layout(title=title, xaxis_title='Age Group', yaxis_title='Count')
    return fig

# Tworzenie wykresu kolowego
def create_pie_chart(data, title, disease_dict):
    data_transposed = data.T
    data_transposed.columns = ['Count']

    data_transposed['Disease Name'] = data_transposed.index.map(disease_dict)

    fig = px.pie(data_transposed, names='Disease Name', values='Count', title=title, hover_data=['Count'], labels={'Disease Name': ''})

    fig.update_layout(showlegend=False)

    return fig

def main():
    df_dict = load_data("dane.xlsx")

    # Tworzenie slownika key -value dla chrob i ich kodow
    disease_info = df_dict["Objaśnienia"].iloc[:19, :2]
    disease_dict = dict(zip(disease_info["s"], disease_info["Rozdziały klasyfikacji ICD-10"]))

    st.title('Zgony według przyczyn w 2020 Roku')
    selected_sheet = st.selectbox('Wybierz arkusz', [sheet for sheet in df_dict.keys() if sheet != 'Objaśnienia'])

    # Przetwarzanie i wizualizacja danych
    if selected_sheet:
        df_age, df_disease = process_data(df_dict[selected_sheet])
        fig = create_bar_chart(df_age, f'Wizulizacja zgonow wg wieku {selected_sheet}')
        pie_fig = create_pie_chart(df_disease, f'Wizulizacja zgonow wg chorob {selected_sheet}', disease_dict)
        st.plotly_chart(fig)
        st.plotly_chart(pie_fig)

if __name__ == "__main__":
    main()
