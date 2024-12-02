# Project: Problem Set

Electric mobility is essential in order to reduce emission of green house gases. In recent years sales and usage of electric vehicles has accelerated significantly. However lack of electric charging stations in many areas remains impediment for further success. Based on geovisualization of different datasets referring to Berlin we want to analyze demand for additional electric charging stations. 

In general, areas with large population and low number of charging stations have demand for more of them. Furthermore large number of one-family-houses reduces demand, because owners of electric car install charger on their private property. However reliable and free data about ratios of housing types is not or only partly available. Therefore only population numbers and numbers of charging stations will be considered:

---

Final result can be seen here: https://berlin-charging-station-mapping.streamlit.app/

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

---

### Evaluation

Our group thought that the central districts of Berlin, such as Mitte, Friedrichshain, and Kreuzberg, have the highest density of residents based on the "Residents" heatmap. This suggests that these areas are likely to have a very high demand for electric vehicle charging infrastructure. The high population density in these districts means a greater concentration of potential EV users who would require accessible charging facilities.

Additionally, other inner districts, including Neukölln, Charlottenburg-Wilmersdorf, and Tempelhof-Schöneberg, also show significant resident populations. However, based on the "Charging Stations" heatmap, these areas appear to lack sufficient coverage of charging stations. This mismatch between resident density and infrastructure coverage highlights these districts as key priority areas for the addition of new charging stations.

Furthermore, we thought that in outer districts such as Spandau, Reinickendorf, and Marzahn-Hellersdorf, although the population density is lower, the current number of charging stations seems inadequate for the geographical size and spread of these areas. These districts may require additional stations to ensure equitable access, particularly for suburban EV users.

Districts like Treptow-Köpenick and Lichtenberg, while having lower population densities, still need a basic number of charging stations to support commuters and residents with electric vehicles.

Evaluating the potential demand in charging stations, we would add the following amounts per district:

| **District**               | **Suggested Additions** | **Reason**                              |
|----------------------------|-------------------------|------------------------------------------|
| Mitte                     | 15–20                  | High population, moderate coverage.     |
| Friedrichshain-Kreuzberg  | 15–20                  | High population, moderate coverage.     |
| Neukölln                  | 10–15                  | Growing EV demand.                      |
| Charlottenburg-Wilmersdorf| 10–12                  | Moderate density, more infrastructure.  |
| Tempelhof-Schöneberg      | 8–10                   | Moderate density.                       |
| Spandau                   | 5–7                    | Suburban EV users.                      |
| Reinickendorf             | 5                      | Moderate suburban population.           |
| Marzahn-Hellersdorf       | 5                      | Low population density, still needed.   |
| Treptow-Köpenick          | 3–5                    | Coverage for commuters.                 |
| Lichtenberg               | 3–5                    | Basic coverage for low demand.          |
