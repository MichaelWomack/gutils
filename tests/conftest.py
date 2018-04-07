import pytest

from tests import bucket_name
from gutils.gcp.storage import CloudStorage


@pytest.fixture
def cloud_storage():
	return CloudStorage.with_default_credentials()


@pytest.fixture
def prepped_storage_blob( cloud_storage: CloudStorage ):
	blob_content = 'What a great blob!'
	blob_name = 'test-blob.txt'
	blob = cloud_storage.upload_blob_from_string( bucket_name, blob_name, blob_content, content_type='text/plain' )
	return blob


@pytest.fixture( autouse=True )
def cleanup_bucket( cloud_storage: CloudStorage ):
	test_bucket = cloud_storage.get_bucket( bucket_name )
	[ blob.delete() for blob in test_bucket.list_blobs() ]
