MCB185 Course
=============

This is the course plan for MCB185 as taught in Winter 2022.

## Lessons ##

The lessons are currently designed for a 10-week quarter with some flexibility.
Lesson 0 may take more than 1 week because of late adds and drops. For grading
purposes, there are homework assignments in Lessons 0-6 and a final project for
the end of class.

+ Lesson 0: Tools of the Trade
+ Lesson 1: Variables, Math, and Loops
+ Lesson 2: Loops and Conditionals
+ Lesson 3: Tuples and Lists
+ Lesson 4: Functions
+ Lesson 5: Dictionaries and Regex
+ Lesson 6: Modules and CLI
+ Lesson 7: Complex Data

Lesson 0: Tools of the Trade
============================

## Learning Objectives ##

* GitHub - create your account, clone and fork repos
* Unix - basic commands, files, directories
* Markdown - simple and flexible text file formatting
* Python - write your first program

## Lesson Plan ##

Follow the directions in `GUMPY.md`.

At the end of the lesson, you will have your own GitHub repository with your
first Python program: `00helloworld.py`. Along the way you will have learned
some of the most useful Unix commands, be able to navigate the Unix directory
structure, and save typing with tab-completion. You will also learn how to use
Markdown to create simple text files that can be easily converted to HTML, PDF,
etc.

Lesson 1: Variables, Math, and Loops
====================================

## Learning Objectives ##

* Variables - strings, ints, floats, None, type()
* Math - math operators and functions
* Text - string operators and functions

## Tutorials ##

Start with `10variables.py`. The first thing you will learn is about comments.
That is, text you put into programs that don't actually do anything other than
provide information. Comments start with a `#` sign, which is called number
sign, pound, or hash, but not hashtag. Comments are used during programming for
debugging. One way to comment-out a large section of code is with triple
quotes. Each tutorial file is meant to be _uncovered_ a few lines at a time by
moving the triple quotes downward.

In `10variables.py` you will learn that variables are containers that can hold
different kinds of things, like numbers and text. Each variable has a *type*
which can be seen with the `type()` function. Variables of different types
don't always play well together, so you may need to convert them with functions
like `int()`, `float()`, or `str()`. You are also introduced to the `None`
type, which turns out to be a really useful for debugging later.

Next, follow `11math.py`. Here, you will learn that the typical mathematics
operations you are already familar (addition, subtraction, multiplication,
division, exponentiation) are also in Python. However, the symbol for
multiplication is `*` and exponentiation is `**`. The standard rules for
precedence are: multiplication and division before addition and subtraction.
But what about exponentiation and other operations like `%` (modulo)? Use
parentheses when in doubt. Heck, use parentheses even when not in doubt.

In `11math.py` you are first introduced to the concept of libraries (also
called modules). For example, the `log2()` function is in the `math` library.
You must first `import` that math libray and then the `log2()` function becomes
available.

	import math()
	print(math.log2(1))

Next, follow `12text.py`. Here, you will learn that some of the math operators
like `+` and `*` also work on strings. You will also see the `len()` function
for the first time, which returns the length of a string (also the length of a
list, but that comes later). You are also introduced to the string slice
syntax, which allows you to retrieve part of a string. Finally, you will learn
how to format strings for printing.

In `13loops.py` you will be _introduced_ to loops. We will be spending much
more time with loops in future lessons. This is but the introduction. Here, you
will learn how to iterate over a `range()` of numbers or the characters in a
string.

## Coding Exercises ##

Change directory to the `Programs` directory and try programming the following
2 programs. The instructions and the expected output are in the file. You
_just_ have to write the code.

1. 11codons.py
2. 12sumfac.py

When you've completed the homework, copy the files to your homework repo. Don't
forget to _push_ them back up to GitHub.

## Python Manifest ##

### Operators

	=
	+
	-
	*
	/
	**
	%
	//
	\
	[:]

### Keywords

	in

### Functions

	float()
	int()
	len()
	range()
	str()
	type()

### Libraries

A little bit of the `math` library was used in the tutorial. Here are some
useful constants and functions.

	math.e
	math.pi
	math.inf
	math.nan
	math.tau
	math.ceil()
	math.factorial()
	math.log()
	math.log2()
	math.floor()
	math.sqrt()

