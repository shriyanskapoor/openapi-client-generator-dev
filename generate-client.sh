npx @openapitools/openapi-generator-cli generate \
  -i openapi.yaml \
  -g typescript-axios \
  -o ./typescript-client/ \
  --generate-alias-as-model \
  --additional-properties="npmName=@jsq/main-openapi-axios,npmVersion=10.0.0" \
  -t ./updated_templates/