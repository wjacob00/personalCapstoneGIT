import yaml

config = {
        'version': '3',
        'services': {
                'apachephp': {
                        'image': 'apachephp:latest',
                        'volumes': ['../../static/:/var/www/html'],
                        'ports': ['80:80']
                }
        }

}

with open('docker-compose.yml','w') as f:
        yaml.dump(config, f)
