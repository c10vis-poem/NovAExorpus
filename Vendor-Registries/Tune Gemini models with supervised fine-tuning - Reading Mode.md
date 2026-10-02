<!-- Converted from Tune Gemini models with supervised fine-tuning - Reading Mode.pdf — 28 pages -->

## Page 1

# Tune Gemini models with supervised fine-tuning
Skip to main content
# Tune Gemini models with supervised fine-tuning Stay organized with collections Save and categorize content based on
# your preferences.
On this page
Before you begin
Supported models
Create a tuning job
Tuning hyperparameters
View a list of tuning jobs
Get details of a tuning job
Cancel a tuning job
Evaluate the tuned model
Delete a tuned model
Tuning and validation metrics
Model tuning metrics
Model validation metrics
What's next
This document describes how to tune a Gemini model by using supervised fine-tuning.
# Before you begin
Before you begin, you must prepare a supervised fine-tuning dataset. Depending on your use case, there are different requirements for preparing a dataset:
Text tuning
Image tuning
Document tuning
Audio tuning
Video tuning
Tune function calling
# Supported models
The following Gemini models support supervised tuning:
# Click to expand supported models
Gemini 3.5 Flash
Gemini 3.1 Flash-Lite
Gemini 2.5 Pro
Gemini 2.5 Flash-Lite
Gemini 2.5 Flash
# Create a tuning job
You can create a supervised fine-tuning job by using the Google Cloud console, the Google Gen AI SDK, the REST API, or Colab Enterprise.

---

## Page 2

Optional: (Preview) Include the evaluationConfig to automatically run an evaluation using the Gen AI evaluation service after the tuning job completes. This evaluation configuration is available in the us-central1 region.
To tune a text model with supervised fine-tuning by using the Google Cloud console, perform the following steps:
1. In the Gemini Enterprise Agent Platform section of the Google Cloud console, go to the Agent Platform Studio page.
Go to Agent Platform Studio
2. Click Create tuned model.
3. Under Model details, configure the following:
1. In the Tuned model name field, enter a name for your new tuned model, up to 128 characters.
2. In the Base model field, select the foundation model to tune.
3. In the Region drop-down field, select the region where the pipeline tuning job runs and where the tuned model is deployed.
4. Under Tuning setting, configure the following:
1. In the Number of epochs field, enter the number of steps to run for model tuning.
2. In the Adapter Size field, enter the adapter size to use for model tuning.
3. In the Learning rate multiplier field, enter the step size at each iteration. The default value is 1. .
5. Optional: To disable intermediate checkpoints and use only the latest checkpoint, click the Export last checkpoint only toggle.
6. Click Continue.
The Tuning dataset page opens.
7. To upload a dataset file, select one of the following:
1. If you haven't uploaded a dataset yet, select the radio button for Upload file to Cloud Storage.
1. In the Select JSONL file field, click Browse and select your dataset file.
2. In the Dataset location field, click Browse and select the Cloud Storage bucket where you want to store your dataset file.
2. If your dataset file is already in a Cloud Storage bucket, select the radio button for Existing file on Cloud Storage.
1. In Cloud Storage file path field, click Browse and select the Cloud Storage bucket where your dataset file is located.
8. (Optional) To get validation metrics during training, click the Enable model validation toggle.
1. In the Validation dataset file, enter the Cloud Storage path of your validation dataset.
9. Click Start Tuning.
Your new model appears under the Tuned Models section on the Tune and Distill page. When the model is finished tuning, the Status says Succeeded. Install the Google Gen AI SDK: pip install --upgrade google-genai
To learn more, see the SDK reference documentation.
Set environment variables to use the Google Gen AI SDK with Gemini Enterprise Agent Platform: # Replace the `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` values # with appropriate values for your project. export GOOGLE_CLOUD_PROJECT=GOOGLE_CLOUD_PROJECT export GOOGLE_CLOUD_LOCATION=us-central1 export GOOGLE_GENAI_USE_ENTERPRISE=True
Create the tuning job: To create a model tuning job, send a POST request by using the tuningJobs.create method. Some of the parameters are not supported by all of the models. Ensure that you include only the applicable parameters for the model that you're tuning.
Before using any of the request data, make the following replacements:
PROJECT_ID: Your project ID.

---

## Page 3

