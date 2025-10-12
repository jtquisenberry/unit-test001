import pytest
from minio import S3Error

from tests.mocks.minio_mock import MinioMock


def test_count_minio_buckets():
    minio_client = MinioMock()
    buckets = minio_client.list_buckets()
    actual = len(buckets)
    expected = 3
    assert actual == expected


def test_get_buckets():
    minio_client = MinioMock()
    actual = minio_client.list_buckets()
    expected = ['bucket1', 'bucket2', 'bucket3']
    assert actual == expected


def test_bucket_s3error():
    minio_client = MinioMock()
    minio_client.set_success(False, 's3error')
    with pytest.raises(S3Error) as excinfo:
        buckets = minio_client.list_buckets()
        a = 1


def test_bucket_exception():
    minio_client = MinioMock()
    minio_client.set_success(False, 'exception')
    with pytest.raises(Exception) as excinfo:
        buckets = minio_client.list_buckets()
        b = 1


