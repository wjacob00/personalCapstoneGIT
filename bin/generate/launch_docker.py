import subprocess

subprocess.run(["docker", "build", "-t", "apachephp:latest", "."], check=True)
subprocess.run(["docker", "run", "-d", "--rm", "apachephp:latest"], check=True)

#Can inject files or run commands inside containers here subprocess.run(["docker", "exec", "-it", "my-container", "bash"], check=True)
subprocess.run(["docker", "compose", "up", "-d"], check=True)
