I'm giving a talk at PyCon next month called "Systems programming as a swiss
army knife". Almost all of my talks start off as blog posts, so, let's start!

It's at PyCon, which is meant to be a Python programming conference. In this
talk, I want to explain to you how to debug your Python programs without
knowing or using Python. Everything in this talk generalizes to *any* other
programming language.

You have an operating system on your computer, every single program you write
is constantly interacting with it, and there are tons of generic tools you can
use to get it tell you what it's up to. So we're going to **make friends with
our operating system**.

The operating system I'll talk about here is Linux, because practically every
machine I use runs Linux, and in any case it's all I know about.

### What do I mean by a "systems tool"?

There are (at least) two ways to debug a program. You can 

a) use a programming-language specific profiling or debugging tool, or 
b) use an operating-system specific tool

### The case of the mystery configuration file



### The case of the slow client

You're in an interview, and you're handed 3 programs. They're all slow, for
three totally different reasons:

* is doing a CPU-intensive operation
* is reading a ton of data over a slow connection
* is trying to communicate with servers that are overloaded and slow to respond

You need to figure out which one is which, and you have 10 minutes. How do you
spend those 10 minutes?

### The CPU-intensive operation

I actually have no idea how to identify this!

### Is my program CPU-bound or I/O bound?

The regular Python way to measure this is: read the 


So, let's talk about things your operating system knows, and how you can ask for them

### Which files are open? (lsof)

Is `mount` telling you that 

### Wk

### iostat




Instead it's a talk
about systems and Linux and how better understanding your operating system
makes you a better programmer.


And to me it actually feels weird to go to a Python conference and watch a
whole bunch of Python talks, because, honestly, I don't really care that much about
Python. It's probably maybe the language I'm the most comfortable


