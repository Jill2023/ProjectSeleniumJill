Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@Jill2023 
SeleniumHQ
/
selenium
Public
Fork your own copy of SeleniumHQ/selenium
Code
Issues
145
Pull requests
34
Actions
Projects
1
Wiki
Security
Insights
You’re making changes in a project you don’t have write access to. We’ve created a fork of this project for you to commit your proposed changes to. Submitting a change will write it to a new branch in your fork, so you can send a pull request.
selenium
/
README.md
in
SeleniumHQ:trunk
 

Spaces

2

Soft wrap
1
# Selenium
2
​
3
[![CI](https://github.com/SeleniumHQ/selenium/actions/workflows/ci.yml/badge.svg?branch=trunk&event=schedule)](https://github.com/SeleniumHQ/selenium/actions/workflows/ci.yml)
4
​
5
<a href="https://selenium.dev"><img src="https://selenium.dev/images/selenium_logo_square_green.png" width="180" alt="Selenium"/></a>
6
​
7
Selenium is an umbrella project encapsulating a variety of tools and
8
libraries enabling web browser automation. Selenium specifically
9
provides an infrastructure for the [W3C WebDriver specification](https://w3c.github.io/webdriver/)
10
— a platform and language-neutral coding interface compatible with all
11
major web browsers.
12
​
13
The project is made possible by volunteer contributors who've
14
generously donated thousands of hours in code development and upkeep.
15
​
16
Selenium's source code is made available under the [Apache 2.0 license](https://github.com/SeleniumHQ/selenium/blob/trunk/LICENSE).
17
​
18
## Documentation
19
​
20
Narrative documentation:
21
​
22
* [User Manual](https://selenium.dev/documentation/)
23
​
24
API documentation:
25
​
26
* [C#](https://seleniumhq.github.io/selenium/docs/api/dotnet/)
27
* [JavaScript](https://seleniumhq.github.io/selenium/docs/api/javascript/)
28
* [Java](https://seleniumhq.github.io/selenium/docs/api/java/index.html)
29
* [Python](https://seleniumhq.github.io/selenium/docs/api/py/)
30
* [Ruby](https://seleniumhq.github.io/selenium/docs/api/rb/)
31
​
32
## Pull Requests
33
​
34
Please read [CONTRIBUTING.md](https://github.com/SeleniumHQ/selenium/blob/trunk/CONTRIBUTING.md)
35
before submitting your pull requests.
36
​
37
## Requirements
38
​
39
* [Bazelisk](https://github.com/bazelbuild/bazelisk), a Bazel wrapper that automatically downloads
40
  the version of Bazel specified in `.bazelversion` file and transparently passes through all
41
  command-line arguments to the real Bazel binary.
42
* Java JDK version 11 or greater (e.g., [Java 11 OpenJDK](https://openjdk.java.net/))
43
* `java` and `jar` on the `$PATH` (make sure you use `java` executable from JDK but not JRE).
44
  * To test this, try running the command `javac`. This command won't exist if you only have the JRE
No file chosen
Attach files by dragging & dropping, selecting or pasting them.
Styling with Markdown is supported
@Jill2023
Propose changes
Commit summary
Create README.md
Optional extended description
Add an optional extended description…
 
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
