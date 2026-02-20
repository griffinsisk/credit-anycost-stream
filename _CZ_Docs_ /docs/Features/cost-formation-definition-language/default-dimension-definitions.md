---
title: Default Dimension Definitions
category: features
createdAt: '2022-01-25T13:45:03.526Z'
hidden: false
slug: default-dimension-definitions
updatedAt: '2024-11-18T16:09:32.891Z'
---
The following are the definitions for the current default dimensions. See [Additional Cloud Provider Dimensions](/docs/cfdl-reference#additional-cloud-provider-dimensions) for their IDs and a brief description of each.

```yaml
############################################
# Updates
# -  Update AWS Targetting To Better Support Demo Environments
# - Update Resource Summary ID bug for GCP which affected 
############################################
Metadata:
  Version: 1.0.16

Dimensions:
  Elasticity:
    Child: Service
    DefaultValue: Fixed Costs
    Hide: True
    Name: Elasticity
    Rules:
    - Conditions:
      - Equals: Storage
        Source: CZ:Defined:Category
      Name: Storage
      Type: Group
    - Conditions:
      - Equals: Snowflake
        Source: CloudProvider
      - Equals:
        - Networking
        - Content Delivery
        - Machine Learning
        - Appliation Integration
        - Analytics
        - Internet of Things
        - Cloud Management
        - Security
        Source: CZ:Defined:Category
      - Equals:
        - AWSLambda
        - AmazonEKS
        - AmazonECS
        - AmazonECR
        Source: Service
      - Equals:
        - Data Transfer
        - API Request
        - API Calls
        Source: UsageFamily
      - And:
        - Equals: AmazonEC2
        - Equals:
          - Spot Instance
          - NAT Gateway
          Source: UsageFamily
      - And:
        - Equals: AmazonRDS
        - Equals: System Operation
          Source: UsageFamily
      - And:
        - Equals: AmazonDynamoDB
        - Equals: Amazon DynamoDB PayPerRequest Throughput
          Source: UsageFamily
      - And:
        - Equals: AWSCloudTrail
        - Equals: Management Tools - AWS CloudTrail Data Events Recorded
          Source: UsageFamily
      Name: Variable Costs
      Type: Group
    Source: Service

  NetworkingCategory:         # Problem referencing Azure tag which might not exist
    Name: Networking Category
    Child: CZ:Defined:NetworkingSubCategory
    Source: Service
    DefaultValue: Non-Networking Spend
    Rules:
      - Type: Group
        Name: Unsupported Cloud Provider
        Conditions:
          - Not:
            - Source: CloudProvider
              Contains: [AWS, Azure, GCP]
      #--------------------------------------
      # AWS Logic
      #--------------------------------------
      - Type: Group
        Name: CloudFront    # Must come first
        Conditions:
          - And:
            - Equals: AmazonCloudFront
            - Source: UsageFamily
              Equals: Data Transfer
      - Type: Group
        Name: Data Transfer
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: AWS
            - Source: UsageFamily
              Equals: Data Transfer
      - Type: Group
        Name: NAT Gateway
        Conditions:
          - Source: UsageFamily
            Equals: NAT Gateway
      - Type: Group
        Name: VPC Endpoint
        Conditions:
          - Source: UsageFamily
            Equals: VpcEndpoint
      - Type: Group
        Name: Direct Connect
        Conditions:
          - Equals: AWSDirectConnect
      - Type: Group
        Name: VPC Client VPN
        Conditions:
          - And:
            - Equals: AmazonVPC
            - Source: UsageType
              Contains: ClientVPN
      - Type: Group
        Name: VPC Transit Gateway
        Conditions:
          - And:
            - Equals: AmazonVPC
            - Source: UsageType
              Contains: TransitGateway
      - Type: Group
        Name: VPC Peering
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: AWS
            - Source: UsageFamily
              Equals: VPC Peering
      - Type: Group
        Name: VPC
        Conditions:
          - Equals: AmazonVPC
      - Type: Group
        Name: Load Balancing
        Conditions:
          - Equals: AWSELB
      - Type: Group
        Name: DNS
        Conditions:
          - Equals: AmazonRoute53
      - Type: Group
        Name: VPC Flowlogs
        Conditions:
          - Source: CZ:Defined:ResourceType
            Equals: ["EC2: vpc-flow-log", "CloudWatch: vpc-flow-log"]
      - Type: Group
        Name: File Transfer
        Conditions:
          - Equals: AWSTransfer
      #--------------------------------------
      # GCP Logic
      #--------------------------------------
      - Type: Group
        Name: Load Balancing     # Must come first
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: GCP
            - Source: UsageFamily
              Contains: Load Balancing
      - Type: Group
        Name: Data Transfer
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: GCP
            - Source: UsageFamily
              BeginsWith: Network
      - Type: Group
        Name: DNS
        Conditions:
          - Equals: Cloud DNS
      - Type: Group
        Name: Networking
        Conditions:
          - Equals: Networking
      #--------------------------------------
      # Azure Logic
      #--------------------------------------
      - Type: Group
        Name: Virtual Network
        Conditions:
          - Equals: virtual network
          - And:
            - Equals: microsoft.network
            - Source: UsageFamily
              Equals: Virtual Network
      - Type: Group
        Name: Load Balancing
        Conditions:
          - And:
            - Equals: microsoft.network
            - Source: UsageFamily
              Equals: Load Balancer
      - Type: Group
        Name: NAT Gateway
        Conditions:
          - And:
            - Equals: microsoft.network
            - Source: UsageFamily
              Equals: NAT Gateway
      - Type: Group
        Name: DNS
        Conditions:
          - And:
            - Equals: microsoft.network
            - Source: UsageFamily
              Equals: Azure DNS
      - Type: Group
        Name: Networking
        Conditions:
          - Equals: microsoft.network

  NetworkingSubCategory:      # Problem referencing Azure tag which might not exist
    Name: Networking Sub-Category
    Source: UsageFamily
    DefaultValue: Other
    Rules:
      - Type: Group
        Name: Unsupported Cloud Provider
        Conditions:
          - Not:
            - Source: CloudProvider
              Contains: [AWS, Azure, GCP]
      - Type: Group
        Name: Non-Networking Spend
        Conditions:
          - Source: CZ:Defined:NetworkingCategory
            Equals: Non-Networking Spend
      #--------------------------------------
      # AWS Logic
      #--------------------------------------
      - Type: GroupBy
        Source: TransferType
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonCloudfront
            - Equals: Data Transfer
      - Type: Group
        Name: S3 Inbound
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonS3
            - Equals: Data Transfer
            - Source: UsageType
              Contains: DataTransfer-In-Bytes
      - Type: Group
        Name: S3 Outbound
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonS3
            - Equals: Data Transfer
            - Source: UsageType
              Contains: DataTransfer-Out-Bytes
      - Type: Group
        Name: IntraRegion - AZ to AZ
        Conditions:
          - And:
            - Equals: Data Transfer
            - Source: UsageType
              Contains: DataTransfer-Regional-Bytes
      - Type: Group
        Name: AWS Inbound
        Conditions:
          - And:
            - Equals: Data Transfer
            - Source: UsageType
              Contains: DataTransfer-In-Bytes
      - Type: Group
        Name: AWS Outbound
        Conditions:
          - And:
            - Equals: Data Transfer
            - Source: UsageType
              Contains: DataTransfer-Out-Bytes
      - Type: Group
        Name: InterRegion Inbound
        Conditions:
          - And:
            - Equals: Data Transfer
            - Source: UsageType
              Contains: AWS-In-Bytes
      - Type: Group
        Name: InterRegion Outbound
        Conditions:
          - And:
            - Equals: Data Transfer
            - Source: UsageType
              Contains: AWS-Out-Bytes
      - Type: Group
        Name: Data Transfer
        Conditions:
          - Equals: Data Transfer
      - Type: Group
        Name: NAT Gateway (Bytes)
        Conditions:
          - And:
            - Equals: NAT Gateway
            - Source: UsageType
              Contains: Bytes
      - Type: Group
        Name: NAT Gateway (Hours)
        Conditions:
          - And:
            - Equals: NAT Gateway
            - Source: UsageType
              Contains: Hours
      - Type: Group
        Name: NAT Gateway (Other)
        Conditions:
          - Equals: NAT Gateway
      - Type: Group
        Name: VPC PublicIPv4-InUseAddress
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonVPC
            - Source: UsageType
              Contains: "PublicIPv4:InUseAddress"
      - Type: Group
        Name: VPC PublicIPv4-IdleAddress
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonVPC
            - Source: UsageType
              Contains: "PublicIPv4:IdleAddress"
      - Type: Group
        Name: VPC Endpoint (Bytes)
        Conditions:
          - And:
            - Equals: VpcEndpoint
            - Source: UsageType
              Contains: Bytes
      - Type: Group
        Name: VPC Endpoint (Hours)
        Conditions:
          - And:
            - Equals: VpcEndpoint
            - Source: UsageType
              Contains: Hours
      - Type: Group
        Name: VpcPeering Out-Bytes
        Conditions:
          - And:
            - Equals: VPC Peering
            - Source: UsageType
              Contains: VpcPeering-Out-Bytes
      - Type: Group
        Name: VpcPeering In-Bytes
        Conditions:
          - And:
            - Equals: VPC Peering
            - Source: UsageType
              Contains: VpcPeering-In-Bytes
      - Type: Group
        Name: VPC Endpoint (Other)
        Conditions:
          - Equals: VpcEndpoint
      - Type: Group
        Name: Transit Gateway (Bytes)
        Conditions:
          - And:
            - Source: UsageType
              Contains: TransitGateway
            - Source: UsageType
              Contains: Bytes
      - Type: Group
        Name: Transit Gateway (Hours)
        Conditions:
          - And:
            - Source: UsageType
              Contains: TransitGateway
            - Source: UsageType
              Contains: Hours
      - Type: Group
        Name: Transit Gateway (Other)
        Conditions:
          - Source: UsageType
            Contains: TransitGateway
      - Type: Group
        Name: Client VPN (Bytes)
        Conditions:
          - And:
            - Source: UsageType
              Contains: ClientVPN
            - Source: UsageType
              Contains: Bytes
      - Type: Group
        Name: Client VPN (Hours)
        Conditions:
          - And:
            - Source: UsageType
              Contains: ClientVPN
            - Source: UsageType
              Contains: Hours
      - Type: Group
        Name: Client VPN (Other)
        Conditions:
          - Source: UsageType
            Contains: ClientVPN
      - Type: GroupBy
        Source: UsageFamily
        Conditions:
          - Source: Service
            Equals:
              - AmazonVPC
              - AWSDirectConnect
              - AWSELB
      #--------------------------------------
      # GCP Logic
      #--------------------------------------
      # Load Balancing
      - Type: Group
        Name: HTTP Load Balancing
        Conditions:
          - BeginsWith: HTTP Load Balancing
      - Type: Group
        Name: Internal Load Balancing
        Conditions:
          - BeginsWith: Network Internal Load Balancing
      - Type: Group
        Name: Network Load Balancing
        Conditions:
          - BeginsWith: Network Load Balancing
      - Type: Group
        Name: Network HTTP Load Balancing
        Conditions:
          - BeginsWith: Network HTTP Load Balancing
      - Type: Group
        Name: Networking Cloud Load Balancing
        Conditions:
          - BeginsWith: Networking Cloud Load Balancing
      # "Networking"
      - Type: Group
        Name: Cloud Armor
        Conditions:
          - BeginsWith: Networking Cloud Armor
      - Type: Group
        Name: Service Directory Resource
        Conditions:
          - BeginsWith: Networking Service Directory
      # Data Transfer
      - Type: Group
        Name: Traffic Egress
        Conditions:
          - BeginsWith: Networking Traffic Egress
      - Type: Group
        Name: Traffic Ingress
        Conditions:
          - BeginsWith: Networking Traffic Ingress
      - Type: Group
        Name: Google Egress
        Conditions:
          - BeginsWith: Network Google Egress
      - Type: Group
        Name: Google Ingress
        Conditions:
          - BeginsWith: Network Google Ingress
      - Type: Group
        Name: Internal Load Balancing
        Conditions:
          - BeginsWith: Network Internal Load Balancing
      - Type: Group
        Name: Internet Region Egress
        Conditions:
          - BeginsWith: Network Internet Egress
      - Type: Group
        Name: Internet Region Ingress
        Conditions:
          - BeginsWith: Network Internet Ingress
      - Type: Group
        Name: Intra Zone Egress
        Conditions:
          - BeginsWith: Network Intra Zone Egress
      - Type: Group
        Name: Intra Zone Ingress
        Conditions:
          - BeginsWith: Network Intra Zone Ingress
      - Type: Group
        Name: Inter Zone Egress
        Conditions:
          - BeginsWith: Network Inter Zone Egress
      - Type: Group
        Name: Inter Zone Ingress
        Conditions:
          - BeginsWith: Network Inter Zone Ingress
      - Type: Group
        Name: Inter Region Egress
        Conditions:
          - BeginsWith: Network Inter Region Egress
      - Type: Group
        Name: Inter Region Ingress
        Conditions:
          - BeginsWith: Network Inter Region Ingress
      - Type: Group
        Name: HTTP Load Balancing Egress
        Conditions:
          - BeginsWith: Network HTTP Load Balancing Egress
      - Type: Group
        Name: HTTP Load Balancing Ingress
        Conditions:
          - BeginsWith: Network HTTP Load Balancing Ingress
      #--------------------------------------
      # Azure Logic
      #--------------------------------------
      - Type: GroupBy
        Source: Operation
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: Azure
            - Not:
              - Source: CZ:Defined:NetworkingCategory
                Equals: Other

  BillingLineItem:
    Name: Billing Line Item
    Rules:
      #--------------------------------------
      # AWS Override Logic
      #--------------------------------------
      - Type: Group
        Name: Tax
        Conditions:
          - Source: LineItemType
            Equals: Tax
      - Type: Group
        Name: Support
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: AWS
            - Source: Service
              Equals: [OCBPremiumSupport, AWSSupportEnterprise, AWSSupportBusiness, AWSDeveloperSupport]
      - Type: Group
        Name: EdpRefund
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: AWS
            - Source: LineItemType
              Equals: Refund
            - Source: Description
              Equals: Enterprise Program Discount
      - Type: Group
        Name: MAP Credit
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: AWS
            - Source: LineItemType
              Equals: Credit
            - Source: Description
              Contains: [_MPE, _MAP, DBA_NC, SLS_SAP]
      - Type: Group
        Name: Credit
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: AWS
            - Source: LineItemType
              Equals: Refund
            - Source: Description
              Transforms:
                - Type: Lower
              Contains: credit
      - Type: Group
        Name: RICoveredUsage
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: AWS
            - Source: LineItemType
              Equals: DiscountedUsage
      - Type: Group
        Name: RIUpfrontFee
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: AWS
            - Source: LineItemType
              Equals: Fee
            - Source: Description
              BeginsWith: [Sign up charge for subscription, RI Marketplace charge]
            - Not:
              - Source: Service
                Equals: APNFee
      #--------------------------------------
      # GCP Override Logic
      #--------------------------------------
      - Type: Group
        Name: Support
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: GCP
            - Source: LineItemType
              Equals: Usage
            - Source: Service
              Equals: Support
      - Type: Group
        Name: Fee
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: GCP
            - Source: LineItemType
              Equals: Purchase
      - Type: Group
        Name: DiscountedUsage
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: GCP
            - Or:
              - And:
                - Source: LineItemType
                  Equals: Usage
                - Source: UsageFamily
                  BeginsWith: Commitment
              - And:
                - Source: LineItemType
                  Equals: Credit
                - Source: Description
                  Contains: COMMITTED_USAGE_DISCOUNT
      - Type: Group
        Name: Discount
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: GCP
            - And:
              - Source: LineItemType
                Equals: Credit
              - Not:
                - Source: Description
                  Contains: PROMOTION
      #------------------------------------
      # Default Logic
      #------------------------------------
      - Type: GroupBy
        Source: LineItemType

  Category:                             # Needs Improvement - Needs CZ:Defined:Category_Azure dimension
    Name: Service Category
    Child: Service
    Source: CloudProvider
    Transforms:
      - Type: Lower
    DefaultValue: Other
    Rules:
      - Type: Group
        Name: Service Category Unavailable
        Conditions:
          - Not:
            - Contains: [aws, azure, gcp, snowflake, mongodb, databricks, newrelic, datadog, anthropic, baidu, chatgpt, claude, cohere, deepmind, deepsearch, gemini, llama, meta, minstral, openai, open-ai]
      #--------------------------------------
      # Cloud Provider Specific Logic
      #--------------------------------------
      - Type: GroupBy
        Source: CZ:Defined:Category_AWS
        Conditions:
          - Not:
            - Source: CZ:Defined:Category_AWS
              BeginsWith: Admin
      - Type: GroupBy
        Source: CZ:Defined:Category_GCP
        Conditions:
          - Not:
            - Source: CZ:Defined:Category_GCP
              BeginsWith: Admin
      - Type: GroupBy
        Source: CZ:Defined:Category_Azure
        Conditions:
          - Not:
            - Source: CZ:Defined:Category_Azure
              BeginsWith: Admin
      #--------------------------------------
      # AnyCost Adapter Explcit Mapping
      #--------------------------------------
      - Type: Group
        Name: Databases
        Conditions:
          - Contains: [snowflake, mongodb]
      - Type: Group
        Name: Management and Governance
        Conditions:
          - Contains: [newrelic, datadog]
      - Type: Group
        Name: AI and Machine Learning
        Conditions:
          - Contains: [anthropic, baidu, chatgpt, claude, cohere, deepmind, deepsearch, gemini, llama, meta, minstral, openai, open-ai]

  Category_AWS:                         # HIDDEN
    Name: Service Category - AWS
    Hide: True
    Source: Service
    Rules:
      - Type: Group
        Name: Admin - Non-AWS Spend
        Conditions:
          - Not:
            - Source: CloudProvider
              BeginsWith: AWS
      - Type: Group
        Name: Support
        Conditions:
          - Source: Service
            Equals: [OCBPremiumSupport, AWSDeveloperSupport, AWSSupportBusiness]
      - Type: Group
        Name: Networking          # Must come first
        Conditions:
          - Source: UsageFamily
            Equals: [Data Transfer, NAT Gateway, VPC Peering]
          - Equals: [AmazonCloudFront, AmazonRoute53, AmazonVPC, AWSCloudMap,
                    AWSDirectConnect, AWSGlobalAccelerator, AWSDataTransfer, AWSELB]
          - Equals: AWSCloudWAN    # Not explicitly listed by AWS
      - Type: Group
        Name: Storage          # Must come second
        Conditions:
          - Source: CZ:Defined:ResourceType
            Equals: ["EC2: volume", "EC2: snapshot"]
          - Equals: [AmazonEFS, AmazonFSx, AmazonS3, AmazonS3GlacierDeepArchive, AmazonGlacier,
                    AWSBackup, AWSStorageGateway, AWSElasticDisasterRecovery, AmazonECR, AmazonECRPublic]
      - Type: Group
        Name: AI and Machine Learning     # Must come above compute
        Conditions:
          - Equals: [CodeGuru, comprehend, AmazonBedrock, AmazonDevOpsGuru, AmazonForecast, AmazonKendra, AmazonLex,
                    AmazonLookoutEquipment, AmazonLookoutMetrics, AmazonLookoutVision, AmazonPersonalize,
                    AmazonPolly, AmazonQ, AmazonRekognition, AmazonSageMaker, AmazonTextract, transcribe, translate,
                    AWSDeepComposer, AWSDeepLens, AWSDeepRacer]
          - Equals: AmazonML    # Not explicitly listed by AWS
          - Contains: Bedrock   # Using Contains because there are a number of marketplace services that have Bedrock in the name
          - And:
            - Equals: AmazonEC2
            - Source: CZ:Defined:InstanceType
              Contains: [c7g, dl, f1, g3, g4, g5, g6, inf, p3, p4, p5, trn, vt]
      - Type: Group
        Name: Analytics
        Conditions:
          - Equals: [AmazonAthena, AmazonCloudSearch, ElasticMapReduce, AmazonKinesis, AmazonKinesisFirehose,
                    AmazonKinesisAnalytics, AmazonMSK, AmazonES, AmazonQuickSight, AmazonRedshift, datapipeline,
                    AWSGlue, AWSLakeFormation]
      - Type: Group
        Name: Business Applications
        Conditions:
          - Equals: [AlexaWebInfoService, AmazonChime, AmazonChimeDialin, AmazonChimeFeatures, AmazonChimeVoiceConnector,
                    AmazonConnect, AmazonPinpoint, AmazonSES, AmazonWorkDocs, AmazonWorkMail]
          - Equals: [ContactCenterTelecomm, ContactLensAmazonConnect]   # Not explicitly listed by AWS
          - Equals: [AmazonAppStream, AmazonWorkSpaces]   # AWS Categories this as End User Computing
      - Type: Group
        Name: Compute
        Conditions:
          - Equals: [AmazonEC2, AmazonECS, AmazonEKS, AmazonLightsail, AWSAppRunner, AWSLambda, VMwareCloudOnAWS]
          - Equals: ComputeSavingsPlans   # Not explicitly listed by AWS
      - Type: Group
        Name: Databases
        Conditions:
          - Equals: [AmazonDocDB, AmazonDynamoDB, AmazonDAX, AmazonElastiCache, AmazonMemoryDB, AmazonNeptune,
                    AmazonRDS, AmazonRedshift, AmazonTimestream, AWSDatabaseMigrationSvc]
      - Type: Group
        Name: Developer Tools
        Conditions:
          - Equals: [AWSCloudShell, AWSCodeArtifact, CodeBuild, AWSCodeCommit, AWSCodePipeline, AWSDeviceFarm, AWSXRay]
      - Type: Group
        Name: Integration
        Conditions:
          - Equals: [AppFlow, AWSEvents, AmazonMWAA, AmazonMQ, AmazonSNS, AWSQueueService, AmazonStates]
      - Type: Group
        Name: Internet of Things
        Conditions:
          - Contains: IoT
      - Type: Group
        Name: Management and Governance
        Conditions:
          - Equals: [AmazonCloudWatch, AmazonGrafana, AmazonPrometheus, AWSCloudFormation, AWSCloudTrail, AWSConfig,
                    OpsWorks, AmazonRegistrar, AWSResilienceHub, AWSServiceCatalog, AWSSystemsManager]
          - Equals: [AWSCostExplorer]   # AWS Categories this Cloud Financial Management
      - Type: Group
        Name: Media
        Conditions:
          - Contains: ElementalMedia
          - Equals: AmazonKinesisVideo
      - Type: Group
        Name: Migration
        Conditions:
          - Equals: [AWSApplicationMigrationSvc, AWSDatabaseMigrationSvc, AWSDataSync, AWSMigrationHubRefactorSpaces, AWSTransfer]
      - Type: Group
        Name: Security
        Conditions:
          - Equals: [AmazonCognito, AmazonCognitoSync, AmazonDetective, AmazonGuardDuty, AmazonInspector, AmazonInspectorV2,
                    AmazonMacie, AmazonSecurityLake, auditmanager, AWSCertificateManager, CloudHSM, AWSDirectoryService,
                    AWSFMS, awskms, AWSNetworkFirewall, AWSSecretsManager, AWSSecurityHub, AWSShield, awswaf]
      - Type: Group
        Name: Web
        Conditions:
          - Equals: [AmazonApiGateway, AmazonLocationService, AmazonPinpoint, AmazonSES, AWSAmplify, AWSAppSync, AWSDeviceFarm]
      #-------------------------------------------
      # Put Marketplace at the end so we can get the AI Services into AI
      #-------------------------------------------
      - Type: Group
        Name: Marketplace
        Conditions:
          - Source: CloudProvider
            Equals: AWS Marketplace

  Category_GCP:                         # HIDDEN
    Name: Service Cateogry - GCP
    Hide: True
    Source: Service
    Rules:
      - Type: Group
        Name: Admin - Non-AWS Spend
        Conditions:
          - Not:
            - Source: CloudProvider
              BeginsWith: GCP
      - Type: Group
        Name: Support
        Conditions:
          - And:
            - Source: Account
              HasValue: False
            - Source: Service
              Equals: Support
      - Type: Group
        Name: Marketplace
        Conditions:
          - And:
            - Source: Account
              HasValue: False
            - Source: LineItemType
              Equals: Usage
            - Not:
              - Source: Service
                Equals: [Compute Engine, Support]
            - Not:
              - Source: UsageFamily
                BeginsWith: [Commitment - dollar based]
      - Type: Group
        Name: AI and Machine Learning
        Conditions:
          - Equals: [Vertex AI, Vertex AI Workbench, Vertex Explainable AI]
          - Equals: [AutoML, Dialogflow, Media Translation, Natural Language AI, Recommendations AI, Speech-to-Text,
                    Text-to-Speech, Translation AI, Video AI, Vision AI]
          - Equals: [AI Infrastructure, Cloud TPUs, Deep Learning VM Image, Deep Learning Containers, TensorFlow Enterprise]
          - Equals: [Contact Center AI, Document AI, Intelligent Products, Product Discovery]
          - Equals: [Transcribe, Translate]
          - Contains: [Claude, Llama, Mistral]    # AI Keywords
      - Type: Group
        Name: Analytics
        Conditions:
          - Equals: [BigQuery, BigQuery BI Engine, BigQuery Reservation API, Looker, Dataproc, Cloud Dataflow, Cloud Pub/Sub, Cloud Data Fusion, Data Catalog, Cloud Composer, Dataprep,
                    Dataplex, Analytics Hub, Looker Studio, Google Marketing Platform, Cloud Life Sciences, Earth Engine, BigLake,
                    Elastic Cloud (managed Elasticsearch Service)]
          - Equals: [Custom Search]
      - Type: Group
        Name: Compute
        Conditions:
          - Equals: [App Engine, Bare Metal Solution, Batch, Cloud GPUs, Cloud Run, Compute Engine, Migrate to Virtual Machines,
                    Spot VMs, Recommender, Shielded VMs, Sole-tenant Nodes, SQL Server on Google Cloud, VMware Engine]
          - Equals: [Kubernetes Engine, Artifact Registry, Container Registry, Container Security, Deep Learning Containers,    # Azure Categories this as Containers
                    Google Kubernetes Engine (GKE), Knative, Kubernetes applications on Google Cloud Marketplace]
          - Equals: [Cloud Functions, Workflows]    # Azure Categories this as Serverless Computing
      - Type: Group
        Name: Databases
        Conditions:
          - Equals: [AlloyDB for PostgreSQL, Bare Metal Solution, Cloud Bigtable, Cloud Spanner, Cloud SQL, Database Migration Service,
                    Firestore, Firebase Realtime Database, Cloud Memorystore for Redis, Datastream]
      - Type: Group
        Name: Developer Tools
        Conditions:
          - Equals: [Artifact Registry, Assured Open Source Software, Cloud Build, Cloud Code, Cloud Scheduler, Cloud SDK,
                    Cloud Source Repositories, Cloud Tasks, Cloud Workstations, Container Registry, Firebase Crashlytics, Firebase Test Lab,
                    Google Cloud Deploy, Gradle App Engine Plugin, Maven App Engine Plugin, Tekton, Tools for Eclipse, Tools for PowerShell]
      - Type: Group
        Name: Internet of Things
        Conditions:
          - Equals: [Edge TPU, IoT Core]
      - Type: Group
        Name: Multicloud
        Conditions:
          - Equals: [Anthos, Apigee API Management, Cloud Run for Anthos, Migrate to Containers, Google Distributed Cloud]
      - Type: Group
        Name: Management and Governance
        Conditions:
          - Equals: [Anthos Config Management, Anthos Service Mesh, Carbon Footprint, Cloud APIs, Cloud Console, Cloud Mobile App,
                    Cloud Shell, Config Connector, Cost Management, Deployment Manager, Service Catalog, Terraform on Google Cloud,
                    Stackdriver Monitoring, Stackdriver Trace]
          - Equals: Payment Gateway   # Azure Categories this as Financial Services
          - Equals: [Cloud Debugger, Cloud Logging, Cloud Monitoring, Cloud Profiler, Cloud Trace, Cloud Error Reporting]    # Azure Categories this as Operations
      - Type: Group
        Name: Media
        Conditions:
          - Equals: [Live Stream API, OpenCue, Transcoder API, Video Stitcher API]
      - Type: Group
        Name: Migration
        Conditions:
          - Equals: [Application migration, BigQuery Data Transfer Service, Cloud Foundation Toolkit, Migrate to Containers,
                    Migrate to Virtual Machines, Migration Center, Transfer Appliance]
      - Type: Group
        Name: Networking
        Conditions:
          - Equals: [Networking, Cloud Armor, Cloud CDN, Cloud Domains, Cloud DNS, Cloud IDS, Cloud Load Balancing, Cloud NAT, Hybrid Connectivity,
                    Media CDN, Network Connectivity Center, Network Intelligence Center, Network Service Tiers, Private Service Connect,
                    Service Directory, Spectrum Access System (SAS), Traffic Director, Virtual Private Cloud (VPC)]
      - Type: Group
        Name: Security
        Conditions:
          - Equals: [Access Transparency, Assured Workloads, Chronicle Security Operations, Chronicle SIEM, Cloud Asset Inventory,
                    Cloud Data Loss Prevention, Cloud Key Management Service (KMS), Confidential Computing, Cloud Firewall, Risk Protection Program,
                    Secret Manager, Security Commander Center, Shielded VMs, Chronicle SOAR, VirusTotal, VPC Service Controls]
          - Equals: [BeyondCorp Enterprise, Certificate Authority Service, Cloud Identity, Identity and Access Management,
                    Identity-Aware Proxy, Identity Platform, Managed Service for Microsoft Active Directory, Policy Intelligence,
                    Resource Manager, Titan Security Key, Workforce Identity Federation]
          - Equals: [reCAPTCHA Enterprise, Web Risk]
          - Equals: [Assured Open Source Software, Software Delivery Shield]
          - Equals: [Mandiant Threat Intelligence, Mandiant Attack Surface Management, Mandiant Digital Threat Monitoring,
                    Mandiant Security Validation, Mandiant Ransomware Defense Validation]
          - Equals: [Mandiant Automated Defense, Mandiant Managed Detection and Response, Mandiant Breach Analytics for Chronicle]
          - Equals: [Mandiant Incident Resposne Services, Mandiant Consulting Services, Mandiant Experise on Demand, Mandiant Academy]
          - Equals: [Container Registry Vulnerability Scanning]
      - Type: Group
        Name: Storage
        Conditions:
          - Equals: [BigQuery Storage API, Storage Transfer Service, Cloud Storage, Cloud Storage for Firebase, Cloud Filestore, Google Workspace Essentials, Local SSD,
                    Persistent Disk, Google Cloud Backup and DR]

  Category_Azure:                       # HIDDEN
    Name: Service Category - Azure
    Hide: True
    Source: Service
    Rules:
      - Type: Group
        Name: Admin - Non-Azure Spend
        Conditions:
          - Not:
            - Source: CloudProvider
              BeginsWith: Azure
      - Type: Group
        Name: Marketplace
        Conditions:
          - Source: Service
            Equals: marketplace
      #-----------------------------------------
      # Service Overrides Based On Usage Family
      #-----------------------------------------
      - Type: Group
        Name: Analytics
        Conditions:
          - Source: UsageFamily
            Equals: [Azure Synapse Analytics, Logic Apps]
      - Type: Group
        Name: Integration
        Conditions:
          - Source: UsageFamily
            Equals: Service Bus
      - Type: Group
        Name: Compute
        Conditions:
          - Source: UsageFamily
            Equals: Virtual Machines
      - Type: Group
        Name: Networking
        Conditions:
          - Source: UsageFamily
            Equals: [Azure DNS, Bandwidth, Load Balancer, Virtual Network]
      - Type: Group
        Name: Security
        Conditions:
          - Source: UsageFamily
            BeginsWith: Microsoft Defender
      - Type: Group
        Name: Storage
        Conditions:
          - Source: UsageFamily
            Equals: Storage
      #-----------------------------------------
      # Service Mapping
      #-----------------------------------------
      - Type: Group
        Name: AI and Machine Learning
        Conditions:
          - Equals: [microsoft.aisearch, microsoft.botservice, microsoft.cognitiveservices, microsoft.contentsafety, microsoft.customvision, microsoft.databricks, 
                     microsoft.documentintelligence, microsoft.face, microsoft.openai, microsoft.immersivereader, microsoft.language, microsoft.machinelearning, 
                     microsoft.machinelearningservices, microsoft.speech, microsoft.syntex, microsoft.translator, microsoft.videoindexer, microsoft.vision]
      - Type: Group
        Name: Analytics
        Conditions:
          - Equals: [microsoft.analysisservices, microsoft.datafactory, microsoft.datalakestore, microsoft.digitaltwins,
                     microsoft.fabric, microsoft.hdinsight, microsoft.kusto, microsoft.powerbidedicated,
                     microsoft.purview, microsoft.signalrservice, microsoft.streamanalytics, microsoft.synapse]
      - Type: Group
        Name: Business Applications
        Conditions:
          - Equals: [microsoft.saas]
      - Type: Group
        Name: Compute
        Conditions:
          - Equals: [microsoft.app, microsoft.batch, microsoft.certificateregistration, microsoft.classiccompute, microsoft.compute,
                     microsoft.containerservice, microsoft.web, microsoft.containerinstance, microsoft.containerregistry]
      - Type: Group
        Name: Databases
        Conditions:
          - Equals: [microsoft.cache, microsoft.dbformariadb, microsoft.dbformysql, microsoft.dbforpostgresql,
                     microsoft.documentdb, microsoft.sql]
      - Type: Group
        Name: Developer Tools
        Conditions:
          - Equals: [api management, github, marketplace, microsoft.appconfiguration, microsoft.dashboard, microsoft.devcenter,
                     microsoft.labservices, microsoft.loadtestservice, microsoft.visualstudio]
      - Type: Group
        Name: Integration
        Conditions:
          - Equals: [microsoft.appplatform, microsoft.healthcareapis, microsoft.logic, microsoft.maps, 
                     microsoft.relay, microsoft.servicebus]
      - Type: Group
        Name: Internet of Things
        Conditions:
          - Equals: [microsoft.devices, microsoft.eventgrid, microsoft.eventhub, microsoft.notificationhubs]
      - Type: Group
        Name: Management and Governance
        Conditions:
          - Equals: [microsoft.automation, microsoft.insights, microsoft.monitor, microsoft.operationalinsights, microsoft.recoveryservices]
      - Type: Group
        Name: Networking
        Conditions:
          - Equals: [bastion scale units, microsoft.cdn, microsoft.classicnetwork, microsoft.network, virtual network]
      - Type: Group
        Name: Security
        Conditions:
          - Equals: [microsoft.aad, microsoft.azureactivedirectory, microsoft.dataprotection, microsoft.easm,
                     microsoft.hybridcompute, microsoft.keyvault, microsoft.security]
      - Type: Group
        Name: Storage
        Conditions:
          - Equals: [microsoft.classicstorage, microsoft.elasticsan, microsoft.netapp, microsoft.storage]
      - Type: Group
        Name: Web
        Conditions:
          - Equals: [microsoft.bing, microsoft.media, microsoft.search]

  InstanceType:
    Name: Instance Type
    Hide: False
    DefaultValue: No Instance Type
    Rules:
      - Type: Group
        Name: Instance Type Categorization Unavailable
        Conditions:
          - Not:
            - Source: CloudProvider
              Contains: [AWS, Azure, GCP]
      #--------------------------------------
      # AWS Logic
      #--------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: ':'
            Index: 2
        Conditions:
          - Source: UsageFamily
            Contains: [Instance, CPU Credits, Dedicated Host]
          - And:
            - Source: UsageType
              Contains: [BoxUsage, SpotUsage, HeavyUsage, NodeUsage]
            - Not:
              - Source: Service
                Equals: AmazonDynamoDB
      #--------------------------------------
      # GCP Logic
      #--------------------------------------
      - Type: GroupBy
        Source: Tag:gcp:compute.googleapis.com/machine_spec
        Conditions:
          - Source: Service
            Equals: Compute Engine
      - Type: GroupBy
        Source: UsageFamily
        Transforms:
          - Type: Split
            Delimiter: ' running in'
            Index: 1
        Conditions:
          - And:
            - Source: Service
              Equals: Compute Engine      
            - Source: UsageFamily
              Contains: running in
      #--------------------------------------
      # Azure Logic
      #--------------------------------------
      - Type: GroupBy
        Source: 
          - UsageType
          - Operation
        Format: '{0} - {1}'
        Conditions:
          - And:
            - Source: Service
              Equals: "microsoft.compute"
            - Source: UsageFamily
              Equals: Virtual Machines
            - Source: PricingUnit
              Equals: 1 Hour
          - And:
            - Source: Service
              BeginsWith: "microsoft"
            - Source: Service
              Contains: "sql"
            - Source: UsageType
              Contains: Compute
            - Source: PricingUnit
              Equals: 1 Hour
      - Type: GroupBy
        Source: Operation
        Conditions:
          - Or:
            - And:
              - Source: Service
                Equals: "microsoft.cache"
              - Source: PricingUnit
                Equals: 1 Hour
            - And:
              - Source: Service
                Equals: "microsoft.web"
              - Source: UsageFamily
                Equals: Azure App Service
              - Source: PricingUnit
                Equals: 1 Hour

  PaymentOption:                        # Needs Improvement - How to identify RI/SP purchases in GCP / Azure
    Name: Payment Option
    Hide: False
    DefaultValue: On-Demand
    Rules:
      - Type: Group
        Name: Payment Option Unavailable
        Conditions:
          - Not:
            - Source: CloudProvider
              Contains: [AWS, Azure, GCP, Datadog]
      #--------------------------------------
      # AWS Logic
      #--------------------------------------
      - Type: Group
        Name: Reservation
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: AWS
            - Source: CZ:Defined:BillingLineItem      # Needs CZ:Defined:BillingLineItem and not regular LineItemType
              Equals: [DiscountedUsage, RICoveredUsage, RIFee, RIUpfrontFee]
      - Type: Group
        Name: Savings Plan
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: AWS
            - Source: CZ:Defined:BillingLineItem
              Equals: [SavingsPlanCoveredUsage, SavingsPlanNegation, SavingsPlanRecurringFee, SavingsPlanUpfrontFee]
      - Type: Group
        Name: Spot
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: AWS
            - Source: UsageType
              Contains: SpotUsage
      - Type: Group
        Name: Provisioned
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: AWS
            - Or:
              - Source: UsageFamily
                Contains: [Provisioned, CapacityUnit]
              - Source: UsageType
                Transforms:
                  - Type: Lower
                Contains: [piops, p-iops]
              - And:
                - Source: Service
                  Contains: AmazonBedrock
                - Source: PricingUnit
                  Contains: Instance-hrs
      - Type: Group
        Name: On-Demand - Instances
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: AWS
            - Source: UsageFamily
              Contains: [Instance, CPU Credits]
      #--------------------------------------
      # Azure Logic
      #--------------------------------------
      - Type: Group
        Name: Reservation
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: Azure
            - Source: CZ:Defined:BillingLineItem      # Needs CZ:Defined:BillingLineItem and not regular LineItemType
              Equals: [DiscountedUsage, RICoveredUsage]
      - Type: Group
        Name: Savings Plan
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: Azure
            - Source: CZ:Defined:BillingLineItem
              Equals: SavingsPlanCoveredUsage
      - Type: Group
        Name: Spot
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: Azure
            - Source: Operation
              Contains: Spot
      - Type: Group
        Name: On-Demand - Instances
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: Azure
            - Source: UsageFamily    # Already updated to accomodate Bob's changes
              Equals: Virtual Machines
      #--------------------------------------
      # GCP Logic
      #--------------------------------------
      - Type: Group
        Name: Spot
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: GCP
            - Source: UsageFamily
              BeginsWith: Spot
      - Type: Group
        Name: Reservation       # These are technically "Flexible CUDs"
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: GCP
            - Source: UsageFamily
              BeginsWith: Commitment - dollar based
      - Type: Group
        Name: Reservation
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: GCP
            - Source: UsageFamily
              BeginsWith: Commitment
      - Type: Group
        Name: On-Demand - Instances
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: GCP
            - Source: CZ:Defined:ResourceType
              Contains: ": instances"
      #--------------------------------------
      # Datadog Logic
      # Can't support datadog until we can do it without referencing resource
      #--------------------------------------
      - Type: Group
        Name: Committed
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: Datadog
            - Source: CZ:Defined:ResourceDisplay
              Contains: -committed

  ResourceType:
    Name: Resource Type
    Hide: False
    Rules:
      #--------------------------------------
      # Non-Usage lineitem types
      # Decided to remove this logic on 11/7/2024
      #--------------------------------------
      #- Type: Group
      #  Name: Non-Usage Cost
      #  Conditions:
      #    - Not:
      #      - Source: LineItemType
      #        Equals: [Usage, DiscountedUsage, SavingsPlanCoveredUsage]
      #--------------------------------------
      # Default Logic
      #--------------------------------------
      - Type: GroupBy
        Source:
          - CZ:Defined:ServiceDisplay
          - CZ:Defined:ResourceType_Split
        Format: '{0}: {1}'

  ResourceType_Split:                   # HIDDEN
    Name: Resource Type - Split
    Hide: True
    DefaultValue: service-usage
    Rules:
      #--------------------------------------
      # Cases where there isn't a valid CZRN
      #--------------------------------------
      - Type: Group
        Name: service-usage
        Conditions:
          - Source: Resource
            Contains: ":unknown:"
      - Type: Group
        Name: service-usage
        Conditions:
          - Source: Resource
            BeginsWith: "billingitem-"
      #--------------------------------------
      # Data Transfer
      #--------------------------------------
      - Type: Group
        Name: data-transfer
        Conditions:
          - Source: UsageFamily
            Equals: Data Transfer
      - Type: Group
        Name: vpc-peering
        Conditions:
          - Source: UsageFamily
            Equals: VPC Peering
      #--------------------------------------
      # Default Logic
      #--------------------------------------
      - Type: GroupBy
        Source: Resource
        Transforms:
          - Type: Split
            Delimiter: ':'
            Index: 6

  ServiceDetail:
    Name: Service Detail
    Hide: False
    Rules:
      - Type: Group
        Name: Service Detail Unavailable
        Conditions:
          - Not:
            - Source: CloudProvider
              Contains: [AWS, Azure, GCP]
      #-------------------------------------
      # Non-Usage Elements
      #-------------------------------------
      - Type: GroupBy
        Source: LineItemType
        Format: 'Non-Usage: {0}'
        Conditions:
          - Not:
            - Source: LineItemType
              Equals: [Usage, DiscountedUsage, SavingsPlanCoveredUsage]
      #-------------------------------------
      # Service Detail Breakdown
      #-------------------------------------
      #----AWS-----
      - Type: GroupBy
        Source:
          - UsageFamily
          - CZ:Defined:ServiceDetail_Breakdown_AWS
        Format: '{0}: {1}'
        Conditions:
          - Not:
            - Source: CZ:Defined:ServiceDetail_Breakdown_AWS
              BeginsWith: Admin
      #----Azure-----
      - Type: GroupBy
        Source:
          - UsageFamily
          - CZ:Defined:ServiceDetail_Breakdown_Azure
        Format: '{0}: {1}'
        Conditions:
          - Not:
            - Source: CZ:Defined:ServiceDetail_Breakdown_Azure
              BeginsWith: Admin
      #----GCP-----
      - Type: GroupBy
        Source: UsageFamily
        Conditions:
          - Source: CloudProvider
            BeginsWith: GCP

  ServiceDetail_Breakdown_AWS:          # HIDDEN
    Name: Service Detail - Breakdown - AWS
    Hide: True
    Rules:
      #-------------------------------------
      # ADMIN - EXCLUDE
      #-------------------------------------
      - Type: Group
        Name: Admin - Non-AWS
        Conditions:
          - Not:
            - Source: CloudProvider
              BeginsWith: AWS
      #-------------------------------------
      # Data Transfer
      #-------------------------------------
      - Type: GroupBy
        Source: CZ:Defined:ServiceDetail_DT_InterRegion_AWS
        Format: 'InterRegion: {0}'
        Conditions:
          - Source: CZ:Defined:NetworkingSubCategory
            Equals: InterRegion Outbound
      - Type: GroupBy
        Source: Region
        Format: 'IntraRegion: {0}'
        Conditions:
          - Source: CZ:Defined:NetworkingSubCategory
            Equals: IntraRegion - AZ to AZ
      - Type: GroupBy
        Source: Region
        Format: 'Outbound: {0}'
        Conditions:
          - Source: CZ:Defined:NetworkingSubCategory
            Equals: AWS Outbound
      - Type: GroupBy
        Source: CZ:Defined:NetworkingSubCategory
        Format: '{0}'
        Conditions:
          - Source: UsageFamily
            Equals: Data Transfer
      #-------------------------------------
      # Extended Support
      #-------------------------------------
      - Type: Group
        Name: ExtendedSupport
        Conditions:
          - Source: UsageType
            Transforms:
              - Type: Lower
            Contains: extendedsupport
      #-------------------------------------
      # AWS CloudFront
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Edge-'
            Index: 2
        Format: 'Lambda-Edge-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonCloudFront
            - Source: UsageFamily
              Equals: Serverless
      - Type: GroupBy
        Source: Operation
        Conditions:
          - Source: Service
            Equals: AmazonCloudFront
      #-------------------------------------
      # AWS CloudWatch
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'CW:'
            Index: 2
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonCloudWatch
            - Source: UsageFamily
              Equals:
                - Metric
                - Canaries
      - Type: GroupBy
        Source: Operation
        Format: '{0}-S3-Egress-Bytes'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonCloudWatch
            - Source: UsageType
              Contains: S3-Egress-Bytes
      - Type: GroupBy
        Source: Operation
        Format: '{0}-VendedLog-Bytes'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonCloudWatch
            - Source: UsageType
              Contains: VendedLog-Bytes
      - Type: GroupBy
        Source: Operation
        Format: '{0}-DataProcessing-Bytes'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonCloudWatch
            - Source: UsageType
              Contains: DataProcessing-Bytes
      - Type: GroupBy
        Source: Operation
        Format: '{0}-DataScanned-Bytes'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonCloudWatch
            - Source: UsageType
              Contains: DataScanned-Bytes
      #-------------------------------------
      # AWS Config
      #-------------------------------------
      - Type: Group
        Name: ConfigurationItemRecorded
        Conditions:
          - And:
            - Source: Service
              Equals: AWSConfig
            - Source: UsageType
              Contains: ConfigurationItemRecorded
      #-------------------------------------
      # AWS AmazonConnect
      #-------------------------------------
      - Type: Group
        Name: end-customer-mins
        Conditions:
          - Source: Service
            Equals: AmazonConnect
      #-------------------------------------
      # AWS S3
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: "TimedStorage-"
            Index: 2
        Format: 'S3: TimedStorage-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonS3
            - Source: UsageFamily
              Equals:
                - Storage
                - Usage
      - Type: Group
        Name: StorageLens
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonS3
            - Source: UsageType
              Contains: "StorageLens"
      - Type: Group
        Name: StorageAnalytics
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonS3
            - Source: UsageType
              Contains: "StorageAnalytics"
      - Type: GroupBy
        Source: Operation
        Format: 'Request-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonS3
            - Source: UsageFamily
              Equals: API Request
            - Source: UsageType
              Contains: "Requests-"
      - Type: GroupBy
        Source: Operation
        Format: 'Retrieval-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonS3
            - Source: UsageFamily
              Equals: API Request
            - Source: UsageType
              Contains: "Retrieval-"
      #-------------------------------------
      # AWS RDS Storage & System Operation
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: '-'
            Index: 2
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonRDS
            - Source: UsageFamily
              Equals: [Database Storage, Storage Snapshot, System Operation]
      - Type: GroupBy
        Source: UsageType
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonRDS
            - Source: UsageFamily
              Equals: [Database Storage, Storage Snapshot, System Operation]
      #-------------------------------------
      # AWS DB Instances
      #-------------------------------------
      - Type: Group
        Name: MySQL
        Conditions:
          - Source: Operation
            Equals: CreateDBInstance:0002
      - Type: Group
        Name: SQL Server Web
        Conditions:
          - Source: Operation
            Equals: CreateDBInstance:0011
      - Type: Group
        Name: SQL Server
        Conditions:
          - Source: Operation
            Equals:
              - CreateDBInstance:0010
              - CreateDBInstance:0012
              - CreateDBInstance:0015
      - Type: Group
        Name: PostgreSQL
        Conditions:
          - Source: Operation
            Equals: CreateDBInstance:0014
      - Type: Group
        Name: Aurora MYSQL
        Conditions:
          - Source: Operation
            Equals: CreateDBInstance:0016
      - Type: Group
        Name: MariaDB
        Conditions:
          - Source: Operation
            Equals: CreateDBInstance:0018
      - Type: Group
        Name: Oracle
        Conditions:
          - Source: Operation
            Equals:
              - CreateDBInstance:0005
              - CreateDBInstance:0019
              - CreateDBInstance:0020
      - Type: Group
        Name: Aurora PostgreSQL
        Conditions:
          - Source: Operation
            Equals: CreateDBInstance:0021
      - Type: Group
        Name: Neptune
        Conditions:
          - Source: Operation
            Equals: CreateDBInstance:0023
      - Type: Group
        Name: DocDB
        Conditions:
          - Source: Operation
            Equals: CreateDBInstance:0023
      #-------------------------------------
      # AWS Cache Instances
      #-------------------------------------
      - Type: Group
        Name: Memcached
        Conditions:
          - Source: Operation
            Equals: CreateCacheCluster:0001
      - Type: Group
        Name: Redis
        Conditions:
          - Source: Operation
            Equals: CreateCacheCluster:0002
      #-------------------------------------
      # AWS Storage
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: 'piops'
            Index: 2
        Format: 'Storage-piops{0}'
        Conditions:
          - Source: UsageType
            Transforms:
              - Type: Lower
            Contains: piops
      - Type: Group
        Name: Storage-GP2
        Conditions:
          - Source: UsageType
            Transforms:
              - Type: Lower
            Contains: gp2
      - Type: Group
        Name: Storage-GP3
        Conditions:
          - Source: UsageType
            Transforms:
              - Type: Lower
            Contains: gp3
      - Type: Group
        Name: Storage-IO2
        Conditions:
          - Source: UsageType
            Transforms:
              - Type: Lower
            Contains: io2
      - Type: Group
        Name: Storage-ST1
        Conditions:
          - Source: UsageType
            Transforms:
              - Type: Lower
            Contains: st1
      - Type: Group
        Name: Storage-SC1
        Conditions:
          - Source: UsageType
            Transforms:
              - Type: Lower
            Contains: sc1
      - Type: Group
        Name: Storage-P-IOPS
        Conditions:
          - Source: UsageType
            Transforms:
              - Type: Lower
            Contains: piops
      - Type: Group
        Name: Storage-Aurora
        Conditions:
          - Source: UsageType
            Transforms:
              - Type: Lower
            Contains: "aurora:storageusage"
      - Type: Group
        Name: Storage
        Conditions:
          - Source: UsageType
            Transforms:
              - Type: Lower
            Contains: storageusage
      #-------------------------------------
      # AWS EC2 Compute - Capacity Reservations
      # Must come before EC2 Compute
      #-------------------------------------
      - Type: Group
        Name: CapacityReservation - UnusedBox
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonEC2
            - Source: UsageFamily
              Equals: Compute Instance
            - Source: UsageType
              Contains: UnusedBox
      - Type: Group
        Name: CapacityReservation - Reservation
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonEC2
            - Source: UsageFamily
              Equals: Compute Instance
            - Source: UsageType
              Contains: Reservation
      #-------------------------------------
      # AWS EC2 Compute
      #-------------------------------------
      - Type: Group
        Name: 'BoxUsage-Linux'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonEC2
            - Source: UsageType
              Contains: [BoxUsage, DedicatedUsage, SpotUsage]
            - Or:
              - Source: Operation
                Equals: RunInstances
              - Source: Operation
                BeginsWith: ["RunInstances:SV", "RunInstances:0004"]
      - Type: Group
        Name: 'BoxUsage-Windows'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonEC2
            - Source: UsageType
              Contains: [BoxUsage, DedicatedUsage, SpotUsage]
            - Source: Operation
              BeginsWith: ["RunInstances:0002", "RunInstances:0006", "RunInstances:01",
                            "RunInstances:02", "RunInstances:08"]
      - Type: Group
        Name: 'BoxUsage-SUSE'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonEC2
            - Source: UsageType
              Contains: [BoxUsage, DedicatedUsage, SpotUsage]
            - Source: Operation
              Equals: "RunInstances:000g"
      - Type: Group
        Name: 'BoxUsage-RHEL'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonEC2
            - Source: UsageType
              Contains: [BoxUsage, DedicatedUsage, SpotUsage]
            - Source: Operation
              Equals: "RunInstances:0010"
      - Type: Group
        Name: 'BoxUsage-Red Hat Enterprise Linux with HA'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonEC2
            - Source: UsageType
              Contains: [BoxUsage, DedicatedUsage, SpotUsage]
            - Source: Operation
              Equals: "RunInstances:1010"
      - Type: GroupBy
        Source: Operation
        Format: 'BoxUsage-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonEC2
            - Source: UsageType
              Contains: [BoxUsage, DedicatedUsage, SpotUsage]
      - Type: GroupBy
        Source: Operation
        Format: 'EBSOptimized-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonEC2
            - Source: UsageType
              Contains: EBSOptimized
      - Type: GroupBy
        Source: Operation
        Format: 'HostBoxUsage-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonEC2
            - Source: UsageType
              Contains: HostBoxUsage
      #-------------------------------------
      # AWS EC2 NATGateway
      #-------------------------------------
      - Type: GroupBy
        Source: CZ:Defined:NetworkingSubCategory
        Conditions:
          - Source: UsageFamily
            Equals: NAT Gateway
      #-------------------------------------
      # AWS ECS Compute
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Fargate-'
            Index: 2
        Format: 'Fargate-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonECS
            - Source: UsageType
              Contains: Fargate-
      #-------------------------------------
      # AWS EKS Compute
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'AmazonEKS-'
            Index: 2
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonEKS
            - Source: UsageType
              Contains: AmazonEKS-
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Fargate-'
            Index: 2
        Format: 'Fargate-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonEKS
            - Source: UsageType
              Contains: Fargate-
      #-------------------------------------
      # AWS EMR
      #-------------------------------------
      - Type: Group
        Name: EMR-Serverless - StorageGBHours
        Conditions:
          - And:
            - Source: Service
              Equals: ElasticMapReduce
            - Source: UsageType
              Contains: EMR-SERVERLESS-StorageGBHours
      - Type: Group
        Name: EMR-Serverless - vCPUHours
        Conditions:
          - And:
            - Source: Service
              Equals: ElasticMapReduce
            - Source: UsageType
              Contains: EMR-SERVERLESS-vCPUHours
      - Type: Group
        Name: EMR-Serverless - MemoryGBHours
        Conditions:
          - And:
            - Source: Service
              Equals: ElasticMapReduce
            - Source: UsageType
              Contains: EMR-SERVERLESS-MemoryGBHours
      #-------------------------------------
      # AWS Grafana
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Grafana:'
            Index: 2
        Conditions:
          - Source: Service
            Equals: AmazonGrafana
      #-------------------------------------
      # AWS GuardDuty
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Paid'
            Index: 2
        Format: 'Paid{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonGuardDuty
            - Source: UsageType
              Contains: Paid
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Free'
            Index: 2
        Format: 'Free{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonGuardDuty
            - Source: UsageType
              Contains: Free
      #-------------------------------------
      # AWS Kinesis Analytics
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'KPU-'
            Index: 2
        Format: 'KPU-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonKinesisAnalytics
            - Source: UsageType
              Contains: KPU-
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Running'
            Index: 2
        Format: 'Running{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonKinesisAnalytics
            - Source: UsageType
              Contains: Running
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Durable'
            Index: 2
        Format: 'Durable{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonKinesisAnalytics
            - Source: UsageType
              Contains: Durable
      #-------------------------------------
      # AWS MemoryDB
      #-------------------------------------
      - Type: Group
        Name: NodeUsage
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonMemoryDB
            - Source: UsageType
              Contains: NodeUsage
      #-------------------------------------
      # AWS MQ
      #-------------------------------------
      - Type: Group
        Name: Single-AZ
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonMemoryDB
            - Source: UsageFamily
              Equals:
                - Broker Instances
                - EdpDiscount
            - Source: UsageType
              Contains: Single-AZ
      - Type: Group
        Name: Multi-AZ
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonMemoryDB
            - Source: UsageFamily
              Equals:
                - Broker Instances
                - EdpDiscount
            - Source: UsageType
              Contains: Multi-AZ
      - Type: Group
        Name: RabbitMQ-3
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonMemoryDB
            - Source: UsageFamily
              Equals:
                - Broker Instances
                - EdpDiscount
            - Source: UsageType
              Contains: RabbitMQ-3
      - Type: Group
        Name: RabbitMQ-Single
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonMemoryDB
            - Source: UsageFamily
              Equals:
                - Broker Instances
                - EdpDiscount
            - Source: UsageType
              Contains: RabbitMQ-Single
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'TimedStorage-'
            Index: 2
        Format: 'TimedStorage-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonMQ
            - Source: UsageFamily
              Equals:
                - Broker Storage
                - Storage
      #-------------------------------------
      # AWS MWAA
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Airflow-'
            Index: 2
        Format: 'Airflow-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonMWAA
            - Source: UsageType
              Contains: Airflow-
      #-------------------------------------
      # AWS Pinpoint
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Phone'
            Index: 2
        Format: 'Phone-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonPinpoint
            - Source: UsageType
              Contains: Phone
      - Type: Group
        Name: SMS-Standard-Tollfree-MessageFees
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonPinpoint
            - Source: UsageType
              Contains: SMS
            - Source: UsageType
              Contains: Standard-Tollfree-MessageFees
      - Type: Group
        Name: SMS-Standard-Tollfree-CarrierFees
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonPinpoint
            - Source: UsageType
              Contains: SMS
            - Source: UsageType
              Contains: Standard-Tollfree-CarrierFees
      - Type: Group
        Name: SMS-Standard-Sharedroute-MessageFees
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonPinpoint
            - Source: UsageType
              Contains: SMS
            - Source: UsageType
              Contains: Standard-Sharedroute-MessageFees
      - Type: Group
        Name: SMS-Standard-Sharedroute-CarrierFees
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonPinpoint
            - Source: UsageType
              Contains: SMS
            - Source: UsageType
              Contains: Standard-Sharedroute-CarrierFees
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Deliverability-'
            Index: 2
        Format: 'Deliverability-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonPinpoint
            - Source: UsageType
              Contains: Deliverability-
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Domain-'
            Index: 2
        Format: 'Domain-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonPinpoint
            - Source: UsageType
              Contains: Domain-
      #-------------------------------------
      # AWS SageMaker
      #-------------------------------------
      - Type: Metadata
        Source: UsageType
        Conditions:
          - Source: Service
            Equals: AmazonSageMaker
        Values:
          - Host
          - Notebk
          - Processing
          - Studio-DW
          - Studio-KernelGateway
          - Train
          - Trspt
          - Tsform
      #-------------------------------------
      # AWS SES
      #-------------------------------------
      - Type: Group
        Name: Message
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonSES
            - Source: UsageFamily
              Equals: Receiving Email
            - Source: UsageType
              Contains: Message
      - Type: Group
        Name: ReceivedChunk
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonSES
            - Source: UsageFamily
              Equals: Receiving Email
            - Source: UsageType
              Contains: ReceivedChunk
      #-------------------------------------
      # AWS SNS
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'DeliveryAttempts-'
            Index: 2
        Format: 'DeliveryAttempts-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonSNS
            - Source: UsageType
              Contains: DeliveryAttempts-
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'SMS-'
            Index: 2
        Format: 'SMS-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonSNS
            - Source: UsageType
              Contains: SMS-
      #-------------------------------------
      # AWS SWF
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Initiated'
            Index: 2
        Format: 'Initiated{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonSWF
            - Source: UsageType
              Contains: Initiated
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Closed'
            Index: 2
        Format: 'Closed{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonSWF
            - Source: UsageType
              Contains: Closed
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Open'
            Index: 2
        Format: 'Open{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonSWF
            - Source: UsageType
              Contains: Open
      #-------------------------------------
      # AWS VPC
      #-------------------------------------
      - Type: Group
        Name: TransitGateway-Bytes
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonVPC
            - Source: UsageType
              Contains: TransitGateway-Bytes
      - Type: Group
        Name: TransitGateway-Hours
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonVPC
            - Source: UsageType
              Contains: TransitGateway-Hours
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: '-'
            Index: 2
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonVPC
            - Source: UsageFamily
              Equals: Usage
      #-------------------------------------
      # AWS WorkDocs
      #-------------------------------------
      - Type: Metadata
        Source: UsageType
        Conditions:
          - Source: Service
            Equals: AmazonWorkDocs
        Values:
          - ListAPICalls
          - ReadAPICalls
          - WriteAPICalls
          - InclStorageByteHrs
          - WSOnly-UserHrs
          - WSUpgraded-UserHrs
          - UserHrs
      #-------------------------------------
      # AWS Workspaces
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'HW-'
            Index: 2
        Format: 'HW-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonWorkSpaces
            - Source: UsageType
              Contains: HW-
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'HWL-'
            Index: 2
        Format: 'HWL-{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonWorkSpaces
            - Source: UsageType
              Contains: HWL-
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'SW'
            Index: 2
        Format: 'SW{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AmazonWorkSpaces
            - Source: UsageType
              Contains: SW
      #-------------------------------------
      # AWS CloudFormation
      #-------------------------------------
      - Type: Metadata
        Source: UsageType
        Conditions:
          - Source: Service
            Equals: AWSCloudTrail
        Values:
          - DataEventsRecorded
          - FreeEventsRecorded
          - FreeTrialIngestion-Bytes
          - FreeTrialQueryScanned-Bytes
          - Ingestion-Bytes
          - InsightsEvents
          - PaidEventsRecorded
          - QueryScanned-Bytes
      #-------------------------------------
      # AWS DirectConnect
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'HCPortUsage'
            Index: 2
        Format: 'HCPortUsage{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AWSDirectConnect
            - Source: UsageType
              Contains: HCPortUsage
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'PortUsage'
            Index: 2
        Format: 'PortUsage{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AWSDirectConnect
            - Source: UsageType
              Contains: PortUsage
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Site'
            Index: 2
        Format: 'Site{0}'
        Conditions:
          - And:
            - Source: Service
              Equals: AWSDirectConnect
            - Source: UsageType
              Contains: Site
      #-------------------------------------
      # AWS SecurityHub
      #-------------------------------------
      - Type: Metadata
        Source: UsageType
        Conditions:
          - Source: Service
            Equals: AWSSecurityHub
        Values:
          - ComplianceCheck
          - PaidFindingsIngestion
      #-------------------------------------
      # AWS UsageType - Delimiter '-' - 2nd Half
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: '-'
            Index: 2
        Conditions:
          - Source: Service
            Equals:
              - AmazonApiGateway
              - AmazonAppStream
              - AmazonAthena
              - AmazonDevOpsGuru
              - AmazonForecast
              - AmazonFSx
              - AmazonMacie
              - AmazonMemoryDB
              - AmazonPinpoint
              - AmazonTextract
              - AmazonTimestream
              - AWSBackup
              - AWSConfig
          - Source: UsageFamily
            Equals:
              - Amazon DynamoDB PayPerRequest Throughput
              - Provisioned IOPS
              - Storage Snapshot
      #-------------------------------------
      # Fallback - Usage Operation
      #-------------------------------------
      - Type: GroupBy
        Source: Operation

  ServiceDetail_DT_InterRegion_AWS:     # HIDDEN
    Name: Service Detail - InterRegion Data Transfer
    Hide: True
    Rules:
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: '-AWS-Out-Bytes'
            Index: 1
        Conditions:
          - And:
            - Source: UsageType
              Contains: -AWS-Out-Bytes
            - Source: UsageFamily
              Equals: Data Transfer

  ServiceDetail_Breakdown_Azure:        # HIDDEN
    Name: Service Detail - Breakdown -  Azure
    Hide: True
    Rules:
      #-------------------------------------
      # ADMIN - EXCLUDE
      #-------------------------------------
      - Type: Group
        Name: Admin - Non-Azure
        Conditions:
          - Not:
            - Source: CloudProvider
              BeginsWith: Azure
      #-------------------------------------
      # Azure Microsoft.Cache
      #-------------------------------------
      - Type: GroupBy
        Source: UsageType   # Already changed to accomodate Bob's remapping
        Conditions:
          - Source: Service
            Equals: "microsoft.cache"
      #-------------------------------------
      # Fallback - Usage Operation
      #-------------------------------------
      - Type: GroupBy
        Source: Operation

  TaggableVsUntaggable:                 # Needs Improvement - How to identify taggable in Azure
    Name: Taggable vs. Untaggable
    Hide: False
    Child: Service
    Source: CZ:Defined:ResourceType
    DefaultValue: Taggable
    Rules:
      - Type: Group
        Name: Tagging Categorization Unavailable
        Conditions:
          - Not:
            - Source: CloudProvider
              Contains: [AWS, GCP]
      #---------------------------------------
      # Non-Usage Based Costs
      #---------------------------------------
      - Type: Group
        Name: Untaggable - Non-Usage
        Conditions:
          - Not:
            - Source: LineItemType
              Equals: [Usage, DiscountedUsage, SavingsPlanCoveredUsage]
      #---------------------------------------
      # AWS Logic For What is Untaggable
      #---------------------------------------
      - Type: Group
        Name: Untaggable - Entire Service
        Conditions:
          - Source: Service
            Equals:
              - AmazonChime
            #  - AmazonCloudSearch --- Can tag as of 11/17/22
              - AmazonDetective
              - AmazonInspector
              - AmazonPinpoint
              - AmazonQLDB
              - AmazonSES
              - AmazonSimpleDB
              - AmazonWorkDocs
              - AmazonWorkMail
              - AppFlow
              - AWSAmplify
              - AWSBudgets
              - AWSCloudShell
              - AWSCostExplorer
              - AWSElementalMediaStore
              - AWSEvents
              - AmazonGuardDuty
              - AWSSecurityHub
              - AWSServiceCatalog
              - AWSSystemsManager
              - AWSSupportEnterprise
              - ContactCenterTelecomm
              - OpsWorks
              - translate
              - AmazonPinpoint
      - Type: Group
        Name: Untaggable - Service Charges
        Conditions:
          - And:
            - Source: CZ:Defined:ResourceType
              Contains: service-usage
            - Source: LineItemType
              Contains: Usage
          - Equals:
            - "ApiGateway: account"
            - "AppSync: DataSource"
            - "AppSync: GraphQLApi"
            - "CloudWatch: dashboard"
            - "CodeDeploy: application"
            - "CodeDeploy: deploymentconfig"
            - "CodePipeline: customactiontype"
            - "DataExchange: revision"
            - "DirectConnect: transit-gateway"
            - "DMS: certificate"
            - "DMS: endpoint"
            - "DMS: eventsubscription"
            - "DMS: replicationinstance"
            - "DMS: replicationsubnetgroup"
            - "DMS: replicationtask"
            - "ElasticBeanstalk: applicationversion"
            - "ElasticBeanstalk: configurationtemplate"
            - "ElasticBeanstalk: environment"
            - "DynamoDB: backup"
            - "EC2: capacityreservation"
            - "EC2: host"
            - "EC2: launchtemplate"
            - "EC2: transitgateway"
            - "EC2: transitgatewayroutetable"
            - "EC2: vpcpeeringconnection"
            - "ECR: jobrun"
            - "ECS: containerinstance"
            - "ECS: service"
            - "FraudDetector: detectorversion"
            - "FraudDetector: modelversion"
            - "FraudDetector: rule"
            - "Glue: database"
            - "IAM: role"
            - "IAM: virtualmfadevice"
            - "IAM: assessmenttemplate"
            - "IoT: topicrule"
            - "IoTAnalytics: channel"
            - "IoTAnalytics: datastore"
            - "IoTAnalytics: pipeline"
            - "Kinesis: stream-consumer"
            - "KinesisAnalyticsV2: application"
            - "KinesisFirehose: deliverystream"
            - "KMS: alias"
            - "Lambda: alias"
            - "Lambda: eventsourcemapping"
            - "Lambda: layerversion"
            - "Lambda: version"
            - "Neptune: cluster-backup"
            - "Neptune: cluster-snapshot"
            - "Organizations: organizationalunit"
            - "Organizations: policy"
            - "QLDB: stream"
            - "RDS: cluster-backup"
            - "Redshift: clustersecuritygroup"
            - "Route53: bound-network-interface"
            - "S3: storage-lens"
            - "SageMaker: endpointconfig"
            - "SageMaker: hyperparametertuningjob"
            - "SageMaker: labelingjob"
            - "SageMaker: model"
            - "SageMaker: pipeline"
            - "SageMaker: trainingjob"
            - "SageMaker: transformjob"
            - "SageMaker: workteam"
            - "SageMaker: trainingjob"
            - "ServiceCatalog: cloudformationproduct"
            - "ServiceCatalog: portfolio"
            - "ServiceQuotas: quota"
            - "Shield: root"
            - "SSM: document"
            - "SSM: maintenancewindow"
            - "SSM: managedinstance"
            - "SSM: patchbaseline"
            - "StorageGateway: volume"
            - "VPC: network-insights-analysis"
      #---------------------------------------
      # GCP Logic For What is Untaggable
      #---------------------------------------
      - Type: Group
        Name: Untaggable - Entire Service
        Conditions:
          - Source: Service
            Equals:
              - BigQuery Reservation API
              - BigQuery Storage API
              - Geocoding API
              - Cloud Logging
              - Cloud DNS
              - Custom Search
              - Support
              - Transcoder API
              - Translate
      - Type: Group
        Name: Untaggable - Service Charges
        Conditions:
          - And:
            - Source: Service
              Equals: Compute Engine
            - Source: UsageFamily
              BeginsWith: "Network Load Balancing: Forwarding Rule"
          - And:
            - Source: Service
              Equals: BigQuery
            - Source: UsageFamily
              Equals: Analysis
          - And:
            - Source: Service
              Equals: Networking
            - Source: UsageFamily
              BeginsWith: [Networking Cloud CDN Traffic Cache Egress, Networking Cloud Nat]

  ResourceSummaryID:
    Name: Resource Summary
    Source: Resource
    Rules:
      #-------------------------
      # Billing Line Item Logic
      #-------------------------
      - Type: GroupBy
        Source: [CZ:Defined:BillingLineItem, Description]
        Format: '{0} - {1}'
        Conditions:
          - Source: CZ:Defined:BillingLineItem
            Equals: [Credit, Refund, Fee]
      - Type: GroupBy
        Source: CZ:Defined:CommittedUseSubscription_Display
        Format: 'Subscription - {0}'
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: AWS
            - Source: CZ:Defined:BillingLineItem
              Equals: [SavingsPlanRecurringFee, SavingsPlanUpfrontFee, RIFee, RIUpfrontFee]
      - Type: GroupBy
        Source: CZ:Defined:BillingLineItem
        Conditions:
          - Not:
            - Source: CZ:Defined:BillingLineItem
              Contains: Usage
      #-------------------------
      # AWS - EC2 Logic
      #-------------------------
      - Type: GroupBy
        Source: Tag:aws:elasticmapreduce:job-flow-id
        Conditions:
          - Source: Service
            Equals: AmazonEC2
      - Type: GroupBy
        Source: Tag:Name
        Conditions:
          - Source: Service
            Equals: AmazonEC2
      - Type: GroupBy
        Source: Tag:aws:eks:cluster-name
        Conditions:
          - Source: Service
            Equals: AmazonEC2
      - Type: GroupBy
        Source: Resource
        Format: 'ec2-{0}s'
        Transforms:
          - Type: Split
            Delimiter: ':'
            Index: 6
        Conditions:
          - Source: CZ:Defined:ResourceType
            Equals: ["EC2: data-transfer", "EC2: dedicated-host", "EC2: instance", "EC2: volume", "EC2: snapshot"]
      #-------------------------
      # Other Services To Group By Name
      #-------------------------            
      - Type: GroupBy
        Source: Tag:Name
        Conditions:
          - Source: Service
            Equals: [AmazonCloudFront, AmazonVPC, AWSCertificateManager, AWSDirectConnect]
      #-------------------------
      # AWS - fallback instance aggregation
      #-------------------------   
      - Type: Group
        Name: cloudwatch-instances
        Conditions:
          - Source: CZ:Defined:ResourceType
            Equals: "CloudWatch: instance"
      - Type: Group
        Name: inspector-v2-instances
        Conditions:
          - Source: CZ:Defined:ResourceType
            Equals: "InspectorV2: instance"       
      - Type: Group
        Name: directconnect-instances
        Conditions:
          - And:
            - Source: Service
              Equals: AWSDirectConnect
            - Source: Resource
              Contains: ":instance:"  
      #-------------------------
      # AWS - Edge Cases For Aggregation
      #-------------------------
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay
        Transforms:
          - Type: Split
            Delimiter: '|'
            Index: 1
        Conditions:
          - Source: Service
            Equals: AmazonECS
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay
        Transforms:
          - Type: Split
            Delimiter: '|'
            Index: 1
        Conditions:
          - Source: CZ:Defined:ResourceType
            Equals: "DynamoDB: backup"
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay
        Transforms:
          - Type: Split
            Delimiter: '/contact'
            Index: 1
        Format: '{0}/contact'
        Conditions:
          - And:
            - Source: Resource
              Contains: ':connect:'
            - Source: CZ:Defined:ResourceDisplay
              Contains: /contact
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay
        Transforms:
          - Type: Split
            Delimiter: '/agent'
            Index: 1
        Format: '{0}/agent'
        Conditions:
          - And:
            - Source: Resource
              Contains: ':connect:'
            - Source: CZ:Defined:ResourceDisplay
              Contains: /agent
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay
        Transforms:
          - Type: Split
            Delimiter: '/'
            Index: 1
        Conditions:
          - Source: Resource
            Contains: ':connect:'           
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay
        Transforms:
          - Type: Split
            Delimiter: '.'
            Index: 1
        Conditions:
          - Source: Service
            Equals: transcribe
      - Type: Group
        Name: cloudformation-stacks
        Conditions:
          - Source: Service
            Equals: AWSCloudFormation
      - Type: Group
        Name: system-manager-interfaces
        Conditions:
          - Source: Service
            Equals: AWSSystemsManager
      - Type: Group
        Name: kms-keys
        Conditions:
          - Source: Service
            Equals: awskms
      - Type: Group
        Name: backup-recovery-points
        Conditions:
          - Source: CZ:Defined:ResourceType
            Equals: 'Backup: recovery-point'
      - Type: Group
        Name: sagemaker-training-jobs
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: AWS
            - Contains: ':training-job:'            
      - Type: Group
        Name: sagemaker-transform-jobs
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: AWS
            - Contains: ':transform-job:'
      - Type: Group
        Name: transcription-jobs
        Conditions:
          - Source: CZ:Defined:ResourceType
            Equals: 'transcribe: transcription-job'
      - Type: Group
        Name: vpc-endpoints
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: AWS
            - Contains: ':vpc-endpoint:'
      - Type: Group
        Name: vpc-network-interfaces
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: AWS
            - Contains: ':network-interface:'
      - Type: Group
        Name: webacls
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: AWS
            - Contains: 'webacl/FMManagedWebACL'
      - Type: Group
        Name: elb-classic-load-balancers
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: AWS
            - Contains: ':classic-load-balancer:'
      - Type: Group
        Name: cloudwatch-sagemaker-endpoints
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: AWS
            - Contains: ':log-group:/aws/sagemaker/Endpoints/'
      #-------------------------
      # AWS - Service Usage
      #-------------------------
      - Type: GroupBy
        Source: CZ:Defined:ServiceDisplay
        Format: '{0}: service-usage'
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: AWS
            - Source: CZ:Defined:ResourceType
              Contains: service-usage
      #-------------------------
      # Azure
      #-------------------------
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay
        Transforms:
          - Type: Split
            Delimiter: '|virtualmachine'
            Index: 1
        Conditions:
          - And:
            - Source: CZ:Defined:ResourceType
              Equals: "microsoft.compute: virtualmachinescalesets"
            - Source: CZ:Defined:ResourceDisplay
              Contains: "|virtualmachine"
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay
        Transforms:
          - Type: Split
            Delimiter: '|database'
            Index: 1
        Conditions:
          - And:
            - Source: CZ:Defined:ResourceType
              Equals: "microsoft.sql: servers"
            - Source: CZ:Defined:ResourceDisplay
              Contains: "|database"
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay
        Transforms:
          - Type: Split
            Delimiter: '|pipelines'
            Index: 1
        Conditions:
          - And:
            - Source: CZ:Defined:ResourceType
              Equals: "microsoft.datafactory: factories"
            - Source: CZ:Defined:ResourceDisplay
              Contains: "|pipelines"
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay
        Transforms:
          - Type: Split
            Delimiter: '|sqlpool'
            Index: 1
        Conditions:
          - And:
            - Source: CZ:Defined:ResourceType
              Equals: "microsoft.synapse: workspaces"
            - Source: CZ:Defined:ResourceDisplay
              Contains: "|sqlpool"
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay
        Transforms:
          - Type: Split
            Delimiter: '|blobservices'
            Index: 1
        Conditions:
          - And:
            - Source: CZ:Defined:ResourceType
              Equals: "microsoft.storage: storageaccounts"
            - Source: CZ:Defined:ResourceDisplay
              Contains: "|blobservices"
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay
        Transforms:
          - Type: Split
            Delimiter: '|fileservices'
            Index: 1
        Conditions:
          - And:
            - Source: CZ:Defined:ResourceType
              Equals: "microsoft.storage: storageaccounts"
            - Source: CZ:Defined:ResourceDisplay
              Contains: "|fileservices"
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay
        Transforms:
          - Type: Split
            Delimiter: '|'
            Index: 1
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: Azure
            - Source: CZ:Defined:ResourceDisplay
              Contains: "|"
      #-------------------------
      # GCP
      #-------------------------
      - Type: Group
        Name: 'bigquery-jobs'
        Conditions:
          - Source: CZ:Defined:ResourceType
            Equals: "BigQuery: job"
      - Type: Group
        Name: 'bigquery-dataset-scripts'
        Conditions:
          - And:
            - Source: CZ:Defined:ResourceType
              Equals: "BigQuery: datasets"
            - Source: CZ:Defined:ResourceDisplay
              BeginsWith: "_script"
      - Type: Group
        Name: 'bigquery-reservation-api-jobs'
        Conditions:
          - Source: CZ:Defined:ResourceType
            Equals: "BigQuery Reservation API: job"
      #-------------------------
      # GCP - Instances with NULL account
      #-------------------------
      - Type: GroupBy
        Source: UsageFamily
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: GCP
            - Source: Account
              HasValue: False     
      #-------------------------
      # GCP - Compute Engine (mainly useful for instances and disk)
      #-------------------------      
      - Type: GroupBy
        Source:
          - Tag:gcp_cz:resource_name
          - Tag:goog-k8s-cluster-name
          - Tag:name
        CoalesceSources: True
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: GCP
            - Source: Service
              Equals: Compute Engine
      #-------------------------
      # Databricks
      #-------------------------
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay
        Transforms:
          - Type: Split
            Delimiter: '|'
            Index: 1
        Conditions:
          - And:
            - Source: CloudProvider
              BeginsWith: Databricks
            - Source: CZ:Defined:ResourceType
              Contains: ": job"
            - Source: CZ:Defined:ResourceDisplay
              Contains: "|"
      #-------------------------
      # BillingItem - "Bad" CZRNs
      #-------------------------
      - Type: Group
        Name: kafka_network_read
        Conditions:
          - And:
            - Source: CZ:Defined:ResourceDisplay
              BeginsWith: billingitem-Usage
            - Source: CZ:Defined:ResourceDisplay
              Contains: KAFKA_NETWORK_READ
      - Type: Group
        Name: kafka_network_write
        Conditions:
          - And:
            - Source: CZ:Defined:ResourceDisplay
              BeginsWith: billingitem-Usage
            - Source: CZ:Defined:ResourceDisplay
              Contains: KAFKA_NETWORK_WRITE
      - Type: Group
        Name: kafka_num_ckus
        Conditions:
          - And:
            - Source: CZ:Defined:ResourceDisplay
              BeginsWith: billingitem-Usage
            - Source: CZ:Defined:ResourceDisplay
              Contains: KAFKA_NUM_CKUS
      - Type: Group
        Name: kafka_storage
        Conditions:
          - And:
            - Source: CZ:Defined:ResourceDisplay
              BeginsWith: billingitem-Usage
            - Source: CZ:Defined:ResourceDisplay
              Contains: KAFKA_STORAGE
      - Type: Group
        Name: kafka
        Conditions:
          - And:
            - Source: CZ:Defined:ResourceDisplay
              BeginsWith: billingitem-Usage
            - Source: CZ:Defined:ResourceDisplay
              Contains: -Kafka-
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay
        Transforms:
          - Type: Split
            Delimiter: 'arn:'
            Index: 2
            Maxsplit: 2
          - Type: Split
            Delimiter: ':'
            Index: 5
        Conditions:
          - Source: CZ:Defined:ResourceDisplay
            Contains: "arn:"
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay
        Transforms:
          - Type: Split
            Delimiter: '-'
            Index: 5
            Maxsplit: 5
        Conditions:
          - Source: CZ:Defined:ResourceDisplay
            BeginsWith: billingitem-Usage
      #-------------------------
      # Default Logic - Show CZRN
      #-------------------------
      - Type: GroupBy
        Source: Resource

# GenAI Dimensions
  GenAI_Platform:
    Name: GenAI Platform
    Child: CZ:Defined:GenAI_Model_Family
    Source: CloudProvider
    Transforms:
      - Type: Lower
    DefaultValue: Not Applicable
    Rules:
      #----------------------------------
      # AWS Logic
      #----------------------------------
      - Type: Group
        Name: Bedrock
        Conditions:
          - Source: Service
            Equals: AmazonBedrock
      - Type: Group
        Name: Anthropic
        Conditions:
          - And:
            - Equals: aws marketplace
            - Source: Service
              Contains: Bedrock
            - Source: Service
              Contains: Claude
      - Type: Group
        Name: Meta
        Conditions:
          - And:
            - Equals: aws marketplace
            - Source: Service
              Contains: Bedrock
            - Source: Service
              Contains: Llama
      - Type: Group
        Name: Cohere
        Conditions:
          - And:
            - Equals: aws marketplace
            - Source: Service
              Contains: Bedrock
            - Source: Service
              Contains: Cohere
      - Type: Group
        Name: DeepSeek
        Conditions:
          - And:
            - Equals: aws marketplace
            - Source: Service
              Contains: Bedrock
            - Source: Service
              Contains: DeepSeek
      - Type: Group
        Name: Luma
        Conditions:
          - And:
            - Equals: aws marketplace
            - Source: Service
              Contains: Bedrock
            - Source: Service
              Contains: Luma
      - Type: Group
        Name: Minstral
        Conditions:
          - And:
            - Equals: aws marketplace
            - Source: Service
              Contains: Bedrock
            - Source: Service
              Contains: Minstral
      #----------------------------------
      # GCP Logic
      #----------------------------------
      - Type: Group
        Name: Vertex AI
        Conditions:
          - And:
            - Contains: gcp
            - Source: Service
              Equals: Vertex AI
            - Source: PricingUnit
              Equals: count
      - Type: Group
        Name: Anthropic
        Conditions:
          - And:
            - Contains: gcp
            - Source: Service
              Contains: Claude
            - Source: PricingUnit
              Equals: count
      - Type: Group
        Name: Meta
        Conditions:
          - And:
            - Contains: gcp
            - Source: Service
              Contains: Llama
            - Source: PricingUnit
              Equals: count
      - Type: Group
        Name: Mistral
        Conditions:
          - And:
            - Contains: gcp
            - Source: Service
              Contains: Mistral
            - Source: PricingUnit
              Equals: count
      - Type: Group
        Name: OpenAI
        Conditions:
          - And:
            - Contains: azure
            - Source: Service
              Equals: microsoft.cognitiveservices
            - Source: UsageType
              Equals: Azure OpenAI
      #----------------------------------
      # Other Logic
      #----------------------------------
      - Type: Group
        Name: OpenAI        # Need this because there are multiple versions of the OpenAI adapter
        Conditions:
          - Equals: [openai, open-ai]
      - Type: GroupBy
        Source: CloudProvider
        Conditions:
          - Source: CloudProvider
            Transforms:
              - Type: Lower
            Equals: [anthropic, baidu, chatgpt, claude, cohere, deepmind, deepsearch, fireworks, gemini, llama, meta, minstral]

  GenAI_TokenType:
    Name: GenAI Token Type
    Source: [UsageFamily, UsageType, CZ:Defined:ServiceDetail, CZ:Defined:ResourceSummaryDisplay]
    Transforms:
      - Type: Lower
    DefaultValue: Other
    Rules:
      - Type: Group
        Name: Not Applicable
        Conditions:
          - Source: CZ:Defined:GenAI_Platform
            Equals: Not Applicable
      - Type: Group
        Name: Cached Read Input
        Conditions:
          - And: 
            - Contains: cache
            - Contains: read
            - Contains: inp
      - Type: Group
        Name: Cached Write Input
        Conditions:
          - And: 
            - Contains: cache
            - Contains: write
            - Contains: inp
      - Type: Group
        Name: Cached Input
        Conditions:
          - And: 
            - Contains: cache
            - Contains: inp
      - Type: Group
        Name: Cached Output
        Conditions:
          - And: 
            - Contains: cache
            - Contains: outp
      - Type: Group
        Name: Input
        Conditions:
          - Contains: inp
      - Type: Group
        Name: Output
        Conditions:
          - Contains: outp

  GenAI_Model:
    Name: GenAI Model
    Override: CZ:Defined:GenAI_Model
    Sources: CZ:Defined:ServiceDetail
    DefaultValue: Other
    Rules:
      - Type: Group
        Name: Not Applicable
        Conditions:
          - Source: CZ:Defined:GenAI_Platform
            Equals: Not Applicable
      #--------------------------------------
      # AWS Bedrock Logic - Customer override for internal models
      #--------------------------------------
      - Type: GroupBy
        Source: CZ:Defined:GenAI_Model_Bedrock
      #--------------------------------------
      # AWS Logic - Externalized becuase it may be custom at each customer
      #--------------------------------------
      #-------Marketplace purchased models
      - Type: GroupBy
        Source: CZ:Defined:ResourceSummaryDisplay
        Conditions:
          - And:
            - Source: CloudProvider
              Equals: AWS Marketplace
            - Source: Service
              Contains: Bedrock
      #-------AWS Bedrock     
      - Type: GroupBy
        Source: UsageType
        Transforms:
          - Type: Split
            Delimiter: 'Guardrail-'
            Index: 2
        Format: 'Guardrail-{0}'
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: AWS
            - Not:
              - Source: CloudProvider
                Contains: Marketplace
            - Source: User:Defined:Test_GenAI_Platform
              Equals: Bedrock
      - Type: GroupBy
        Source: CZ:Defined:ResourceType
        Transforms:
          - Type: Split
            Delimiter: ': '
            Index: 2
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: AWS
            - Not:
              - Source: CloudProvider
                Contains: Marketplace
            - Source: CZ:Defined:GenAI_Platform
              Equals: Bedrock
            - Source: CZ:Defined:ResourceType
              Equals: ["Bedrock: model-invocation-job", "Bedrock: data-automation-invocation"]
      - Type: GroupBy
        Source: CZ:Defined:ResourceSummaryDisplay
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: AWS
            - Not:
              - Source: CloudProvider
                Contains: Marketplace
            - Source: CZ:Defined:GenAI_Platform
              Equals: Bedrock
            - Source: CZ:Defined:ResourceSummaryDisplay
              Contains: ["-v1", "-v2", "-v3", "-v4", "-v5", "-v6"]
      - Type: Group
        Name: aws-bedrock-custom-model
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: AWS
            - Not:
              - Source: CloudProvider
                Contains: Marketplace
            - Source: CZ:Defined:GenAI_Platform
              Equals: Bedrock
      #--------------------------------------
      # GCP Logic
      #--------------------------------------
      - Type: GroupBy
        Source: CZ:Defined:ServiceDisplay
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Not:
              - Source: CZ:Defined:GenAI_Platform
                Equals: Vertex AI
      - Type: Group
        Name: PaLM Text Bison
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: CZ:Defined:GenAI_Platform
              Equals: Vertex AI
            - Source: UsageFamily
              Contains: PaLM Text Bison
      - Type: GroupBy
        Source: UsageFamily
        Transforms:
          - Type: Split
            Delimiter: ' Input'
            Index: 1
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: CZ:Defined:GenAI_Platform
              Equals: Vertex AI
            - Source: UsageFamily
              Contains: Input
      - Type: GroupBy
        Source: UsageFamily
        Transforms:
          - Type: Split
            Delimiter: ' Output'
            Index: 1
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: CZ:Defined:GenAI_Platform
              Equals: Vertex AI
            - Source: UsageFamily
              Contains: Output
      - Type: GroupBy
        Source: UsageFamily
        Transforms:
          - Type: Split
            Delimiter: ' ('
            Index: 1
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: CZ:Defined:GenAI_Platform
              Equals: Vertex AI
            - Source: UsageFamily
              Contains: " ("
      - Type: GroupBy
        Source: UsageFamily
        Conditions:
          - Source: CloudProvider
            Contains: GCP
          - Source: CZ:Defined:GenAI_Platform
            Equals: Vertex AI
      #--------------------------------------
      # Azure Logic
      #--------------------------------------
      - Type: GroupBy
        Source: Operation
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: ' cache'
            Index: 1
        Conditions:
          - And: 
            - Source: CloudProvider
              Equals: Azure
            - Source: Operation
              Transforms:
                - Type: Lower
              Contains: " cache"
      - Type: GroupBy
        Source: Operation
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: '-cache'
            Index: 1
        Conditions:
          - And: 
            - Source: CloudProvider
              Equals: Azure
            - Source: Operation
              Transforms:
                - Type: Lower
              Contains: "-cache"
      - Type: GroupBy
        Source: Operation
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: ' inp'
            Index: 1
        Conditions:
          - And: 
            - Source: CloudProvider
              Equals: Azure
            - Source: Operation
              Transforms:
                - Type: Lower
              Contains: " inp"
      - Type: GroupBy
        Source: Operation
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: '-inp'
            Index: 1
        Conditions:
          - And: 
            - Source: CloudProvider
              Equals: Azure
            - Source: Operation
              Transforms:
                - Type: Lower
              Contains: "-inp"
      - Type: GroupBy
        Source: Operation
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: ' outp'
            Index: 1
        Conditions:
          - And: 
            - Source: CloudProvider
              Equals: Azure
            - Source: Operation
              Transforms:
                - Type: Lower
              Contains: " outp"
      - Type: GroupBy
        Source: Operation
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: '-outp'
            Index: 1
        Conditions:
          - And: 
            - Source: CloudProvider
              Equals: Azure
            - Source: Operation
              Transforms:
                - Type: Lower
              Contains: "-outp"
      - Type: GroupBy
        Source: Operation
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: ' regional'
            Index: 1
        Conditions:
          - And: 
            - Source: CloudProvider
              Equals: Azure
            - Source: Operation
              Transforms:
                - Type: Lower
              Contains: " regional"
      - Type: GroupBy
        Source: Operation
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: '-regional'
            Index: 1
        Conditions:
          - And: 
            - Source: CloudProvider
              Equals: Azure
            - Source: Operation
              Transforms:
                - Type: Lower
              Contains: "-regional"
      - Type: GroupBy
        Source: Operation
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: ' glbl'
            Index: 1
        Conditions:
          - And: 
            - Source: CloudProvider
              Equals: Azure
            - Source: Operation
              Transforms:
                - Type: Lower
              Contains: " glbl"
      - Type: GroupBy
        Source: Operation
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: '-glbl'
            Index: 1
        Conditions:
          - And: 
            - Source: CloudProvider
              Equals: Azure
            - Source: Operation
              Transforms:
                - Type: Lower
              Contains: "-glbl"
      - Type: GroupBy
        Source: Operation
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: ' std'
            Index: 1
        Conditions:
          - And: 
            - Source: CloudProvider
              Equals: Azure
            - Source: Operation
              Transforms:
                - Type: Lower
              Contains: " std"
      - Type: GroupBy
        Source: Operation
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: '-std'
            Index: 1
        Conditions:
          - And: 
            - Source: CloudProvider
              Equals: Azure
            - Source: Operation
              Transforms:
                - Type: Lower
              Contains: "-std"
      - Type: GroupBy
        Source: Operation
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: ' hd'
            Index: 1
        Conditions:
          - And: 
            - Source: CloudProvider
              Equals: Azure
            - Source: Operation
              Transforms:
                - Type: Lower
              Contains: " hd"
      - Type: GroupBy
        Source: Operation
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: '-hd'
            Index: 1
        Conditions:
          - And: 
            - Source: CloudProvider
              Equals: Azure
            - Source: Operation
              Transforms:
                - Type: Lower
              Contains: "-hd"
      #--------------------------------------
      # OpenAI Logic
      #--------------------------------------
      - Type: GroupBy
        Source: Tag:open_ai_cz:model      # Might not exist for older adapters
        Transforms:
          - Type: Split
            Delimiter: ' | '
            Index: 2
      - Type: GroupBy
        Source: Tag:open_ai_cz:model      # Might not exist for older adapters        
      - Type: GroupBy
        Source: CZ:Defined:ResourceSummaryDisplay
        Transforms:
          - Type: Split 
            Delimiter: '|'  
            Index: 1
        Conditions:
          - Source: CloudProvider
            Transforms:
              - Type: Lower
            Equals: openai
      #--------------------------------------
      # Anthropic Logic
      #--------------------------------------
      - Type: GroupBy
        Source: Service
        Conditions:
          - Source: CloudProvider
            Contains: Anthropic

  GenAI_Model_Family:
    Name: GenAI Model Family
    Child: CZ:Defined:GenAI_Model
    Source: UsageFamily
    DefaultValue: Other
    Rules:
      - Type: Group
        Name: Not Applicable
        Conditions:
          - Source: CZ:Defined:GenAI_Platform
            Equals: Not Applicable
      #--------------------------------------
      # Anthropic AnyCost Adapter Logic
      #--------------------------------------
      - Type: GroupBy
        Source: CZ:Defined:GenAI_Model
        Transforms:
          - Type: Split
            Delimiter: ' 2024'
            Index: 1
        Conditions:
          - And:
            - Source: CloudProvider
              Equals: Anthropic
            - Source: CZ:Defined:GenAI_Model
              Contains: 2024-
      - Type: GroupBy
        Source: CZ:Defined:GenAI_Model
        Transforms:
          - Type: Split
            Delimiter: ' 2025'
            Index: 1
        Conditions:
          - And:
            - Source: CloudProvider
              Equals: Anthropic
            - Source: CZ:Defined:GenAI_Model
              Contains: 2025-
      - Type: GroupBy
        Source: CZ:Defined:GenAI_Model
        Transforms:
          - Type: Split
            Delimiter: ' 2026'
            Index: 1
        Conditions:
          - And:
            - Source: CloudProvider
              Equals: Anthropic
            - Source: CZ:Defined:GenAI_Model
              Contains: 2026-
      - Type: GroupBy
        Source: CZ:Defined:GenAI_Model
        Conditions:
          - Source: CloudProvider
            Equals: Anthropic
      #--------------------------------------
      # Anthropic Generic Logic
      #--------------------------------------
      - Type: Group
        Name: Claude 3.7 Sonnet
        Conditions:
          - Source: CZ:Defined:GenAI_Model
            Transforms:
              - Type: Normalize
            Contains: [claude-3-7-sonnet, claude-37-sonnet]
      - Type: Group
        Name: Claude 3.7 Haiku
        Conditions:
          - Source: CZ:Defined:GenAI_Model
            Transforms:
              - Type: Normalize
            Contains: [claude-3-7-haiku, claude-37-haiku]
      - Type: Group
        Name: Claude 3.5 Sonnet
        Conditions:
          - Source: CZ:Defined:GenAI_Model
            Transforms:
              - Type: Normalize
            Contains: [claude-3-5-sonnet, claude-35-sonnet]
      - Type: Group
        Name: Claude 3.5 Haiku
        Conditions:
          - Source: CZ:Defined:GenAI_Model
            Transforms:
              - Type: Normalize
            Contains: [claude-3-5-haiku, claude-35-haiku]
      - Type: Metadata
        Source: CZ:Defined:GenAI_Model
        Values:
          - Claude 3 Sonnet: [claude3sonnet]
          - Claude 3 Haiku: [claude3haiku]
          - Claude
      #--------------------------------------
      # AWS Marketplace Logic - Externalized becuase it may be custom at each customer
      #--------------------------------------
      - Type: GroupBy
        Source: Service
        Transforms:
          - Type: Split
            Delimiter: ' (Amazon Bedrock Edition)'
            Index: 1
        Conditions:
          - And:
            - Source: CloudProvider
              Equals: AWS Marketplace
            - Source: Service
              Contains: Bedrock
      #--------------------------------------
      # AWS Bedrock Customer Specific Logic
      #--------------------------------------
      - Type: GroupBy
        Source: CZ:Defined:GenAI_Model_Family_Bedrock
      #--------------------------------------
      # AWS Bedrock Generic Logic
      #--------------------------------------
      - Type: Group
        Name: Bedrock Guardrails
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: AWS
            - Not:
              - Source: CloudProvider
                Contains: Marketplace
            - Source: User:Defined:Test_GenAI_Platform
              Equals: Bedrock
            - Source: User:Defined:Test_GenAI_Model
              BeginsWith: Guardrail
      - Type: Group
        Name: Bedrock AI jobs
        Conditions:
          - Source: User:Defined:Test_GenAI_Model
            Equals: [model-invocation-job, data-automation-invocation]
      - Type: Metadata
        Source: CZ:Defined:GenAI_Model
        Values:
          - Nova Canvas: [novacanvas]
          - Nova Lite: [novalite]
          - Nova Micro: [novamicro]
          - Nova Pro: [novapro]
          - Nova Reel: [novareel]
          - Olympus Image Generator
          - Titan Embeddings G1: [titanembed, titan-embed]
          - Titan Image Generator G1: [titan-image-generator, titanimagegenerator, titanimage]
          - Titan Text G1 - Express: [titan-text-express, titantextexpress, titantext-express, titantextg1-express]
          - Titan Text G1 - Lite: [titan-text-lite, titantextlite, titantext-lite, titantextg1-lite]
          - Titan Text G1 - Premier: [titan-text-premier, titantextpremier, titantext-premier, titantextg1-premier]
          - Titan Text G1: [titantext, titan-text]
      #--------------------------------------
      # Cohere Logic
      #--------------------------------------
      - Type: Metadata
        Sources: CZ:Defined:GenAI_Model
        Values:
          - Rerank
          - Command Light: [commandlight]
          - Command R: [commandr]
          - Command
      #--------------------------------------
      # Deepseek General Logic
      #--------------------------------------
      - Type: Metadata
        Source: CZ:Defined:GenAI_Model
        Values:
          - DeepSeek-R1: [deepseekr1]
      #--------------------------------------
      # GCP Vertex Logic
      #--------------------------------------
      # Non-Vertex Providers
      - Type: GroupBy
        Source: CZ:Defined:ServiceDisplay
        Transforms:
          - Type: Split
            Delimiter: ' ('
            Index: 1
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Not:
              - Source: CZ:Defined:GenAI_Platform
                Equals: Vertex AI
      # Vertex Providers
      - Type: Group
        Name: PaLM Text Bison
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: CZ:Defined:GenAI_Platform
              Equals: Vertex AI
            - Source: CZ:Defined:GenAI_Model
              Equals: PaLM Text Bison
      - Type: Group
        Name: PaLM Text Bison
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: CZ:Defined:GenAI_Platform
              Equals: Vertex AI
            - Source: CZ:Defined:GenAI_Model
              Equals: PaLM Text Bison
      # Bad data with leading spaces which requires these specific rules
      - Type: Group
        Name: Gemini 2.5 Pro
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: UsageFamily
              Contains: Gemini 2.5 Pro
      - Type: Group
        Name: Gemini 2.5 Flash
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: UsageFamily
              Contains: Gemini 2.5 Flash
      - Type: Group
        Name: Gemini 2.0 Pro
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: UsageFamily
              Contains: Gemini 2.0 Pro
      - Type: Group
        Name: Gemini 2.0 Flash
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: UsageFamily
              Contains: Gemini 2.0 Flash
      - Type: Group
        Name: Gemini 1.5 Pro
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: UsageFamily
              Contains: Gemini 1.5 Pro
      - Type: Group
        Name: Gemini 1.5 Flash
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: UsageFamily
              Contains: Gemini 1.5 Flash
      - Type: Group
        Name: Gemini 1.0 Flash
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: UsageFamily
              Contains: Gemini 1.0 Flash
      - Type: Group
        Name: Evaluation Service
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: UsageFamily
              Contains: Evaluation service
      # Dynamic logic for future values
      - Type: GroupBy
        Source: UsageFamily
        Transforms:
          - Type: Split
            Delimiter: ' Pro'
            Index: 1
        Format: '{0} Pro'
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: CZ:Defined:GenAI_Platform
              Equals: Vertex AI
            - Source: UsageFamily
              Contains: Pro
      - Type: GroupBy
        Source: UsageFamily
        Transforms:
          - Type: Split
            Delimiter: ' Flash'
            Index: 1
        Format: '{0} Flash'
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: CZ:Defined:GenAI_Platform
              Equals: Vertex AI
            - Source: UsageFamily
              Contains: Flash
      - Type: GroupBy
        Source: CZ:Defined:GenAI_Model
        Transforms:
          - Type: Split
            Delimiter: ' Text'
            Index: 1
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: CZ:Defined:GenAI_Platform
              Equals: Vertex AI
            - Source: CZ:Defined:GenAI_Model
              Contains: Text
            - Not:
              - Source: CZ:Defined:GenAI_Model
                BeginsWith: Embedding
      - Type: GroupBy
        Source: CZ:Defined:GenAI_Model
        Transforms:
          - Type: Split
            Delimiter: ' Video'
            Index: 1
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: CZ:Defined:GenAI_Platform
              Equals: Vertex AI
            - Source: CZ:Defined:GenAI_Model
              Contains: Video
      - Type: GroupBy
        Source: CZ:Defined:GenAI_Model
        Transforms:
          - Type: Split
            Delimiter: ' Audio'
            Index: 1
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: GCP
            - Source: CZ:Defined:GenAI_Platform
              Equals: Vertex AI
            - Source: CZ:Defined:GenAI_Model
              Contains: Audio 
      - Type: Metadata
        Sources: CZ:Defined:GenAI_Model
        Conditions:
          - Source: CloudProvider
            Contains: GCP
          - Source: CZ:Defined:GenAI_Platform
            Equals: Vertex AI
        Values:
          #- Vertex Colab
          - AI Pipeline
          - Embeddings for Text
          - ShieldGemma 2
          - PaliGemma
          - CodeGemma
          - TxGemma
          - Gemma 3
          - Gemma 2
          - Gemma
          - Imagen 4 for Generation: [imagen-4-generation]
          - Imagen 4 Ultra Generate
          - Imagen 3 for Editing and Customization
          - Imagen 3 for Fast Generation: [imagen-3-fast-generation]
          - Imagen 3 for Generation: [imagen-3-generation]
          - Imagen for Image Generation
          - Imagen for Upscaling
          - Imagen
          - LLM Grounding
          - Multimodal Embeddings
          - MedLM-large-large
          - MedLM-medium
          - Rescap
          - Veo 3 for Generation: [veo-3-generation]
          - Veo 2 for Generation: [veo-2-generation] 
          - Veo
      #--------------------------------------
      # Luma AI General Logic
      #--------------------------------------
      - Type: Metadata
        Source: CZ:Defined:GenAI_Model
        Values:
          - Ray2
      #--------------------------------------
      # Meta Generic Logic
      #--------------------------------------
      - Type: GroupBy
        Source: CZ:Defined:GenAI_Model
        Format: 'Llama 3.5 {0}'
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: 'llama3-5-'
            Index: 2
          - Type: Split
            Delimiter: '-'
            Index: 1
      - Type: GroupBy
        Source: CZ:Defined:GenAI_Model
        Format: 'Llama 3.4 {0}'
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: 'llama3-4-'
            Index: 2
          - Type: Split
            Delimiter: '-'
            Index: 1
      - Type: GroupBy
        Source: CZ:Defined:GenAI_Model
        Format: 'Llama 3.3 {0}'
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: 'llama3-3-'
            Index: 2
          - Type: Split
            Delimiter: '-'
            Index: 1
      - Type: GroupBy
        Source: CZ:Defined:GenAI_Model
        Format: 'Llama 3.2 {0}'
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: 'llama3-2-'
            Index: 2
          - Type: Split
            Delimiter: '-'
            Index: 1
      - Type: GroupBy
        Source: CZ:Defined:GenAI_Model
        Format: 'Llama 3.1 {0}'
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: 'llama3-1-'
            Index: 2
          - Type: Split
            Delimiter: '-'
            Index: 1
      - Type: GroupBy
        Source: CZ:Defined:GenAI_Model
        Format: 'Llama 3 {0}'
        Transforms:
          - Type: Lower
          - Type: Split
            Delimiter: 'llama3-'
            Index: 2
          - Type: Split
            Delimiter: '-'
            Index: 1
      - Type: Metadata
        Source: CZ:Defined:GenAI_Model
        Values:
          - Llama 4 Maverick: [llama4-maverick]
          - Llama 4 Scout: [llama4-scout]
          - Llama 3: [llama3]
          - Llama
      #--------------------------------------
      # Mistral Generic Logic
      #--------------------------------------
      - Type: Metadata
        Source: CZ:Defined:GenAI_Model
        Values:
          - Pixtral Large: [pixtrallarge, mistrallarge, mistral7b, mistralsmall]
          - Pixtral
          - Minstral
      #--------------------------------------
      # OpenAI Logic
      #--------------------------------------
      - Type: Group
        Name: GPT-4.5 mini
        Conditions:
          - Source: CZ:Defined:GenAI_Model
            Transforms:
              - Type: Normalize
            Contains: [gpt-4-5-mini, gpt-45-mini]
      - Type: Group
        Name: GPT-4.1 nano
        Conditions:
          - Source: CZ:Defined:GenAI_Model
            Transforms:
              - Type: Normalize
            Contains: [gpt-4-1-nano, gpt-41-nano]
      - Type: Group
        Name: GPT-4.1 mini
        Conditions:
          - Source: CZ:Defined:GenAI_Model
            Transforms:
              - Type: Normalize
            Contains: [gpt-4-1-mini, gpt-41-mini]
      - Type: Group
        Name: GPT-4.1
        Conditions:
          - Source: CZ:Defined:GenAI_Model
            Transforms:
              - Type: Normalize
            Contains: [gpt-4-1, gpt-41]
      - Type: Group
        Name: GPT-3.5 Turbo
        Conditions:
          - Source: CZ:Defined:GenAI_Model
            Transforms:
              - Type: Normalize
            Contains: [gpt-3-5-turbo, gpt-35-turbo]
      - Type: Metadata
        Sources: CZ:Defined:GenAI_Model
        Values:
          - Babbage
          - codex-mini
          - codex
          - computer-use-preview
          - Dall-E 4
          - Dall-E 3
          - Dall-E 2
          - Davinci
          #---GPT models are in a specific order to ensure matching
          - ChatGPT-4o
          - GPT Image 2
          - GPT Image 1
          - GPT-4o mini Search Preview
          - GPT-4o Search Preview
          - GPT-4o mini Transcribe
          - GPT-4o Transcribe
          - GPT-4o mini TTS
          - GPT-4o mini Realtime
          - GPT-4o Realtime
          - GPT-4o mini Audio
          - GPT-4o Audio
          - GPT-4o mini
          - GPT-4o
          - GPT 4 Mini
          - GPT-4 Turbo
          - GPT-4
          - GPT
          #---
          - o4-mini
          - o3-mini
          - o4
          - o3
          - o1-mini
          - o1-pro
          - o1
          - omni-moderation
          - text-moderation
          - text-embedding-3
          - text-embedding-ada-002
          - TTS-1 HD
          - TTS-1
          - Whisper
          - ada
      #--------------------------------------
      # Fallback Logic For AWS Bedrock (keep at bottom)
      #--------------------------------------
      - Type: Group
        Name: AWS Bedrock Managed Model
        Conditions:
          - And:
            - Source: CloudProvider
              Contains: AWS
            - Not:
              - Source: CloudProvider
                Contains: Marketplace
            - Source: CZ:Defined:GenAI_Platform
              Equals: Bedrock

  GenAI_Model_Bedrock:                # HIDDEN - To be overriden for custom bedrock scenarios
    Name: GenAI Model - AWS Bedrock
    Hide: True
    Rules:
      - Type: Group
        Name: Override Logic
        Conditions:  
          - And:
            - Source: CloudProvider
              Contains: AWS
            - Source: CZ:Defined:GenAI_Platform
              Equals: Bedrock
            - Source: Service
              Contains: OverrideLogic

  GenAI_Model_Family_Bedrock:         # HIDDEN - To be overriden for custom bedrock scenarios
    Name: GenAI Model Family - AWS Bedrock Managed Models
    Hide: True
    Rules:
      - Type: Group
        Name: Override Logic
        Conditions:  
          - And:
            - Source: CloudProvider
              Equals: AWS
            - Source: CZ:Defined:GenAI_Platform
              Equals: Bedrock
            - Source: Service
              Contains: OverrideLogic

# Hidden and used for dimensions
  ResourceSummaryDisplay:              # HIDDEN
    Name: Resource Summary Display
    Hide: True
    Source: CZ:Defined:ResourceSummaryID
    Rules:
      - Type: GroupBy
        Source: CZ:Defined:ResourceSummaryID
        Conditions:
          - Not:
            - BeginsWith: czrn
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay

  ResourceDisplay:                     # HIDDEN
    Name: Resource Display
    Hide: True
    Rules:
      #-----------------------------------------
      # AnyCost Adapters
      #-----------------------------------------
      - Type: GroupBy
        Source: Resource
        Transforms:
          - Type: Split
            Delimiter: ':'
            Index: 7
        Conditions:
          - Not:
            - Source: CloudProvider
              BeginsWith: [AWS, GCP, Azure, Snowflake, Datadog, New Relic, MongoDB, Databricks]      
      - Type: GroupBy
        Source: Resource
        Transforms:
          - Type: Split
            Delimiter: ':'
            Index: 6
        Conditions:
          - Not:
            - Source: CloudProvider
              BeginsWith: [AWS, GCP, Azure, Snowflake, Datadog, New Relic, MongoDB, Databricks]   
      - Type: GroupBy
        Source: Resource
        Conditions:
          - Not:
            - Source: CloudProvider
              BeginsWith: [AWS, GCP, Azure, Snowflake, Datadog, New Relic, MongoDB, Databricks]   
      #-----------------------------------------
      # Default Logic
      #-----------------------------------------
      - Type: GroupBy
        Source: Resource
        Transforms:
          - Type: Split
            Delimiter: ':'
            Index: 7
        Conditions:
          - Source: Resource
            BeginsWith: czrn
      - Type: GroupBy
        Source: Resource
        Transforms:
          - Type: Split
            Delimiter: ':'
            Index: 6
        Conditions:
          - Source: Resource
            BeginsWith: czrn
      - Type: Group
        Name: service-usage
        Conditions:
          - Source: Resource
            BeginsWith: czrn
      - Type: GroupBy
        Source: Resource
        Transforms:
          - Type: Split
            Delimiter: ':'
            Index: 6
        Conditions:
          - Source: Resource
            BeginsWith: [arn, billingitem-Usage]
      - Type: Group
        Name: service-usage
        Conditions:
          - Source: Resource
            BeginsWith: [arn, billingitem-Usage]
      - Type: GroupBy
        Source: Resource

  ResourceNameOnly:                     # DEPRICATED; HIDDEN
    Name: Resource Name
    Hide: True
    Rules:
      - Type: GroupBy
        Source: CZ:Defined:ResourceDisplay

  ServiceDisplay:                       # HIDDEN
    Name: Service Display
    Hide: True
    Source: Service
    Rules:
      #--------------------------------------
      # Datadog Service Name Mapping
      #--------------------------------------
      - Type: Group
        Name: APM
        Conditions:
          - Equals: apm_host
      - Type: Group
        Name: APM(ExcludesUSMHosts)
        Conditions:
          - Equals: apm_host_no_usm
      - Type: Group
        Name: APMDevSecOpsEnterprise
        Conditions:
          - Equals: apm_ent_devsecops
      - Type: Group
        Name: APMEnterprise
        Conditions:
          - Equals: apm_host_enterprise
      - Type: Group
        Name: APMPro
        Conditions:
          - Equals: apm_host_pro
      - Type: Group
        Name: APMProfiler
        Conditions:
          - Equals: apm_profiler_host
      - Type: Group
        Name: ApplicationSecurity-ThreatManagement
        Conditions:
          - Equals: application_security_host
      - Type: Group
        Name: ApplicationVulnerabilityManagement-OSS
        Conditions:
          - Equals: application_vulnerability_management_oss_host
      - Type: Group
        Name: AuditTrail
        Conditions:
          - Equals: audit_trail
      - Type: Group
        Name: CloudCostManagement
        Conditions:
          - Equals: cloud_cost_management
      - Type: Group
        Name: CloudSecurityManagement
        Conditions:
          - Equals: cspm_host
      - Type: Group
        Name: CloudSecurityManagementContainersEnterprise
        Conditions:
          - Equals: csm_container_enterprise
      - Type: Group
        Name: CloudSecurityManagementEnterprise
        Conditions:
          - Equals: csm_host_enterprise
      - Type: Group
        Name: CloudSecurityManagementPro
        Conditions:
          - Equals: csm_host_pro
      - Type: Group
        Name: CloudSIEM-Indexed
        Conditions:
          - Equals: siem_indexed
      - Type: Group
        Name: CloudSIEM
        Conditions:
          - Equals: siem
      - Type: Group
        Name: CloudWorkloadSecurity
        Conditions:
          - Equals: cws_host
      - Type: Group
        Name: Cont.DevSecOpsPro
        Conditions:
          - Equals: cont_devsecops_pro
      - Type: Group
        Name: CSMProContainers
        Conditions:
          - Equals: cspm_container
      - Type: Group
        Name: CustomEvents
        Conditions:
          - Equals: custom_event
      - Type: Group
        Name: CustomMetrics
        Conditions:
          - Equals: timeseries
      - Type: Group
        Name: CWSContainers
        Conditions:
          - Equals: cws_container
      - Type: Group
        Name: DatabaseMonitoring-NormalizedQueries
        Conditions:
          - Equals: dbm_normalized_queries
      - Type: Group
        Name: DatabaseMonitoring
        Conditions:
          - Equals: dbm_host
      - Type: Group
        Name: DataStreamsMonitoring
        Conditions:
          - Equals: data_stream_monitoring
      - Type: Group
        Name: DrawdownMinimumSpend
        Conditions:
          - Equals: drawdown_min_spend
      - Type: Group
        Name: ErrorTracking
        Conditions:
          - Equals: error_tracking
      - Type: Group
        Name: Fargate(APMandProfiler)
        Conditions:
          - Equals: fargate_container_apm_and_profiler
      - Type: Group
        Name: Fargate(ApplicationSecurity-ThreatManagement)
        Conditions:
          - Equals: application_security_fargate
      - Type: Group
        Name: Fargate(ContinuousProfiler)
        Conditions:
          - Equals: fargate_container_profiler
      - Type: Group
        Name: FargateTasks(APM)
        Conditions:
          - Equals: apm_fargate
      - Type: Group
        Name: FargateTasks(Pro)
        Conditions:
          - Equals: fargate_container
      - Type: Group
        Name: FlexLogs-ExtraSmall
        Conditions:
          - Equals: flex_compute_logs_extra_small
      - Type: Group
        Name: FlexLogs-Medium
        Conditions:
          - Equals: flex_compute_logs_medium
      - Type: Group
        Name: FlexLogs-Small
        Conditions:
          - Equals: flex_compute_logs_small
      - Type: Group
        Name: FlexLogs-Starter
        Conditions:
          - Equals: flex_logs_starter
      - Type: Group
        Name: FlexStoredLogs
        Conditions:
          - Equals: flex_stored_logs
      - Type: Group
        Name: HostDevSecOpsProPlus
        Conditions:
          - Equals: host_devsecops_proplus
      - Type: Group
        Name: IncidentManagement
        Conditions:
          - Equals: incident_management
      - Type: Group
        Name: IndexedLogEvents
        Conditions:
          - Equals: logs_indexed
      - Type: Group
        Name: IndexedSpans
        Conditions:
          - Equals: apm_trace_search
      - Type: Group
        Name: InfrastructureandAPMHosts
        Conditions:
          - Equals: infra_and_apm_host
      - Type: Group
        Name: InfrastructureContainers
        Conditions:
          - Equals: infra_container
      - Type: Group
        Name: InfrastructureContainers(ExcludesAgent)
        Conditions:
          - Equals: infra_container_excl_agent
      - Type: Group
        Name: InfrastructureHosts
        Conditions:
          - Equals: infra_host
      - Type: Group
        Name: IngestedCustomMetrics
        Conditions:
          - Equals: ingested_timeseries
      - Type: Group
        Name: IngestedSpans
        Conditions:
          - Equals: ingested_spans
      - Type: Group
        Name: IntelligentTestRunner
        Conditions:
          - Equals: ci_intelligent_test_runner
      - Type: Group
        Name: LogIngestion
        Conditions:
          - Equals: logs_ingested
      - Type: Group
        Name: Logs-ForwardingtoCustomDestinations
        Conditions:
          - Equals: logs_forwarding
      - Type: Group
        Name: Logs-IndexedLogEvents(15-day)
        Conditions:
          - Equals: logs_indexed_15day
      - Type: Group
        Name: Logs-IndexedLogEvents(180-day)
        Conditions:
          - Equals: logs_indexed_180day
      - Type: Group
        Name: Logs-IndexedLogEvents(3-day)
        Conditions:
          - Equals: logs_indexed_3day
      - Type: Group
        Name: Logs-IndexedLogEvents(30-day)
        Conditions:
          - Equals: logs_indexed_30day
      - Type: Group
        Name: Logs-IndexedLogEvents(45-day)
        Conditions:
          - Equals: logs_indexed_45day
      - Type: Group
        Name: Logs-IndexedLogEvents(60-day)
        Conditions:
          - Equals: logs_indexed_60day
      - Type: Group
        Name: Logs-IndexedLogEvents(7-day)
        Conditions:
          - Equals: logs_indexed_7day
      - Type: Group
        Name: Logs-IndexedLogEvents(90-day)
        Conditions:
          - Equals: logs_indexed_90day
      - Type: Group
        Name: Logs-IndexedLogEvents(CustomRetention)
        Conditions:
          - Equals: logs_indexed_custom_retention
      - Type: Group
        Name: MobileAppTesting
        Conditions:
          - Equals: synthetics_mobile_app_testing
      - Type: Group
        Name: NetflowMonitoring
        Conditions:
          - Equals: netflow_monitoring
      - Type: Group
        Name: NetworkDeviceMonitoring
        Conditions:
          - Equals: network_device
      - Type: Group
        Name: NetworkPerformanceMonitoring
        Conditions:
          - Equals: npm_host
      - Type: Group
        Name: ObservabilityPipelines-VCPU
        Conditions:
          - Equals: observability_pipeline_vcpu
      - Type: Group
        Name: ObservabilityPipelines
        Conditions:
          - Equals: observability_pipeline
      - Type: Group
        Name: OnlineArchive
        Conditions:
          - Equals: online_archive
      - Type: Group
        Name: PipelineIndexedSpans
        Conditions:
          - Equals: ci_pipeline_indexed_spans
      - Type: Group
        Name: PipelineVisibility
        Conditions:
          - Equals: ci_pipeline
      - Type: Group
        Name: PremierSupport
        Conditions:
          - Equals: premier_support
      - Type: Group
        Name: ProfiledContainers
        Conditions:
          - Equals: prof_container
      - Type: Group
        Name: ProfiledHosts
        Conditions:
          - Equals: prof_host
      - Type: Group
        Name: RealUserMonitoringSessions
        Conditions:
          - Equals: rum
      - Type: Group
        Name: RUMBrowserandMobileSessions
        Conditions:
          - Equals: rum_lite
      - Type: Group
        Name: RUMPremium
        Conditions:
          - Equals: rum_replay
      - Type: Group
        Name: SensitiveDataScanner
        Conditions:
          - Equals: sensitive_data_scanner
      - Type: Group
        Name: ServerlessAPM
        Conditions:
          - Equals: serverless_apm
      - Type: Group
        Name: ServerlessFunctions
        Conditions:
          - Equals: lambda_function
      - Type: Group
        Name: ServerlessInvocation
        Conditions:
          - Equals: serverless_invocation
      - Type: Group
        Name: ServerlessWorkloadMonitoring-Apps
        Conditions:
          - Equals: serverless_apps
      - Type: Group
        Name: ServerlessWorkloads
        Conditions:
          - Equals: serverless_infra
      - Type: Group
        Name: StandardCustomMetrics
        Conditions:
          - Equals: standard_timeseries
      - Type: Group
        Name: SyntheticsAPITests
        Conditions:
          - Equals: synthetics_api_tests
      - Type: Group
        Name: SyntheticsAppTesting
        Conditions:
          - Equals: synthetics_app_testing
      - Type: Group
        Name: SyntheticsBrowserTests
        Conditions:
          - Equals: synthetics_browser_checks
      - Type: Group
        Name: TestingIndexedSpans
        Conditions:
          - Equals: ci_test_indexed_spans
      - Type: Group
        Name: TestingVisibility
        Conditions:
          - Equals: ci_testing
      - Type: Group
        Name: UniversalServiceMonitoring-withinInfraHosts
        Conditions:
          - Equals: usm_within_infra_host
      - Type: Group
        Name: UniversalServiceMonitoring
        Conditions:
          - Equals: usm_standalone
      - Type: Group
        Name: WorkflowAutomation
        Conditions:
          - Equals: workflow_execution  
      #--------------------------------------
      # AWS Logic
      #--------------------------------------
      # Override Logic
      - Type: Group
        Name: "OpenSearch (ES)"
        Conditions:
          - Equals: AmazonES
      #--------------------------------------
      # Default Logic
      #--------------------------------------
      - Type: GroupBy
        Source: Service
        Transforms:
          - Type: Split
            Delimiter: Amazon
            Index: 2
        Conditions:
          - Source: Service
            BeginsWith: Amazon
      - Type: GroupBy
        Source: Service
        Transforms:
          - Type: Split
            Delimiter: AWS
            Index: 2
        Conditions:
          - Source: Service
            BeginsWith: AWS
      #--------------------------------------
      # Fallback Logic
      #--------------------------------------
      - Type: GroupBy
        Source: Service

  CommittedUseSubscription_Display:
    Name: Committed Use Subscription Display
    Hide: True
    Rules:
      - Type: GroupBy
        Source: CommittedUseSubscription
        Transforms:
          - Type: Split
            Delimiter: ':savingsplan/'
            Index: 2
        Format: 'savingsplan: {0}'
        Conditions:
          - Source: CommittedUseSubscription
            Contains: ":savingsplan/"
      - Type: GroupBy
        Source: CommittedUseSubscription
        Transforms:
          - Type: Split
            Delimiter: ':ri:'
            Index: 2
        Format: 'ri: {0}'
        Conditions:
          - Source: CommittedUseSubscription
            Contains: ":ri:"
      - Type: GroupBy
        Source: CommittedUseSubscription
        Transforms:
          - Type: Split
            Delimiter: ':reserved-instance:'
            Index: 2
        Format: 'reserved-instance: {0}'
        Conditions:
          - Source: CommittedUseSubscription
            Contains: ":reserved-instance:"
      - Type: GroupBy
        Source: CommittedUseSubscription
        Transforms:
          - Type: Split
            Delimiter: ':reserved-instances/'
            Index: 2
        Format: 'reserved-instance: {0}'
        Conditions:
          - Source: CommittedUseSubscription
            Contains: ":reserved-instances/"
      - Type: GroupBy
        Source: CommittedUseSubscription
        Transforms:
          - Type: Split
            Delimiter: ':reserved-instance-exchange/'
            Index: 2
        Format: 'reserved-instance-exchange: {0}'
        Conditions:
          - Source: CommittedUseSubscription
            Contains: ":reserved-instance-exchange/"
      - Type: GroupBy
        Source: CommittedUseSubscription

```