TUNING_JOB_REGION: The region where the tuning job runs. This is also the default region for where the tuned model is uploaded.
BASE_MODEL: Name of the foundation model to tune.
TRAINING_DATASET_URI: Cloud Storage URI of your training dataset. The dataset must be formatted as a JSONL file. For best results, provide at least 100 to 500 examples. For more information, see About supervised tuning datasets .
VALIDATION_DATASET_URIOptional: The Cloud Storage URI of your validation dataset file.
EPOCH_COUNTOptional: The number of complete passes the model makes over the entire training dataset during training. Leave it unset to use the pre-populated recommended value.
ADAPTER_SIZEOptional: The Adapter size to use for the tuning job. The adapter size influences the number of trainable parameters for the tuning job. A larger adapter size implies that the model can learn more complex tasks, but it requires a larger training dataset and longer training times.
LEARNING_RATE_MULTIPLIER: Optional: A multiplier to apply to the recommended learning rate. Leave it unset to use the recommended value.
EXPORT_LAST_CHECKPOINT_ONLYOptional: Set to true to use only the latest checkpoint.
METRIC_SPECOptional: One or more metric specs you are using to run an evaluation using the Gen AI evaluation service. You can use the following metric specs: "pointwise_metric_spec", "pairwise_metric_spec", "exact_match_spec", "bleu_spec", and "rouge_spec".
METRIC_SPEC_FIELD_NAMEOptional: The required fields for your chosen metric spec. For example, "metric_prompt_template"
METRIC_SPEC_FIELD_NAME_CONTENTOptional: The field content for your chosen metric spec. For example, you can use the following field content for a pointwise evaluation: "Evaluate the fluency of this sentence: {response}. Give score from 0 to 1. 0 -not fluent at all. 1 - very fluent."
CLOUD_STORAGE_BUCKETOptional: The Cloud Storage bucket to store the results of an evaluation run by the Gen AI evaluation service.
TUNED_MODEL_DISPLAYNAMEOptional: A display name for the tuned model. If not set, a random name is generated.
KMS_KEY_NAMEOptional: The Cloud KMS resource identifier of the customer-managed encryption key used to protect a resource. The key has the format: projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key. The key needs to be in the same region as where the compute resource is created. For more information, see Customer-managed encryption keys (CMEK).
SERVICE_ACCOUNTOptional: The service account that the tuningJob workload runs as. If not specified, the Agent Platform Secure Fine-Tuning Service Agent in the project is used. See Tuning Service Agent. If you plan to use a customer-managed Service Account, you must grant the roles/aiplatform.tuningServiceAgent role to the service account. Also grant the Tuning Service Agent roles/iam.serviceAccountTokenCreator role to the customer-managed Service Account.
HTTP method and URL:
POST https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuning
Request JSON body:
{ "baseModel": "BASE_MODEL", "supervisedTuningSpec" : { "trainingDatasetUri": "TRAINING_DATASET_URI", "validationDatasetUri": "VALIDATION_DATASET_URI", "hyperParameters": { "epochCount": "EPOCH_COUNT", "adapterSize": "ADAPTER_SIZE", "learningRateMultiplier": "LEARNING_RATE_MULTIPLIER" }, "exportLastCheckpointOnly": EXPORT_LAST_CHECKPOINT_ONLY, "evaluationConfig": { "metrics": [ { "aggregation_metrics": ["AVERAGE", "STANDARD_DEVIATION"], "METRIC_SPEC": { "METRIC_SPEC_FIELD_NAME": METRIC_SPEC_FIELD_CONTENT } },

---

## Page 4

], "outputConfig": { "gcs_destination": { "output_uri_prefix": "CLOUD_STORAGE_BUCKET" } },
},
}, "tunedModelDisplayName": "TUNED_MODEL_DISPLAYNAME", "encryptionSpec": { "kmsKeyName": "KMS_KEY_NAME" }, "serviceAccount": "SERVICE_ACCOUNT"
}
To send your request, choose one of these options: Save the request body in a file named request.json, and execute the following command:
curl -X POST \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ -H "Content-Type: application/json; charset=utf-8" \ -d @request.json \ "https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tunin Save the request body in a file named request.json, and execute the following command:
$cred = gcloud auth print-access-token $headers = @{ "Authorization" = "Bearer $cred" } Invoke-WebRequest ` -Method POST ` -Headers $headers ` -ContentType: "application/json; charset=utf-8" ` -InFile request.json ` -Uri "https:// TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJobs" | Selec
You should receive a JSON response similar to the following.
### Response
{ "name": "projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJobs/TUNING_JOB_ID", "createTime": CREATE_TIME, "updateTime": UPDATE_TIME, "status": "STATUS", "supervisedTuningSpec": { "trainingDatasetUri": "TRAINING_DATASET_URI", "validationDatasetUri": "VALIDATION_DATASET_URI", "hyperParameters": { "epochCount": EPOCH_COUNT, "adapterSize": "ADAPTER_SIZE", "learningRateMultiplier": LEARNING_RATE_MULTIPLIER }, }, "tunedModelDisplayName": "TUNED_MODEL_DISPLAYNAME", "encryptionSpec": { "kmsKeyName": "KMS_KEY_NAME" }, "serviceAccount": "SERVICE_ACCOUNT" }
### Example curl command
PROJECT_ID=myproject LOCATION=global

---

## Page 5

curl \ -X POST \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ -H "Content-Type: application/json; charset=utf-8" \ "https://${LOCATION}-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/${LOCATION}/tuningJobs" \ -d \ $'{ "baseModel": "gemini-3.5-flash", "supervisedTuningSpec" : { "training_dataset_uri": "gs://YOUR_BUCKET_NAME/YOUR_TRAIN_DATASET", "validation_dataset_uri": "gs://YOUR_BUCKET_NAME/YOUR_VALIDATION_DATASET" }, "tunedModelDisplayName": "tuned_gemini" }' You can create a model tuning job in Agent Platform by using the side panel in Colab Enterprise. The side panel adds the relevant code snippets to your notebook. Then, you modify the code snippets and run them to create your tuning job. To learn more about using the side panel with your Agent Platform tuning jobs, see Interact with Agent Platform to tune a model.
1. In the Google Cloud console, go to the Colab Enterprise My notebooks page.
Go to My notebooks
2. In the Region menu, select the region that contains your notebook.
3. Click the notebook that you want to open. If you haven't created a notebook yet, create a notebook.
4. To the right of your notebook, in the side panel, click the Tuning button.
The side panel expands the Tuning tab.
5. Click the Tune a Gemini model button.
Colab Enterprise adds code cells to your notebook for tuning a Gemini model.
6. In your notebook, find the code cell that stores parameter values. You'll use these parameters to interact with Agent Platform.
7. Update the values for the following parameters:
PROJECT_ID: The ID of the project that your notebook is in.
REGION: The region that your notebook is in.
TUNED_MODEL_DISPLAY_NAME: The name of your tuned model.
8. In the next code cell, update the model tuning parameters:
source_model: The Gemini model that you want to use, for example, gemini-2.0-flash-001.
train_dataset: The URL of your training dataset.
validation_dataset: The URL of your validation dataset.
Adjust the remaining parameters as needed.
9. Run the code cells that the side panel added to your notebook.
10. After the last code cell runs, click the View tuning job button that appears.
11. The side panel shows information about your model tuning job.
The Monitor tab shows tuning metrics when the metrics are ready.
The Dataset tab shows a summary and metrics about your dataset after the dataset has been processed.
The Details tab shows information about your tuning job, such as the tuning method and the base model (source model) that you used.
12. After the tuning job has completed, you can go directly from the Tuning details tab to a page where you can test your model. Click Test.
The Google Cloud console opens to the Agent Platform Text chat page, where you can test your model.
### Tuning hyperparameters
It's recommended to submit your first tuning job without changing the hyperparameters. The default value is the recommended value based on our benchmarking results to yield the best model output quality.

---

## Page 6

Epochs: The number of complete passes the model makes over the entire training dataset during training. Gemini Enterprise Agent Platform automatically adjusts the default value to your training dataset size. This value is based on benchmarking results to optimize model output quality.
Adapter size: The Adapter size to use for the tuning job. The adapter size influences the number of trainable parameters for the tuning job. A larger adapter size implies that the model can learn more complex tasks, but it requires a larger training dataset and longer training times.
Learning Rate Multiplier: A multiplier to apply to the recommended learning rate. You can increase the value to converge faster, or decrease the value to avoid overfitting.
For a discussion of best practices for supervised fine-tuning, see the blog post Supervised Fine Tuning for Gemini: A best practices guide.
### View a list of tuning jobs
You can view a list of tuning jobs in your current project by using the Google Cloud console, the Google Gen AI SDK, or by sending a GET request by using the tuningJobs method.
To view your tuning jobs in the Google Cloud console, go to the Agent Platform Studio page.
Go to Agent Platform Studio
Your Gemini tuning jobs are listed in the table under the Tuned Models section. To view a list of model tuning jobs, send a GET request by using the tuningJobs.list method.
Before using any of the request data, make the following replacements:
PROJECT_ID: Your project ID.
TUNING_JOB_REGION: The region where the tuning job runs. This is also the default region for where the tuned model is uploaded.
HTTP method and URL:
GET https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJ
To send your request, choose one of these options: Execute the following command:
curl -X GET \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tunin Execute the following command:
$cred = gcloud auth print-access-token $headers = @{ "Authorization" = "Bearer $cred" } Invoke-WebRequest ` -Method GET ` -Headers $headers ` -Uri "https:// TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJobs" | Selec
You should receive a JSON response similar to the following.
### Response
{ "tuning_jobs": [ TUNING_JOB_1, TUNING_JOB_2, ... ] }
### Get details of a tuning job
You can get the details of a tuning job in your current project by using the Google Cloud console, the Google Gen AI SDK, or by sending a GET request by using the tuningJobs method.
1. To view details of a tuned model in the Google Cloud console, go to the Agent Platform Studio page.

---

## Page 7

