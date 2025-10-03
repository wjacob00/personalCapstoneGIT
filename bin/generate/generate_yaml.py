import yaml

def load_env(filepath):
	env = {}
	with open(filepath) as f:
		for line in f:
			if '=' in line:
				key, value = line.strip().split('=', 1)
				env[key] = value
	return env

env = load_env('config.env')

config = {
	'version': '3',
	'services': {
		'apachephp': {
			'image': 'apachephp:latest',
			'volumes': ['../../static/:/var/www/html'],
			'ports': [f"{env['APACHE_PORT']}:80"],
			'environment': {
				'APACHE_IP': env['APACHE_IP']
			}
		}
	}
}

with open('docker-compose.yml','w') as f:
	yaml.dump(config, f)
