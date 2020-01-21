# Function suite

UnitTestCase folder contains function test suite for this project.

# Setup

To setup you need to install Python 2.7.16 from `https://www.python.org/downloads/release/python-2716/`
Once installed python you can run setup.sh from bin as below.

```
$: chmod +x /bin/setup.sh
bin $: ./setup.sh
```

This will install all the dependent libraries. 

## Usage

You can run the full suite from `Parking_lot_` by doing
```
Parking_lot_/bin $: chmod +x run_functional_tests.sh
Parking_lot_ $ bin/run_functional_tests.sh
```

You can run the full suite directly from `Parking_lot_/UnitTestCase` by doing
```
Parking_lot_/UnitTestCase $ python UnitTestCase.py
```

You can have interactive run by running below command from `Parking_lot_/bin`:

```
Parking_lot_/bin $: chmod +x parking_lot.sh
Parking_lot_/bin $: python ./parking_lot.sh
```

To run from input file from `Parking_lot_/bin`:
```
Parking_lot_/bin $: chmod +x parking_lot.sh
Parking_lot_/bin $: python ./parking_lot.sh ../file_input.txt
```

