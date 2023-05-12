from diagrams import Diagram, Cluster, Edge
from diagrams.programming.flowchart import Database
from diagrams.azure.iot import IotHub
from diagrams.azure.database import DataFactory
from diagrams.azure.database import DataLake
from diagrams.azure.analytics import Databricks, StreamAnalyticsJobs
from diagrams.azure.ml import CognitiveServices, MachineLearningServiceWorkspaces
from diagrams.onprem.analytics import Powerbi
from diagrams.generic.os import Windows

graph_attr = {
    "bgcolor": "transparent",
    "dpi": "192"
}

root_clus_attr = {
    "bgcolor": "transparent",
    "pencolor":"transparent",
}


with Diagram("Lambda Architecture on Azure", direction="LR", show=False):

    with Cluster("-", graph_attr=root_clus_attr):
        with Cluster("--", graph_attr=root_clus_attr):
            data_source_1 = Database("Data Source 1")
            data_source_2 = Database("Data Source 2")
            data_source_3 = Database("Data Source 3")
            data_source_4 = Database("Data Source 4")
            data_source_5 = Database("Data Source 5")


        with Cluster("        ", graph_attr=root_clus_attr):
            with Cluster("   ", graph_attr=root_clus_attr):
                iot_hub = IotHub("Azure IoT Hub")
                data_factory = DataFactory("Azure Data Factory")

                with Cluster("  "):
                    data_lake = DataLake("Azure Data Lake")
                    databricks = Databricks("Databricks")
                    #databricks << Edge(style="invis") >> data_lake # needed to display cluster horizontally

                stream_analytics = StreamAnalyticsJobs("Azure Stream Analytics") 

            

                with Cluster("ML"):
                    cognitive_services = CognitiveServices("Azure Cognitive Services")
                    machine_learning = MachineLearningServiceWorkspaces("Azure Machine Learning")
                    #cognitive_services << Edge(style="invis") >> machine_learning # needed to display cluster horizontally

        with Cluster("BI", graph_attr={"rank": "max", "dir": "none"}):
            power_bi_1 = Powerbi("Power BI")
            power_bi_2 = Powerbi("Power BI")
            power_bi_3 = Windows("Microsoft Excel")

    [data_source_1, 
     data_source_2,
     data_source_3,
     data_source_4] >> Edge(color="blue") >> data_factory >> Edge(color="blue") >> [data_lake, databricks]  
    data_lake << Edge(color="blue") >> cognitive_services
    databricks >> Edge(color="blue") >> [power_bi_2, power_bi_3]

    data_source_5 >> Edge(color="red") >> iot_hub >>  Edge(color="red") >> stream_analytics >> Edge(color="red") >> [databricks,  power_bi_1]
    iot_hub >>  Edge(color="red") >> data_lake


