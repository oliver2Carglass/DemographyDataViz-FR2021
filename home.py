import plotly.graph_objects as go
import streamlit as st
from streamlit_option_menu import option_menu as option_menu 
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import json
import base64
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import altair as alt

st.set_page_config(layout='wide')

coder="animations/Animation1.json"
mail="animations/Animation2.json"

p1= Image.open("images/p1.png")

def load_lot(url):
    r = requests.get(url)
    if r.status_code!= 200 : 
        return None
    else :
        return r.json()

def load_local_animation(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

# @st.experimental_memo
def get_image_as_base64(img):
    with open(img, "rb") as f :
        data = f.read()
    return base64.b64encode(data).decode()


pro1=get_image_as_base64("images/p1.png")
pro2=get_image_as_base64("images/p2.png")
pro3=get_image_as_base64("images/p3.png")


css = f"""
<style>
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(3) > div > pre > div > code > span{{
    font-size: 60px;
   
}}



.pro{{
    
    height: 350px;
    border-radius: 25px;
    
    display: flex;
    flex-direction:row;
    gap: 15px;
    margin: 15px 7% 15px 3%;
    border: 10px solid rgba(189, 189, 223, 0.075);
    box-shadow: 
        rgba(0, 0, 0, 0.24) 0px 3px 8px, /* Existing semi-transparent shadow */
        rgba(0, 0, 0, 1) 0px 0px 1px; /* New opaque black shadow */
}}

.pro:hover{{
    box-shadow: 
        rgba(0, 0, 0, 0.50) 0px 3px 8px, /* Existing semi-transparent shadow */
        rgba(0, 0, 0, 1) 0px 0px 1px; /* New opaque black shadow */
    cursor:pointer;
    background-color: rgba(189, 189, 223, 0.2) ;
}}
.ima{{
    border-radius: 15px;
    border: 1px solid black;
    margin: 45px;
    width: 250px;
    height: 250px;
    background-size: cover;      
    background-position: center; 
    background-repeat: no-repeat;
    box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
}}

#p1{{
    background-image: url('data:image/png;base64,{pro1}');
}}
#p2{{
    background-image: url('data:image/png;base64,{pro2}');
}}
#p3{{
    background-image: url('data:image/png;base64,{pro3}');
}}

h3{{
    margin-top: 50px;
    font-size: 35px;
}}

h4{{
    font-size: 23px;
    font-family: 'Courier New', Courier, monospace;
    color: grey;
}}
a {{
    font-size: 18px;
}}

#form{{
    display: flex;
    flex-direction: column;
    background-color: rgba(189, 189, 223, 0.3);
    height: 500px;
    width: 800px;
    border-radius: 25px;
    border: 10px solid rgba(189, 189, 223, 0.075);
    box-shadow: 
        rgba(0, 0, 0, 0.24) 0px 3px 8px, /* Existing semi-transparent shadow */
        rgba(0, 0, 0, 1) 0px 0px 1px; /* New opaque black shadow */
    
   
}}
input{{
    margin-left: 5%;
    margin-right: 15%;
}}
textarea{{
    margin-left: 5%;
    margin-right: 15%;
}}
label{{
    margin-left: 5%;
    margin-right: 15%;
}}
.lottie-animation {{
        margin-left: 1500px;
    }}

/* From Uiverse.io by kamehame-ha */ 
.button1 {{
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 25px 35px;
  gap: 15px;
  background-color: #181717;
  outline: 3px #181717 solid;
  outline-offset: -3px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  transition: 400ms;
}}

.button1 .text {{

  color: white;
  font-weight: 700;
  font-size: 1em;
  transition: 400ms;
}}

.button1 svg path {{
  transition: 400ms;
}}

.button1:hover {{
  background-color: transparent;
}}

.button1:hover .text {{
  color: #181717;
}}

.button1:hover svg path {{
  fill: #181717;
}}

.st-emotion-cache-463q5x .token.string{{
    color: #FF4B4B;
}}

pre{{
    border: 3px solid black;
    width:100%;
}}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

    


# Fonction pour la page d'accueil
def home():
    st.title("Bienvenue sur mon site :)")
    st.write("Bienvenue sur la page d'accueil !")
    
    with st.container():
        col1,col2 = st.columns(2)
        with col1 :
            st.write("Fait par by Jérémy VIOT le 17/10/2024")
            st.write('##')
            st.subheader("Je suis un futur ingénieur en science du numérique passionné par l'IA et la donnée")
        with col2:
            ani_code = load_local_animation(coder)
            if ani_code:
                st_lottie(ani_code, height='500px')























# Fonction pour la page A
def page_a():

    st.title("A Propos de moi")
    st.write("Voici mes reseaux :")
    st.markdown("""
<div style='display:flex; flex-direction: row;'>
  <button class="button0" onclick="window.location.href='https://www.linkedin.com/in/jeremy-viot-66a12a222/';"> 
    <svg viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill="none">
      <path fill="#ffffff" d="M12.225 12.225h-1.778V9.44c0-.664-.012-1.519-.925-1.519-.926 0-1.068.724-1.068 1.47v2.834H6.676V6.498h1.707v.783h.024c.348-.594.996-.95 1.684-.925 1.802 0 2.135 1.185 2.135 2.728l-.001 3.14zM4.67 5.715a1.037 1.037 0 01-1.032-1.031c0-.566.466-1.032 1.032-1.032.566 0 1.031.466 1.032 1.032 0 .566-.466 1.032-1.032 1.032zm.889 6.51h-1.78V6.498h1.78v5.727zM13.11 2H2.885A.88.88 0 002 2.866v10.268a.88.88 0 00.885.866h10.226a.882.882 0 00.889-.866V2.865a.88.88 0 00-.889-.864z"></path>
    </svg>
    Continue with LinkedIn
  </button>

  <style>
    .button0 {
      display: flex;
      background-color: #0A66C2;
      color: #ffffff;
      padding: 0.5rem 1.4rem;
      font-size: 0.875rem;
      line-height: 1.25rem;
      font-weight: 700;
      text-align: center;
      vertical-align: middle;
      align-items: center;
      border-radius: 0.5rem;
      gap: 0.75rem;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
      transition: .6s ease;
    }

    .button0 svg {
      height: 30px;
    }

    .button0:hover {
      box-shadow: none;
    }
  </style>

  <button class="button2"> 
    <svg fill="#ffffff" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
      <g stroke-width="0" id="SVGRepo_bgCarrier"></g>
      <g stroke-linejoin="round" stroke-linecap="round" id="SVGRepo_tracerCarrier"></g>
      <g id="SVGRepo_iconCarrier"> 
        <title>github</title> 
        <rect fill="none" height="24" width="24"></rect> 
        <path d="M12,2A10,10,0,0,0,8.84,21.5c.5.08.66-.23.66-.5V19.31C6.73,19.91,6.14,18,6.14,18A2.69,2.69,0,0,0,5,16.5c-.91-.62.07-.6.07-.6a2.1,2.1,0,0,1,1.53,1,2.15,2.15,0,0,0,2.91.83,2.16,2.16,0,0,1,.63-1.34C8,16.17,5.62,15.31,5.62,11.5a3.87,3.87,0,0,1,1-2.71,3.58,3.58,0,0,1,.1-2.64s.84-.27,2.75,1a9.63,9.63,0,0,1,5,0c1.91-1.29,2.75-1,2.75-1a3.58,3.58,0,0,1,.1,2.64,3.87,3.87,0,0,1,1,2.71c0,3.82-2.34,4.66-4.57,4.91a2.39,2.39,0,0,1,.69,1.85V21c0,.27.16.59.67.5A10,10,0,0,0,12,2Z"></path> 
      </g>
    </svg>
    Continue with Github
  </button>

  <style>
    .button2 {
      display: flex;
      background-color: rgb(24, 23, 23);
      color: #ffffff;
      padding: 0.5rem 1.4rem;
      font-size: 0.875rem;
      line-height: 1.25rem;
      font-weight: 700;
      text-align: center;
      vertical-align: middle;
      align-items: center;
      border-radius: 0.5rem;
      gap: 0.75rem;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
      transition: .6s ease;
    }

    .button2 svg {
      height: 30px;
    }
  </style>
</div>
""", unsafe_allow_html=True)

    


  
    st.write("---")
    st.write("##")
    st.subheader('language skills :')
    with st.container():
        col3,col4 = st.columns(2)
        with col3 :
            st.subheader("Mon niveau d'anglais basé sur le TOEIC :")
            

            # Données pour le camembert
            labels = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'maybe S7']
            scores = [550, 620, 667, 715, 760, 815, 990]

            # Calcul des tailles des segments du camembert
            sizes = [scores[0]] + [scores[i] - scores[i - 1] for i in range(1, len(scores))]

            # Couleurs personnalisées
            colors = [
                'rgba(255, 0, 0, 0.3)',   # Rouge transparent
                'rgba(0, 255, 0, 0.3)',   # Vert transparent
                'rgba(0, 0, 255, 0.3)',   # Bleu transparent
                'rgba(255, 255, 0, 0.3)', # Jaune transparent
                'rgba(255, 0, 255, 0.3)', # Magenta transparent
                'rgba(0, 255, 255, 0.3)', # Cyan transparent
                'rgba(51, 51, 51, 0.5)'   # Gris foncé avec alpha 0.5 pour "Maybe S7"
            ]

            # Créer le camembert avec Plotly
            fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, 
                                        textinfo='percent+value', 
                                        hoverinfo='label+percent+value',
                                        marker=dict(colors=colors),
                                        pull=[0, 0, 0, 0, 0, 0, 0.1])])  # "maybe S7" légèrement détaché

            # Ajouter un titre au graphique
       

            # Afficher le graphique dans Streamlit
            st.plotly_chart(fig)
        with col4 :
            
            # Titre et sous-titre
            st.subheader('Mon niveau de Mandarin (je sais juste dire bonjour)')

            # Données pour le pie chart
            sizes = [0.1, 99.9]  # Les valeurs représentant 1% et 99%
            labels = ['juste "nǐ hǎo"', 'Le reste du language']  # Étiquettes pour chaque section

            # Couleurs personnalisées
            colors = [
                'rgba(51, 51, 51, 0.5)',  # Gris foncé avec alpha 0.5 pour 1%
                'rgba(204, 204, 204, 0.4)' # Gris clair avec alpha 0.4 pour 99%
            ]

            # Créer le camembert avec Plotly
            fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, 
                                        textinfo='percent+value', 
                                        hoverinfo='label+percent+value',
                                        marker=dict(colors=colors))])  # Pas de détachement ici

      

            # Afficher le graphique dans Streamlit
            st.plotly_chart(fig)
    st.write('---')
    col1, col2, col3 = st.columns([1, 7, 1])
    with col2 :
        data = {
        "Category": ["WebSite", "Python", "IA", "Data", "chrome-extension", "computer-science-knowledge"],
        "2022": [0.1, 0.4, 0.0, 0.0, 0.0, 0.25],
        "2023": [0.5, 0.15, 0.2, 0.1, 0.5, 0.25],
        "2024": [0.15, 0.40, 0.6, 0.6, 0.05, 0.25],
    }

        # Create the DataFrame
        df = pd.DataFrame(data)

        # Melt the DataFrame for easier plotting
        df_melted = df.melt(id_vars='Category', var_name='année', value_name='Value')


        # Create the Altair chart with overlapping bars
        chart = alt.Chart(df_melted).mark_bar().encode(
            x=alt.X('Category:O', title='Category'),
            y=alt.Y('Value:Q', title='Value'),
            color=alt.Color('année:N',
                            scale=alt.Scale(domain=['2022', '2023', '2024'], 
                                            range=['rgba(0, 128, 0, 0.5)',    # Green for 2022
                                                'rgba(0, 0, 255, 0.5)',     # Blue for 2023
                                                'rgba(0, 105, 180, 0.5)'])),
            tooltip=['Category', 'année', 'Value']
        ).properties(
            width=400,
            height=400,
            title='My Skills Bar Chart by Category and Year'
        ).configure_mark(
            opacity=0.8  # Adjust opacity of the bars
        )

        # Render the chart in Streamlit
        st.title("My skills using BAR CHART")

        st.altair_chart(chart, use_container_width=True)
    st.write("---")


    st.write("##")
    with st.container():
        col3,col4 = st.columns(2)
        with col3 :
            st.subheader("""
            Education :
            - EFREI (2021-2026)
            - ILAC (2023)
            - french BAC
                        """)
        with col4 :
            st.subheader("""
                        EXPERIENCES :
                        - 6 month InternShip In Darty Company (as project leader in AI data management)
                        - 5 month INRAE (as database developer)
                        - 1 month Manouche Malta (as waiter) 
""")





















# Fonction pour la page B
def page_b():
     with st.container():
        st.header("Mes projets")
        st.write('##')
        st.markdown("""
<span class='pro'>
    <div>
        <div id='p1' class="ima"></div>
    </div>
    <div>
        <h3>Universal Approximation Theorem</h3>
        <h4>This project aim to demonstrate the Universal Approxmiation Theorem that say the following thing : every non linear function can be approximated by a MLPL with only one hidden layer and the good amount of neurons</h4>
        <a href="">visit github repo</a>
    </div>
</span>
""", unsafe_allow_html=True)
        st.markdown("""
<span class='pro'>
    <div>
        <div id='p2' class="ima"></div>
    </div>
    <div>
        <h3>Microsoft Market Stock 2021</h3>
        <h4>This project aim to predict the futur microsoft capital fluctuation based on 2021 stock market data set, it use a MLP to make non linear prediction</h4>
        <a href="">visit github repo</a>
    </div>
</span>
""", unsafe_allow_html=True)
        st.markdown("""
<span class='pro'>
    <div>
        <div id='p3' class="ima"></div>
    </div>
    <div>
        <h3> DIABETE BINARY CLASSIFICATION </h3>
        <h4> This project aim to predict case of diabete based a lot of diferents feature, the hardest part is in the data set we used there, hwere half data contain missing values, if you wanna see how I dealt with it please click on the link bellow</h4>
        <a href="">visit github repo</a>
    </div>
</span>
""", unsafe_allow_html=True)


# Fonction pour la page C



















def page_c():

    import pandas as pd


    # Charger les données dans un DataFrame
    df_mort = pd.read_csv("data\etatcivil2021_dec2021_csv\FD_DEC_2021.csv", delimiter=";")

    # Afficher les premières lignes
  


    # Charger les données dans un DataFrame
    df_nai = pd.read_csv("data\etatcivil2021_nais2021_csv\FD_NAIS_2021.csv", delimiter=";")

    # Afficher les premières lignes
   
    # Charger les données dans un DataFrame
    df_mar = pd.read_csv("data\etatcivil2021_mar2021_csv\mar2021.csv", delimiter=";")
    df_mort = df_mort.rename(columns={
    'ADEC': 'Annee_mort',
    'MDEC': 'Mois_mort',
    'JDEC': 'Jour_mort',
    'DEPDEC': 'Dep_dec',
    'SEXE': 'Sexe',
    'ANAIS': 'Annee_nai',
    'MNAIS': 'mois_nai',
    'JNAIS': 'jour_nai',
    'DEPNAIS': 'dep_nai',
    'PNAIS': 'pays_nai'
    })
    df_dec=df_mort.copy()
    df_dec['Date_mort'] = pd.to_datetime(
        df_dec['Jour_mort'].astype(str) + '-' + 
        df_dec['Mois_mort'].astype(str) + '-' + 
        df_dec['Annee_mort'].astype(str),
        format='%d-%m-%Y'
    )


    df_dec[['Annee_mort', 'Mois_mort', 'Jour_mort', 'Date_mort']].head()

    # Créer une nouvelle colonne "Date_nai" en combinant Annee_nai, mois_nai et jour_nai
    df_dec['Date_nai'] = pd.to_datetime(
        df_dec['jour_nai'].astype(str) + '-' + 
        df_dec['mois_nai'].astype(str) + '-' + 
        df_dec['Annee_nai'].astype(str),
    format='%d-%m-%Y'
    )

    

    # Supprimer les colonnes qui ne sont plus nécessaires
    df_dec.drop(columns=['Annee_mort', 'Mois_mort', 'Jour_mort', 'Annee_nai', 'mois_nai', 'jour_nai',"pays_nai"], inplace=True)

    df_born=df_nai.copy()
    df_born.drop(columns=['ACCOUCHR','ANAIS','AGEXACTM','AGEXACTP','AMAR','ARECC',	'ARECM','ARECP','DEPDOM','DMARNAIS','DMARNAIS','DURECEVP','INDLNM','INDLNP','INDNATM','INDNATP','JRECC','JRECM','JRECP','SITUATMR','SITUATPR','MRECC', 'MRECM', 'MRECP','ORIGINOM','TUCOM','TUDOM'], inplace=True)
    

    df_mari=df_mar.copy()
    df_mari.drop(columns=['AMAR','DEPNAIS1','DEPNAIS2','ETAMAT1','ETAMAT2','INDNAT1','INDNAT2','TUCOM', 'TUDOM'], inplace=True)
    df_mari['ANAIS1']= 2021 - df_mari['ANAIS1']
    df_mari['ANAIS2']= 2021 - df_mari['ANAIS2']










































    st.title("Démographie 2021")
    st.write("Cette partie de mon site porte sur l'étude des mariages, naissance et mortalités de 2021")
    st.write("""Le but est de défaire et écalairecir rumeurs et question du genre :           
- la population frnacaise est elle en train décroitre ou croitre ?
- Les hommes vivent t'il moins longtemps que les femmes ?
- Combien de cas represente une naissance unique ?""")
    st.write("""⚠️ avertissement 2021 est une année assez particuliere car en plein confinement COVID, on peut donc s'attendre aux choses suivantes : 
- Mortalité : La surmortalité liée au COVID-19 s'est poursuivie en 2021. Selon l'INSEE, il y a eu une hausse de la mortalité en France, en particulier chez les personnes âgées. Cette surmortalité a perturbé les tendances habituelles des décès.
- Naissances : Les confinements et l’incertitude économique et sociale ont également eu un effet sur la natalité. La France a connu une baisse des naissances, avec un nombre de naissances historiquement bas début 2021. Ce phénomène est directement lié aux effets psychosociaux de la pandémie en 2020.
- Espérance de vie : L'espérance de vie a baissé en 2020 à cause de la pandémie, et en 2021 elle a lentement commencé à remonter sans toutefois retrouver ses niveaux d’avant la crise sanitaire.
- Mariages et divorces : Les confinements et les restrictions ont perturbé les mariages et les divorces. En 2021, après une forte baisse des mariages en 2020, un rattrapage a été observé, avec plus de mariages enregistrés, mais encore en deçà des niveaux d’avant crise.""")
    st.write('---')
    c1,c2,c3=st.columns(3)
    with c1 :
        st.subheader("Le data set sur la Mortalité")
        df_dec
    with c2 :
        st.subheader("Le data set sur La natalité")
        df_born
    with c3:
        st.subheader("Le data set sur les mariages")
        df_mari
    st.write("##")
    st.write("---")
    st.write("##")
    st.title("La mortalité")
    

    df_dec['Mois_mort'] = df_dec['Date_mort'].dt.month

    # Sélecteur pour le choix d'affichage
    affichage = st.selectbox('Choisissez le type d\'affichage :', 
                            ['Par mois', 'Par saison'])

    # Compter les décès en fonction de l'option choisie
    if affichage == 'Par mois':
        # Compter les décès par mois
        deces_par_mois = df_dec['Mois_mort'].value_counts().sort_index()
        df_plot = pd.DataFrame({
            'Mois': deces_par_mois.index,
            'Nombre_de_deces': deces_par_mois.values
        })
        
        # Créer un label pour chaque mois
        mois_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        df_plot['Mois'] = [mois_labels[m - 1] for m in df_plot['Mois']]
        
    elif affichage == 'Par saison':
        # Fonction pour assigner une saison à chaque mois
        def saison(mois):
            if mois in [12, 1, 2]:
                return 'Hiver'
            elif mois in [3, 4, 5]:
                return 'Printemps'
            elif mois in [6, 7, 8]:
                return 'Été'
            elif mois in [9, 10, 11]:
                return 'Automne'

        # Appliquer la fonction pour créer une nouvelle colonne 'Saison'
        df_dec['Saison'] = df_dec['Mois_mort'].apply(saison)

        # Compter les décès par saison
        deces_par_saison = df_dec['Saison'].value_counts()
        df_plot = pd.DataFrame({
            'Saison': deces_par_saison.index,
            'Nombre_de_deces': deces_par_saison.values
        })

    # Créer le graphique à barres avec Plotly
    if affichage == 'Par mois':
        fig = px.bar(df_plot, x='Mois', y='Nombre_de_deces',
                    title='Nombre de décès par mois',
                    labels={'Nombre_de_deces': 'Nombre de décès', 'Mois': 'Mois'},
                    color='Nombre_de_deces', 
                    color_continuous_scale=px.colors.sequential.Sunset)
    else:  # 'Par saison'
        fig = px.bar(df_plot, x='Saison', y='Nombre_de_deces',
                    title='Nombre de décès par saison',
                    labels={'Nombre_de_deces': 'Nombre de décès', 'Saison': 'Saison'},
                    color='Nombre_de_deces', 
                    color_continuous_scale=px.colors.sequential.Sunset)

    # Afficher le graphique dans Streamlit
    st.plotly_chart(fig)




    sexe_labels = {1: 'Masculin', 2: 'Féminin'}
    df_sexe = df_dec['Sexe'].value_counts().reset_index()
    df_sexe.columns = ['Sexe', 'Nombre_de_deces']
    df_sexe['Sexe'] = df_sexe['Sexe'].map(sexe_labels)

    # Créer le pie chart pour la répartition par sexe
    fig_sexe = px.pie(df_sexe, values='Nombre_de_deces', names='Sexe',
                    title='Répartition des décès par sexe',
                    color='Sexe', 
                    color_discrete_sequence=px.colors.qualitative.Set1)

    # Graphique 2 : Décès au même endroit que la naissance
    df_dec['Same_Department'] = df_dec['Dep_dec'] == df_dec['dep_nai']
    same_dep_counts = df_dec['Same_Department'].value_counts().reset_index()
    same_dep_counts.columns = ['Same_Department', 'Nombre_de_deces']
    same_dep_counts['Same_Department'] = same_dep_counts['Same_Department'].map({True: 'Oui', False: 'Non'})

    # Créer le pie chart pour la comparaison des départements
    fig_location = px.pie(same_dep_counts, values='Nombre_de_deces', names='Same_Department',
                        title='Décès au même endroit que la naissance',
                        color='Same_Department', 
                        color_discrete_sequence=px.colors.qualitative.Set1)

    # Afficher les graphiques dans Streamlit
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(fig_sexe)

    with col2:
        st.plotly_chart(fig_location)
    




    df_dec['Date_mort'] = pd.to_datetime(df_dec['Date_mort'])

    # Calculer l'âge à la date de décès
    df_dec['Age'] = df_dec['Date_mort'].dt.year - df_mort['Annee_nai']

    # Séparer les âges par sexe
    df_femmes = df_dec[df_dec['Sexe'] == 2]
    df_hommes = df_dec[df_dec['Sexe'] == 1]

    # Regrouper par date de décès (par jour)
    age_femmes = df_femmes.groupby(df_femmes['Date_mort'].dt.date)['Age'].mean()
    age_hommes = df_hommes.groupby(df_hommes['Date_mort'].dt.date)['Age'].mean()

    # Créer l'area chart avec Plotly
    fig = go.Figure()

    # Ajouter la zone pour les femmes
    fig.add_trace(go.Scatter(
        x=age_femmes.index,
        y=age_femmes,
        fill='tozeroy',
        mode='none',  # Mode none pour ne pas afficher de lignes
        name='Femmes',
        fillcolor='skyblue'
    ))

    # Ajouter la zone pour les hommes
    fig.add_trace(go.Scatter(
        x=age_hommes.index,
        y=age_hommes,
        fill='tozeroy',
        mode='none',  # Mode none pour ne pas afficher de lignes
        name='Hommes',
        fillcolor='lightcoral'
    ))

    # Ajouter des détails au graphique
    fig.update_layout(
        title='Âge de Décès des Femmes et des Hommes au Fil des Jours',
        xaxis_title='Date',
        yaxis_title='Âge moyen de décès',
        yaxis=dict(range=[55, 100]),  # Limiter l'axe Y entre 55 et 100
        xaxis=dict(
            tickmode='array',
            tickvals=pd.date_range(start=age_femmes.index.min(), end=age_femmes.index.max(), freq='MS'),  # Affiche seulement les débuts de mois
            ticktext=pd.date_range(start=age_femmes.index.min(), end=age_femmes.index.max(), freq='MS').strftime('%b %Y')  # Mois et année en format lisible
        ),
        legend=dict(x=0.01, y=0.99),  # Position de la légende
        template='plotly_white'  # Thème
    )

    # Afficher le graphique dans Streamlit
    st.title("Analyse de l'Âge de Décès")
    st.plotly_chart(fig)

    d1,d2 =st.columns([3,8])
    with d1 :
        departement_to_region = {
            '01': 'Auvergne-Rhône-Alpes', '02': 'Hauts-de-France', '03': 'Auvergne-Rhône-Alpes', 
            '04': 'Provence-Alpes-Côte d\'Azur', '05': 'Provence-Alpes-Côte d\'Azur', '06': 'Provence-Alpes-Côte d\'Azur', 
            '07': 'Auvergne-Rhône-Alpes', '08': 'Grand Est', '09': 'Occitanie', '10': 'Grand Est', 
            '11': 'Occitanie', '12': 'Occitanie', '13': 'Provence-Alpes-Côte d\'Azur', '14': 'Normandie', 
            '15': 'Auvergne-Rhône-Alpes', '16': 'Nouvelle-Aquitaine', '17': 'Nouvelle-Aquitaine', 
            '18': 'Centre-Val de Loire', '19': 'Nouvelle-Aquitaine', '2A': 'Corse', '2B': 'Corse', 
            '21': 'Bourgogne-Franche-Comté', '22': 'Bretagne', '23': 'Nouvelle-Aquitaine', '24': 'Nouvelle-Aquitaine', 
            '25': 'Bourgogne-Franche-Comté', '26': 'Auvergne-Rhône-Alpes', '27': 'Normandie', '28': 'Centre-Val de Loire', 
            '29': 'Bretagne', '30': 'Occitanie', '31': 'Occitanie', '32': 'Occitanie', '33': 'Nouvelle-Aquitaine', 
            '34': 'Occitanie', '35': 'Bretagne', '36': 'Centre-Val de Loire', '37': 'Centre-Val de Loire', 
            '38': 'Auvergne-Rhône-Alpes', '39': 'Bourgogne-Franche-Comté', '40': 'Nouvelle-Aquitaine', 
            '41': 'Centre-Val de Loire', '42': 'Auvergne-Rhône-Alpes', '43': 'Auvergne-Rhône-Alpes', 
            '44': 'Pays de la Loire', '45': 'Centre-Val de Loire', '46': 'Occitanie', '47': 'Nouvelle-Aquitaine', 
            '48': 'Occitanie', '49': 'Pays de la Loire', '50': 'Normandie', '51': 'Grand Est', 
            '52': 'Grand Est', '53': 'Pays de la Loire', '54': 'Grand Est', '55': 'Grand Est', 
            '56': 'Bretagne', '57': 'Grand Est', '58': 'Bourgogne-Franche-Comté', '59': 'Hauts-de-France', 
            '60': 'Hauts-de-France', '61': 'Normandie', '62': 'Hauts-de-France', '63': 'Auvergne-Rhône-Alpes', 
            '64': 'Nouvelle-Aquitaine', '65': 'Occitanie', '66': 'Occitanie', '67': 'Grand Est', 
            '68': 'Grand Est', '69': 'Auvergne-Rhône-Alpes', '70': 'Bourgogne-Franche-Comté', 
            '71': 'Bourgogne-Franche-Comté', '72': 'Pays de la Loire', '73': 'Auvergne-Rhône-Alpes', 
            '74': 'Auvergne-Rhône-Alpes', '75': 'Île-de-France', '76': 'Normandie', '77': 'Île-de-France', 
            '78': 'Île-de-France', '79': 'Nouvelle-Aquitaine', '80': 'Hauts-de-France', '81': 'Occitanie', 
            '82': 'Occitanie', '83': 'Provence-Alpes-Côte d\'Azur', '84': 'Provence-Alpes-Côte d\'Azur', 
            '85': 'Pays de la Loire', '86': 'Nouvelle-Aquitaine', '87': 'Nouvelle-Aquitaine', 
            '88': 'Grand Est', '89': 'Bourgogne-Franche-Comté', '90': 'Bourgogne-Franche-Comté', 
            '91': 'Île-de-France', '92': 'Île-de-France', '93': 'Île-de-France', '94': 'Île-de-France', 
            '95': 'Île-de-France', '971': 'Guadeloupe', '972': 'Martinique', '973': 'Guyane', 
            '974': 'La Réunion', '976': 'Mayotte'
        }


        # Ajouter une colonne "Région" au DataFrame en mappant les départements aux régions
        df_dec['Région'] = df_dec['Dep_dec'].astype(str).map(departement_to_region)

        # Compter le nombre de décès par région
        deces_par_region = df_dec['Région'].value_counts()

        # Trier les résultats par nombre de décès
        deces_par_region_sorted = deces_par_region.sort_values(ascending=False)

        

        # Si vous utilisez Streamlit pour afficher les résultats dans l'application :
        

        st.subheader("Régions triées par nombre de décès")
        st.write(deces_par_region_sorted)

    with d2 :
        

        deces_par_departement = df_dec['Dep_dec'].value_counts().reset_index()
        deces_par_departement.columns = ['Dep_dec', 'Nombre_deces']

    # Importer un fichier GeoJSON contenant les géométries des départements français
        geojson_url = 'https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements.geojson'

        # Créer la carte choroplèthe
        fig = px.choropleth(
            deces_par_departement,
            geojson=geojson_url,  # Le fichier GeoJSON des départements
            locations='Dep_dec',  # Colonne correspondant aux départements dans ton DataFrame
            featureidkey="properties.code",  # Clé dans le GeoJSON qui correspond aux départements
            color='Nombre_deces',  # Ce que l'on colorie (le nombre de décès)
            color_continuous_scale="Blues",  # Echelle de couleurs
            scope="europe",  # Zoom sur la France
            labels={'Nombre_deces': 'Nombre de décès'},  # Etiquette pour la légende
            title='Répartition des Décès par Département'
        )

        # Mise à jour du layout pour ajuster la carte
        fig.update_geos(
            visible=False,
            resolution=50,
            showcountries=False,
            showcoastlines=False,
            showland=False,
            fitbounds="locations"
        )

        fig.update_layout(
        width=1200,  # Largeur de la carte
        height=800   # Hauteur de la carte
        )
        # Afficher la carte dans Streamlit
        st.subheader("Répartition des Décès par Département en France")
        st.plotly_chart(fig)
    
    st.write("---")
    st.title("Natalités :")
    st.write('##')
    c1,c2 = st.columns([3,8])

    with c1 :
        df_dec['Région_naissance'] = df_dec['dep_nai'].astype(str).map(departement_to_region)



        # Compter le nombre de naissances par région
        naissances_par_region = df_dec['Région_naissance'].value_counts()

        # Trier les résultats par nombre de naissances
        naissances_par_region_sorted = naissances_par_region.sort_values(ascending=False)

        # Afficher les résultats
        st.subheader("Régions triées par nombre de naissances")
        st.write(naissances_par_region_sorted)
    with c2 :
        df_dec['dep_nai'] = df_dec['dep_nai'].astype(str).str.zfill(2)

        # Compter le nombre de naissances par département
        naissances_par_departement = df_dec['dep_nai'].value_counts().reset_index()
        naissances_par_departement.columns = ['dep_nai', 'nombre_naissances']

        # Créer la carte choroplèthe avec Plotly
        fig = px.choropleth(
            naissances_par_departement,
            geojson="https://france-geojson.gregoiredavid.fr/repo/departements.geojson",  # GeoJSON des départements français
            locations='dep_nai',  # Les départements de naissance
            featureidkey="properties.code",  # Le code INSEE dans le GeoJSON
            color='nombre_naissances',  # Le nombre de naissances par département
            color_continuous_scale="Blues",  # Echelle de couleur
            labels={'nombre_naissances': 'Nombre de Naissances'}
        )

        # Ajuster la mise en page de la carte
        fig.update_geos(
            fitbounds="locations",  # Zoom automatique sur les départements concernés
            visible=False  # Masquer les frontières
        )

        fig.update_layout(
            height=1000,
            width=1200,  # Ajuster la hauteur de la carte
            margin={"r":0,"t":50,"l":0,"b":0},  # Marges pour une meilleure vue
            coloraxis_colorbar=dict(
                title="Nombre de Naissances"
            )
        )

        # Afficher la carte dans Streamlit
        st.subheader("Carte des Naissances par Département")
        st.plotly_chart(fig)




    df_dec['Région_naissance'] = df_dec['dep_nai'].astype(str).map(departement_to_region)
    df_dec['Région_deces'] = df_dec['Dep_dec'].astype(str).map(departement_to_region)

    # Compter le nombre de naissances par région
    naissances_par_region = df_dec['Région_naissance'].value_counts()

    # Compter le nombre de décès par région
    deces_par_region = df_dec['Région_deces'].value_counts()

    # Créer un DataFrame combiné pour les naissances et les décès
    regions_combined = pd.DataFrame({
        'Naissances': naissances_par_region,
        'Décès': deces_par_region
    }).fillna(0)  # Remplir les valeurs manquantes par 0

    # Créer le graphique avec deux barres empilées
    fig = px.bar(
        regions_combined,
        x=regions_combined.index,
        y=['Naissances', 'Décès'],  # Colonnes à afficher
        labels={'value': 'Nombre', 'x': 'Région'},
        title='Nombre de Naissances et de Décès par Région',
        barmode='group',  # Choix "group" pour afficher les barres côte à côte (ou "stack" pour empiler)
        color_discrete_map={'Naissances': 'blue', 'Décès': 'red'}  # Couleurs personnalisées pour chaque série
    )

    # Ajuster la mise en page du graphique
    fig.update_layout(
        xaxis_title="Région",
        yaxis_title="Nombre",
        xaxis_tickangle=-45,  # Rotation des labels pour une meilleure lisibilité
        width=1200,  # Ajuster la largeur du graphique
        height=800   # Ajuster la hauteur du graphique
    )

    # Afficher le graphique dans Streamlit
    st.title("Analyse des Naissances et Décès par Région")
    st.plotly_chart(fig)


    repartition_sexe = df_born['SEXE'].value_counts().reset_index()
    repartition_sexe.columns = ['SEXE', 'Nombre']

    # Remplacer les codes par les noms correspondants
    repartition_sexe['SEXE'] = repartition_sexe['SEXE'].replace({1: 'Masculin', 2: 'Féminin'})

    # Créer le pie chart pour la répartition par sexe
    fig_sexe = px.pie(
        repartition_sexe,
        values='Nombre',
        names='SEXE',
        title='Répartition des Sexes à la Naissance',
        color='SEXE',
        color_discrete_map={'Masculin': 'blue', 'Féminin': 'pink'}  # Couleurs pour les sexes
    )

    # Compter la répartition du nombre d'enfants par naissance
    repartition_nb_enfants = df_born['NBENF'].value_counts().reset_index()
    repartition_nb_enfants.columns = ['NBENF', 'Nombre']

    # Créer le pie chart pour la répartition du nombre d'enfants par naissance
    fig_nb_enfants = px.pie(
        repartition_nb_enfants,
        values='Nombre',
        names='NBENF',
        title='Répartition du Nombre d\'Enfants par Naissance',
        color='NBENF',
        color_discrete_sequence=px.colors.qualitative.Set3  # Choix de couleurs
    )



    # Afficher les pie charts dans Streamlit

    
    c1,c2 = st.columns(2)
    with c1 :
        st.subheader("nombre d'enfant par naissance")
        st.plotly_chart(fig_nb_enfants)
    with c2 :
        st.subheader("genre des nouveaux nés")
        st.plotly_chart(fig_sexe)


    affichage = st.selectbox('Choisissez le type d\'affichage :', 
                         ['Par mois', 'Par saison'], key='selectbox_naissances')

    # Compter les naissances en fonction de l'option choisie
    if affichage == 'Par mois':
        # Compter les naissances par mois
        naissances_par_mois = df_born['MNAIS'].value_counts().sort_index()
        df_plot = pd.DataFrame({
            'Mois': naissances_par_mois.index,
            'Nombre_de_naissances': naissances_par_mois.values
        })
        
        # Créer un label pour chaque mois
        mois_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        df_plot['Mois'] = [mois_labels[m - 1] for m in df_plot['Mois']]
        
    elif affichage == 'Par saison':
        # Fonction pour assigner une saison à chaque mois
        def saison(mois):
            if mois in [12, 1, 2]:
                return 'Hiver'
            elif mois in [3, 4, 5]:
                return 'Printemps'
            elif mois in [6, 7, 8]:
                return 'Été'
            elif mois in [9, 10, 11]:
                return 'Automne'

        # Appliquer la fonction pour créer une nouvelle colonne 'Saison'
        df_born['Saison'] = df_born['MNAIS'].apply(saison)

        # Compter les naissances par saison
        naissances_par_saison = df_born['Saison'].value_counts()
        df_plot = pd.DataFrame({
            'Saison': naissances_par_saison.index,
            'Nombre_de_naissances': naissances_par_saison.values
        })

    # Créer le graphique à barres avec Plotly
    if affichage == 'Par mois':
        fig = px.bar(df_plot, x='Mois', y='Nombre_de_naissances',
                    title='Nombre de Naissances par Mois',
                    labels={'Nombre_de_naissances': 'Nombre de Naissances', 'Mois': 'Mois'},
                    color='Nombre_de_naissances', 
                    color_continuous_scale=px.colors.sequential.Sunset)
    else:  # 'Par saison'
        fig = px.bar(df_plot, x='Saison', y='Nombre_de_naissances',
                    title='Nombre de Naissances par Saison',
                    labels={'Nombre_de_naissances': 'Nombre de Naissances', 'Saison': 'Saison'},
                    color='Nombre_de_naissances', 
                    color_continuous_scale=px.colors.sequential.Sunset)

    # Afficher le graphique dans Streamlit
    st.plotly_chart(fig)

    

    fig = go.Figure()

    # Histogramme pour l'âge des mères
    fig.add_trace(go.Histogram(
        x=df_born['AGEMERE'],
        name='Âge des Mères',
        opacity=0.5,  # Niveau de transparence
        marker=dict(color='red'),  # Couleur rouge pour les mères
        histnorm='probability',  # Normaliser pour afficher les proportions
        nbinsx=30  # Nombre de bacs
    ))

    # Histogramme pour l'âge des pères
    fig.add_trace(go.Histogram(
        x=df_born['AGEPERE'],
        name='Âge des Pères',
        opacity=0.5,  # Niveau de transparence
        marker=dict(color='blue'),  # Couleur bleue pour les pères
        histnorm='probability',  # Normaliser pour afficher les proportions
        nbinsx=30  # Nombre de bacs
    ))

    # Ajouter des détails au graphique
    fig.update_layout(
        title='Répartition des Âges des Mères et des Pères en Fonction des Naissances',
        xaxis_title='Âge',
        yaxis_title='Proportion',
        barmode='overlay',  # Superposer les histogrammes
        template='plotly_white',  # Thème
        legend=dict(x=0.01, y=0.99)  # Position de la légende
    )

    # Afficher le graphique dans Streamlit
    st.title("Analyse de l'Âge des Parents en Fonction des Naissances")
    st.plotly_chart(fig)

    st.write("##")
    st.write("---")
    st.write("##")
    st.title('MARIAGES :')
    st.write("##")
    mariages_par_jour = df_mari['JSEMAINE'].value_counts().sort_index()

    # Créer un selectbox pour choisir les départements
    departements_uniques = df_mari['DEPMAR'].unique()
    departement_selection = st.multiselect('Sélectionnez les départements à inclure :', options=departements_uniques, default=departements_uniques.tolist())

    # Filtrer les données en fonction des départements sélectionnés
    if departement_selection:
        df_filtré = df_mari[df_mari['DEPMAR'].isin(departement_selection)]
    else:
        df_filtré = df_mari

    # Compter le nombre de mariages par jour de la semaine après filtrage
    mariages_par_jour_filtré = df_filtré['JSEMAINE'].value_counts().sort_index()

    # Créer le DataFrame pour Plotly
    df_plot = pd.DataFrame({
        'Jour': mariages_par_jour_filtré.index,
        'Nombre de Mariages': mariages_par_jour_filtré.values
    })

    # Créer le bar plot avec Plotly
    fig = px.bar(
        df_plot,
        x='Jour',
        y='Nombre de Mariages',
        title='Nombre de Mariages par Jour de la Semaine',
        labels={'Nombre de Mariages': 'Nombre de Mariages', 'Jour': 'Jour de la Semaine'},
        color='Nombre de Mariages',  # Couleur selon le nombre de mariages
        color_continuous_scale=px.colors.sequential.Viridis  # Palette de couleurs
    )

    # Ajuster la mise en page du graphique
    fig.update_layout(
        xaxis_title="Jour de la Semaine",
        yaxis_title="Nombre de Mariages",
        width=800,  # Ajuster la largeur du graphique
        height=600  # Ajuster la hauteur du graphique
    )

    # Afficher le graphique dans Streamlit
    st.title("Analyse des Mariages par Jour de la Semaine")
    st.plotly_chart(fig)

    mariages_par_mois = df_mari['MMAR'].value_counts().sort_index()

# Créer un selectbox pour choisir les départements
    departements_uniques = df_mari['DEPMAR'].unique()
    departement_selection = st.multiselect(
        'Sélectionnez les départements à inclure :', 
        options=departements_uniques, 
        default=departements_uniques.tolist(),
        key='departement_selection'  # Ajout d'une clé unique pour éviter les doublons
    )

    # Filtrer les données en fonction des départements sélectionnés
    if departement_selection:
        df_filtré = df_mari[df_mari['DEPMAR'].isin(departement_selection)]
    else:
        df_filtré = df_mari

    # Compter le nombre de mariages par mois après filtrage
    mariages_par_mois_filtré = df_filtré['MMAR'].value_counts().sort_index()

    # Créer le DataFrame pour Plotly
    df_plot = pd.DataFrame({
        'Mois': mariages_par_mois_filtré.index,
        'Nombre de Mariages': mariages_par_mois_filtré.values
    })

    # Créer le bar plot avec Plotly
    fig = px.bar(
        df_plot,
        x='Mois',
        y='Nombre de Mariages',
        title='Nombre de Mariages par Mois',
        labels={'Nombre de Mariages': 'Nombre de Mariages', 'Mois': 'Mois'},
        color='Nombre de Mariages',  # Couleur selon le nombre de mariages
        color_continuous_scale=px.colors.sequential.Viridis  # Palette de couleurs
    )

    # Ajuster la mise en page du graphique
    fig.update_layout(
        xaxis_title="Mois",
        yaxis_title="Nombre de Mariages",
        width=800,  # Ajuster la largeur du graphique
        height=600  # Ajuster la hauteur du graphique
    )

    # Afficher le graphique dans Streamlit
    st.title("Analyse des Mariages par Mois")
    st.plotly_chart(fig)


    c1,c2 =st.columns([7,3])
    with c1:
        fig = go.Figure()

        # Ajout de la trace pour ANAIS1
        fig.add_trace(go.Histogram(
            x=df_mari['ANAIS1'],
            name='HOMME',
            marker_color='blue',  # Couleur rouge pour ANAIS1
            opacity=0.6,
            bingroup=1
        ))

        # Ajout de la trace pour ANAIS2
        fig.add_trace(go.Histogram(
            x=df_mari['ANAIS2'],
            name='FEMME',
            marker_color='pink',  # Couleur bleue pour ANAIS2
            opacity=0.6,
            bingroup=2
        ))

        # Configuration des paramètres de mise en page
        fig.update_layout(
            title='Histogramme Groupé des Mariage par genre',
            xaxis_title='Âge',
            yaxis_title='Nombre de mariage',
            barmode='overlay',  # Overlay pour voir les barres superposées
            width=800,
            height=600,
            legend=dict(x=0.01, y=0.99),  # Position de la légende
            template='plotly_white'  # Thème
        )

        # Afficher le graphique dans Streamlit
        st.title("Histogramme Groupé des Mariage par genre")
        st.plotly_chart(fig)
    with c2 :
        #Calculer la différence d'âge (valeur absolue)
        df_mari['Diff_Age'] = abs(df_mari['ANAIS1'] - df_mari['ANAIS2'])

        # Agréger la différence d'âge par département
        diff_age_par_departement = df_mari.groupby('DEPMAR')['Diff_Age'].mean().reset_index()

        # Trier par différence d'âge
        diff_age_par_departement = diff_age_par_departement.sort_values(by='Diff_Age', ascending=False)

        # Afficher la liste des départements et de leurs différences d'âge
        st.subheader("Différence d'âge par département")

        # Option 1: Afficher en format tableau
        st.dataframe(diff_age_par_departement.rename(columns={"Diff_Age": "Différence d'âge moyenne (ans)"}))

# Option 2: Afficher comme une liste formatée (décommentez si vous préférez cette option)
# for index, row in diff_age_par_departement.iterrows():
#     st.write(f"Département: **{row['DEPMAR']}**, Différence d'âge moyenne: **{row['Diff_Age']:.2f} ans**")

    df_mari['DEPMAR'] = df_mari['DEPMAR'].astype(str).str.zfill(2)

    # Compter le nombre de mariages par département
    mariages_par_departement = df_mari['DEPMAR'].value_counts().reset_index()
    mariages_par_departement.columns = ['DEPMAR', 'Nombre_Mariages']

    # Créer la carte choroplèthe avec Plotly
    fig = px.choropleth(
        mariages_par_departement,
        geojson="https://france-geojson.gregoiredavid.fr/repo/departements.geojson",  # GeoJSON des départements français
        locations='DEPMAR',  # Les départements des mariages
        featureidkey="properties.code",  # Le code INSEE dans le GeoJSON
        color='Nombre_Mariages',  # Le nombre de mariages par département
        color_continuous_scale="Reds",  # Échelle de couleur
        labels={'Nombre_Mariages': 'Nombre de Mariages'},  # Légende
        title='Nombre de Mariages par Département'
    )

    # Ajuster la mise en page de la carte
    fig.update_geos(
        fitbounds="locations",  # Zoom automatique sur les départements concernés
        visible=False  # Masquer les frontières
    )

    fig.update_layout(
        height=800,
        width=1200,  # Ajuster la largeur de la carte
        margin={"r":0,"t":50,"l":0,"b":0},  # Marges pour une meilleure vue
        coloraxis_colorbar=dict(
            title="Nombre de Mariages"
        )
    )

    # Afficher la carte dans Streamlit
    st.subheader("Carte des Mariages par Département")
    st.plotly_chart(fig)






































def page_d():
    st.header('Get in Touch !')
    st.write("##")
    st.subheader("Si vous voulez me communiquer bug, recommandation ou information qui vous semblerait utile, envoyez moi un mail a travers ce fomulaire : ")
    st.write("##")
    col1, col2 = st.columns([7,3])
    with col1 :
        contact_form= """
        <form id="form" action="https://formsubmit.co/jeremy.viot@efrei.net" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <label for="">Body :</label>
            <textarea style="height: 500px;" id="largeText" name="largeText" placeholder="Entrez un grand volume de texte ici..."></textarea><br><br>
            <div style="text-align: center; margin-top:100px;">
                <button type="submit" class="button">
                        <span>Submit</span>
                    </button>
            </div>
            
            
        </form>
    """
    
        st.markdown(contact_form, unsafe_allow_html=True)
    with col2 :    
        ani_mail = load_local_animation(mail)
        if ani_mail:
            st_lottie(ani_mail, height="200px")  # Appel pour rendre l'animation



# Créer la barre latérale pour la navigation
st.sidebar.title("Dash Board sur la demographie 2021")
pages = {
    
    "Accueil": home,
    "A propos de moi": page_a,
    "Mes Projets": page_b,
    "Data visualisation": page_c,
    "Contacter": page_d
}





# Utiliser selectbox pour choisir la page
selected_page = st.sidebar.selectbox("Sélectionnez une page", list(pages.keys()))

# Appeler la fonction de la page sélectionnée
pages[selected_page]()
