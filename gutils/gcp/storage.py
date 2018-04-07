from google.api_core.page_iterator import HTTPIterator
from google.cloud import storage
from google.cloud.storage import Blob, Bucket


class CloudStorage( object ):


	def __init__( self, client ):
		self.client = client



	@classmethod
	def with_default_credentials( cls ):
		return cls( client=storage.Client() )



	@classmethod
	def from_service_account( cls, service_account_json_path ):
		return cls( client=storage.Client().from_service_account_json( service_account_json_path ) )



	def get_bucket( self, bucket_name ) -> Bucket:
		return self.client.get_bucket( bucket_name=bucket_name )



	def get_blob( self, blob_name, bucket_name ) -> Blob:
		bucket = self.get_bucket( bucket_name )
		return bucket.get_blob( blob_name )



	def list_blobs( self, bucket_name, **kwargs ) -> HTTPIterator:
		bucket = self.get_bucket( bucket_name )
		return bucket.list_blobs( **kwargs )



	def upload_blob_from_file( self, bucket_name, blob_name, file_obj, **kwargs ) -> Blob:
		bucket = self.get_bucket( bucket_name )
		blob = bucket.blob( blob_name )
		blob.upload_from_file( file_obj, **kwargs )
		return blob



	def upload_blob_from_string( self, bucket_name, blob_name, string_obj, **kwargs ) -> Blob:
		bucket = self.get_bucket( bucket_name )
		blob = bucket.blob( blob_name )
		blob.upload_from_string( string_obj, **kwargs )
		return blob
