# Use Agent Platform Vector Search with RAG Engine  -  Gemini Enterprise Agent Platform  -  Google Cloud Documentation

Use Agent Platform Vector Search
with RAG Engine
The VPC-SC security controls
(/gemini-enterprise-agent-platform/models/security-controls) and CMEK are supported
by Agent Platform RAG Engine. Data residency and AXT security controls aren't supported.
To see an example of using RAG Engine with Vector Search, run the "RAG Engine with
Vector Search" notebook in one of the following environments:
Open in Colab
(https://colab.research.google.com/github/GoogleCloudPlatform/generative-
ai/blob/main/gemini/rag-engine/rag_engine_vector_search.ipynb)
|
Open in Colab Enterprise
(https://console.cloud.google.com/agent-
platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlat
form%2Fgenerative-ai%2Fmain%2Fgemini%2Frag-
engine%2Frag_engine_vector_search.ipynb)
|
Open in Agent Platform Workbench
(https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?
download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2F
generative-ai%2Fmain%2Fgemini%2Frag-engine%2Frag_engine_vector_search.ipynb)
|
content_copy arrow_drop_down


View on GitHub
(https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/rag-
engine/rag_engine_vector_search.ipynb)
This page shows you how to connect your RAG Engine to Gemini Enterprise
Agent Platform Vector Search
(/gemini-enterprise-agent-platform/build/vector-search/overview).
You can also follow along using the RAG Engine with Agent Platform Vector
Search
(https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/rag-
engine/rag_engine_vector_search.ipynb)
notebook.
Agent Platform Vector Search setup
Agent Platform Vector Search is based on Vector Search technology developed
by Google research. With Vector Search you can use the same infrastructure
that provides a foundation for Google products such as Google Search,
YouTube, and Google Play.
To integrate with RAG Engine, an empty Vector Search index is required.
Set up Vertex AI SDK
To set up Vertex AI SDK, see Setup
(/gemini-enterprise-agent-platform/build/vector-search/quickstart#setup).
Create Vector Search index
To create a Vector Search index that's compatible with your RAG Corpus, the
index has to meet the following criteria:


1. IndexUpdateMethod must be STREAM_UPDATE, see Create stream index
 (/gemini-enterprise-agent-platform/build/vector-search/create-manage-
index#create-stream-index)
.
2. Distance measure type must be explicitly set to one of the following:
DOT_PRODUCT_DISTANCE
COSINE_DISTANCE
3. Dimension of the vector must be consistent with the embedding model
you plan to use in the RAG corpus. Other parameters can be tuned based
on your choices, which determine whether the additional parameters can
be tuned.
To learn how to install or update the Vertex AI SDK for Python, see Install
the Vertex AI SDK for Python (/vertex-ai/docs/start/use-vertex-ai-python-sdk).
For more information, see the Python API reference documentation
 (/python/docs/reference/aiplatform/latest).
Python
Vertex AI SDK
-ai-
sdk)
def vector_search_create_streaming_index(
project: str, location: str, display_name: str, gcs_uri: Optional[str] = None
) -> aiplatform.MatchingEngineIndex:
"""Create a vector search index.
   Args:
       project (str): Required. Project ID
       location (str): Required. The region name
       display_name (str): Required. The index display name
       gcs_uri (str): Optional. The Google Cloud Storage uri for index content
   Returns:


Create Vector Search index endpoint
Public endpoints
(/gemini-enterprise-agent-platform/build/vector-search/deploy-index-public) are
supported by RAG Engine.
To learn how to install or update the Vertex AI SDK for Python, see Install
the Vertex AI SDK for Python (/vertex-ai/docs/start/use-vertex-ai-python-sdk).
For more information, see the Python API reference documentation
 (/python/docs/reference/aiplatform/latest).
       The created MatchingEngineIndex.
   """
# Initialize the Vertex AI client
aiplatform.init(project=project, location=location)
# Create Index
index = aiplatform.MatchingEngineIndex.create_tree_ah_index(
display_name=display_name,
contents_delta_uri=gcs_uri,
description="Matching Engine Index",
dimensions=100,
approximate_neighbors_count=150,
leaf_node_embedding_count=500,
leaf_nodes_to_search_percent=7,
index_update_method="STREAM_UPDATE", # Options: STREAM_UPDATE, BATC
distance_measure_type=aiplatform.matching_engine.matching_engine_index_c
)
return index
Python
Vertex AI SDK
-ai-
sdk)


