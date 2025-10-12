from minio import Minio
from minio.error import S3Error
from http.client import HTTPResponse
import socket


class MinioMock:
    def __init__(self, endpoint = '', access_key = '', secret_key = '', secure = False):
        self.endpoint = endpoint
        self.access_key = access_key
        self.secret_key = secret_key
        self.secure = secure

        self.method_successful = True
        self.error_type = ''

    def set_success(self, method_successful, error_type=''):
        self.method_successful = method_successful
        self.error_type = error_type


    def list_buckets(self):
        if self.method_successful:
            return ['bucket1', 'bucket2', 'bucket3']
        else:
            if self.error_type == 's3error':
                # sock = socket.socket()
                # response = HTTPResponse(sock=socket.socket())
                raise S3Error(None, code='0', message="Bucket creation failed",
                              resource=None, request_id='a', host_id='', bucket_name=None,
                              object_name=None)
            elif self.error_type == 'exception':
                raise Exception("Exception message")
            else:
                raise Exception("Unknown error")


if __name__ == '__main__':
    client = MinioMock(
                    "play.min.io",  # MinIO endpoint
                    access_key="minioadmin",  # Access key
                    secret_key="minioadmin",  # Secret key
                    secure=True  # Use HTTPS
                )
    client.set_success(False)
    try:
        client.list_buckets()
    except Exception as e:
        print(f"AAAAAAAAAAAAAAAAA {e}")
        b = 1
    a = 1