Go to Agent Platform Studio
2. In the Tuned Models table, find your model and click Details.
The details of your model are shown. To view a list of model tuning jobs, send a GET request by using the tuningJobs.get method and specify the TuningJob_ID.
Before using any of the request data, make the following replacements:
PROJECT_ID: Your project ID.
TUNING_JOB_REGION: The region where the tuning job runs. This is also the default region for where the tuned model is uploaded.
TUNING_JOB_ID: The ID of the tuning job.
HTTP method and URL:
GET https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJ
To send your request, choose one of these options: Execute the following command:
curl -X GET \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tunin Execute the following command:
$cred = gcloud auth print-access-token $headers = @{ "Authorization" = "Bearer $cred" } Invoke-WebRequest ` -Method GET ` -Headers $headers ` -Uri "https:// TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJobs/TUNING_J
You should receive a JSON response similar to the following.
### Response
{ "name": "projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJobs/TUNING_JOB_ID", "tunedModelDisplayName": "TUNED_MODEL_DISPLAYNAME", "createTime": CREATE_TIME, "endTime": END_TIME, "tunedModel": { "model": "projects/PROJECT_ID/locations/TUNING_JOB_REGION/models/MODEL_ID", "endpoint": "projects/PROJECT_ID/locations/TUNING_JOB_REGION/endpoints/ENDPOINT_ID" }, "experiment": "projects/PROJECT_ID/locations/TUNING_JOB_REGION/metadataStores/default/contexts/EXPERIMENT_ID", "tuning_data_statistics": { "supervisedTuningDataStats": { "tuninDatasetExampleCount": "TUNING_DATASET_EXAMPLE_COUNT", "totalBillableTokenCount": "TOTAL_BILLABLE_TOKEN_COUNT", "tuningStepCount": "TUNING_STEP_COUNT" } }, "status": "STATUS", "supervisedTuningSpec" : { "trainingDatasetUri": "TRAINING_DATASET_URI", "validationDataset_uri": "VALIDATION_DATASET_URI", "hyperParameters": { "epochCount": EPOCH_COUNT, "learningRateMultiplier": LEARNING_RATE_MULTIPLIER }

---

## Page 8

}
}
### Cancel a tuning job
You can cancel a tuning job in your current project by using the Google Cloud console, the Google Gen AI SDK, or by sending a POST request using the tuningJobs method.
1. To cancel a tuning job in the Google Cloud console, go to the Agent Platform Studio page.
Go to Agent Platform Studio
2. In the Tuned Models table, click Manage run.
3. Click Cancel. To cancel a model tuning job, send a POST request by using the tuningJobs.cancel method and specify the TuningJob_ID.
Before using any of the request data, make the following replacements:
PROJECT_ID: Your project ID.
TUNING_JOB_REGION: The region where the tuning job runs. This is also the default region for where the tuned model is uploaded.
TUNING_JOB_ID: The ID of the tuning job.
HTTP method and URL:
POST https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuning
To send your request, choose one of these options: Execute the following command:
curl -X POST \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ -H "Content-Type: application/json; charset=utf-8" \ -d "" \ "https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tunin Execute the following command:
$cred = gcloud auth print-access-token $headers = @{ "Authorization" = "Bearer $cred" } Invoke-WebRequest ` -Method POST ` -Headers $headers ` -Uri "https:// TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJobs/TUNING_J
You should receive a JSON response similar to the following.
### Response
{}
### Evaluate the tuned model
If you didn't configure the Gen AI evaluation service to run automatically after the tuning job, you can interact with the tuned model endpoint the same way as base Gemini by using the Google Gen AI SDK, or by sending a POST request using the generateContent method.
For thinking models, we recommend to turn off thinking or set the thinking budget to the minimum on tuned tasks for optimal performance and cost efficiency. During supervised fine-tuning, the model learns to mimic the ground truth in tuning dataset, omitting the thinking process. Therefore, tuned model is able to handle the task without thinking budget effectively.
The following example prompts a model with the question "Why is sky blue?".
1. To view details of a tuned model in the Google Cloud console, go to the Agent Platform Studio page.
Go to Agent Platform Studio

---

## Page 9

2. In the Tuned Models table, select Test.
A page where you can create a conversation with your tuned model is displayed. To test a tuned model with a prompt, send a POST request and specify the `MREP_LOCATION` and `ENDPOINT_ID`. Before using any of the request data, make the following replacements:
MREP_LOCATION: The Google Cloud multi-region endpoint location that the tuning job runs in. The following are accepted values:
us
eu
PROJECT_ID: Your project ID.
ENDPOINT_ID: The tuned model endpoint ID from the GET API.
TEMPERATURE: The temperature is used for sampling during response generation, which occurs when topP and topK are applied. Temperature controls the degree of randomness in token selection. Lower temperatures are good for prompts that require a less open-ended or creative response, while higher temperatures can lead to more diverse or creative results. A temperature of 0 means that the highest probability tokens are always selected. In this case, responses for a given prompt are mostly deterministic, but a small amount of variation is still possible.
If the model returns a response that's too generic, too short, or the model gives a fallback response, try increasing the temperature. If the model enters infinite generation, increasing the temperature to at least 0.1 may lead to improved results. 1.0 is the recommended starting value for temperature.
TOP_P: Top-P changes how the model selects tokens for output. Tokens are selected from the most probable to least probable until the sum of their probabilities equals the top-P value. For example, if tokens A, B, and C have a probability of 0.3, 0.2, and 0.1 and the top-P value is 0.5, then the model will select either A or B as the next token by using temperature and excludes C as a candidate.
Specify a lower value for less random responses and a higher value for more random responses.
TOP_K: Top-K changes how the model selects tokens for output. A top-K of 1 means the next selected token is the most probable among all tokens in the model's vocabulary (also called greedy decoding), while a top-K of 3 means that the next token is selected from among the three most probable tokens by using temperature.
For each token selection step, the top-K tokens with the highest probabilities are sampled. Then tokens are further filtered based on top-P with the final token selected using temperature sampling.
Specify a lower value for less random responses and a higher value for more random responses.
MAX_OUTPUT_TOKENS: Maximum number of tokens that can be generated in the response. A token is approximately four characters. 100 tokens correspond to roughly 60-80 words.
Specify a lower value for shorter responses and a higher value for potentially longer responses.
HTTP method and URL:
POST https://aiplatform.MREP_LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/MREP_LOCATION/endpoints/
Request JSON body:
{ "contents": [ { "role": "USER", "parts": { "text" : "Why is sky blue?" } } ], "generation_config": { "temperature":TEMPERATURE, "topP": TOP_P, "topK": TOP_K, "maxOutputTokens": MAX_OUTPUT_TOKENS } }

---

## Page 10

