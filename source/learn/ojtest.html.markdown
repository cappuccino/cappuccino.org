`OJTest` is a collection Framework that aim to provide a comprehensive testing solution for Cappuccino applications. The `OJTest` frameworks is another repositoty of the Cappuccino project. You can find it [here](https://github.com/cappuccino/OJTest).

`OJTest` are the perfect frameworks to create unit-tests and test algorithms. `OJTest` runs in a shell and do not use any headless browser, it means that no DOM element are created along with your tests. To achieve DOM element testing, you can take a look to the next topic [cucapp](/learn/cucapp.html).

These frameworks are used to test the Framework Cappuccino, you can find a lot of examples in the folder `Tests/` of the Cappuccino's source.

### Installation

OJTest is installed by default when you install Cappuccino from the source. If you did not do it, please follow the tutorial [Advanced: Install from Source](/learn/build-source.html).

Once Cappuccino installed, you do not have the last version of `OJTest` installed. If you like adventure and you would like to use the latest version of `OJTest`, please follow the following procedure.

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


### OJUnit - a xUnit Framework

To explain how OJUnit works, we are going to create a very simple test to check if one feature of the class `CPDateFormatter` works as expected.

#### Structure of your test file

One of the first rule you need to follow when creating tests is the name of your test file. OJTest will only launch tests on files name which follow the pattern `*Test.j`. In our case `CPDateFormatterTest.j`.

Secondly, you need to create a class which has the <b>exact class name as the name of your file</b>. This class should inherit from `OJTestCase`.

`OJTest` gives possibilities to setup and clean your environement before and after your test as well.

    :::objj
    @import <Foundation/Foundation.j>
    @import <OJUnit/OJTestCase.j>

    @implementation CPDateFormatterTest : OJTestCase
    {
    }

    // Only called one time, before every tests
    + (void)setUp
    {
        // You could here create data files you are about to use in a test
    }

    // Only called one time, after every tests
    + (void)tearDown
    {
        // You could here delete the data files created in the setUp
    }

    // Called before each test
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

    // Called after each test
    - (void)tearDown
    {
        // You could here do extra works on your test environement
    }

    @end

#### Write the test

This method is a test to check if the method `CPDateFormatter -stringFromDate` works as expected with a specific environement.

    :::objj
    - (void)testStringFromDateDateFullStyleTimeFullStyle
    {
        // Here we put the environment we want to test
        [_dateFormatter setDateStyle:CPDateFormatterFullStyle];
        [_dateFormatter setTimeStyle:CPDateFormatterFullStyle];

        // Here we send a message stringFromDate to an instance of CPDateFormatter
        var result = [_dateFormatter stringFromDate:_date];

        // Here we test if the result is the one we expect
        [self assert:result equals:@"Wednesday, October 5, 2011 6:34:38 PM Pacific Daylight Time"];
    }

One of the first thing you should notice, the name of the method starts with the key word test. This is a <b>must do</b>, it allows `OJTest` to know which methods are running tests.

As you can see, we advice to seperate your test in three different parts. The first one is about the environement you want to use for your test, the second is the action you want to realize and the third one is the result you want to check.

Also we advice to test one only thing per test. This will help you and your team when a test will fail in the future. And they will !

#### Launch the tests

Simply use the command `ojtest` on the targeted file :

    :::bash
    ojtest path/to/your/test/repository/CPDateFormatterTest.j

### OJMoq - a mocking Framework

`OJMoq` allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.

It provides a core `OJMoqSpy` class removing the need to create a host of stubs throughout your test suite. After performing an action, you can make assertions about which methods / attributes were used and arguments they were called with.

`OJMoq` can be used for a lot of different scenarios! For instance it's the perfect tool to test if a class calls delegate or dataSource methods with the good arguments and in order.

#### Write a test

Let's check the behavior of the `CPTableView`'s dataSource. For a data set of five objects, we know that the method `-numberOfRowsInTableView:` should be called one time and the method `tableView:objectValueForTableColumn:row:` should be called five times while the argument row should increase from zero to four.

    :::objj
    @import <Foundation/Foundation.j>
    @import <AppKit/AppKit.j>
    @import <OJMoq/OJMoq.j>

    @implementation CPTableViewTest : OJTestCase
    {
        CPArray         _datas;
        CPTableView     _tableView;
        CPTableColumn   _tableColumn;

        OJMoqSpy    dataSourceSpy
    }

    - (void)setUp
    {
        // This will init the global var CPApp which are used internally in the AppKit
        [[CPApplication alloc] init];

        _datas = [1, 2, 3, 4, 5];

        // Here we create our CPTableView
        _tableView = [[CPTableView alloc] initWithFrame:CGRectMake(0, 0, 100, 100)];
        _tableColumn = [[CPTableColumn alloc] initWithIdentifier:@"Foo"];

        [_tableView addTableColumn:_tableColumn];

        [_tableView setDataSource:self];

        // Here we create a spy which will spy the class CPTableViewTest
        dataSourceSpy = spy(self);
    }

    - (void)tearDown
    {
        [dataSourceSpy reset];
    }

    - (void)testDataSourceCPTableView
    {
        // Reset the spy here, make sure to have an empty state when beginning the test
        [dataSourceSpy reset];

        // As the class CPTableViewTest is the dataSource of the CPTableView, the following methods should be called when reloading the data
        [dataSourceSpy selector:@selector(numberOfRowsInTableView:) times:1 arguments:[_tableView]];
        [dataSourceSpy selector:@selector(tableView:objectValueForTableColumn:row:) times:1 arguments:[_tableView, _tableColumn, 0]];
        [dataSourceSpy selector:@selector(tableView:objectValueForTableColumn:row:) times:1 arguments:[_tableView, _tableColumn, 1]];
        [dataSourceSpy selector:@selector(tableView:objectValueForTableColumn:row:) times:1 arguments:[_tableView, _tableColumn, 2]];
        [dataSourceSpy selector:@selector(tableView:objectValueForTableColumn:row:) times:1 arguments:[_tableView, _tableColumn, 3]];
        [dataSourceSpy selector:@selector(tableView:objectValueForTableColumn:row:) times:1 arguments:[_tableView, _tableColumn, 4]];

        // Let's check that nothing is called with the argument row equals to 5
        [dataSourceSpy selector:@selector(tableView:objectValueForTableColumn:row:) times:0 arguments:[_tableView, _tableColumn, 5]];

        // We reload the data here and flush the run loop
        [_tableView reloadData];
        [[CPRunLoop currentRunLoop] limitDateForMode:CPDefaultRunLoopMode];

        // We verufy that every expectations were met
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

You should play with this example; try to change the order of the selectors or change the argument times and you will see how the test fails.

### The ojtest command

The command `ojtest` comes with different options, some of them are very usefull when debugging/testing an application.

You can stop to run your suite of tests after the first failure or error test with the option x :

    :::bash
    ojtest -x Tests/Foundation/CPDateFormatterTest.j

You can only launch one test of a test file by respecting the following format:

    :::bash
    ojtest Tests/Foundation/CPDateFormatterTest.j:testStringFromDateDateFullStyleTimeFullStyle

You can run the test coverage along with your OJUnit test :

    :::bash
    ojtest Tests/Foundation/CPDateFormatterTest.j

### Addtional Info

OJTest provides a doxygen help, you will find this help in the folder documentation of the repository OJTest.

If you have suggestions for improvements to this guide, or if you have
questions that haven't been answered here, please let us know on
[gitter](https://gitter.im/cappuccino/cappuccino).

