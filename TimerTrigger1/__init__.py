import datetime
import logging

import azure.functions as func
from azure.storage.blob import BlockBlobService

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    logging.info('Funcao de backup executada as: %s', utc_timestamp)
    copy_azure_files()

def copy_azure_files():
    blob_service = BlockBlobService(account_name='labcyhw2', account_key='zy2m8C1qjV0+7A9QL6hpCeFAO3fxplOS900adzDuTGlKU9LkIERYfN/VG5STbXxYK6BMvyaRMWjPaEUNmU8GoA==')

    copy_from_container = 'prod'
    copy_to_container = 'bkp'
    listagem = blob_service.list_blobs(copy_from_container)
    for blob in listagem:
        blob_url = blob_service.make_blob_url(copy_from_container, blob.name)
        blob_service.copy_blob(copy_to_container, blob.name, blob_url)
        print(blob.name)