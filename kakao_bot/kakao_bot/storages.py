from storages.backends.azure_storage import AzureStorage 

class StaicStorage(AzureStorage):
    azure_container = 'static'

class MediaStorage(AzureStorage):
    azure_container = 'media'