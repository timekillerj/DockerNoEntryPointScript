# About
This script is used to derive the Entrypoint and CMD of a given docker image. If no Entrypoint is specified then the default `/bin/sh -c` is used.

# Why?
When creating Fargate Tasks, it is sometimes necessary to explicitly add a EntryPoint. Though not all Dockerfile files list and EntryPoint, all docker images do in fact have one.Docker uses the default `/bin/sh -c` when no `ENTRYPOINT` is given.

# Usage
`python get_exec_params.py [Docker Image]`

# Output Example:
`python get_exec_params.py timekillerj/twistlock-fargate`

```
{
    "EntryPoint": [
        "/bin/sh",
        "-c"
    ],
    "Command": [
        "entry.sh"
    ]
}
```