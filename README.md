# Moblang
A simple interpreted language written in python and [sly](https://sly.readthedocs.io/en/latest/sly.html)

# Important 
This language is not meant for programming, right now this language have simple arithmatic operators and variables. Also the language is full of bugs.

# Getting Started

Clone it 
```git
git clone https://github.com/ni1l/mob-lang.git
```

Install sly
```shell
pip install sly
```

Run mob.py
```shell
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

-- Arithmatic operators
10 + 10 
10 - 10 
10 * 10 
10 / 10 

-- with variables
a = 10
b = 20
c = 4
sum = $a * $b
$main = $sum / $c
$sum
```

