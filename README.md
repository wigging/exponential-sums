# Exponential Sums

The `expsum` package plots several functions as exponential sums. This work is inspired by John Cook's article "[Exponential sums make pretty pictures][1]".

An exponential sum is represented by the formula 

<img src="assets/expsum.pdf" height="90"/>

where f is a real-valued function defined on positive integers.

## Installation and Usage

Just clone this repository and run the following command:

```bash
python expsum func1
```

## Examples

Functions available in the `expsum` package are listed below. Examples of plotting each function as an exponential sum are also provided. 

### Function 1

<img src="assets/func1eq.pdf" height="50"/>

```bash
>>> python expsum func1 2000 10 7 17
```

<img src="assets/func1a.pdf" height="400"/>

```bash
>>> python expsum func1 8000 11 21 31
```

<img src="assets/func1b.pdf" height="400"/>

### Function 2

<img src="assets/func2eq.pdf" height="50"/>

```bash
>>> python expsum func2 1200 100
```

<img src="assets/func2a.pdf" height="400"/>

```bash
>>> python expsum func2 4000 800
```

<img src="assets/func2b.pdf" height="400"/>

### Function 3

<img src="assets/func3eq.pdf" height="30"/>

```bash
>>> python expsum func3 1000
```

<img src="assets/func3a.pdf" height="400"/>

```bash
>>> python expsum func3 4000
```

<img src="assets/func3b.pdf" height="400"/>

### Function 4

<img src="assets/func4eq.pdf" height="30"/>

```bash
>>> python expsum func4 4000 4
```

<img src="assets/func4a.pdf" height="400"/>

### Function 5

<img src="assets/func5eq.pdf" height="40"/>

```bash
python expsum func5 4000 50 100
```

<img src="assets/func5a.pdf" height="400"/>

### Function 6

<img src="assets/func6eq.pdf" height="40"/>

```bash
>>> python expsum func6 2000 4
```

<img src="assets/func6a.pdf" height="400"/>

### Function 7

<img src="assets/func7eq.pdf" height="40"/>

```bash
>>> python expsum func7 8000 4
```

<img src="assets/func7a.pdf" height="400"/>


## Contributing

Submit a Pull Request if you would like to contribute to this project. Questions and other comments can be submitted on the Issues page. Or you can leave me a tip to show your appreciation of open source code.

## Tip Jar

If you have found this project interesting, please consider making a donation at [paypal.me/gavinwiggins](https://www.paypal.me/gavinwiggins). Thank you 😁

## References

1. John D. Cook. Exponential sums make pretty pictures. October 7, 2017. [Link][1]
2. David Angell. Exponential sums. School of Mathematics and Statistics, UNSW. Accessed July 7, 2019. [Link][2]
3. here

[1]: https://www.johndcook.com/blog/2017/10/07/exponential-sums-make-pretty-pictures/
[2]: https://www.maths.unsw.edu.au/about/exponential-sums