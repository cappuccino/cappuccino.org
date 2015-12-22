OJTest is a collection Framework that aim to provide a comprehensive testing solution for Cappuccino applications. The OJTest framework is another repositoty of the Cappuccino project. You can find it [here](https://github.com/cappuccino/OJTest).

OJTest are the perfect frameworks to create unit-tests and test algorithms. OJTest runs in a shell and do not use any headless browser, it means that no DOM element are created along with your tests. To achieve that, you can take a look to the next topic [cucapp](/learn/cucapp.html).

These frameworks are used to test the Framework Cappuccino, you can find a lot of examples in the folder `Tests/` of the Cappuccino's source.

### Installation

OJTest is installed by default when you install Cappuccino from the source. If you did not do it, please follow the tutorial [Advanced: Install from Source](/learn/build-source.html).

Once Cappuccino installed, you do not have the last version of OJTest installed. If you like adventure and you would like to use the latest version of OJTest, please follow the following procedure.

Firstly clone the git repository of OJTest :

    :::bash
    git clone https://github.com/cappuccino/OJTest

Then move to the OJTest directory and launch the install command :

    :::bash
    cd OJTest; jake install

To be sure everything runs fine, verify that you have the ojtest command in your PATH:

    :::bash
    # ojtest -h
    Usage: ojtest [OPTIONS] INPUT_FILE ...
    [...]


### OJUnit - an xUnit Framework

To explain how OJUnit works, we will follow the tests created to test the Cappuccino class `CPDateFormatter`. You can find these tests in the Cappuccino repository in `Tests/Foundation/CPDateFormatterTest.j`.

#### Structure of your test file

One of the first rule you need to follow when creating tests is the name of your test file. OJTest will only launch tests on files name which follow the pattern `*Test.j`. In our case `CPDateFormatterTest.j`.

Secondly, you need to implemente a class with the exact same name as the name of your file. This class should inherit from `OJTestCase`

    :::objj
    @import <Foundation/Foundation.j>
    @import <OJUnit/OJTestCase.j>

    @implementation CPDateFormatterTest : OJTestCase
    {
    }

    @end

The class OJTestCase comes with different features, as every decent testing framework it provides an API to install or clean your environement.

It provides the class methods `+setUp` and `+tearDown`, these methods are only call one time, setUp before the first test is launched and tearDown just after the last test was launched.

    :::objj
    + (void)setUp
    {
        // You could here create data files you are about to use in a test
    }

    + (void)tearDown
    {
        // You could here delete the data files created in the setUp
    }

Then it provides the instance methods `-setUp` and `-tearDown`, these methods are call between each tests.

    :::objj
    - (void)setUp
    {
        // Here we create a CPDate and a CPDateFormatter
        // These objects are going to be used for our tests
        _date = [[CPDate alloc] initWithString:@"2011-10-05 16:34:38 -0900"];

        _dateFormatter = [[CPDateFormatter alloc] init];
        [_dateFormatter setDateStyle:CPDateFormatterMediumStyle];
        [_dateFormatter setTimeStyle:CPDateFormatterShortStyle];
        [_dateFormatter setLocale:[[CPLocale alloc] initWithLocaleIdentifier:@"en_US"]];
        [_dateFormatter setTimeZone:[CPTimeZone timeZoneWithAbbreviation:@"PDT"]];
    }

    - (void)tearDown
    {
        // You could here do extra works on your test environement
    }


#### Write a test

Let's take a look to the following test :

    :::objj
    - (void)testStringFromDateDateFullStyleTimeFullStyle
    {
        // Here we put the environment we want to test
        [_dateFormatter setDateStyle:CPDateFormatterFullStyle];
        [_dateFormatter setTimeStyle:CPDateFormatterFullStyle];

        // Here we send a message stringFromDate to an instance of CPDateFormatter
        var result = [_dateFormatter stringFromDate:_date];

        // Here we test if the result is what we expect
        [self assert:result equals:@"Wednesday, October 5, 2011 6:34:38 PM Pacific Daylight Time"];
    }

One of the first thing you should notice is the name of this method starts with the key word test. This is a must do, it allows OJTest to know which methods are running tests.

As you can see, we advice to seperate your test in three different parts. The first one is about the environement you want to use for your test, the second is the action you want to realize and the third one is the result you want to test.

Also we advice to only test one only thing per test. This will help you and your team when a test will fail in the future. And they will !

#### Launch the tests

Simply use the command `ojtest` on the targeted file :

    :::bash
    ojtest Tests/Foundation/CPDateFormatterTest.j

#### Documentation

OJTest provides a doxygen help, you will find this help in the folder documentation of the repository OJTest.


### OJMoq - a mocking Framework

### The ojtest command

The command `ojtest` comes with different options, some of them are very usefull when debugging/testing an application.

You can stop to run your suite of tests after the first failure or error test with the option x :

    :::bash
    ojtest -x Tests/Foundation/CPDateFormatterTest.j

You can only launch one test of a test file by respecting the following format:

    :::bash
    ojtest Tests/Foundation/CPDateFormatterTest.j:testStringFromDateDateFullStyleTimeFullStyle

Run the test coverage along with your OJUnit test :

    :::bash
    ojtest Tests/Foundation/CPDateFormatterTest.j

### Addtional Info

If you have suggestions for improvements to this guide, or if you have
questions that haven't been answered here, please let us know on
[gitter](https://gitter.im/cappuccino/cappuccino).