Deploy an index to an index endpoint
Before we do the nearest neighbor search, the index has to be deployed to an
index endpoint.
To learn how to install or update the Vertex AI SDK for Python, see Install
the Vertex AI SDK for Python (/vertex-ai/docs/start/use-vertex-ai-python-sdk).
def vector_search_create_index_endpoint(
project: str, location: str, display_name: str
) -> None:
"""Create a vector search index endpoint.
Args:
project (str): Required. Project ID
location (str): Required. The region name
display_name (str): Required. The index endpoint display name
"""
# Initialize the Vertex AI client
aiplatform.init(project=project, location=location)
# Create Index Endpoint
index_endpoint = aiplatform.MatchingEngineIndexEndpoint.create(
display_name=display_name,
public_endpoint_enabled=True,
description="Matching Engine Index Endpoint",
)
print(index_endpoint.name)
Python
Vertex AI SDK
-ai-
sdk)


For more information, see the Python API reference documentation
 (/python/docs/reference/aiplatform/latest).
def vector_search_deploy_index(
project: str,
location: str,
index_name: str,
index_endpoint_name: str,
deployed_index_id: str,
) -> None:
"""Deploy a vector search index to a vector search index endpoint.
Args:
project (str): Required. Project ID
location (str): Required. The region name
index_name (str): Required. The index to update. A fully-qualified index
resource name or a index ID. Example:
"projects/123/locations/us-central1/indexes/my_index_id" or
"my_index_id".
index_endpoint_name (str): Required. Index endpoint to deploy the index
to.
deployed_index_id (str): Required. The user specified ID of the
DeployedIndex.
"""
# Initialize the Vertex AI client
aiplatform.init(project=project, location=location)
# Create the index instance from an existing index
index = aiplatform.MatchingEngineIndex(index_name=index_name)
# Create the index endpoint instance from an existing endpoint.
index_endpoint = aiplatform.MatchingEngineIndexEndpoint(
index_endpoint_name=index_endpoint_name
)
# Deploy Index to Endpoint


