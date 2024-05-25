import streamlit as st
import pandas as pd
import plotly.express as px

# Einführungstext
st.title("Willkommen zur Datenvisualisierungs-App von ulricdo1")
st.markdown("""
Diese App lädt ein Beispiel-Datenset von Pinguinen aus dem Netz und stellt es interaktiv dar. Die Daten können nach verschiedenen Kriterien gefiltert und visualisiert werden.

### Funktionen:
1. **Datenanzeige:** Die App zeigt die Rohdaten in einer Tabelle an.
2. **Interaktive Filter:** Wähle eine Pinguinart und die minimale Flossenlänge aus, um die Daten zu filtern.
3. **Visualisierung:** Ein Streudiagramm stellt die Beziehung zwischen Flossenlänge und Körpermasse der gefilterten Daten dar.

Viel Spass bei der Pinguin-Entdeckung :) !
""")

# Laden des Datensets aus dem Netz und Caching der Daten
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

# URL zum Datenset
data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
df = load_data(data_url)

#Datenreinigung und Aufbereitung
@st.cache_data
def fetch_and_clean_data(df):
    # Beispiel für Datenbereinigung: Entfernen von fehlenden Werten
    df_cleaned = df.dropna()
    return df_cleaned

# Daten bereinigen
df_cleaned = fetch_and_clean_data(df)

# Anzeige der Daten in einer Tabelle
st.subheader("Rohdaten")
st.write(df_cleaned.head())

# Benutzersteuerung durch Radio-Buttons und Slider
species = st.radio("Wähle eine Pinguinart aus:", df_cleaned['species'].unique())
flipper_length = st.slider("Wähle die Flossenlänge:", int(df_cleaned['flipper_length_mm'].min()), int(df_cleaned['flipper_length_mm'].max()))

# Filtern der Daten basierend auf Benutzerauswahl
filtered_data = df_cleaned[(df_cleaned['species'] == species) & (df_cleaned['flipper_length_mm'] >= flipper_length)]

# Anzeige der gefilterten Daten in einer Tabelle
st.subheader("Gefilterte Daten")
st.write(filtered_data)

# Erstellung und Anzeige eines Streudiagramms
st.subheader("Streudiagramm: Flossenlänge vs. Körpermasse")
fig = px.scatter(filtered_data, x='flipper_length_mm', y='body_mass_g', color='species', title='Flossenlänge vs. Körpermasse')
st.plotly_chart(fig)
