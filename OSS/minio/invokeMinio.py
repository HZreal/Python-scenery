from minio import Minio
from minio.error import S3Error

# https://min.io/docs/minio/linux/developers/python/minio-py.html

ACCESS_KEY = '5WXG4qQaYJGDGec3z7hk'
SECRET_KEY = 'NtBJ9z2Zb241vl3EjNtJGfsrsiXwgEICeGAb0NDn'


def invoke_minio():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "127.0.0.1:50021",
        access_key=ACCESS_KEY,
        secret_key=SECRET_KEY,
        secure=False
    )

    # Make 'mydoc' bucket if not exist.
    found = client.bucket_exists("mydoc")
    if not found:
        client.make_bucket("mydoc")
    else:
        print("Bucket 'mydoc' already exists")

    # Upload '/home/user/Photos/asiaphotos.zip' as object name
    # 'asiaphotos-2015.zip' to bucket 'mydoc'.
    client.fput_object(
        "mydoc", "img-desktop-1.jpg", "./img-desktop-1.jpg",
    )
    print(
        "'img-desktop-1.jpg' is successfully uploaded as "
        "object 'img-desktop-1.jpg' to bucket 'mydoc'."
    )


if __name__ == "__main__":
    try:
        invoke_minio()
    except S3Error as exc:
        print("error occurred.", exc)
