from diagrams import Diagram, Cluster, Edge
from diagrams.azure.analytics import StreamAnalyticsJobs, SynapseAnalytics
from diagrams.azure.database import DataLake
from diagrams.azure.iot import IotHub
from diagrams.programming.flowchart import Database
from diagrams.onprem.analytics import Powerbi
from diagrams.azure.ml import CognitiveServices, MachineLearningServiceWorkspaces

with Diagram("Kappa Architecture on Azure", direction="LR", show=False):
    data_source_1 = Database("Data Source 1")
    data_source_2 = Database("Data Source 2")
    data_source_3 = Database("Data Source 3")
    iot_hub = IotHub("IoT Hub")
    stream_analytics = StreamAnalyticsJobs("Azure Stream Analytics")
    power_bi_1 = Powerbi("Power BI")
    power_bi_2 = Powerbi("Power BI")
    #cognitive_services = CognitiveServices("Azure Cognitive Services")
    #machine_learning = MachineLearningServiceWorkspaces("Azure Machine Learning")

    with Cluster("Data Sources"):
        cognitive_services = CognitiveServices("Azure Cognitive Services")
        machine_learning = MachineLearningServiceWorkspaces("Azure Machine Learning")

    with Cluster(" ", direction="TB"):
            synapse = SynapseAnalytics("Azure Synapse")
            data_lake = DataLake("Azure Data Lake")


    data_source_1 >> Edge(color="red") >> iot_hub 
    data_source_2 >> Edge(color="orange") >> iot_hub 
    data_source_3 >> Edge(color="orange") >> iot_hub
    iot_hub >> Edge(color="red") >> stream_analytics 
    iot_hub >> Edge(color="orange") >> synapse
    machine_learning << Edge(color="orange") >> synapse
    data_lake >> Edge(style="invis") >> cognitive_services

    cognitive_services >> Edge(style="invis") >> machine_learning
   # synapse >> Edge(style="invis") >> data_lake
    stream_analytics >> Edge(color="red") >> power_bi_1
    synapse >> Edge(color="orange") >> power_bi_2
