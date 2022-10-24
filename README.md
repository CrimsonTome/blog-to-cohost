# blog-to-cohost

bot using [cohost.py](https://github.com/valknight/Cohost.py) and feedparser to automate posting blog posts to cohost

## System requirements

- Linux (Windows may work but is not tested)
- Python
- Pip
- Bash
- Docker (optional) - broken as of [abfa1f6](https://github.com/CrimsonTome/blog-to-cohost/commit/abfa1f6c7debead66a1f6ebc14928d9abfac020a)

## Quicktstart

- clone the repo from <https://github.com/CrimsonTome/blog-to-cohost>
- `pip install -r requirements.txt` to install dependencies
- edit `scripts/main.py` with your changes
- `python3 scripts/main.py` to run
<!-- more steps soon -->

## Building

### Python

<!--  steps here -->

- `python3 scripts/main.py`

### Docker

<!-- steps here -->
- `docker build -t blog-to-cohost .`

## Contributing

<!-- TODO Add contributing guidelines -->

## License, Credits and Disclaimers

blog-to-cohost is licensed under the MIT License. The full license text is included in the [LICENSE](LICENSE) file in this repository. Tldr legal have a [great summary](https://www.tldrlegal.com/l/mit) of the license if you're interested.  

This repo is built off [cohost.py](https://github.com/valknight/Cohost.py), a library for [cohost.org](https://cohost.org/)

No part of this code is approved by [cohost](https://cohost.org/), this uses an **unofficial** API.
