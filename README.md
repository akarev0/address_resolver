Server based on ```https://github.com/openvenues/libpostal``` on python to parse world addresses.
1. Pull the repo
2. Build separate container for ```parse_addresses```
3. Update ```docker-compose.override.yaml``` file and add new service
3. Run project with ```docker-compose up -d```