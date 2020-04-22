import cloudinary.uploader

from project.utils.constans.keys_cloudinary import KeysCloudinary


class Cloudinary:
    _response = None

    def __init__(self, cloud_name, api_key, api_secret):
        cloudinary.config(cloud_name=cloud_name,
                          api_key=api_key,
                          api_secret=api_secret)

    def upload_image(self, file_name):
        self._response = cloudinary.uploader.upload(file_name)

    def get_url_uploaded_image(self):
        return self._response[KeysCloudinary.URL.value]