To send your request, choose one of these options: Save the request body in a file named request.json, and execute the following command:
curl -X POST \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ -H "Content-Type: application/json; charset=utf-8" \ -d @request.json \ "https://aiplatform.MREP_LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/MREP_LOCATION/endpoints Save the request body in a file named request.json, and execute the following command:
$cred = gcloud auth print-access-token $headers = @{ "Authorization" = "Bearer $cred" } Invoke-WebRequest ` -Method POST ` -Headers $headers ` -ContentType: "application/json; charset=utf-8" ` -InFile request.json ` -Uri "https://aiplatform. MREP_LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/MREP_LOCATION/endpoints/ENDPOINT_ID:generateCont
You should receive a JSON response similar to the following.
### Response
{ "candidates": [ { "content": { "role": "model", "parts": [ { "text": "The sky appears blue due to a phenomenon called Rayleigh scattering, where shorter blue wavelengths of sunlight are scattered more strongly by the Earth's atmosphere than longer red wavelengths." } ] }, "finishReason": "STOP", "safetyRatings": [ { "category": "HARM_CATEGORY_HATE_SPEECH", "probability": "NEGLIGIBLE", "probabilityScore": 0.06325052, "severity": "HARM_SEVERITY_NEGLIGIBLE", "severityScore": 0.03179867 }, { "category": "HARM_CATEGORY_DANGEROUS_CONTENT", "probability": "NEGLIGIBLE", "probabilityScore": 0.09334688, "severity": "HARM_SEVERITY_NEGLIGIBLE", "severityScore": 0.027742893 }, { "category": "HARM_CATEGORY_HARASSMENT", "probability": "NEGLIGIBLE", "probabilityScore": 0.17356819, "severity": "HARM_SEVERITY_NEGLIGIBLE", "severityScore": 0.025419652 }, { "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",

---

## Page 11

"probability": "NEGLIGIBLE", "probabilityScore": 0.07864238, "severity": "HARM_SEVERITY_NEGLIGIBLE", "severityScore": 0.020332353
} ]
} ], "usageMetadata": { "promptTokenCount": 5, "candidatesTokenCount": 33, "totalTokenCount": 38 }
} To test a tuned model with a prompt, send a POST request and specify the `TUNED_ENDPOINT_ID`. Before using any of the request data, make the following replacements:
PROJECT_ID: Your project ID.
TUNING_JOB_REGION: The region where the tuning job runs. This is also the default region for where the tuned model is uploaded.
ENDPOINT_ID: The tuned model endpoint ID from the GET API.
TEMPERATURE: The temperature is used for sampling during response generation, which occurs when topP and topK are applied. Temperature controls the degree of randomness in token selection. Lower temperatures are good for prompts that require a less open-ended or creative response, while higher temperatures can lead to more diverse or creative results. A temperature of 0 means that the highest probability tokens are always selected. In this case, responses for a given prompt are mostly deterministic, but a small amount of variation is still possible.
If the model returns a response that's too generic, too short, or the model gives a fallback response, try increasing the temperature. If the model enters infinite generation, increasing the temperature to at least 0.1 may lead to improved results. 1.0 is the recommended starting value for temperature.
TOP_P: Top-P changes how the model selects tokens for output. Tokens are selected from the most probable to least probable until the sum of their probabilities equals the top-P value. For example, if tokens A, B, and C have a probability of 0.3, 0.2, and 0.1 and the top-P value is 0.5, then the model will select either A or B as the next token by using temperature and excludes C as a candidate.
Specify a lower value for less random responses and a higher value for more random responses.
TOP_K: Top-K changes how the model selects tokens for output. A top-K of 1 means the next selected token is the most probable among all tokens in the model's vocabulary (also called greedy decoding), while a top-K of 3 means that the next token is selected from among the three most probable tokens by using temperature.
For each token selection step, the top-K tokens with the highest probabilities are sampled. Then tokens are further filtered based on top-P with the final token selected using temperature sampling.
Specify a lower value for less random responses and a higher value for more random responses.
MAX_OUTPUT_TOKENS: Maximum number of tokens that can be generated in the response. A token is approximately four characters. 100 tokens correspond to roughly 60-80 words.
Specify a lower value for shorter responses and a higher value for potentially longer responses.
HTTP method and URL:
POST https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/endpoi
Request JSON body:
{ "contents": [ { "role": "USER", "parts": { "text" : "Why is sky blue?" } }

---

## Page 12

], "generation_config": { "temperature":TEMPERATURE, "topP": TOP_P, "topK": TOP_K, "maxOutputTokens": MAX_OUTPUT_TOKENS }
}
To send your request, choose one of these options: Save the request body in a file named request.json, and execute the following command:
curl -X POST \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ -H "Content-Type: application/json; charset=utf-8" \ -d @request.json \ "https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/endpo Save the request body in a file named request.json, and execute the following command:
$cred = gcloud auth print-access-token $headers = @{ "Authorization" = "Bearer $cred" } Invoke-WebRequest ` -Method POST ` -Headers $headers ` -ContentType: "application/json; charset=utf-8" ` -InFile request.json ` -Uri "https:// TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/endpoints/ENDPOINT_
You should receive a JSON response similar to the following.
### Response
{ "candidates": [ { "content": { "role": "model", "parts": [ { "text": "The sky appears blue due to a phenomenon called Rayleigh scattering, where shorter blue wavelengths of sunlight are scattered more strongly by the Earth's atmosphere than longer red wavelengths." } ] }, "finishReason": "STOP", "safetyRatings": [ { "category": "HARM_CATEGORY_HATE_SPEECH", "probability": "NEGLIGIBLE", "probabilityScore": 0.06325052, "severity": "HARM_SEVERITY_NEGLIGIBLE", "severityScore": 0.03179867 }, { "category": "HARM_CATEGORY_DANGEROUS_CONTENT", "probability": "NEGLIGIBLE", "probabilityScore": 0.09334688, "severity": "HARM_SEVERITY_NEGLIGIBLE", "severityScore": 0.027742893 },

---

## Page 13

{
"category": "HARM_CATEGORY_HARASSMENT", "probability": "NEGLIGIBLE", "probabilityScore": 0.17356819, "severity": "HARM_SEVERITY_NEGLIGIBLE", "severityScore": 0.025419652
}, {
"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "probability": "NEGLIGIBLE", "probabilityScore": 0.07864238, "severity": "HARM_SEVERITY_NEGLIGIBLE", "severityScore": 0.020332353
} ]
} ], "usageMetadata": { "promptTokenCount": 5, "candidatesTokenCount": 33, "totalTokenCount": 38 }
}
### Delete a tuned model
To delete a tuned model:
Call the models.delete method.
Before using any of the request data, make the following replacements:
PROJECT_ID: Your project ID.
REGION: The region where the tuned model is located.
MODEL_ID: The model to delete.
HTTP method and URL:
DELETE https://REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/models/MODEL_ID
To send your request, choose one of these options: Execute the following command:
curl -X DELETE \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/models/MODEL_ID" Execute the following command:
$cred = gcloud auth print-access-token $headers = @{ "Authorization" = "Bearer $cred" } Invoke-WebRequest ` -Method DELETE ` -Headers $headers ` -Uri "https:// REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/models/MODEL_ID" | Select-Object -Ex
You should receive a successful status code (2xx) and an empty response.
### Tuning and validation metrics

---

## Page 14

You can configure a model tuning job to collect and report model tuning and model evaluation metrics, which can then be visualized in Agent Platform Studio.
1. To view details of a tuned model in the Google Cloud console, go to the Agent Platform Studio page.
Go to Agent Platform Studio
2. In the Tune and Distill table, click the name of the tuned model that you want to view metrics for.
The tuning metrics appear under the Monitor tab.
## Model tuning metrics
The model tuning job automatically collects the following tuning metrics for the model:
/train_total_loss: Loss for the tuning dataset at a training step.
/train_fraction_of_correct_next_step_preds: The token accuracy at a training step. A single inference consists of a sequence of predicted tokens. This metric measures the accuracy of the predicted tokens when compared to the ground truth in the tuning dataset.
/train_num_predictions: Number of predicted tokens at a training step.
## Model validation metrics
You can configure a model tuning job to collect the following validation metrics for the model:
/eval_total_loss: Loss for the validation dataset at a validation step.
/eval_fraction_of_correct_next_step_preds: The token accuracy at an validation step. A single inference consists of a sequence of predicted tokens. This metric measures the accuracy of the predicted tokens when compared to the ground truth in the validation dataset.
/eval_num_predictions: Number of predicted tokens at a validation step.
The metrics visualizations are available after the tuning job starts running. It will be updated in real time as tuning progresses. If you don't specify a validation dataset when you create the tuning job, only the visualizations for the tuning metrics are available.
## What's next
Learn about deploying a tuned Gemini model.
To learn how supervised fine-tuning can be used in a solution that builds a generative AI knowledge base, see Jump Start Solution: Generative AI knowledge base. Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-10-01 UTC.
Skip to main content
## Tune Gemini models with supervised fine-tuning Stay organized with collections Save and categorize content based on
## your preferences.
On this page
Before you begin
Supported models
Create a tuning job
Tuning hyperparameters
View a list of tuning jobs
Get details of a tuning job
Cancel a tuning job
Evaluate the tuned model
Delete a tuned model

---

## Page 15

Tuning and validation metrics
Model tuning metrics
Model validation metrics
What's next
This document describes how to tune a Gemini model by using supervised fine-tuning.
### Before you begin
Before you begin, you must prepare a supervised fine-tuning dataset. Depending on your use case, there are different requirements for preparing a dataset:
Text tuning
Image tuning
Document tuning
Audio tuning
Video tuning
Tune function calling
### Supported models
The following Gemini models support supervised tuning:
### Click to expand supported models
Gemini 3.5 Flash
Gemini 3.1 Flash-Lite
Gemini 2.5 Pro
Gemini 2.5 Flash-Lite
Gemini 2.5 Flash
### Create a tuning job
You can create a supervised fine-tuning job by using the Google Cloud console, the Google Gen AI SDK, the REST API, or Colab Enterprise.
Optional: (Preview) Include the evaluationConfig to automatically run an evaluation using the Gen AI evaluation service after the tuning job completes. This evaluation configuration is available in the us-central1 region.
To tune a text model with supervised fine-tuning by using the Google Cloud console, perform the following steps:
1. In the Gemini Enterprise Agent Platform section of the Google Cloud console, go to the Agent Platform Studio page.
Go to Agent Platform Studio
2. Click Create tuned model.
3. Under Model details, configure the following:
1. In the Tuned model name field, enter a name for your new tuned model, up to 128 characters.
2. In the Base model field, select the foundation model to tune.
3. In the Region drop-down field, select the region where the pipeline tuning job runs and where the tuned model is deployed.
4. Under Tuning setting, configure the following:
1. In the Number of epochs field, enter the number of steps to run for model tuning.
2. In the Adapter Size field, enter the adapter size to use for model tuning.
3. In the Learning rate multiplier field, enter the step size at each iteration. The default value is 1. .

---

## Page 16

5. Optional: To disable intermediate checkpoints and use only the latest checkpoint, click the Export last checkpoint only toggle.
6. Click Continue.
The Tuning dataset page opens.
7. To upload a dataset file, select one of the following:
1. If you haven't uploaded a dataset yet, select the radio button for Upload file to Cloud Storage.
1. In the Select JSONL file field, click Browse and select your dataset file.
2. In the Dataset location field, click Browse and select the Cloud Storage bucket where you want to store your dataset file.
2. If your dataset file is already in a Cloud Storage bucket, select the radio button for Existing file on Cloud Storage.
1. In Cloud Storage file path field, click Browse and select the Cloud Storage bucket where your dataset file is located.
8. (Optional) To get validation metrics during training, click the Enable model validation toggle.
1. In the Validation dataset file, enter the Cloud Storage path of your validation dataset.
9. Click Start Tuning.
Your new model appears under the Tuned Models section on the Tune and Distill page. When the model is finished tuning, the Status says Succeeded. Install the Google Gen AI SDK: pip install --upgrade google-genai
To learn more, see the SDK reference documentation.
Set environment variables to use the Google Gen AI SDK with Gemini Enterprise Agent Platform: # Replace the `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` values # with appropriate values for your project. export GOOGLE_CLOUD_PROJECT=GOOGLE_CLOUD_PROJECT export GOOGLE_CLOUD_LOCATION=us-central1 export GOOGLE_GENAI_USE_ENTERPRISE=True
Create the tuning job: To create a model tuning job, send a POST request by using the tuningJobs.create method. Some of the parameters are not supported by all of the models. Ensure that you include only the applicable parameters for the model that you're tuning.
Before using any of the request data, make the following replacements:
PROJECT_ID: Your project ID.
TUNING_JOB_REGION: The region where the tuning job runs. This is also the default region for where the tuned model is uploaded.
BASE_MODEL: Name of the foundation model to tune.
TRAINING_DATASET_URI: Cloud Storage URI of your training dataset. The dataset must be formatted as a JSONL file. For best results, provide at least 100 to 500 examples. For more information, see About supervised tuning datasets .
VALIDATION_DATASET_URIOptional: The Cloud Storage URI of your validation dataset file.
EPOCH_COUNTOptional: The number of complete passes the model makes over the entire training dataset during training. Leave it unset to use the pre-populated recommended value.
ADAPTER_SIZEOptional: The Adapter size to use for the tuning job. The adapter size influences the number of trainable parameters for the tuning job. A larger adapter size implies that the model can learn more complex tasks, but it requires a larger training dataset and longer training times.
LEARNING_RATE_MULTIPLIER: Optional: A multiplier to apply to the recommended learning rate. Leave it unset to use the recommended value.
EXPORT_LAST_CHECKPOINT_ONLYOptional: Set to true to use only the latest checkpoint.
METRIC_SPECOptional: One or more metric specs you are using to run an evaluation using the Gen AI evaluation service. You can use the following metric specs: "pointwise_metric_spec", "pairwise_metric_spec", "exact_match_spec", "bleu_spec", and "rouge_spec".
METRIC_SPEC_FIELD_NAMEOptional: The required fields for your chosen metric spec. For example, "metric_prompt_template"

---

## Page 17

METRIC_SPEC_FIELD_NAME_CONTENTOptional: The field content for your chosen metric spec. For example, you can use the following field content for a pointwise evaluation: "Evaluate the fluency of this sentence: {response}. Give score from 0 to 1. 0 -not fluent at all. 1 - very fluent."
CLOUD_STORAGE_BUCKETOptional: The Cloud Storage bucket to store the results of an evaluation run by the Gen AI evaluation service.
TUNED_MODEL_DISPLAYNAMEOptional: A display name for the tuned model. If not set, a random name is generated.
KMS_KEY_NAMEOptional: The Cloud KMS resource identifier of the customer-managed encryption key used to protect a resource. The key has the format: projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key. The key needs to be in the same region as where the compute resource is created. For more information, see Customer-managed encryption keys (CMEK).
SERVICE_ACCOUNTOptional: The service account that the tuningJob workload runs as. If not specified, the Agent Platform Secure Fine-Tuning Service Agent in the project is used. See Tuning Service Agent. If you plan to use a customer-managed Service Account, you must grant the roles/aiplatform.tuningServiceAgent role to the service account. Also grant the Tuning Service Agent roles/iam.serviceAccountTokenCreator role to the customer-managed Service Account.
HTTP method and URL:
POST https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuning
Request JSON body:
{ "baseModel": "BASE_MODEL", "supervisedTuningSpec" : { "trainingDatasetUri": "TRAINING_DATASET_URI", "validationDatasetUri": "VALIDATION_DATASET_URI", "hyperParameters": { "epochCount": "EPOCH_COUNT", "adapterSize": "ADAPTER_SIZE", "learningRateMultiplier": "LEARNING_RATE_MULTIPLIER" }, "exportLastCheckpointOnly": EXPORT_LAST_CHECKPOINT_ONLY, "evaluationConfig": { "metrics": [ { "aggregation_metrics": ["AVERAGE", "STANDARD_DEVIATION"], "METRIC_SPEC": { "METRIC_SPEC_FIELD_NAME": METRIC_SPEC_FIELD_CONTENT } }, ], "outputConfig": { "gcs_destination": { "output_uri_prefix": "CLOUD_STORAGE_BUCKET" } }, }, }, "tunedModelDisplayName": "TUNED_MODEL_DISPLAYNAME", "encryptionSpec": { "kmsKeyName": "KMS_KEY_NAME" }, "serviceAccount": "SERVICE_ACCOUNT" }
To send your request, choose one of these options: Save the request body in a file named request.json, and execute the following command:
curl -X POST \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \

---

## Page 18

-H "Content-Type: application/json; charset=utf-8" \ -d @request.json \ "https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tunin Save the request body in a file named request.json, and execute the following command:
$cred = gcloud auth print-access-token $headers = @{ "Authorization" = "Bearer $cred" } Invoke-WebRequest ` -Method POST ` -Headers $headers ` -ContentType: "application/json; charset=utf-8" ` -InFile request.json ` -Uri "https:// TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJobs" | Selec
You should receive a JSON response similar to the following.
### Response
{ "name": "projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJobs/TUNING_JOB_ID", "createTime": CREATE_TIME, "updateTime": UPDATE_TIME, "status": "STATUS", "supervisedTuningSpec": { "trainingDatasetUri": "TRAINING_DATASET_URI", "validationDatasetUri": "VALIDATION_DATASET_URI", "hyperParameters": { "epochCount": EPOCH_COUNT, "adapterSize": "ADAPTER_SIZE", "learningRateMultiplier": LEARNING_RATE_MULTIPLIER }, }, "tunedModelDisplayName": "TUNED_MODEL_DISPLAYNAME", "encryptionSpec": { "kmsKeyName": "KMS_KEY_NAME" }, "serviceAccount": "SERVICE_ACCOUNT" }
### Example curl command
PROJECT_ID=myproject LOCATION=global curl \ -X POST \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ -H "Content-Type: application/json; charset=utf-8" \ "https://${LOCATION}-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/${LOCATION}/tuningJobs" \ -d \ $'{ "baseModel": "gemini-3.5-flash", "supervisedTuningSpec" : { "training_dataset_uri": "gs://YOUR_BUCKET_NAME/YOUR_TRAIN_DATASET", "validation_dataset_uri": "gs://YOUR_BUCKET_NAME/YOUR_VALIDATION_DATASET" }, "tunedModelDisplayName": "tuned_gemini" }' You can create a model tuning job in Agent Platform by using the side panel in Colab Enterprise. The side panel adds the relevant code snippets to your notebook. Then, you modify the code snippets and run them to create your tuning job. To learn more about using the side panel with your Agent Platform tuning jobs, see Interact with Agent Platform to tune a model.
1. In the Google Cloud console, go to the Colab Enterprise My notebooks page.

