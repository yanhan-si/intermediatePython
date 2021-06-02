# Python CLI

Accessing CLI Arguments in Python

The general structure of a command is:

`$ {script} {argument0} {argument1} ... {argumentN}`

```python
import sys

name = sys.argv[1]
city = sys.argv[2]

print(f'hello, {name} from {city}')
```

### Argparser

python arg.py --help  
python arg.py sara --city "new york"  
```python
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Say a Greeting.")
    parser.add_argument('name', type=str)
    parser.add_argument('--city', type=str,
                        default="San Fran", help="where is the person from?")

    args = parser.parse_args()
    name = args.name
    city = args.city
    print(f'Hello, {name} from {city}')
```

### Subprocess

```python
import subprocess
import random

p = subprocess.Popen(['emoj', 'dog'], stdout=subprocess.PIPE)
output, err = p.communicate()
p_status = p.wait()

emoji = output.decode('utf-8').split(' ')

print(random.choice(emoji))
```

Using `subprocess.run`

```python
import subprocess
import random
p = subprocess.run(['emoj', 'dog'], stdout=subprocess.PIPE)
emoji = p.stdout.decode('utf-8').split(' ')
print(random.choice(emoji))
```