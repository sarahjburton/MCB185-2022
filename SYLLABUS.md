Syllabus for MCB185
===================

This is the syllabus for MCB185 as taught in Winter 2022.

## Lessons ##

The lessons are currently designed for a 10-week quarter with Lesson 9 being 2
weeks long. For grading purposes, there are homework assignments in weeks 1-8,
and a final project for weeks 9 + 10.

+ Lesson 1: Tools of the Trade
+ Lesson 2: Variables, Math, and Loops
+ Lesson 3: Loops and Conditionals
+ Lesson 4: Lists and Files
+ Lesson 5: Functions
+ Lesson 6: CLI and Modules
+ Lesson 7: Dictionaries and Regex
+ Lesson 8: Complex Data
+ Lesson 9: Projects

Lesson 1: Tools of the Trade
============================

## Learning Objectives ##

* Unix - basic commands and directory structure
* Python - write your first program
* GitHub - create your first repository
* Markdown - simple and flexible text file formatting

## Lesson Plan ##

Follow the directions in `GUMPY.md`.

At the end of the lesson, you will have your own GitHub repository with your
first Python program: `hello_world.py`. Along the way you will have learned
some of the most useful Unix commands, be able to navigate the Unix directory
structure, and save typing with tab-completion. You will also learn how to use
Markdown to create simple text files that can be easily converted to HTML, PDF,
etc.

Lesson 2: Variables, Math, and Loops
====================================

## Learning Objectives ##

* Variables - strings, ints, floats, None, type()
* Math - math operators and functions
* Text - string operators and functions

## Tutorials ##

Start with `01_variables.py`. The first thing you will learn is about comments.
That is, text you put into programs that don't actually do anything other than
provide information. Comments start with a `#` sign, which is called number
sign, pound, or hash, but not hashtag. Comments are used during programming for
debugging. One way to comment-out a large section of code is with triple
quotes. Each tutorial file is meant to be _uncovered_ a few lines at a time by
moving the triple quotes downward.

In `01_variables.py` you will learn that variables are containers that can hold
different kinds of things, like numbers and text. Each variable has a *type*
which can be seen with the `type()` function. Variables of different types
don't always play well together, so you may need to convert them with functions
like `int()`, `float()`, or `str()`. You are also introduced to the `None`
type, which turns out to be a really useful for debugging later.

Next, follow `02_math.py`. Here, you will learn that the typical mathematics
operations you are already familar (addition, subtraction, multiplication,
division, exponentiation) are also in Python. However, the symbol for
multiplication is `*` and exponentiation is `**`. The standard rules for
precedence are: multiplication and division before addition and subtraction.
But what about exponentiation and other operations like `%` (modulo)? Use
parentheses when in doubt. Heck, use parentheses even when not in doubt.

In `02_math.py` you are first introduced to the concept of libraries (also
called modules). For example, the `log2()` function is in the `math` library.
You must first `import` that math libray and then the `log2()` function becomes
available.

	import math()
	print(math.log2(1))

Next, follow `03_text.py`. Here, you will learn that some of the math operators
like `+` and `*` also work on strings. You will also see the `len()` function
for the first time, which returns the length of a string (also the length of a
list, but that comes later). You are also introduced to the string slice
syntax, which allows you to retrieve part of a string. Finally, you will learn
how to format strings for printing.

In `04_loops.py` you will be _introduced_ to loops. We will be spending much
more time with loops in the next lesson. Here, you will learn how to iterate
over a `range()` of numbers or the characters in a string.

## Coding Exercises ##

Change directory to the `Programs` directory and try programming the following
2 programs. The instructions and the expected output are in the file. You
_just_ have to write the code.

1. `01_codons.py`
2. `02_sumfac.py` to your `learning python` repo and


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

	Tutorials/01_variables.py
	Tutorials/02_math.py
	Tutorials/03_text.py
	Tutorials/04_loops.py
	Programs/01_codons.py
	Programs/02_sumfac.py

Lesson 3: Loops and Conditionals
================================

## Learning Objectives ##

* Conditional Execution - Boolean type, if, elif, else, while, break, continue
* String Formatting - various ways or printing

## Tutorials ##

Start your tutorial session with `05_conditionals.py`. This is in the
'Tutorials' directory of course. Here you will learn about the `if` statement
and its related parts `elif` and `else`. You will use `if` statements
constantly in your programs. Conditional statements evalute to either `True` or
`False`. These are known as Boolean values. The Boolean operators include
`and`, `or`, and `not`. You will also be introduce to the `while` loop, which
uses a conditional statement to stop the loop. In addition, you will be
introduced to the `continue` and `break` statements, which can be used with
both `for` and `while` loops to skip ahead or stop the loop entirely.

Next, follow `06_loops_and_conditionals.py`. The examples here demonstrate how
mixing loops and conditionals can make complex structures.

The tutorials are very short this lesson in order to make room for lots of
programming practice using loops and conditionals.

## Coding Exercises ##

For programming practice, try writing the following programs, which you will
find in the usual `Programs` directory.

