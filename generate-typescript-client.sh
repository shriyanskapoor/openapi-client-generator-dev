npx @openapitools/openapi-generator-cli generate \
  -i openapi.yaml \
  -g typescript-axios \
  -o ./@jsq/main-openapi-axios/ \
  --generate-alias-as-model \
  --additional-properties="npmName=@jsq/main-openapi-axios,npmVersion=10.0.0,axiosVersion=^1.7.7" \
  -t ./updated_templates/