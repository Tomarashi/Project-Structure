from diagrams import Cluster, Diagram, Edge
from diagrams.elastic.elasticsearch import ElasticSearch
from diagrams.ibm.user import Browser, User
from diagrams.onprem.database import Mysql
from diagrams.programming.framework import React, Spring
from diagrams.programming.language import Go as GoLang

with Diagram("Project Structure", filename="structure", strict=True):
    with Cluster("Browser", direction="TB"):
        user = User(label="User")
        brower = Browser(label="Chrome's Extention")

        user >> brower

    with Cluster("Web Application"):
        react = React(label="FrontEnd")
        spring = Spring(label="BackEnd")

        react >> spring
        spring >> react

        user >> Edge(label="User Interface") >> react

    with Cluster("Extention's Service"):
        go = GoLang(label="Gin")
        brower >> Edge(label="Rest API") >> go

    with Cluster("Database", direction="TB"):
        es = ElasticSearch(label="ElasticSearch")
        mysql = Mysql(label="MySql")

        es >> Edge(label="Protocol") >> mysql
        spring >> es
        spring >> Edge(label="Protocol") >> mysql
        go >> es
        go >> Edge(label="Protocol", style="dashed") >> mysql