1. `03_gc.py`
2. `04_fizzbuzz.py`
3. `05_atseq.py`
4. `06_anti.py`
5. `07_frame.py`
7. `08_aapairs.py`
7. `09_gcwin1.py`
8. `10_gcwin2.py`

## Python Manifest ##

### Operators

	and
	not
	or

### Keywords

	while
	break
	continue

### Functions


### Libraries

	random

## File Manifest ##

	Tutorials/05_conditionals.py
	Tutorials/06_loops_and_conditionals.py
	Programs/03_gc.py
	Programs/04_fizzbuzz.py
	Programs/05_atseq.py
	Programs/06_anti.py
	Programs/07_frame.py
	Programs/08_aapairs.py
	Programs/09_gcwin1.py
	Programs/10_gcwin2.py

Lesson 4: Tuples and Lists
==========================

## Learning Objectives ##

* tuples - immutable, comma separated values (in parentheses)
* lists - mutable, comma separarted values [in brackets]
* list functions - append(), pop(), insert(), sort()

## Tutorials ##

In `07_lists.py`, you will learn how to create tuples and lists. The Python
*list* is what other languages call an *array*. A lot of the work in
programming is done by iterating over lists. You will also be introduced to the
`zip()` and `enumerate()` functions. Finally, you will see a bit of optional
syntactic sugar called *list comprehension*.

## Coding Exercises ##

For programming practice, try writing the following programs. The instructions
and expected output are inside each file as usual.

1. `11_birthday.py`
2. `12_entropy.py
3. `13_stats.py`
4. `14_xcoverage.py`

## Python Manifest ##

### Operators

	,
	[]

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

	Tutorials/07_lists.py
	Programs/11_birthday.py
	Programs/12_entropy.py
	Programs/13_stats.py
	Programs/14_xcoverage.py


Lesson 5: Functions
===================

## Learning Objectives ##

* Define functions
* Use assertions
* Open and read from named files
* Search for items inside lists

## Tutorials ##

First, try out `08_functions.py`, where you will learn how to write blocks of
code that perform specific duties whenever you call them. Functions are the
building blocks of complex programs. Here, you will also observe that floating
point math is an approximation of real math. As a result, we have to use
functions like `math.isclose()` to check for equality. This tutorial also
introduces `assert()`, which you can use to ensure your functions receive
proper values.

Next, go on to `09_files.py`, where you will learn to read files.

## Coding Exercises ##

For programming practice, try writing `15_transmembrane.py` in the Programs
directory.

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

	Tutorials/08_functions.py
	Tutorials/09_files.py
	Programs/15_transmembrane.py


Lesson 6: Dictionaries & Data Structures
========================================

## Learning Objectives ##

+ Use dictionaries for efficient look up
+ Create dictionaries for counting
+ Sort by dictionaries by key or value
+ Represent complex data from lists and dictionaries
+ Relate lists, dictionaries, spreadsheets, and JSON to each other

## Tutorials ##

`10_dictionaries.py`
`11_data_structures.py`

## Coding Exercises ##

You will find the following files in the Programs folder.

1. `16_aacomp.py`
2. `17_kmers.py` - count up kmers in a sequence file
3. `18_translate.py` - translate some RNA to protein
4. `19_iid.py` - is IID really IID?

## Python Manifest ##

### Keywords

### Operators

### Functions

### Methods

	dict.keys()
	dict.values()
	dict.items()

### Libraries

## File Manifest ##

	Tutorials/10_dictionary.py
	Programs/16_aacomp.py
	Programs/17_


Lesson 7: Modules and CLI
=========================

## Learning Objectives ##

+ Make your own function library
+ Use argparse to provide a typical Unix command line interface

## Tutorials ##

The tutorials this lesson are a little different from before. Both
`xx_module.py` and `xx_argparse.py` are really short. They are more like
templates for future code than actual tutorials.

Modules (the python word for libraries) are the currency of professional
programmers. Developers write and share libraries. In addition to using other
peoples' libraries, you should also write your own even if you don't share your
code with lots of people. Functions make your code more organized.

The command line interface (CLI) has standards. If you want your program to
look and feel like a typical Unix program (and you do) then use `argparse` to
capture your command line parameters and provide a help interface. We will no
longer be using `sys.argv` to get data into programs because `argparse` is much
better.

## Coding Exercises ##

You will find the following program directions in the Programs folder.

1. `xx_orfogram.py`
2. `xx_seqstats.py`
3. `xx_dust.py`

## Python Manifest ##

### Keywords

### Operators

### Functions

### Methods

### Libraries

	argparse

## File Manifest ##



Lesson 8: ?
=========================

Possible topics

- numpy, scipy
- matplotlib
- notebook
- regex
- data structures vs other things

## Learning Objectives ##

+

## Tutorials ##

12_

## Coding Exercises ##

You will find the following program directions in the Programs folder.


## Python Manifest ##

### Keywords

### Operators

### Functions

### Methods

### Libraries


## File Manifest ##

