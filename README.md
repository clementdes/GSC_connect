# GSC - Streamlit Connector

### README (Français / English)

---

## Description (Français)

Ce dépôt contient une application Streamlit légère qui permet d'extraire des données de la **Google Search Console** (GSC) avec un maximum de 250 000 lignes. Cette application a été créée pour simplifier l'extraction des données de GSC et les rendre facilement téléchargeables sous forme de fichiers CSV.

**Fonctionnalités principales :**
- Connexion OAuth à la Google Search Console.
- Sélection des propriétés GSC disponibles.
- Filtrage par type de recherche (Web, Image, Vidéo, etc.).
- Sélection de la plage de dates.
- Choix des dimensions (page, requête, pays, etc.).
- Export des résultats au format CSV.
- Visualisation des données sous forme de tableau ou de graphique.

## Prérequis

Avant de lancer l'application, assurez-vous d'avoir les éléments suivants :
- Un compte **Google Search Console** avec des accès suffisants aux propriétés que vous souhaitez interroger.
- Un projet Google Cloud avec un fichier de configuration OAuth (client_id, client_secret, redirect_uris).

## Instructions d'installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-repo-url
   ```
2. Installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```
3. Ajoutez les informations de configuration OAuth dans le fichier `secrets.toml` sous `streamlit/secrets.toml` :
   ```toml
   [installed]
   client_id = "votre-client-id"
   client_secret = "votre-client-secret"
   redirect_uris = ["votre-url-de-redirection"]
   ```
4. Lancez l'application Streamlit :
   ```bash
   streamlit run app.py
   ```

## Utilisation

1. Connectez-vous à votre compte Google via le bouton de connexion Google.
2. Sélectionnez la propriété GSC que vous souhaitez interroger.
3. Choisissez les filtres, comme le type de recherche, la plage de dates, et les dimensions.
4. Cliquez sur "Fetch Data" pour afficher les résultats.
5. Téléchargez les données au format CSV ou visualisez-les sous forme de graphique.

---

## Description (English)

This repository contains a lightweight **Streamlit** application designed to extract data from **Google Search Console** (GSC) with a maximum of 250,000 rows. The app simplifies GSC data extraction and allows users to easily download results in CSV format.

**Main Features:**
- OAuth connection to Google Search Console.
- Selection of available GSC properties.
- Filtering by search type (Web, Image, Video, etc.).
- Date range selection.
- Choice of dimensions (page, query, country, etc.).
- Export results to CSV format.
- Data visualization in a table or chart format.

## Prerequisites

Before running the app, ensure that you have:
- A **Google Search Console** account with sufficient access to the properties you wish to query.
- A Google Cloud project with an OAuth configuration file (client_id, client_secret, redirect_uris).

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your OAuth configuration to the `secrets.toml` file under `streamlit/secrets.toml`:
   ```toml
   [installed]
   client_id = "your-client-id"
   client_secret = "your-client-secret"
   redirect_uris = ["your-redirect-url"]
   ```
4. Launch the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Sign in with your Google account using the Google sign-in button.
2. Select the GSC property you want to query.
3. Choose filters such as search type, date range, and dimensions.
4. Click on "Fetch Data" to display results.
5. Download data as CSV or visualize it in a chart.

---

**Auteur / Author** : Clément Desmousseaux
** Inspired by ** : [LeeFoot.co.uk](https://leefoot.co.uk)  
**Contact** : [Twitter](https://x.com/clementdesmouss)
**Wnat to receive amazing tips for your SEO and SEA ** :  [Subscribe to my Newsletter / Inscris-toi à ma newsletter](https://searchlab.email)
