#!/usr/bin/env python
import sys
import json
import subprocess


def inspect_image(docker_image):
    out = subprocess.Popen(["docker", "inspect", docker_image],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    if stderr:
        print(f'ERROR: {stderr}')
        sys.exit(1)
    data = json.loads(stdout)
    return data

def print_exec_params(docker_data):
    if not docker_data[0].get("Config", {}).get("Entrypoint"):
        entrypoint = ["/bin/sh", "-c"]
    else:
        entrypoint = docker_data[0].get("Config", {}).get("Entrypoint")
    cmd = docker_data[0].get("Config", {}).get("Cmd")

    exec_params = {
        "EntryPoint": entrypoint,
        "Command": cmd
    }
    print(json.dumps(exec_params, indent=4))

if __name__ == "__main__":
    docker_image = sys.argv[1]
    docker_data = inspect_image(docker_image)
    print_exec_params(docker_data)