If it's the first time that you're deploying an index to an index endpoint, it takes
approximately 30 minutes to automatically build and initiate the backend
before the index can be stored. After the first deployment, the index is ready in
seconds. To see the status of the index deployment, open the Vector Search
Console
(https://console.cloud.google.com/agent-platform/matching-engine/index-endpoints),
select the Index endpoints tab, and choose your index endpoint.
Identify the resource name of your index and index endpoint, which have the
following formats:
projects/${PROJECT_NUMBER}/locations/${LOCATION_ID}/indexes/${INDEX_ID}
projects/${PROJECT_NUMBER}/locations/${LOCATION_ID}/indexEndpoints/${IND
EX_ENDPOINT_ID}.
Use Agent Platform Vector Search in RAG Engine
After the Vector Search instance is set up, follow the steps in this section to
set the Vector Search instance as the vector database for the RAG application.
Set the vector database to create a RAG corpus
When you create the RAG corpus, specify only the full INDEX_ENDPOINT_NAME
and INDEX_NAME. Make sure to use the numeric ID for both index and index
endpoint resource names. The RAG corpus is created and automatically
index_endpoint = index_endpoint.deploy_index(
index=index, deployed_index_id=deployed_index_id
)
print(index_endpoint.deployed_indexes)


associated with the Vector Search index. Validations are performed on the
criteria (#create_vector-search-name). If any of the requirements aren't met, the
request is rejected.
Before trying this sample, follow the Python setup instructions in the
Agent Platform quickstart using client libraries
 (/gemini-enterprise-agent-platform/machine-learning/start/client-libraries).
To authenticate to Agent Platform, set up Application Default Credentials.
For more information, see Set up authentication for a local development
environment (/docs/authentication/set-up-adc-local-dev-environment).
Python
(#python)
REST (#rest)
import agentplatform
from agentplatform import types
# TODO(developer): Update and un-comment below lines
# PROJECT_ID = "your-project-id"
# vector_search_index_name = "projects/{PROJECT_ID}/locations/{LOCATION}/inde
# vector_search_index_endpoint_name = "projects/{PROJECT_ID}/locations/{LOCAT
# display_name = "test_corpus"
# description = "Corpus Description"
# Initialize Agent Platform client once per session
client = agentplatform.Client(project=PROJECT_ID, location="us-central1")
# Configure embedding model (Optional)
embedding_model_config = types.RagEmbeddingModelConfig(
vertex_prediction_endpoint=types.RagEmbeddingModelConfigVertexPredictionEnd
endpoint="publishers/google/models/text-embedding-005"
)
)


Import files using the RAG API
Use the ragFiles.import API method
(/gemini-enterprise-agent-
platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/import)
to import files from Cloud Storage or Google Drive into the Vector Search
index. The files are embedded and stored in the Vector Search index.
# Configure Vector DB
vector_db = types.RagVectorDbConfigVertexVectorSearch(
index=vector_search_index_name,
index_endpoint=vector_search_index_endpoint_name
)
corpus = client.rag.create_corpus(
rag_corpus=types.RagCorpus(
display_name=display_name,
description=description,
rag_vector_db_config=types.RagVectorDbConfig(
rag_embedding_model_config=embedding_model_config,
vertex_vector_search=vector_db,
),
)
)
print(corpus)
# Example response:
# RagCorpus(name='projects/1234567890/locations/us-central1/ragCorpora/12345
# display_name='test_corpus', description='Corpus Description', embedding_model_c
# ...
REST
(#rest)
Python
Vertex AI SDK


Retrieve relevant contexts using the RAG API
After completion of the file imports, the relevant context can be retrieved from
the Vector Search index by using the RetrieveContexts API.
# TODO(developer): Update and uncomment the following lines:
# RAG_CORPUS_ID = "your-rag-corpus-id"
#
# Google Cloud Storage bucket/file location.
# For example, "gs://rag-fos-test/"
# GCS_URIS= "your-gcs-uris"
# Call ImportRagFiles API to embed files and store in the BigQuery table
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
https://us-central1-aiplatform.googleapis.com/v1beta1/projects/${PROJECT_NUMB
-d '{
 "import_rag_files_config": {
   "gcs_source": {
     "uris": '\""${GCS_URIS}"\"'
   },
   "rag_file_chunking_config": {
     "chunk_size": 512
   }
 }
}'
# Call ListRagFiles API to verify the files are imported successfully
curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
https://us-central1-aiplatform.googleapis.com/v1beta1/projects/${PROJECT_NUMB


Generate content using Agent Platform Gemini API
To generate content using Gemini models, make a call to the Agent Platform
GenerateContent API. By specifying the RAG_CORPUS_RESOURCE in the request,
the API automatically retrieves data from the Vector Search index.
REST
(
)
Python
Vertex AI SDK
# TODO(developer): Update and uncomment the following lines:
# RETRIEVAL_QUERY="your-retrieval-query"
#
# Full RAG corpus resource name
# Format:
# &quot;projects/${PROJECT_NUMBER}/locations/us-central1/ragCorpora/${RAG_C
# RAG_CORPUS_RESOURCE=&quot;your-rag-corpus-resource&quot;
# Call RetrieveContexts API to retrieve relevant contexts
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
https://us-central1-aiplatform.googleapis.com/v1beta1/projects/${PROJECT_NUMB
-d '{
   "vertex_rag_store": {
     "rag_resources": {
         "rag_corpus": '\""${RAG_CORPUS_RESOURCE}"\"',
       },
   },
   "query": {
     "text": '\""${RETRIEVAL_QUERY}"\"',
     "similarity_top_k": 10
   }
 }'
Python


What's next
Use Agent Search as a retrieval backend using RAG Engine
 (/gemini-enterprise-agent-platform/build/rag-engine/use-vertexai-search)
Vertex AI SDK
# TODO(developer): Update and uncomment the following lines:
# MODEL_ID=gemini-2.0-flash
# GENERATE_CONTENT_PROMPT="your-generate-content-prompt"
# GenerateContent with contexts retrieved from the FeatureStoreOnline index
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" https://us-central1-aiplatform.googleapis.com/v
-d '{
 "contents": {
   "role": "user",
   "parts": {
     "text": '\""${GENERATE_CONTENT_PROMPT}"\"'
   }
 },
 "tools": {
   "retrieval": {
     "vertex_rag_store": {
       "rag_resources": {
           "rag_corpus": '\""${RAG_CORPUS_RESOURCE}"\"',
         },
       "similarity_top_k": 8,
       "vector_distance_threshold": 0.32
     }
   }
 }
}'


Except as otherwise noted, the content of this page is licensed under the Creative Commons
Attribution 4.0 License (https://creativecommons.org/licenses/by/4.0/), and code samples
are licensed under the Apache 2.0 License (https://www.apache.org/licenses/LICENSE-2.0).
For details, see the Google Developers Site Policies
(https://developers.google.com/site-policies). Java is a registered trademark of Oracle
and/or its affiliates.
Last updated 2026-07-23 UTC.
