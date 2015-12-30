OJTest is a collection of frameworks which aim to provide a comprehensive testing solution for Cappuccino applications. They are separate from Cappuccino itself. You can find the framworks [here](https://github.com/cappuccino/OJTest).

OJTest is used to create unit-tests and test algorithms. OJTest runs in a shell and, unlike say Cucapp, does not use a web browser. This means there are no DOM elements, the actual browser based bits and pieces that implement the UI in Cappuccino. You still have all the logic but it's running in a 'headless' mode so to speak. (To test with actual DOM elements in play (full UI simulation), see the next topic [Cucapp](/learn/cucapp.html).)

Cappuccino itself is tested using OJTest, so there are many examples in its source code on how to write tests. Check out the `Tests/` folder of the Cappuccino sources.

### Installation

OJTest is installed by default when you install Cappuccino from sources. If you did not do it, please follow the tutorial [Advanced: Install from Source](/learn/build-source.html).

Once Cappuccino is installed, you may choose to install the latest version of OJTest, which might be newer than the version included with Cappuccino. To do so, follow these steps.

First, clone the git repository of OJTest:

    :::bash
    git clone https://github.com/cappuccino/OJTest

Then enter the OJTest directory and launch the install command:

    :::bash
    cd OJTest
    jake install

Verify that `ojtest` is in your `PATH`:

    :::bash
    # ojtest -h
    Usage: ojtest [OPTIONS] INPUT_FILE ...
    [...]


### OJUnit - an xUnit Framework

To explain how OJUnit works we are going to create a very simple test to check if one feature of the class `CPDateFormatter` works as expected.

#### Structure of your test file

There is a rule for how to name your test files when working with OJTest. OJTest will only run tests found in files with names that follow the pattern `*Test.j`. In our example, let's name the test file `CPDateFormatterTest.j`.

Also, you need to name your test class inside of your test file to a <b>class name that exactly matches the name of your file</b>. The class should inherit from `OJTestCase`.

OJTest supports the `setUp` and `tearDown` methods like in other xUnit frameworks. They enable you to configure your test environment. Here's what we will use for this example.

    :::objj
    @import <Foundation/Foundation.j>
    @import <OJUnit/OJTestCase.j>

    @implementation CPDateFormatterTest : OJTestCase
    {
    }

    // Only called one time, before all the tests of the class.
    + (void)setUp
    {
        // You could load data from a test file here or otherwise configure your environment for your test.
    }

    // Only called one time, after all the tests of the class.
    + (void)tearDown
    {
        // If you did anything in + setUp that needs to be undone, this is where to do that.
    }

    // Called before each test.
    - (void)setUp
    {
        _date = [[CPDate alloc] initWithString:@"2011-10-05 16:34:38 -0900"];

        _dateFormatter = [[CPDateFormatter alloc] init];
        [_dateFormatter setDateStyle:CPDateFormatterMediumStyle];
        [_dateFormatter setTimeStyle:CPDateFormatterShortStyle];
        [_dateFormatter setLocale:[[CPLocale alloc] initWithLocaleIdentifier:@"en_US"]];
        [_dateFormatter setTimeZone:[CPTimeZone timeZoneWithAbbreviation:@"PDT"]];
    }

    // Called after each test.
    - (void)tearDown
    {
        // If you did anything in - setUp, this is there to undo it.
    }

    @end

#### Write the test

Here is the test we'll use for our example. It checks that `CPDateFormatter -stringFromDate` works as expected with a specific environment.

    :::objj
    - (void)testStringFromDateDateFullStyleTimeFullStyle
    {
        // Configure the environment we want to test.
        [_dateFormatter setDateStyle:CPDateFormatterFullStyle];
        [_dateFormatter setTimeStyle:CPDateFormatterFullStyle];

        // Send a message, stringFromDate, to an instance of CPDateFormatter.
        var result = [_dateFormatter stringFromDate:_date];

        // Test if the result is the one we expect.
        [self assert:result equals:@"Wednesday, October 5, 2011 6:34:38 PM Pacific Daylight Time"];
    }

Note that the name of the method starts with the keyword test. This is <b>required</b>: it allows `OJTest` to know which methods are actual tests.

We advise you to separate your tests into three different parts. Test specific setup, an action and finally verification. Try to test only one thing per test. This will allow you to give each test a clear and purposeful name so that when a test fails you'll immediately know what failed (and conversely, when it succeeds you know what exactly it is that works).


#### Launch the tests

To run our tests we'll use the `ojtest` command:

    :::bash
    ojtest CPDateFormatterTest.j


### OJMoq - a mocking Framework

OJMoq allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.

It provides a core `OJMoqSpy` class which eliminates the need to create a host of stubs throughout your test suite. After performing an action, you can make assertions about which methods / attributes were used and which arguments they were called with.

OJMoq can be used for a lot of different scenarios! For instance it's the perfect tool to test if a class calls delegate or dataSource methods with correct arguments.

#### Write a test

Let us check the behaviour of the `CPTableView`'s data source. For a data set with five objects, we know that the method `-numberOfRowsInTableView:` should be called one time and the method `tableView:objectValueForTableColumn:row:` should be called five times. The latter method should receive increasing `row` parameters, from zero to four.

Here's how we might test that.

    :::objj
    @import <Foundation/Foundation.j>
    @import <AppKit/AppKit.j>
    @import <OJMoq/OJMoq.j>

    @implementation CPTableViewTest : OJTestCase
    {
        CPArray         _datas;
        CPTableView     _tableView;
        CPTableColumn   _tableColumn;

        OJMoqSpy        dataSourceSpy
    }

    - (void)setUp
    {
        // AppKit requires this to work.
        [[CPApplication alloc] init];

        _datas = [1, 2, 3, 4, 5];

        // Create our CPTableView.
        _tableView = [[CPTableView alloc] initWithFrame:CGRectMake(0, 0, 100, 100)];
        _tableColumn = [[CPTableColumn alloc] initWithIdentifier:@"Foo"];

        [_tableView addTableColumn:_tableColumn];

        [_tableView setDataSource:self];

        // Create a spy which will spy the class CPTableViewTest.
        dataSourceSpy = spy(self);
    }

    - (void)tearDown
    {
        [dataSourceSpy reset];
    }

    - (void)testDataSourceCPTableView
    {
        // Make sure we have empty starting point for the spy at the beginning of our test.
        [dataSourceSpy reset];

        // As the class CPTableViewTest is the dataSource of the CPTableView, the following methods should be called when reloading the data.
        [dataSourceSpy selector:@selector(numberOfRowsInTableView:) times:1 arguments:[_tableView]];
        [dataSourceSpy selector:@selector(tableView:objectValueForTableColumn:row:) times:1 arguments:[_tableView, _tableColumn, 0]];
        [dataSourceSpy selector:@selector(tableView:objectValueForTableColumn:row:) times:1 arguments:[_tableView, _tableColumn, 1]];
        [dataSourceSpy selector:@selector(tableView:objectValueForTableColumn:row:) times:1 arguments:[_tableView, _tableColumn, 2]];
        [dataSourceSpy selector:@selector(tableView:objectValueForTableColumn:row:) times:1 arguments:[_tableView, _tableColumn, 3]];
        [dataSourceSpy selector:@selector(tableView:objectValueForTableColumn:row:) times:1 arguments:[_tableView, _tableColumn, 4]];

        // At the same time we know there should be no call for row 5.
        [dataSourceSpy selector:@selector(tableView:objectValueForTableColumn:row:) times:0 arguments:[_tableView, _tableColumn, 5]];

        // We reload the data here and flush the run loop.
        [_tableView reloadData];
        [[CPRunLoop currentRunLoop] limitDateForMode:CPDefaultRunLoopMode];

        // Were our expectations met?
        [dataSourceSpy verifyThatAllExpectationsHaveBeenMetInOrder];
    }

    @end


    @implementation CPTableViewTest (CPTableViewTestDataSource)

    - (int)numberOfRowsInTableView:(CPTableView)aTableView
    {
        return [_datas count];
    }

    - (id)tableView:(CPTableView)aTableView objectValueForTableColumn:(CPTableColumn)aColumn row:(CPInteger)aRow
    {
        return _datas[aRow];
    }

    @end

You should play with this example. Try to change the order of the selectors or change the `times` argument and you should see the test fail.

### The ojtest command

The command `ojtest` comes with different options. Some of them are very useful when debugging or testing an application.

You can stop your suite of tests after the first failure by using the `-x` option:

    :::bash
    ojtest -x Tests/Foundation/CPDateFormatterTest.j

You can launch a single test of a test file in this manner:

    :::bash
    ojtest Tests/Foundation/CPDateFormatterTest.j:testStringFromDateDateFullStyleTimeFullStyle

You can check the test coverage while running your OJUnit test by using the `-c option:

    :::bash
    ojtest -c Tests/Foundation/CPDateFormatterTest.j

### Additional Info

OJTest has a doxygen help document. You will find these docs in the `documentation` folder of the OJTest repository.

If you have suggestions for improvements to this guide, or if you have questions that haven't been answered here, please let us know on
[gitter](https://gitter.im/cappuccino/cappuccino).
