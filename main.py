currentWorkingDirectory = "."

# -----------------------------------------------------------------------------
import os
os.chdir(currentWorkingDirectory)
print("Current working directory\n" + os.getcwd())

import pandas                        as pd
from core import methods             as m1
from core import HelperTools         as ht
from core.methods import preprop_lstat, preprop_resid, preprop_lstat_add_charging_station_count
from core.methods import make_streamlit_electric_Charging_resid

from config                          import pdict

# -----------------------------------------------------------------------------
@ht.timer
def main():
    """
    Main function: Generates a Streamlit app to visualize 
    electric charging station distribution and resident population in Berlin.
    """

    # Load geospatial data for Berlin postal codes
    df_geodat_plz = pd.read_csv("datasets/geodata_berlin_plz.csv", delimiter=";")

    # Load electric charging station data from an Excel file
    df_lstat = pd.read_excel("datasets/Ladesaeulenregister_SEP.xlsx")

    # Preprocess charging station data for Berlin, filter by postal codes
    df_lstat2 = preprop_lstat(df_lstat, df_geodat_plz, pdict)

    # Aggregate charging station data to count the number of stations per postal code
    gdf_lstat3 = preprop_lstat_add_charging_station_count(df_lstat2)

    # Save the intermediate processed data for later use or debugging
    df_lstat2.to_csv("datasets/df_lstat2.csv", index=False)

    # Load Berlin resident population data (number of residents in each postal code)
    df_residents = pd.read_csv("datasets/plz_einwohner.csv")

    # Preprocess resident data (filtering for valid postal codes and integrating geospatial data)
    gdf_residents2 = preprop_resid(df_residents, df_geodat_plz, pdict)

    # Generate streamlit app (to visualize heatmaps for both residents and charging stations)
    make_streamlit_electric_Charging_resid(gdf_lstat3, gdf_residents2)
# -----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__": 
    main()
