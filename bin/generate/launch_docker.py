import subprocess

subprocess.run(["docker", "build", "-t", "php:8-apache", "."], check=True)
subprocess.run(["docker", "run", "--rm", "php:8-apache"], check=True)

#Can inject files or run commands inside containers here subprocess.run(["docker", "exec", "-it", "my-container", "bash"], check=True)
subprocess.run(["docker", "compose", "up", "-d"], check=True)
