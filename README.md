# event-driven-pipeline
This is a sample Azure Function to trigger a pipeline in Azure Devops when new data lands in Azure Blob Storage. The function builds on the [sample Blob Trigger function](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-storage-blob-triggered-function) and introduces some basic functionality to call the Azure DevOps REST API.

![overview screenshot of function capability](/img/overview.png)

## Prerequisites
- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio Code Azure Functions Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)
- An Azure DevOps Project with a Pipeline that you want to trigger

## Setup
1. Clone the github repo into your environment
1. Create an Azure Function service in your Azure Subscription
1. Generate an [Azure DevOps PAT](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=preview-page#create-personal-access-tokens-to-authenticate-access) and add to the [Azure Function Application Settings](https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings#get-started-in-the-azure-portal) and `local.settings.json` if you plan to test locally.
1. Using your PAT, get the Build ID for the pipeline that you want to trigger by querying the Azure DevOps (Definitions API)[https://docs.microsoft.com/en-us/rest/api/azure/devops/build/definitions/list?view=azure-devops-rest-5.1] for your project, and update the `id` value in the `__init__.py` script (line 42).
1. Update the Azure DevOps pipeline URL in the `__init__.py` script (line 40) with your own [pipeline details](https://docs.microsoft.com/en-us/rest/api/azure/devops/build/builds/queue?view=azure-devops-rest-5.1#definitionreference)
1. Publish the `BlobEventPipelineTrigger` function to your Function Service


