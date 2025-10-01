import yaml

config = {
        'version': '3',
        'services': {
                'web': {
                        'image': 'php:8-apache',
                        'ports': ['80:80']
                }
        }

}

with open('docker-compose.yml','w') as f:
        yaml.dump(config, f)
