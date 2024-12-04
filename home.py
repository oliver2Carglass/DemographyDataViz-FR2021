"""
WELCOME WELCOME!  
This project has been created to address a data visualization problem within an academic context. The goal of this project is to create a dynamic and aesthetically pleasing dashboard using three datasets: Marriage, Death, and Birth.
"""



import plotly.graph_objects as go
import streamlit as st
from streamlit_option_menu import option_menu as option_menu 
import requests
from streamlit_lottie import st_lottie
import json
import base64
import pandas as pd
import plotly.express as px


st.set_page_config(layout='wide')

coder="animations/Animation1.json"

# This function load lotties animation from an URL
def load_lot(url):
    r = requests.get(url)
    if r.status_code!= 200 : 
        return None
    else :
        return r.json()

# This function load lotties animation from an Local work space
def load_local_animation(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

# Here we need to go throught the base 64 format to load local images
def get_image_as_base64(img):
    with open(img, "rb") as f :
        data = f.read()
    return base64.b64encode(data).decode()




css = f"""
<style>
h3{{
    margin-top: 50px;
    font-size: 35px;
}}


.lottie-animation {{
        margin-left: 1500px;
    }}


.st-emotion-cache-463q5x .token.string{{
    color: #FF4B4B;
}}


</style>
"""

st.markdown(css, unsafe_allow_html=True)        #this include css in the web site

    


# Function containing the welcome page
def home():
    st.title("Welcome to my Dash Board :)")
    st.write("This dash board have been made for a class project")
    
    with st.container():
        col1,col2 = st.columns(2)
        with col1 :
            st.write("Made by Jérémy VIOT the 10/17/2024  & and first Updated the 12/04/2024")
            st.write('##')
            st.subheader("I am a futur engineer passionated in AI and data visualization")
        with col2:
            ani_code = load_local_animation(coder)
            if ani_code:
                st_lottie(ani_code, height='500px')






# Function to load dataViz page

def page_dataViz():


    # ====================================================
    # =                  DATA PART                       =
    # ====================================================
 

    # Load data :
    df_d = pd.read_csv("data/2021Death.csv", delimiter=";")
    df_birth = pd.read_csv("data/2021Birth.csv", delimiter=";")
    df_w = pd.read_csv("data/2021Wedding.csv", delimiter=";")

    # renaming variable to a more dev understanding
    df_d = df_d.rename(columns={
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
    df_dec=df_d.copy()
    df_dec['Date_mort'] = pd.to_datetime(
        df_dec['Jour_mort'].astype(str) + '-' + 
        df_dec['Mois_mort'].astype(str) + '-' + 
        df_dec['Annee_mort'].astype(str),
        format='%d-%m-%Y'
    )


    df_dec[['Annee_mort', 'Mois_mort', 'Jour_mort', 'Date_mort']].head()

    # Create a datetime format from 3 var
    df_dec['Date_nai'] = pd.to_datetime(
        df_dec['jour_nai'].astype(str) + '-' + 
        df_dec['mois_nai'].astype(str) + '-' + 
        df_dec['Annee_nai'].astype(str),
    format='%d-%m-%Y'
    )

    

    # Delete useless data
    df_dec.drop(columns=['Annee_mort', 'Mois_mort', 'Jour_mort', 'Annee_nai', 'mois_nai', 'jour_nai',"pays_nai"], inplace=True)

    df_born=df_birth.copy()
    df_born.drop(columns=['ACCOUCHR','ANAIS','AGEXACTM','AGEXACTP','AMAR','ARECC',	'ARECM','ARECP','DEPDOM','DMARNAIS','DMARNAIS','DURECEVP','INDLNM','INDLNP','INDNATM','INDNATP','JRECC','JRECM','JRECP','SITUATMR','SITUATPR','MRECC', 'MRECM', 'MRECP','ORIGINOM','TUCOM','TUDOM'], inplace=True)
    
    df_mari=df_w.copy()
    df_mari.drop(columns=['AMAR','DEPNAIS1','DEPNAIS2','ETAMAT1','ETAMAT2','INDNAT1','INDNAT2','TUCOM', 'TUDOM'], inplace=True)
    df_mari['ANAIS1']= 2021 - df_mari['ANAIS1']
    df_mari['ANAIS2']= 2021 - df_mari['ANAIS2']

    
    



   
    # ====================================================
    # =                  DASHBOARD                       =
    # ====================================================
  
    # Create the top introduction part :

    st.title("Dashboard on 2021 Demography of France")
    st.write("This part contain a dash board based on birth, death and wedding of 2021 years")
    st.write("""The goal is to dismantle and clarify rumors and questions such as:
- Is the French population decreasing or increasing?
- Do men live shorter lives than women?
- How many cases represent a single birth?""")
    st.write("""⚠️ Warning: 2021 was quite a particular year due to the COVID-19 lockdown, so we can expect the following:
- Mortality: The excess mortality related to COVID-19 continued in 2021. According to INSEE, there was an increase in mortality in France, especially among the elderly. This excess mortality disrupted the usual death trends.
- Births: Lockdowns and economic and social uncertainty also had an impact on birth rates. France experienced a decline in births, with historically low numbers of births at the beginning of 2021. This phenomenon is directly linked to the psychosocial effects of the pandemic in 2020.
- Life expectancy: Life expectancy decreased in 2020 due to the pandemic, and in 2021 it slowly began to recover, but it had not yet returned to pre-crisis levels.
- Marriages and divorces: Lockdowns and restrictions disrupted marriages and divorces. In 2021, after a significant drop in marriages in 2020, a recovery was observed, with more marriages being recorded, but still below pre-crisis levels.""")
    st.write("The data come from data.gouv.fr")
    st.write('---')
    #printing datasets
    c1,c2,c3=st.columns(3)
    with c1 :
        st.subheader("Death Dataset")
        df_dec
    with c2 :
        st.subheader("Birth Dataset")
        df_born
    with c3:
        st.subheader("Wedding Dataset")
        df_mari
    st.write("##")
    st.write("---")
    st.write("##")


    # ====================================================
    # =              PART 1 : MORTALITY                  =
    # ====================================================
  

    st.title("MORTALITY")

    df_dec['Mois_mort'] = df_dec['Date_mort'].dt.month
    # Display Selector
    affichage = st.selectbox('Choose your display type :', 
                            ['Month', 'Season'])

    # Counting death depending on what is choosen
    if affichage == 'Month':
        # Compter les décès par mois
        deces_par_mois = df_dec['Mois_mort'].value_counts().sort_index()
        df_plot = pd.DataFrame({
            'Month': deces_par_mois.index,
            'Number_of_death': deces_par_mois.values
        })
        
        # Create a label for each month
        mois_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        df_plot['Month'] = [mois_labels[m - 1] for m in df_plot['Month']]
        
    elif affichage == 'Season':
        # Create the concept of season
        def saison(mois):
            if mois in [12, 1, 2]:
                return 'Winter'
            elif mois in [3, 4, 5]:
                return 'Spring'
            elif mois in [6, 7, 8]:
                return 'Summer'
            elif mois in [9, 10, 11]:
                return 'Autumn'

        # Apply the function to create season
        df_dec['Saison'] = df_dec['Mois_mort'].apply(saison)

        # Count death by season
        deces_par_saison = df_dec['Saison'].value_counts()
        df_plot = pd.DataFrame({
            'Season': deces_par_saison.index,
            'Number_of_death': deces_par_saison.values
        })

    # Create graph using plotly
    if affichage == 'Month':
        fig = px.bar(df_plot, x='Month', y='Number_of_death',
                    title='Number of death per month',
                    labels={'Number_of_death': 'Number of death', 'Mois': 'Mois'},
                    color='Number_of_death', 
                    color_continuous_scale=px.colors.sequential.Sunset)
    else:  # With seasons
        fig = px.bar(df_plot, x='Season', y='Number_of_death',
                    title='Number of death per Season',
                    labels={'Number_of_death': 'Number of death', 'Season': 'Saison'},
                    color='Number_of_death', 
                    color_continuous_scale=px.colors.sequential.Sunset)

    # print using streamlit
    st.plotly_chart(fig)
    st.write("Here is the improved translation in English: \n The reason people are more likely to die in winter and spring is due to the low temperatures. In winter, the cold is especially deadly, and although the sun may shine brightly in spring, the temperatures remain very low, which can have serious effects on health.")
    st.write("---")
    st.subheader("Mortality by Sex and Place")



    sexe_labels = {1: 'Male', 2: 'Female'}
    df_sexe = df_dec['Sexe'].value_counts().reset_index()
    df_sexe.columns = ['Sexe', 'Nombre_de_deces']
    df_sexe['Sexe'] = df_sexe['Sexe'].map(sexe_labels)

    # Create a pie chart for sex repartition
    fig_sexe = px.pie(df_sexe, values='Nombre_de_deces', names='Sexe',
                    title='Death per sex',
                    color='Sexe', 
                    color_discrete_sequence=px.colors.qualitative.Set1)


    # Graph 2 : Death same place than birth
    df_dec['Same_Department'] = df_dec['Dep_dec'] == df_dec['dep_nai']
    same_dep_counts = df_dec['Same_Department'].value_counts().reset_index()
    same_dep_counts.columns = ['Same_Department', 'Nombre_de_deces']
    same_dep_counts['Same_Department'] = same_dep_counts['Same_Department'].map({True: 'Oui', False: 'Non'})

    # Create pie chart for the comparison of departement
    fig_location = px.pie(same_dep_counts, values='Nombre_de_deces', names='Same_Department',
                        title='Death at the same place than birth ',
                        color='Same_Department', 
                        color_discrete_sequence=px.colors.qualitative.Set1)

    # Print using Streamlit
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(fig_sexe)

    with col2:
        st.plotly_chart(fig_location)
    st.write("50/50 looks kinda logical ")
    st.write("---")




    df_dec['Date_mort'] = pd.to_datetime(df_dec['Date_mort'])

    # Calculate the age of death
    df_dec['Age'] = df_dec['Date_mort'].dt.year - df_d['Annee_nai']

    # Split age by sex
    df_femmes = df_dec[df_dec['Sexe'] == 2]
    df_hommes = df_dec[df_dec['Sexe'] == 1]

    # Group by the death date (day)
    age_femmes = df_femmes.groupby(df_femmes['Date_mort'].dt.date)['Age'].mean()
    age_hommes = df_hommes.groupby(df_hommes['Date_mort'].dt.date)['Age'].mean()

    # Create area chart using plotly
    fig = go.Figure()

    # Add the Female zone
    fig.add_trace(go.Scatter(
        x=age_femmes.index,
        y=age_femmes,
        fill='tozeroy',
        mode='none',    # MOd none to not print lines
        name='Female',
        fillcolor='skyblue'
    ))

    # Add the male zone
    fig.add_trace(go.Scatter(
        x=age_hommes.index,
        y=age_hommes,
        fill='tozeroy',
        mode='none',    # MOd none to not print lines
        name='Male',
        fillcolor='lightcoral'
    ))

    # ADdd detail to graph
    fig.update_layout(
        title='Male and Female age depending of the day',
        xaxis_title='Date',
        yaxis_title='Mean age death',
        yaxis=dict(range=[60, 100]),  # Limiter l'axe Y entre 55 et 100
        xaxis=dict(
            tickmode='array',
            tickvals=pd.date_range(start=age_femmes.index.min(), end=age_femmes.index.max(), freq='MS'),  # Affiche seulement les débuts de mois
            ticktext=pd.date_range(start=age_femmes.index.min(), end=age_femmes.index.max(), freq='MS').strftime('%b %Y')  # Mois et année en format lisible
        ),
        legend=dict(x=0.01, y=0.99),  # Position de la légende
        template='plotly_white'  # Thème
    )

    # print using streamlit
    st.subheader("Age of Death ")
    st.plotly_chart(fig)
    st.write('---')




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


        # Add rregion to the dataframe
        df_dec['Région'] = df_dec['Dep_dec'].astype(str).map(departement_to_region)

        # Count the number of death per region
        deces_par_region = df_dec['Région'].value_counts()

        # Sort the result
        deces_par_region_sorted = deces_par_region.sort_values(ascending=False)

        

        st.subheader("Region sorted by number of death")
        st.write(deces_par_region_sorted)

    with d2 :
        
        deces_par_departement = df_dec['Dep_dec'].value_counts().reset_index()
        deces_par_departement.columns = ['Dep_dec', 'Nombre_deces']

        # Import the file with french region 
        geojson_url = 'https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements.geojson'

        # Create the map
        fig = px.choropleth(
            deces_par_departement,
            geojson=geojson_url,  #  GeoJSON file of departements
            locations='Dep_dec',  # Column corresponding to departments of df
            featureidkey="properties.code",  # GEOJSON Value correponding to departement
            color='Nombre_deces',  
            color_continuous_scale="Blues", 
            scope="europe",  
            labels={'Nombre_deces': 'Nunber of death '}, 
            title='Map view of death per departement'
        )


        fig.update_geos(
            visible=False,
            resolution=50,
            showcountries=False,
            showcoastlines=False,
            showland=False,
            fitbounds="locations"
        )

        fig.update_layout(
        width=1200, 
        height=800  
        )
        # Afficher la carte dans Streamlit
        st.subheader("Death repartition depending on departments")
        st.plotly_chart(fig)
    




    # ====================================================
    # =              PART 2 : MATALITY                  =
    # ====================================================
    st.write("---")
    st.title("NATALITY")
    st.write('##')
    c1,c2 = st.columns([3,8])

    with c1 :
        df_dec['Région_naissance'] = df_dec['dep_nai'].astype(str).map(departement_to_region)



        # Count number of birth per dep
        naissances_par_region = df_dec['Région_naissance'].value_counts()

        # Sort result by number of death
        naissances_par_region_sorted = naissances_par_region.sort_values(ascending=False)

        # Print 
        st.subheader("region sorted by birth number")
        st.write(naissances_par_region_sorted)
    with c2 :
        df_dec['dep_nai'] = df_dec['dep_nai'].astype(str).str.zfill(2)
        naissances_par_departement = df_dec['dep_nai'].value_counts().reset_index()
        naissances_par_departement.columns = ['dep_nai', 'nombre_naissances']

        # Create map
        fig = px.choropleth(
            naissances_par_departement,
            geojson="https://france-geojson.gregoiredavid.fr/repo/departements.geojson",
            locations='dep_nai',  
            featureidkey="properties.code",  
            color='nombre_naissances',  
            color_continuous_scale="Blues", 
            labels={'nombre_naissances': 'Number of Birth'}
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
                title="Number of Birth"
            )
        )

        # Afficher la carte dans Streamlit
        st.subheader("Map of Birth per Region")
        st.plotly_chart(fig)
    st.write('---')




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
        labels={'value': 'Number', 'x': 'Region'},
        title='Number of Birth & Death per region ',
        barmode='group',  # Choix "group" pour afficher les barres côte à côte (ou "stack" pour empiler)
        color_discrete_map={'Naissances': 'blue', 'Décès': 'red'}  # Couleurs personnalisées pour chaque série
    )

    # Ajuster la mise en page du graphique
    fig.update_layout(
        xaxis_title="Region",
        yaxis_title="Number",
        xaxis_tickangle=-45,  # Rotation des labels pour une meilleure lisibilité
        width=1200,  # Ajuster la largeur du graphique
        height=800   # Ajuster la hauteur du graphique
    )

    # Afficher le graphique dans Streamlit
    st.title("Analysis of Birth per region")
    st.plotly_chart(fig)
    st.write("---")


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





   



# Créer la barre latérale pour la navigation
st.sidebar.title("Dash Board sur la demographie 2021")
pages = {
    
    "Data visualisation": page_dataViz,
    "Accueil": home
}





# Utiliser selectbox pour choisir la page
selected_page = st.sidebar.selectbox("Sélectionnez une page", list(pages.keys()))

# Appeler la fonction de la page sélectionnée
pages[selected_page]()
