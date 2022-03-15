from __future__ import annotations
import cloudinary


class CloudinaryConnection:
    is_connected = False

    @classmethod
    def cloud_connection(cls) -> bool:
        if not cls.is_connected:
            cloudinary.config(
                cloud_name="diwjly6a7",
                api_key="822617155692878",
                api_secret="uaFJ8xy8RfLzLjgJoyFWSDrn6pM",
            )
            cls.is_connected = True
        return cls.is_connected

    @classmethod
    def get_connection(cls) -> CloudinaryConnection:
        cls.cloud_connection()
        return cls()

    def get_image(self):
        image = cloudinary.utils.cloudinary_url("sample.jpg")
        return image
