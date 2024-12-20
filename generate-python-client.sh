npx @openapitools/openapi-generator-cli generate \
  -i openapi.yaml \
  -g python \
  -o ./@jsq/main_openapi_client/ \
  --generate-alias-as-model \
  --additional-properties="projectName=main-openapi-python,packageName=main_openapi_client,packageVersion=1.1.1" \
  # -t ./updated_templates/