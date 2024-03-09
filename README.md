# WPPS - Wordpress Plugins Scan

WPPS (Wordpress Plugins Scan) is a Python tool designed to scan and detect WordPress plugins for security vulnerabilities. It provides a command-line interface for scanning plugins and detecting vulnerabilities.

## Features

- Scan installed WordPress plugins of the target.
- Detect vulnerabilities of the scan results.
- Easy-to-use command-line interface.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/deshine-VN/WPPS.git
```

2. Navigate to the project directory:

```bash
cd WPPS
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 wpps.py scan -h
```

This will display help for scan function.

```
usage: wpps.py scan [-h] [-u URL] [-t THREADS] [-l LIST]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     target URL (e.g https://example.com)
  -t THREADS, --threads THREADS
                        number of threads to scan (default: 5)
  -l LIST, --list LIST  specify plugins list to scan (default: all plugins -> please change the list until you feel hopeless)
```

For more options and detailed usage instructions, refer to the help option.

## Contributing
Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

## Contact
For any questions or inquiries, feel free to contact me:

Name: Ngo Minh Duc

Email: duc.hacker.ngo@gmail.com

Happy scanning!
