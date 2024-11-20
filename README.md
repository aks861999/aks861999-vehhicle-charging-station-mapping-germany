# Project: Problem Set

Electric mobility is essential in order to reduce emission of green house gases. In recent years sales and usage of electric vehicles has accelerated significantly. However lack of electric charging stations in many areas remains impediment for further success. Based on geovisualization of different datasets referring to Berlin we want to analyze demand for additional electric charging stations. 

In general, areas with large population and low number of charging stations have demand for more of them. Furthermore large number of one-family-houses reduces demand, because owners of electric car install charger on their private property. However reliable and free data about ratios of housing types is not or only partly available. Therefore only population numbers and numbers of charging stations will be considered:

# Ladesäuleninfrastruktur je PLZ
https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/E-Mobilitaet/start.html
# Liste der Ladesäulen (xlsx / 8 MB)
# Liste der Ladesäulen (CSV) (csv / 11 MB)

# Bevölkerungsgröße je PLZ
https://www.suche-postleitzahl.org/downloads
# plz_einwohner.csv

Final result can be seen here: https://berlingeoheatmap1-9ks628b6jdc4vfuzdtyrwn.streamlit.app/

These are the Tasks:
1) Load the correct data from the websites in the links. As the websites are in German, use translators (Browser, AI, etc.) 
2) Use GitHub link: https://github.com/MathforDataScience/berlingeoheatmap_project1
	Install Python Environment and files.
3) Use main_template.py: Rename it into main.py. Use methods from core/methods.py. Fill the gaps in main.py, in order to achieve same result as "final result"
4) Make Streamlit app run on localhost: 
	streamlit run main.py
	Address will be: localhost:8051
5) Create your own GitHub Repo. Load/push program there. 
6) Take it into production on Streamlit: https://streamlit.io/ 
7) Analyze both geovisualizations: Where do you see demand for additional electric charging stations?
8) Write documentation: 
	Program: Structure, What means what?
	Interpretation of results
9)  Additional task (not evaluated): Make separate layers for each KW.
10) Additional task (not evaluated): Check data quality of both source files.
	Requirements: What are necessary columns? Which Formats, value ranges, distributions etc. are plausible?
	Write Python code that checks data Quality automatically