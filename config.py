import os

from google.cloud import secretmanager

project_id = os.environ.get('GOOGLE_CLOUD_PROJECT')

scopes = []
client = secretmanager.SecretManagerServiceClient()

secrets = {}
parent = f"projects/{project_id}"

for secret in client.list_secrets(request={"parent": parent}):
    short_secret_name = client.parse_secret_path(secret.name)['secret']
    version_alias = f"projects/{project_id}/secrets/{short_secret_name}/versions/latest"
    request = secretmanager.GetSecretVersionRequest(
        name=version_alias
    )
    version_name = client.get_secret_version(request=request).name
    response = client.access_secret_version(request={"name": version_name})
    secrets[short_secret_name] = response.payload.data.decode("UTF-8")
