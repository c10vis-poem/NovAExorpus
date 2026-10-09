---
title: "generative-ai_gemini_rag-engine_rag_engine_vector_search.ipynb at main · GoogleCloudPlatform_generative-ai"
source: "google_agentic_ai/Deploying GEMMA4&GeminiFLASH/generative-ai_gemini_rag-engine_rag_engine_vector_search.ipynb at main · GoogleCloudPlatform_generative-ai/generative-ai_gemini_rag-engine_rag_engine_vector_search.ipynb at main · GoogleCloudPlatform_generative-ai.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

main
generative-ai / gemini / rag-engine / rag_engine_vector_search.ipynb
holtskinner Migrate official Notebooks from Gemini 2.0 to Gemini 3 (#2601)
be8ffa5 · 5 months ago
700 lines (700 loc) · 23.7 KB ·
GoogleCloudPlatform
generative-ai
Code
Issues
71
Pull requests
12
Agents
Discussions
Actions
Projects
Security and quality
Insights
Preview
Code
Blame
Raw


Open in Colab
Open in Colab Enterprise
Open in Vertex AI Workbench
View on GitHub
In [ ]:
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
Vertex AI RAG Engine with Vertex AI Vector
Search
Share to:
Author
Holt Skinner
Overview
This notebook illustrates how to use Vertex AI RAG Engine with Vertex AI Vector Search as a
vector database.
For more information, refer to the official documentation.
For more details on RAG corpus/file management and detailed support please visit Vertex AI
RAG Engine API
Get started
Install Vertex AI SDK and other required packages
In [1]:
%pip install --upgrade --quiet google-cloud-aiplatform google-genai


Restart runtime
To use the newly installed packages in this Jupyter runtime, you must restart the runtime. You
can do this by running the cell below, which restarts the current kernel.
The restart might take a minute or longer. After it's restarted, continue to the next step.
In [ ]:
import IPython
app = IPython.Application.instance()
app.kernel.do_shutdown(True)
⚠️ The kernel is going to restart. Wait until it's finished before continuing to the next step.
⚠️
Authenticate your notebook environment (Colab only)
If you're running this notebook on Google Colab, run the cell below to authenticate your
environment.
In [ ]:
import sys
if "google.colab" in sys.modules:
    from google.colab import auth
    auth.authenticate_user()
Set Google Cloud project information and initialize Vertex AI SDK
To get started using Vertex AI, you must have an existing Google Cloud project and enable the
Vertex AI API.
Learn more about setting up a project and a development environment.
In [ ]:
# Use the environment variable if the user doesn't provide Project ID.
import os
from google import genai
from google.cloud import aiplatform
# fmt: off
PROJECT_ID = "[your-project-id]"  # @param {type: "string", placeholder: "[yo
# fmt: on
if not PROJECT_ID or PROJECT_ID == "[your-project-id]":
    PROJECT_ID = str(os.environ.get("GOOGLE_CLOUD_PROJECT"))
LOCATION = os.environ.get("GOOGLE_CLOUD_REGION", "us-central1")
aiplatform.init(project=PROJECT_ID, location=LOCATION)


client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)
(Optional) Setup Vertex AI Vector Search index and
index endpoint
In this section, we have some helper methods to help you setup your Vector Search index.
This section is not required if you already have a Vector Search index ready to use.
The index has to meet the following criteria:
1. IndexUpdateMethod must be STREAM_UPDATE , see Create stream index.
2. Distance measure type must be explicitly set to one of the following:
DOT_PRODUCT_DISTANCE
COSINE_DISTANCE
3. Dimension of the vector must be consistent with the embedding model you plan to use in
the RAG corpus. Other parameters can be tuned based on your choices, which determine
whether the additional parameters can be tuned.
In [ ]:
# create the index
my_index = aiplatform.MatchingEngineIndex.create_tree_ah_index(
    display_name="your_display_name",
    description="your_description",
    dimensions=768,
    approximate_neighbors_count=10,
    leaf_node_embedding_count=500,
    leaf_nodes_to_search_percent=7,
    distance_measure_type="DOT_PRODUCT_DISTANCE",
    feature_norm_type="UNIT_L2_NORM",
    index_update_method="STREAM_UPDATE",
)
RAG Engine supports public endpoints.
In [ ]:
# create IndexEndpoint
my_index_endpoint = aiplatform.MatchingEngineIndexEndpoint.create(
    display_name="your_display_name", public_endpoint_enabled=True
)
Deploy the index to the index endpoint.
If it's the first time that you're deploying an index to an index endpoint, it takes approximately 30
minutes to automatically build and initiate the backend before the index can be stored. After the
first deployment, the index is ready in seconds. To see the status of the index deployment, open
the Vector Search Console, select the Index endpoints tab, and choose your index endpoint.
Identify the resource name of your index and index endpoint, which have the following the


