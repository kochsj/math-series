# Math-Series

**Author**: Stephen Koch
**Version**: 1.0.0

## Overview
Given a number "N", this code involves finding the Nth [Fibonacci Number](https://en.wikipedia.org/wiki/Fibonacci_number) and finding the Nth [Lucas Number](http://en.wikipedia.org/wiki/Lucas_number). Additionally, given a number "N" and two optional parameters, "first_number" and "second_number", the sum_series function will return the Nth value of a fibonacci series with any two starting numbers.

## Getting Started

First, make sure that you have python3 installed:
```
$ python3 --version
Python 3.7.5
```
If you do not:
```
$ brew install python
```
You need to have the files locally. Click on the green clone or download button and Download ZIP:

![Click_to_download](/assets/Click_to_download_x6c0g16lz.png)


In your command line, navigate to this directory:
```
$ cd ~  ##this is your root directory
$ cd Downloads  ##running MacOS: Downloads is a directory inside of your root; and where your file will be downloaded
```
This module is running tests on a given number. Install [pytest](https://docs.pytest.org/en/latest/getting-started.html) to get started:
Installing pytest:
```
$ pip install -U pytest
```
Running tests:
```
$ pytest
```
<!-- To change the input "N", you  -->

## Architecture
When the tests are run, the fibonacci, lucas, and sum_series functions are invoked.
Functions return the resulting value through recursion.
Inputs default to a fibonacci number, starting the series at 0, 1.
If the optional inputs are given, the series will start at those given inputs.
Tests will pass if the expected result is returned from the function.

## Change Log
-- Tue Dec 03 2019 18:09:02 --
Built out series.py module with three functions; Fibonacci, lucas, and sum_series. Sum_series function does the work of both functions.

