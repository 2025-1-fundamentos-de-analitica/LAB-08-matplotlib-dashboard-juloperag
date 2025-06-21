# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

#importacion de librerias
import pandas as pd
import matplotlib.pyplot as plt
import os 

#Carga de data
def load_data():
    df = pd.read_csv("./files/input/shipping-data.csv", sep=",")
    return df

def create_visual_for_shipping_per_warehouse(df):
    df_copy = df.copy()
    plt.figure()
    counts = df_copy.Warehouse_block.value_counts()
    counts.plot.bar(
        title = "Shipping per Warehouse",
        xlabel = "Warehouse block",
        ylabel = "Record Count",
        color = "tab:blue",
        fontsize=8,
    )
    #Eliminacion de bordes
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    #Guardamos grafica
    if not os.path.exists("./docs"):
        os.makedirs("./docs")
    plt.savefig("./docs/shipping_per_warehouse.png")
    #plt.savefig("sss")

def create_visual_for_mode_of_shipment(df):
    df_copy = df.copy()
    plt.figure()
    counts = df_copy.Mode_of_Shipment.value_counts()
    counts.plot.pie(
        title = "Mode_of_Shipment",
        wedgeprops=dict(width=0.35),
        ylabel = "",
        color = ["tab:blue", "tab:orange", "tab:green"],
    )
    #Eliminacion de bordes
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    #Guardamos grafica
    if not os.path.exists("./docs"):
        os.makedirs("./docs")
    plt.savefig("./docs/mode_of_shipment.png")
 
def create_visual_for_average_customer_ranting(df):
    df_copy = df.copy()
    plt.figure()
    df_copy = (df_copy[["Mode_of_Shipment", "Customer_rating"]].groupby("Mode_of_Shipment").describe())
    df_copy.columns = df_copy.columns.droplevel()
    df_copy = df_copy[["mean","min","max"]]
    plt.barh(y=df_copy.index.values, 
            width=df_copy["max"].values-1,
            left=df_copy["min"].values,
            height=0.9,
            color="lightgray",
            alpha=0.8,
            )
    colors = ["tab:green" if value >= 3.0 else "tab:orange" for value in df_copy["mean"].values]
    plt.barh(y=df_copy.index.values, 
             width=df_copy["mean"].values-1,
             left=df_copy["min"].values,
             color=colors,
             height=0.5,
             alpha=1.0,
             )
    plt.title("Average Customer Rating")
    plt.gca().spines["left"].set_color("gray")   
    plt.gca().spines["bottom"].set_color("gray")   
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    #Guardamos grafica
    if not os.path.exists("./docs"):
        os.makedirs("./docs")
    plt.savefig("./docs/average_customer_rating.png")


def create_visual_for_weight_distribution(df):
    df_copy = df.copy()
    plt.figure()
    df_copy.Weight_in_gms.plot.hist(
        title="Shipped Weight Distribution",
        color="Tab:orange",
        edgecolor="white",
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    #Guardamos grafica
    if not os.path.exists("./docs"):
        os.makedirs("./docs")
    plt.savefig("./docs/weight_distribution.png")
    
def crear_dashboard_html():
    if not os.path.exists("./docs"):
        os.makedirs("./docs")
    html_content = """
<!DOCTYPE html>
<html>
    <body>
        <h1>Shipping Dashboard Example</h1>
        <div style="width:45%;float:left">
            <img src="./shipping_per_warehouse.png" alt="Fig 1">
            <img src="./mode_of_shipment.png" alt="Fig 2">
        </div>
        <div style="width:45%;float:left">
            <img src="./average_customer_rating.png" alt="Fig 3">
            <img src="./weight_distribution.png" alt="Fig 4">            
        </div>    
    </body>
</html>
"""
    with open("./docs/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    #Cargar df
    df = load_data()
    #Crear graficas
    create_visual_for_shipping_per_warehouse(df)
    create_visual_for_mode_of_shipment(df)
    create_visual_for_average_customer_ranting(df)
    create_visual_for_weight_distribution(df)
    #Crear achivo HTML para visualizacion de grafcias
    crear_dashboard_html()


