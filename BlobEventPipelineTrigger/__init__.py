from io import BytesIO
import json
import logging
import os
import pandas as pd
import requests
import sys
import traceback

import azure.functions as func

def main(myblob: func.InputStream):
    # Trigger on Blob input
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    # Simple csv file validation
    if f"{myblob.name}"[-3:] == 'csv':
        try:
            blob_bytes = myblob.read(size=5000000)
            blob_to_read = BytesIO(blob_bytes) 
            logging.info("Loading csv file sample to pandas df")
            df = pd.read_csv(blob_to_read, nrows=10)
            logging.info(f"CSV file sample loaded. \n"
                         f"Column headers: {df.columns.values}")
        except Exception as e:
            logging.error(traceback.format_exc())

    # Validate json params
    if f"{myblob.name}"[-11:] == "params.json":
        try:
            params = json.loads(myblob.read().decode('utf-8'))
            logging.info(f"Param file: {params}")
        except Exception as e:
            logging.error(traceback.format_exc())

        # Trigger Azure DevOps pipeline with Params
        try:
            url='https://dev.azure.com/jpazuredev/machinelearning-devops/_apis/build/builds?api-version=5.0'
            logging.info(f"URL: {url}")
            body=json.dumps({"parameters":  json.dumps(params), "definition":  {"id": 8}})
            logging.info(f"Body: {body}")
            headers = {'content-type': 'application/json'}
            logging.info(f"Headers: {headers}")
            AzDOPAT = os.environ["AzDOPAT"]
            resp = requests.post(url, data=body, headers=headers, auth=(AzDOPAT, AzDOPAT))
            logging.info(f"Response: {resp}")
        except Exception as e:
            logging.error(traceback.format_exc())