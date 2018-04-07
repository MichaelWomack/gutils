from google.cloud.storage import Blob, Bucket
from google.api_core.page_iterator import HTTPIterator, Iterator

from gutils.gcp.storage import CloudStorage
from tests import bucket_name


class TestCloudStorage( object ):


	def test_get_bucket( self, cloud_storage: CloudStorage ):
		bucket = cloud_storage.get_bucket( bucket_name )
		assert isinstance( bucket, Bucket )
		assert bucket.name == bucket_name



	def test_get_blob( self, cloud_storage: CloudStorage, prepped_storage_blob: Blob ):
		blob = cloud_storage.get_blob( 'test-blob.txt', bucket_name )
		assert isinstance( blob, Blob )
		assert blob.name == 'test-blob.txt'
		assert blob.bucket.name == bucket_name
		assert blob.download_as_string() == prepped_storage_blob.download_as_string()



	def test_list_blobs( self, cloud_storage: CloudStorage, prepped_storage_blob: Blob ):
		blob_iterator = cloud_storage.list_blobs( bucket_name )
		assert isinstance( blob_iterator, HTTPIterator )
		assert list( blob_iterator )[ 0 ].download_as_string() == prepped_storage_blob.download_as_string()



	def test_upload_from_file( self, cloud_storage: CloudStorage ):
		content = 'My file content.'
		with open( 'my-test-file.txt', 'w' ) as f:
			f.write( content )

		f = open( 'my-test-file.txt', 'rb' )
		upload = cloud_storage.upload_blob_from_file( bucket_name, 'my-upload.txt', f, content_type='text/plain' )
		assert upload is not None
		assert isinstance( upload, Blob )
		assert upload.name == 'my-upload.txt'
		assert upload.download_as_string().decode( 'utf-8' ) == content