---

## Page 19

Go to My notebooks
2. In the Region menu, select the region that contains your notebook.
3. Click the notebook that you want to open. If you haven't created a notebook yet, create a notebook.
4. To the right of your notebook, in the side panel, click the Tuning button.
The side panel expands the Tuning tab.
5. Click the Tune a Gemini model button.
Colab Enterprise adds code cells to your notebook for tuning a Gemini model.
6. In your notebook, find the code cell that stores parameter values. You'll use these parameters to interact with Agent Platform.
7. Update the values for the following parameters:
PROJECT_ID: The ID of the project that your notebook is in.
REGION: The region that your notebook is in.
TUNED_MODEL_DISPLAY_NAME: The name of your tuned model.
8. In the next code cell, update the model tuning parameters:
source_model: The Gemini model that you want to use, for example, gemini-2.0-flash-001.
train_dataset: The URL of your training dataset.
validation_dataset: The URL of your validation dataset.
Adjust the remaining parameters as needed.
9. Run the code cells that the side panel added to your notebook.
10. After the last code cell runs, click the View tuning job button that appears.
11. The side panel shows information about your model tuning job.
The Monitor tab shows tuning metrics when the metrics are ready.
The Dataset tab shows a summary and metrics about your dataset after the dataset has been processed.
The Details tab shows information about your tuning job, such as the tuning method and the base model (source model) that you used.
12. After the tuning job has completed, you can go directly from the Tuning details tab to a page where you can test your model. Click Test.
The Google Cloud console opens to the Agent Platform Text chat page, where you can test your model.
### Tuning hyperparameters
It's recommended to submit your first tuning job without changing the hyperparameters. The default value is the recommended value based on our benchmarking results to yield the best model output quality.
Epochs: The number of complete passes the model makes over the entire training dataset during training. Gemini Enterprise Agent Platform automatically adjusts the default value to your training dataset size. This value is based on benchmarking results to optimize model output quality.
Adapter size: The Adapter size to use for the tuning job. The adapter size influences the number of trainable parameters for the tuning job. A larger adapter size implies that the model can learn more complex tasks, but it requires a larger training dataset and longer training times.
Learning Rate Multiplier: A multiplier to apply to the recommended learning rate. You can increase the value to converge faster, or decrease the value to avoid overfitting.
For a discussion of best practices for supervised fine-tuning, see the blog post Supervised Fine Tuning for Gemini: A best practices guide.
### View a list of tuning jobs
You can view a list of tuning jobs in your current project by using the Google Cloud console, the Google Gen AI SDK, or by sending a GET request by using the tuningJobs method.
To view your tuning jobs in the Google Cloud console, go to the Agent Platform Studio page.
Go to Agent Platform Studio

