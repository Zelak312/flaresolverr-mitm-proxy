# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2026-02-03

- Removed npm things (not needed)
- Bump deps for security
- Add plain text support

## [1.0.8] - 2025-10-10

### Chore

- Fix dependency errors
- Bump h11 from 0.14.0 to 0.16.0
- Bump flask from 3.1.0 to 3.1.1
- Bump h2 from 4.1.0 to 4.3.0
- Bump mitmproxy from 11.1.3 to 12.1.2
- Bump tornado from 6.4.2 to 6.5

## [1.0.7] - 2025-04-26

### Bug Fixes

- Docker compose example using wrong port for PROXY variable
- Working example

### Chore

- Bump cryptography from 43.0.1 to 44.0.1
- Bump jinja2 from 3.1.5 to 3.1.6
- Revert "Bump h11 from 0.14.0 to 0.16.0" (Need new mitmproxy release)
- Upgrade deps and python version for docker image to 3.12
- Bump h11 from 0.14.0 to 0.16.0

## [1.0.6] - 2025-01-11

### Miscellaneous Tasks

- Bump mitm proxy version

### Chore

- Bump jinja2 from 3.1.4 to 3.1.5
- Bump tornado from 6.4.1 to 6.4.2
- Bump werkzeug from 3.0.3 to 3.0.6

## [1.0.5] - 2024-10-13

### Miscellaneous Tasks

- Bumping git-cliff to v2
- Update deps to fix issues + add test cmd for quick testing

### Chore

- Bump cryptography from 42.0.7 to 43.0.1

## [1.0.4] - 2024-08-06

### Miscellaneous Tasks

- Remove skip for some commit messages in cliff

### Chore

- Bump certifi from 2023.7.22 to 2024.7.4
- Bump tornado from 6.3.3 to 6.4.1
- Bump zipp from 3.16.2 to 3.19.1

## [1.0.3] - 2024-05-07

### Bug Fixes

- Issues with requested library versions

### Miscellaneous Tasks

- Remove "example.addon" head comment (#14)
- Return headers[] in url flaresolver response (#15)
- Remove logging

### Chore

- Bump werkzeug from 2.3.8 to 3.0.3
- Bump cryptography from 41.0.6 to 42.0.4
- Bump jinja2 from 3.1.3 to 3.1.4

## [1.0.2] - 2024-01-13

### Features

- Remove headers from query (#12)

### Miscellaneous Tasks

- Change example docker-compose to use latest version

### Chore

- Bump jinja2 from 3.1.2 to 3.1.3

## [1.0.1] - 2024-01-10

### Bug Fixes

- Auth for upstream proxy needs to be passed in an other parameter of mitmdump

## [1.0.0] - 2023-12-22

### Bug Fixes

- Proxy configuration and doc
- Curl example command so it's pastable in cli

### Features

- Add upstream proxy

### Miscellaneous Tasks

- How to send cookies
- Adding buy me a coffee link
- Move platforms to build for

## [1.0.2-beta] - 2023-12-07

### Miscellaneous Tasks

- Bump mitmproxy and pyOpenSSL & fixed docker file
- Adding tools for repo & release script
- Rename current changelog & chmod release
- Change commit from where to create changelog in release.sh
- Adding dev_env.sh script
- Remove redundant pip install of mitmproxy in dockerfile
- Add docker build on tag push
- Prepare docker action for test
- Fix error in docker worflow and warning
- Add fi in docker workflow
- Remove repo name docker worflow
- Fix lowercase + update to last vers
- Revised repo name latest tag

### Chore

- Bump cryptography from 38.0.4 to 41.0.4
- Bump werkzeug from 2.3.6 to 2.3.8
- Bump tornado from 6.3.2 to 6.3.3
- Bump cryptography from 41.0.4 to 41.0.6

