# Scale AI Integration Spike

This repository contains a proof of concept integration with the Scale AI API, demonstrating basic connectivity

## Prerequisites

- Python 3.x
- pip (Python package manager)
- Scale AI account with API key

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv scaleai-env
   source scaleai-env/bin/activate  # On Windows, use: scaleai-env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install scaleapi
   ```

## Configuration

1. Create a `config.py` file in the root directory
2. Add your Scale AI API keys:
   ```python
   API_KEY_TEST = "your_test_api_key_here"  # Starts with 'test_'
   API_KEY_PROD = "your_production_api_key_here"  # Starts with 'live_'
   ```
3. The `config.py` file is gitignored to prevent accidental commit of sensitive credentials

## Usage

The main script `hello_world.py` demonstrates basic Scale AI API connectivity:

- Verifies API key format (test or production)
- Connects to Scale AI API
- Handles connection errors gracefully

To run the script:
```bash
python hello_world.py
```

To use production credentials, set the PRODUCTION environment variable:
```bash
export PRODUCTION=1  # On Windows, use: set PRODUCTION=1
python hello_world.py
```

## Project Structure

```
.
├── README.md
├── hello_world.py      # Main script demonstrating API connectivity
├── config.py          # API key configuration (gitignored)
├── .gitignore         # Git ignore rules
└── scaleai-env/       # Python virtual environment (gitignored)
```

## Success Criteria

This spike is considered complete when:
- [x] Scale AI account is created and API key is generated
- [x] Local machine is set up with Scale AI SDK
- [x] Basic "hello world" scenario is implemented and working
  - Successfully connects to Scale AI API
  - Handles errors appropriately

## Notes

- The script defaults to using test credentials unless the PRODUCTION environment variable is set
- API keys are validated to ensure they start with either 'test_' or 'live_'
- Error handling is implemented for API connection issues