## File Manifest ##

	Tutorials/10variables.py
	Tutorials/11math.py
	Tutorials/12text.py
	Tutorials/13loops.py
	Programs/10codons.py
	Programs/11sumfac.py

Lesson 2: Loops and Conditionals
================================

## Learning Objectives ##

* Conditional Execution - Boolean type, if, elif, else, while, break, continue
* String Formatting - various ways or printing

## Tutorials ##

Start your tutorial session with `20conditionals.py`. This is in the
'Tutorials' directory of course. Here you will learn about the `if` statement
and its related parts `elif` and `else`. You will use `if` statements
constantly in your programs. Conditional statements evalute to either `True` or
`False`. These are known as Boolean values. The Boolean operators include
`and`, `or`, and `not`. You will also be introduce to the `while` loop, which
uses a conditional statement to stop the loop. In addition, you will be
introduced to the `continue` and `break` statements, which can be used with
both `for` and `while` loops to skip ahead or stop the loop entirely.

Next, follow `21loopcond.py`. The examples here demonstrate how mixing loops
and conditionals can make complex behaviors.

The tutorials are very short this lesson in order to make room for lots of
programming practice using loops and conditionals.

## Coding Exercises ##

For programming practice, try writing the following programs, which you will
find in the usual `Programs` directory.

1. 20fizzbuzz.py
2. 21gc.py
3. 22atseq.py
4. 23anti.py
5. 24frame.py
6. 25aapairs.py
7. 26gcwin.py
8. 27gcwin.py

When you're done, copy the programs to your homework repo and push them from
there.

## Python Manifest ##

### Operators

	and
	not
	or

### Keywords

	if
	elif
	else
	while
	break
	continue

### Functions

	random.randint()

### Libraries

	random

## File Manifest ##

	Tutorials/20conditionals.py
	Tutorials/21loopcond.py
	Programs/20fizzbuzz.py
	Programs/21gc.py
	Programs/22atseq.py
	Programs/23anti.py
	Programs/24frame.py
	Programs/25aapairs.py
	Programs/26gcwin.py
	Programs/27gcwin.py

Lesson 3: Tuples and Lists
==========================

## Learning Objectives ##

* tuples - immutable, comma separated values (in parentheses)
* lists - mutable, comma separarted values [in brackets]
* list functions - append(), pop(), insert(), sort()

## Tutorials ##

In `30lists.py`, you will learn how to create tuples and lists. The Python
*list* is what other languages call an *array*. A lot of the work in
programming is done by iterating over lists. You will also be introduced to the
`zip()` and `enumerate()` functions. Finally, you will see a bit of optional
syntactic sugar called *list comprehension*.

## Coding Exercises ##

For programming practice, try writing the following programs. The instructions
and expected output are inside each file as usual.

1. 30stats.py
2. 31entropy.py
3. 32xcoverage.py
4. 33birthday.py

## Python Manifest ##

### Operators

	,

### Functions

	enumerate()
	len(list)
	list()
	zip()

### Methods

	list.append()
	list.insert()
	string.join()
	list.pop()
	list.sort()
	list.split()

### Libraries

	sys

## File Manifest ##

	Tutorials/30lists.py
	Programs/30stats.py
	Programs/31entropy.py
	Programs/32xcoverage.py
	Programs/33birthday.py


Lesson 4: Functions
===================

## Learning Objectives ##

* Define functions
* Use assertions
* Open and read from named files
* Search for items inside lists

## Tutorials ##

First, try out `40functions.py`, where you will learn how to write blocks of
code that perform specific duties whenever you call them. Functions are the
building blocks of complex programs. Here, you will also observe that floating
point math is an approximation of real math. As a result, we have to use
functions like `math.isclose()` to check for equality. This tutorial also
introduces `assert()`, which you can use to ensure your functions receive
proper values.

Next, go on to `41files.py`, where you will learn to read and write text files.
While reading text files is generally safe, writing files can be dangerous if
you accidentally overwrite another file.

## Coding Exercises ##

For programming practice, try writing `40transmembrane.py` and `41aacomp.py` in
the Programs directory.

## Python Manifest ##

