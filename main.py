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
    """Main: Generation of Streamlit App for visualizing electric charging stations & residents in Berlin"""

    df_geodat_plz   = pd.read_csv("datasets/geodata_berlin_plz.csv", delimiter=";")  
    df_lstat        = pd.read_excel("datasets/Ladesaeulenregister_SEP.xlsx")
    df_lstat2       = preprop_lstat(df_lstat, df_geodat_plz, pdict)

    # Group by PLZ and count the number of charging stations
    gdf_lstat3      = preprop_lstat_add_charging_station_count(df_lstat2)

    df_lstat2.to_csv("datasets/df_lstat2.csv", index=False)
    
    
    df_residents    = pd.read_csv("datasets/plz_einwohner.csv")
    gdf_residents2  = preprop_resid(df_residents, df_geodat_plz, pdict)

    make_streamlit_electric_Charging_resid(gdf_lstat3, gdf_residents2)
    
# -----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__": 
    main()
