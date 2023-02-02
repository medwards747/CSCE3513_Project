# Team 15's CSCE3513 Laser Tag Project

Python 3 project to receive and send events from laser tag guns via UDP and keep track of and display the score.

## Installation

### Requirements

- Python 3.9+
  - `pip3`
- `git`
- Graphical environment
- Network connection
  - Sends traffic on port `7500` (UDP)
  - Listens for traffic on port `7501` (UDP)

#### Recommended

- `virtualenv` for Python 3

### Setup

1. Clone and enter the repository

   ```bash
   git clone https://github.com/medwards747/CSCE3513_Project.git
   cd CSCE3513_Project
   ```

2. Create and activate a virtual environment (optional)

   ```bash
   virtualenv -p python3 venv
   source venv/bin/activate
   ```

3. Install dependencies

   ```bash
   pip3 install -r requirements.txt
   ```

4. Install the package

   For development (updates when files are changed):

   ```bash
   pip3 install -e .
   ```

   For production (does not automatically update)):

   ```bash
   pip3 install .
   ```

## Usage

### Running the program

```bash
python3 -m csce3513_gui
```

## Development

### Adding a new dependency

```bash
pip3 install <dependency>
pip3 freeze > requirements.txt
```

Then make sure any unnecessary dependencies are removed from `requirements.txt`.
