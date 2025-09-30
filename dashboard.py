import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# #paikallinen
# df = pd.read_csv("tietojarjestelmaluettelo_2023.csv", sep=";")

#githubissa oleva tiedosto
url = "https://raw.githubusercontent.com/hudegit/IT00EH51-3001-tehtava-dashboard/refs/heads/main/tietojarjestelmaluettelo_2023.csv"
df = pd.read_csv(url, on_bad_lines='skip', sep=";")

st.title("Oulun kaupungin tietojärjestelmäluettelo")
st.header("Koko aineisto")
st.write(df)

järjestelmätoimittajat = df["Toimittajat"].unique()

st.header("Kaikki järjestelmätoimittajat")
st.write(järjestelmätoimittajat)

järjestelmätoimittajat = df["Toimittajat"].unique()
unique_count = len(järjestelmätoimittajat)
st.write(f"Järjestelmätoimittajien määrä: {unique_count}")


Yksikkö = df["Yksiköt"].unique()

st.header("Kaikki yksiköt")
st.write(Yksikkö)

järjestelmätoimittajat = df["Yksiköt"].unique()
unique_count = len(Yksikkö)
st.write(f"Yksikköjen määrä: {unique_count}")


#ei tahdo toimia pie charttina
# yksikkö_määrä = df["Yksiköt"].value_counts()

# fig, ax = plt.subplots(figsize=(50, 50))
# ax.pie(yksikkö_määrä.values, labels=yksikkö_määrä.index, autopct="%1.1f%%", textprops={"fontsize": 22})
# ax.set_title("Yksiköt")

# st.pyplot(fig)

st.header("Graafeja")
toimittaja_maa = df["Sijainti"].value_counts()

fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(toimittaja_maa.values, labels=toimittaja_maa.index, autopct="%1.1f%%", textprops={"fontsize": 10})
ax.set_title("Maantieteellinen alue josta järjestelmät toimitetaan")

st.pyplot(fig)

#kaikki yksiköt
yksikkö_määrä = df["Yksiköt"].value_counts().sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(15, 15))
ax.barh(yksikkö_määrä.index, yksikkö_määrä.values)

ax.set_title("Yksiköt joihin toimitettu", fontsize=18)
ax.set_xlabel("Määrä", fontsize=14)
ax.set_ylabel("Yksikkö", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=15)

st.pyplot(fig)

#siistitty versio
yksiköt_filteröity = df["Yksiköt"].str.split(',').str[0].str.strip()
yksikkö_määrä = yksiköt_filteröity.value_counts().sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(15, 15))
ax.barh(yksikkö_määrä.index, yksikkö_määrä.values)

ax.set_title("Yksiköt joihin toimitettu, filteröity versio", fontsize=18)
ax.set_xlabel("Määrä", fontsize=14)
ax.set_ylabel("Yksikkö", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=15)

st.pyplot(fig)