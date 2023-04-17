# Team 15's CSCE3513 Laser Tag Project

Python 3 project to receive and send events from laser tag guns via UDP and keep track of and display the score.

## Installation

### Requirements

- Python 3.9+ (incompatiable with python 3.11)
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

   alternatively for conda users (optional)

   ```bash
   conda create -n py310 python=3.10
   conda activate py310
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

   For production (does not automatically update):

   ```bash
   pip3 install .
   ```

## Usage

### Running the program

```bash
python3 -m csce3513_gui
```

### Generating Traffic

Run while the game is running.

#### Using the Python script

```bash
python3 ./python_traffic_generator.py
```

And follow the prompts.

#### Using netcat

```bash
nc -u 127.0.0.1 7501
```

Change IP address and port as needed.

Then type in the event you want to send. For example:

```bash
1:2
```

will send a hit event from player ID 1 to player ID 2.

## Development

### Adding a new dependency

```bash
pip3 install <dependency>
pip3 freeze > requirements.txt
```

Then make sure any unnecessary dependencies are removed from `requirements.txt`.

### Writing tests

1. Create a new file in the `tests` directory named `test_<class>.py`
2. Add the following to the top of the file:

   ```python
   import unittest
   from csce3513 import <class>
   ```

3. Create a new class that inherits from `unittest.TestCase` named `Test<ClassName>`
4. Add test methods to the class (use assertions to test the code)

   ```python
   def test_<method>(self):
       self.assertEqual(<expected>, <actual>)
   ```

5. At the bottom of the file, add the following:

   ```python
   if __name__ == '__main__':
       unittest.main()
   ```

### Running tests

```bash
python3 -m unittest
```

#### Running tests for specific files

```bash
python3 -m unittest tests/test_<file>.py
```

```bash
python3 -m unittest tests.test_<file>
```

Don't include the `.py` extension in the second way.

#### Running tests for specific classes

Don't include the `.py` extension for the file.

```bash
python3 -m unittest tests.test_<file>.Test<class>
```

#### Running tests for specific methods

```bash
python3 -m unittest tests.test_<class>.Test<ClassName>.test_<method>
```
