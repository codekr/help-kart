import os
from src.config.common import *  # noqa

ALLOWED_HOSTS = ['*']

# # Django S3 Configuration
# STATICFILES_STORAGE = 'django_s3_storage.storage.StaticS3Storage'
# DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage'
#
# # AWS Configuration
# AWS_REGION = os.getenv('AWS_S3_REGION_NAME')
# AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
#
# # Aws Bucket Configuration
# # AWS_S3_BUCKET_AUTH = False
# AWS_S3_BUCKET_AUTH_STATIC = True
# # AWS_S3_MAX_AGE_SECONDS_STATIC = "94608000"
# AWS_S3_BUCKET_NAME_STATIC = os.getenv("AWS_S3_BUCKET_NAME", "grocery-app-static-assets")
#
# # # These next two lines will serve the static files directly from the s3 bucket
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % os.getenv("AWS_S3_BUCKET_NAME")
# STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
