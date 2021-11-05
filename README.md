# Moblang
A simple interpreted language written in python and [sly](https://sly.readthedocs.io/en/latest/sly.html)

# Important 
This language is not meant for programming, right now you can only do simple arithmatic and assign variables. And the language is full of bugs.

# Getting Started

Clone it 
```
git clone https://github.com/ni1l/mob-lang.git
```

Install sly
```
pip install sly
```

Run mob.py
```
python3 run.py 
```

# Hello, World

```
main = "Hello, World"
$main
```

# More Examples
```
-- Variables
name = "Nil" -- String
age = 0 -- Integer

-- Print them 

$name -- returns "Nil" 
$age -- returns 0 

-- Arithmatic
10 + 10 -- addition
10 - 10 -- Subtraction
10 * 10 -- multiplication
10 / 10 -- dvivision 

-- Arithmatic ith variables
a = 10
b = 10
sum = $a * $b 
$sum -- returns 100
```