formats:
projects/${PROJECT_ID}/locations/${LOCATION_ID}/indexes/${INDEX_ID}
projects/${PROJECT_ID}/locations/${LOCATION_ID}/indexEndpoints/${INDEX
If you aren't sure about the resource name, you can use the following command to check:
In [ ]:
print(my_index_endpoint.resource_name)
print(my_index.resource_name)
In [ ]:
# Deploy Index
my_index_endpoint.deploy_index(
    index=my_index, deployed_index_id="your_deployed_index_id"
)
Use Vertex AI Vector Search in RAG Engine
After the Vector Search instance is set up, follow the steps in this section to set the Vector
Search instance as the vector database for the RAG application.
Set the vector database to create a RAG corpus
In [ ]:
from google.genai.types import (
    GenerateContentConfig,
    Retrieval,
    Tool,
    VertexRagStore,
    VertexRagStoreRagResource,
)
from vertexai import rag
In [ ]:
vector_db = rag.VertexVectorSearch(
    index=my_index.resource_name, index_endpoint=my_index_endpoint.resource_n
)
# Name your corpus
DISPLAY_NAME = ""  # @param  {type:"string"}
# Create RAG Corpus
rag_corpus = rag.create_corpus(
    display_name=DISPLAY_NAME, backend_config=rag.RagVectorDbConfig(vector_db
)
print(f"Created RAG Corpus resource: {rag_corpus.name}")
Upload a file to the corpus
In [ ]:
%%writefile test.txt


Here's a demo for Vertex AI Vector Search RAG.
In [ ]:
rag_file = rag.upload_file(
    corpus_name=rag_corpus.name,
    path="test.txt",
    display_name="test.txt",
    description="my test",
)
print(f"Uploaded file to resource: {rag_file.name}")
Import files from Google Cloud Storage
Remember to grant "Viewer" access to the "Vertex RAG Data Service Agent" (with the format of
service-{project_number}@gcp-sa-vertex-rag.iam.gserviceaccount.com ) for
your Google Cloud Storage bucket
In [ ]:
GCS_BUCKET = ""  # @param {type:"string", "placeholder": "your-gs-bucket"}
response = rag.import_files(
    corpus_name=rag_corpus.name,
    paths=[GCS_BUCKET],
    transformation_config=rag.TransformationConfig(
        chunking_config=rag.ChunkingConfig(
            chunk_size=512,
            chunk_overlap=50,
        )
    ),
)
In [ ]:
# Check the files just imported. It may take a few seconds to process the imp
rag.list_files(corpus_name=rag_corpus.name)
Import files from Google Drive
Eligible paths can be:
https://drive.google.com/drive/folders/{folder_id}
https://drive.google.com/file/d/{file_id}
Remember to grant "Viewer" access to the "Vertex RAG Data Service Agent" (with the format of
service-{project_number}@gcp-sa-vertex-rag.iam.gserviceaccount.com ) for
your Drive folder/files.
In [ ]:
FILE_ID = ""  # @param {type:"string", "placeholder": "your-file-id"}
FILE_PATH = f"https://drive.google.com/file/d/{FILE_ID}"
rag.import_files(
    corpus_name=rag_corpus.name,
paths=[FILE PATH]


    paths [FILE_PATH],
    transformation_config=rag.TransformationConfig(
        chunking_config=rag.ChunkingConfig(
            chunk_size=1024,
            chunk_overlap=100,
        )
    ),
)
In [ ]:
# Check the files just imported. It may take a few seconds to process the imp
rag.list_files(corpus_name=rag_corpus.name)
Use your RAG Corpus to add context to your Gemini
queries
When retrieved contexts similarity distance < vector_distance_threshold , the contexts
(from RagStore ) will be used for content generation.
In [ ]:
MODEL_ID = "gemini-2.5-flash"
rag_retrieval_tool = Tool(
    retrieval=Retrieval(
        vertex_rag_store=VertexRagStore(
            rag_resources=[
                VertexRagStoreRagResource(
                    rag_corpus=rag_corpus.name  # Currently only 1 corpus is
                )
            ],
            similarity_top_k=10,
            vector_distance_threshold=0.4,
        )
    )
)
In [ ]:
# fmt: off
GENERATE_CONTENT_PROMPT = "What is RAG and why it is helpful?"  # @param {typ
# fmt: on
response = client.models.generate_content(
    model=MODEL_ID,
    contents=GENERATE_CONTENT_PROMPT,
    config=GenerateContentConfig(tools=[rag_retrieval_tool]),
)
display(Markdown(response.text))
Using other generation API with Rag Retrieval Tool
The retrieved contexts can be passed to any SDK or model generation API to generate final
results.


In [ ]:
RETRIEVAL_QUERY = "What is RAG and why it is helpful?"  # @param {type:"strin
rag_resource = rag.RagResource(
    rag_corpus=rag_corpus.name,
    # Need to manually get the ids from rag.list_files.
    # rag_file_ids=[],
)
response = rag.retrieval_query(
    rag_resources=[rag_resource],  # Currently only 1 corpus is allowed.
    text=RETRIEVAL_QUERY,
    rag_retrieval_config=rag.RagRetrievalConfig(
        top_k=10,  # Optional
        filter=rag.Filter(
            vector_distance_threshold=0.5,  # Optional
        ),
    ),
)
# The retrieved context can be passed to any SDK or model generation API to g
retrieved_context = " ".join(