### Keywords

	def
	return
	with
	yield

### Functions

	open()

### Methods

	close()
	readline()
	readlines()
	write()

### Libraries

## File Manifest ##

	Tutorials/40functions.py
	Tutorials/41files.py
	Programs/40transmembrane.py
	Programs/41aacomp.py


Lesson 5: Dictionaries & Regex
==============================

## Learning Objectives ##

+ Use dictionaries for efficient look up
+ Create dictionaries for counting
+ Sort by dictionaries by key or value
+ Parse files using regular expressions

## Tutorials ##

In `50dictionaries.py` you will be introduced to the magic of dictionaries. On
the one hand, dictionaries are simply lists but instead of putting numbers in
square brackets, you use text (or other immutable things). Dictionaries are
both incredibly efficient and convenient. Once you start using them, you will
use them all the time. However, they are sometimes difficult to understand in
the beginning.

In `51regex.py` you will be introduced to another piece of coding magic:
regular expressions. You have seen something like this before with Unix `grep`.
Python has its own regex engine which you can use to parse files to find
specific pieces of data.

## Coding Exercises ##

You will find the following files in the Programs folder.

1. 50kmers.py - count up kmers in a sequence file
2. 51translate.py - translate some RNA to protein
3. 52digest.py - perform a restriction digest

## Python Manifest ##

### Keywords

	del

### Operators

	{}

### Functions

### Methods

	dict.keys()
	dict.values()
	dict.items()
	re.search()
	re.findall()
	re.finditer()

### Libraries

	re

## File Manifest ##

	Tutorials/50dictionaries.py
	Tutorials/51datastructures
	Programs/50kmers.py
	Programs/51translate.py


Lesson 6: Modules and CLI
=========================

## Learning Objectives ##

+ Use argparse to provide a typical Unix command line interface
+ Make your own function library

## Tutorials ##

Modules (the python word for libraries) are the currency of professional
programmers. Developers write and share libraries. In addition to using other
peoples' libraries, you should also write your own even if you don't share your
code with lots of people. Libraries make your code more organized.

The command line interface (CLI) has standards. If you want your program to
look and feel like a typical Unix program (and you do) then use `argparse` to
capture your command line parameters and provide a help interface. We will no
longer be using `sys.argv` to get data into programs because `argparse` is much
better.

The tutorials in this lesson are a little different from before.
`60argparse.py` is a template for all your future programs, not a tutorial.
That is, every program you write from now on should use the argparse library to
handle the command line. `60argparse.py` is a reminder of how to do that.

The other tutorial-ish file, `mcb185.py` is a library with a couple useful
functions inside. Make an alias from `~/Work/lib/mcb185.py` that points to
`~/Work/MCB185-2022/Tutorials/mcb185.py` so that python can find your library
from anywhere. Alternatively, you can also put an alias into whatever directory
you happen to be working in (e.g. homework).

## Coding Exercises ##

You will find the following program directions in the Programs folder.

1. 60seqstats.py
2. 61dust.py

## Python Manifest ##

### Keywords

### Operators

### Functions

### Methods

### Libraries

	argparse

## File Manifest ##

	Tutorials/60argparse.py
	Tutorials/mcb185.py
	Programs/60seqstats.py
	Programs/61dust.py


Lesson 7: Complex Data
=========================

## Learning Objectives ##

+ Create multi-dimensional data structures
+ Relate spreadsheets to lists and dictionaries
+ Relate JSON to python

## Tutorials ##

The lists and dictionaries we've used so far have been one-dimensional. But
there's a lot of data that is better modeled in multiple dimensions. A commong
format for two-dimensional data is the spreadsheet. One can think of this as a
2-dimensional list or a a combination of a list and dictionary. In
`70datastructures.py` you will be introduced to several ways of combining lists
and dictionaries. You will also see the very popular
[https://www.json.org/json-en.html](JSON) format for data interchange. Take a
looked at the linked website.

## Coding Exercises ##

There are no coding exercises this week. You should be working on a final
project. Ask your instructor.

## Python Manifest ##

### Keywords

### Operators

### Functions

### Methods

	json.dumps()
	json.loads()

### Libraries

	json

## File Manifest ##

	Tutorials/70datastructures.py