---

## Page 20

Your Gemini tuning jobs are listed in the table under the Tuned Models section. To view a list of model tuning jobs, send a GET request by using the tuningJobs.list method.
Before using any of the request data, make the following replacements:
PROJECT_ID: Your project ID.
TUNING_JOB_REGION: The region where the tuning job runs. This is also the default region for where the tuned model is uploaded.
HTTP method and URL:
GET https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJ
To send your request, choose one of these options: Execute the following command:
curl -X GET \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tunin Execute the following command:
$cred = gcloud auth print-access-token $headers = @{ "Authorization" = "Bearer $cred" } Invoke-WebRequest ` -Method GET ` -Headers $headers ` -Uri "https:// TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJobs" | Selec
You should receive a JSON response similar to the following.
### Response
{ "tuning_jobs": [ TUNING_JOB_1, TUNING_JOB_2, ... ] }
### Get details of a tuning job
You can get the details of a tuning job in your current project by using the Google Cloud console, the Google Gen AI SDK, or by sending a GET request by using the tuningJobs method.
1. To view details of a tuned model in the Google Cloud console, go to the Agent Platform Studio page.
Go to Agent Platform Studio
2. In the Tuned Models table, find your model and click Details.
The details of your model are shown. To view a list of model tuning jobs, send a GET request by using the tuningJobs.get method and specify the TuningJob_ID.
Before using any of the request data, make the following replacements:
PROJECT_ID: Your project ID.
TUNING_JOB_REGION: The region where the tuning job runs. This is also the default region for where the tuned model is uploaded.
TUNING_JOB_ID: The ID of the tuning job.
HTTP method and URL:
GET https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJ
To send your request, choose one of these options:

---

## Page 21

Execute the following command:
curl -X GET \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tunin Execute the following command:
$cred = gcloud auth print-access-token $headers = @{ "Authorization" = "Bearer $cred" } Invoke-WebRequest ` -Method GET ` -Headers $headers ` -Uri "https:// TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJobs/TUNING_J
You should receive a JSON response similar to the following.
### Response
{ "name": "projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJobs/TUNING_JOB_ID", "tunedModelDisplayName": "TUNED_MODEL_DISPLAYNAME", "createTime": CREATE_TIME, "endTime": END_TIME, "tunedModel": { "model": "projects/PROJECT_ID/locations/TUNING_JOB_REGION/models/MODEL_ID", "endpoint": "projects/PROJECT_ID/locations/TUNING_JOB_REGION/endpoints/ENDPOINT_ID" }, "experiment": "projects/PROJECT_ID/locations/TUNING_JOB_REGION/metadataStores/default/contexts/EXPERIMENT_ID", "tuning_data_statistics": { "supervisedTuningDataStats": { "tuninDatasetExampleCount": "TUNING_DATASET_EXAMPLE_COUNT", "totalBillableTokenCount": "TOTAL_BILLABLE_TOKEN_COUNT", "tuningStepCount": "TUNING_STEP_COUNT" } }, "status": "STATUS", "supervisedTuningSpec" : { "trainingDatasetUri": "TRAINING_DATASET_URI", "validationDataset_uri": "VALIDATION_DATASET_URI", "hyperParameters": { "epochCount": EPOCH_COUNT, "learningRateMultiplier": LEARNING_RATE_MULTIPLIER } } }
### Cancel a tuning job
You can cancel a tuning job in your current project by using the Google Cloud console, the Google Gen AI SDK, or by sending a POST request using the tuningJobs method.
1. To cancel a tuning job in the Google Cloud console, go to the Agent Platform Studio page.
Go to Agent Platform Studio
2. In the Tuned Models table, click Manage run.
3. Click Cancel. To cancel a model tuning job, send a POST request by using the tuningJobs.cancel method and specify the TuningJob_ID.
Before using any of the request data, make the following replacements:
PROJECT_ID: Your project ID.

