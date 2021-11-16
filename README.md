# Moblang
A simple interpreted language written in python with [sly](https://sly.readthedocs.io/en/latest/sly.html) library

# Important 
This language is not meant for programming, right now this language have simple arithmatic operators and variables. Also the language is full of bugs.

# Getting Started

Install sly
```shell
pip install sly
```

Clone it 
![Getting started](https://github.com/ni1l/mob-lang/blob/main/assets/Screenshot%202021-11-09%20205911.jpg)


Run it
```shell
python3 run.py 
```

# Hello, World

![Hello, World](https://github.com/ni1l/mob-lang/blob/main/assets/Screenshot%202021-11-09%20210123.jpg)

# Comments 

![Comments](https://github.com/ni1l/mob-lang/blob/main/assets/Screenshot%202021-11-09%20210228.jpg)

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