---

## Page 22

TUNING_JOB_REGION: The region where the tuning job runs. This is also the default region for where the tuned model is uploaded.
TUNING_JOB_ID: The ID of the tuning job.
HTTP method and URL:
POST https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuning
To send your request, choose one of these options: Execute the following command:
curl -X POST \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ -H "Content-Type: application/json; charset=utf-8" \ -d "" \ "https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tunin Execute the following command:
$cred = gcloud auth print-access-token $headers = @{ "Authorization" = "Bearer $cred" } Invoke-WebRequest ` -Method POST ` -Headers $headers ` -Uri "https:// TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJobs/TUNING_J
You should receive a JSON response similar to the following.
### Response
{}
### Evaluate the tuned model
If you didn't configure the Gen AI evaluation service to run automatically after the tuning job, you can interact with the tuned model endpoint the same way as base Gemini by using the Google Gen AI SDK, or by sending a POST request using the generateContent method.
For thinking models, we recommend to turn off thinking or set the thinking budget to the minimum on tuned tasks for optimal performance and cost efficiency. During supervised fine-tuning, the model learns to mimic the ground truth in tuning dataset, omitting the thinking process. Therefore, tuned model is able to handle the task without thinking budget effectively.
The following example prompts a model with the question "Why is sky blue?".
1. To view details of a tuned model in the Google Cloud console, go to the Agent Platform Studio page.
Go to Agent Platform Studio
2. In the Tuned Models table, select Test.
A page where you can create a conversation with your tuned model is displayed. To test a tuned model with a prompt, send a POST request and specify the `MREP_LOCATION` and `ENDPOINT_ID`. Before using any of the request data, make the following replacements:
MREP_LOCATION: The Google Cloud multi-region endpoint location that the tuning job runs in. The following are accepted values:
us
eu
PROJECT_ID: Your project ID.
ENDPOINT_ID: The tuned model endpoint ID from the GET API.
TEMPERATURE: The temperature is used for sampling during response generation, which occurs when topP and topK are applied. Temperature controls the degree of randomness in token selection. Lower temperatures are good for prompts that require a less open-ended or creative response, while higher temperatures can lead to more diverse or creative results. A temperature of 0 means that the highest probability tokens are always selected. In this case, responses for a given prompt are mostly deterministic, but a small amount of variation is still possible.

---

## Page 23

If the model returns a response that's too generic, too short, or the model gives a fallback response, try increasing the temperature. If the model enters infinite generation, increasing the temperature to at least 0.1 may lead to improved results. 1.0 is the recommended starting value for temperature.
TOP_P: Top-P changes how the model selects tokens for output. Tokens are selected from the most probable to least probable until the sum of their probabilities equals the top-P value. For example, if tokens A, B, and C have a probability of 0.3, 0.2, and 0.1 and the top-P value is 0.5, then the model will select either A or B as the next token by using temperature and excludes C as a candidate.
Specify a lower value for less random responses and a higher value for more random responses.
TOP_K: Top-K changes how the model selects tokens for output. A top-K of 1 means the next selected token is the most probable among all tokens in the model's vocabulary (also called greedy decoding), while a top-K of 3 means that the next token is selected from among the three most probable tokens by using temperature.
For each token selection step, the top-K tokens with the highest probabilities are sampled. Then tokens are further filtered based on top-P with the final token selected using temperature sampling.
Specify a lower value for less random responses and a higher value for more random responses.
MAX_OUTPUT_TOKENS: Maximum number of tokens that can be generated in the response. A token is approximately four characters. 100 tokens correspond to roughly 60-80 words.
Specify a lower value for shorter responses and a higher value for potentially longer responses.
HTTP method and URL:
POST https://aiplatform.MREP_LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/MREP_LOCATION/endpoints/
Request JSON body:
{ "contents": [ { "role": "USER", "parts": { "text" : "Why is sky blue?" } } ], "generation_config": { "temperature":TEMPERATURE, "topP": TOP_P, "topK": TOP_K, "maxOutputTokens": MAX_OUTPUT_TOKENS } }
To send your request, choose one of these options: Save the request body in a file named request.json, and execute the following command:
curl -X POST \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ -H "Content-Type: application/json; charset=utf-8" \ -d @request.json \ "https://aiplatform.MREP_LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/MREP_LOCATION/endpoints Save the request body in a file named request.json, and execute the following command:
$cred = gcloud auth print-access-token $headers = @{ "Authorization" = "Bearer $cred" } Invoke-WebRequest ` -Method POST ` -Headers $headers ` -ContentType: "application/json; charset=utf-8" `

---

## Page 24

-InFile request.json ` -Uri "https://aiplatform. MREP_LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/MREP_LOCATION/endpoints/ENDPOINT_ID:generateCont
You should receive a JSON response similar to the following.
### Response
{ "candidates": [ { "content": { "role": "model", "parts": [ { "text": "The sky appears blue due to a phenomenon called Rayleigh scattering, where shorter blue wavelengths of sunlight are scattered more strongly by the Earth's atmosphere than longer red wavelengths." } ] }, "finishReason": "STOP", "safetyRatings": [ { "category": "HARM_CATEGORY_HATE_SPEECH", "probability": "NEGLIGIBLE", "probabilityScore": 0.06325052, "severity": "HARM_SEVERITY_NEGLIGIBLE", "severityScore": 0.03179867 }, { "category": "HARM_CATEGORY_DANGEROUS_CONTENT", "probability": "NEGLIGIBLE", "probabilityScore": 0.09334688, "severity": "HARM_SEVERITY_NEGLIGIBLE", "severityScore": 0.027742893 }, { "category": "HARM_CATEGORY_HARASSMENT", "probability": "NEGLIGIBLE", "probabilityScore": 0.17356819, "severity": "HARM_SEVERITY_NEGLIGIBLE", "severityScore": 0.025419652 }, { "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "probability": "NEGLIGIBLE", "probabilityScore": 0.07864238, "severity": "HARM_SEVERITY_NEGLIGIBLE", "severityScore": 0.020332353 } ] } ], "usageMetadata": { "promptTokenCount": 5, "candidatesTokenCount": 33, "totalTokenCount": 38 } } To test a tuned model with a prompt, send a POST request and specify the `TUNED_ENDPOINT_ID`. Before using any of the request data, make the following replacements:

---

## Page 25

PROJECT_ID: Your project ID.
TUNING_JOB_REGION: The region where the tuning job runs. This is also the default region for where the tuned model is uploaded.
ENDPOINT_ID: The tuned model endpoint ID from the GET API.
TEMPERATURE: The temperature is used for sampling during response generation, which occurs when topP and topK are applied. Temperature controls the degree of randomness in token selection. Lower temperatures are good for prompts that require a less open-ended or creative response, while higher temperatures can lead to more diverse or creative results. A temperature of 0 means that the highest probability tokens are always selected. In this case, responses for a given prompt are mostly deterministic, but a small amount of variation is still possible.
If the model returns a response that's too generic, too short, or the model gives a fallback response, try increasing the temperature. If the model enters infinite generation, increasing the temperature to at least 0.1 may lead to improved results. 1.0 is the recommended starting value for temperature.
TOP_P: Top-P changes how the model selects tokens for output. Tokens are selected from the most probable to least probable until the sum of their probabilities equals the top-P value. For example, if tokens A, B, and C have a probability of 0.3, 0.2, and 0.1 and the top-P value is 0.5, then the model will select either A or B as the next token by using temperature and excludes C as a candidate.
Specify a lower value for less random responses and a higher value for more random responses.
TOP_K: Top-K changes how the model selects tokens for output. A top-K of 1 means the next selected token is the most probable among all tokens in the model's vocabulary (also called greedy decoding), while a top-K of 3 means that the next token is selected from among the three most probable tokens by using temperature.
For each token selection step, the top-K tokens with the highest probabilities are sampled. Then tokens are further filtered based on top-P with the final token selected using temperature sampling.
Specify a lower value for less random responses and a higher value for more random responses.
MAX_OUTPUT_TOKENS: Maximum number of tokens that can be generated in the response. A token is approximately four characters. 100 tokens correspond to roughly 60-80 words.
Specify a lower value for shorter responses and a higher value for potentially longer responses.
HTTP method and URL:
POST https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/endpoi
Request JSON body:
{ "contents": [ { "role": "USER", "parts": { "text" : "Why is sky blue?" } } ], "generation_config": { "temperature":TEMPERATURE, "topP": TOP_P, "topK": TOP_K, "maxOutputTokens": MAX_OUTPUT_TOKENS } }
To send your request, choose one of these options: Save the request body in a file named request.json, and execute the following command:
curl -X POST \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ -H "Content-Type: application/json; charset=utf-8" \ -d @request.json \ "https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/endpo

---

## Page 26

Save the request body in a file named request.json, and execute the following command:
$cred = gcloud auth print-access-token $headers = @{ "Authorization" = "Bearer $cred" } Invoke-WebRequest ` -Method POST ` -Headers $headers ` -ContentType: "application/json; charset=utf-8" ` -InFile request.json ` -Uri "https:// TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/endpoints/ENDPOINT_
You should receive a JSON response similar to the following.
### Response
{ "candidates": [ { "content": { "role": "model", "parts": [ { "text": "The sky appears blue due to a phenomenon called Rayleigh scattering, where shorter blue wavelengths of sunlight are scattered more strongly by the Earth's atmosphere than longer red wavelengths." } ] }, "finishReason": "STOP", "safetyRatings": [ { "category": "HARM_CATEGORY_HATE_SPEECH", "probability": "NEGLIGIBLE", "probabilityScore": 0.06325052, "severity": "HARM_SEVERITY_NEGLIGIBLE", "severityScore": 0.03179867 }, { "category": "HARM_CATEGORY_DANGEROUS_CONTENT", "probability": "NEGLIGIBLE", "probabilityScore": 0.09334688, "severity": "HARM_SEVERITY_NEGLIGIBLE", "severityScore": 0.027742893 }, { "category": "HARM_CATEGORY_HARASSMENT", "probability": "NEGLIGIBLE", "probabilityScore": 0.17356819, "severity": "HARM_SEVERITY_NEGLIGIBLE", "severityScore": 0.025419652 }, { "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "probability": "NEGLIGIBLE", "probabilityScore": 0.07864238, "severity": "HARM_SEVERITY_NEGLIGIBLE", "severityScore": 0.020332353 } ] } ],

---

## Page 27

"usageMetadata": { "promptTokenCount": 5, "candidatesTokenCount": 33, "totalTokenCount": 38 }
}
### Delete a tuned model
To delete a tuned model:
Call the models.delete method.
Before using any of the request data, make the following replacements:
PROJECT_ID: Your project ID.
REGION: The region where the tuned model is located.
MODEL_ID: The model to delete.
HTTP method and URL:
DELETE https://REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/models/MODEL_ID
To send your request, choose one of these options: Execute the following command:
curl -X DELETE \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/models/MODEL_ID" Execute the following command:
$cred = gcloud auth print-access-token $headers = @{ "Authorization" = "Bearer $cred" } Invoke-WebRequest ` -Method DELETE ` -Headers $headers ` -Uri "https:// REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/models/MODEL_ID" | Select-Object -Ex
You should receive a successful status code (2xx) and an empty response.
### Tuning and validation metrics
You can configure a model tuning job to collect and report model tuning and model evaluation metrics, which can then be visualized in Agent Platform Studio.
1. To view details of a tuned model in the Google Cloud console, go to the Agent Platform Studio page.
Go to Agent Platform Studio
2. In the Tune and Distill table, click the name of the tuned model that you want to view metrics for.
The tuning metrics appear under the Monitor tab.
### Model tuning metrics
The model tuning job automatically collects the following tuning metrics for the model:
/train_total_loss: Loss for the tuning dataset at a training step.
/train_fraction_of_correct_next_step_preds: The token accuracy at a training step. A single inference consists of a sequence of predicted tokens. This metric measures the accuracy of the predicted tokens when compared to the ground truth in the tuning dataset.
/train_num_predictions: Number of predicted tokens at a training step.

---

## Page 28

### Model validation metrics
/eval_total_loss: Loss for the validation dataset at a validation step.
/eval_fraction_of_correct_next_step_preds
/eval_num_predictions: Number of predicted tokens at a validation step.
### What's next
Learn about deploying a tuned Gemini model.
knowledge base.
under the Apache 2.0 License. For details, see the Last updated 2026-10-01 UTC.
Jump Start Solution: Generative AI
You can configure a model tuning job to collect the following validation metrics for the model:
: The token accuracy at an validation step. A single inference consists of a sequence of predicted tokens. This metric measures the accuracy of the predicted tokens when compared to the ground truth in the validation dataset.
The metrics visualizations are available after the tuning job starts running. It will be updated in real time as tuning progresses. If you don't specify a validation dataset when you create the tuning job, only the visualizations for the tuning metrics are available.
To learn how supervised fine-tuning can be used in a solution that builds a generative AI knowledge base, see
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.