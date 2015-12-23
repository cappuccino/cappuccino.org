`Cucapp` is a framework which allows you to create tests in [Cucumber](https://cucumber.io) for testing your Cappuccino Application. `Cucapp` can be used either for unit-testing or functional testing. `Cucapp` is a tool which can be used in a black / grey / white box testing.

By default `Cucapp` will launch the browser firefox when running the tests. We advise you to work with a headless browser like [phantomjs](http://phantomjs.org) though.

When launching your tests with `Cucapp`, the Cappuccino application is served via a [thin](http://code.macournoyer.com/thin/) server and a small piece of code is injected. This code connects back to your Cucumber script via AJAX requests.

`Cucapp` provides an abstract layer of steps to simulate actions and check values of controls.

The `Cucapp` framework is another repository of the Cappuccino project. You can find it [here](https://github.com/cappuccino/cucapp).

### Installation

Cappuccino has to be installed to use `Cucapp`. If not please follow the tutorial [Advanced: Install from Source](/learn/build-source.html).

`Cucapp` is not installed at the same time as Cappuccino. Please follow the procedure below.

<span class="label label-info">Info</span> Ruby needs to be installed on your system. We advise to work with [RVM](http://rvm.io). It allows to easily manage a ruby environment.

To get started, download the current version of Cuccap:

    :::bash
    git clone git://github.com/cappuccino/cucapp.git

Then install `Cucapp` on your system:

    :::bash
    cd cucapp; jake install

When installing `Cucapp`, the following gems are going to be installed `Cucumber`, `Thin`, `Nokogiri`, `JSON` and `Watir-Webdriver`.

To be sure everything runs fine, verify that you have the `cucapp` command in your PATH:

    :::bash
    # cucapp
    Usage: cucapp [OPTIONS] -p PATH ...

### The cucapp command

The `cucapp` has only one goal yet. It allows you to create a testing architecture for your Cappuccino Application.

Launch `cucapp` on the targeted application with the following command:

    :::bash
    cucapp -p path/to/your/application

When performing this command, `cucapp` will create a folder `features` in your application. This folder contains default Cucumber steps and utilities to easily create tests for your application.

A new task will be added to your `Jakefile` as well. The new command `jake cucumber-test` will launch the Cucumber tests on your application.

You should see that the category `CPResponder+CuCapp.j` has been added as well. This category adds the property `cucappIdentifier` to the `CPResponder` class.

### Usage

To explain how `Cucapp` works, we are going to test the application created in the tutorial [Xcode Interface Builder](/learn/xcode-basics.html). You can find the source of this application [here](files/AdvancedHelloWorld.zip).

Unzip the file AdvancedHelloWorld.zip and launch the command below:

    :::bash
    cd AdvancedHelloWorld; capp gen -fl .; nib2cib Resources/MainMenu.xib

#### Link Cucapp to the project

The first step to create tests for this application is to link `Cucapp` to this project. Please do:

    :::bash
    cucapp -p path/to/AdvancedHelloWorld/

Once done you should see the folder features in AdvancedHelloWorld.

#### Create the test

First, for this test we need to make few modifications in the `AppController`. We need to import the category `CPResponder+CuCapp.j` and set a `cucappIdentifier` to the `CPTextField`. This allows us to have an unique identifier for our CPTextFields.

    :::objj
    /*
     * AppController.j
     * AdvancedHelloWorld
     *
     * Created by You on December 8, 2011.
     * Copyright 2011, Your Company All rights reserved.
     */

    @import <Foundation/CPObject.j>

    @import "CPResponder+Cucapp.j"

    @implementation AppController : CPObject
    {
        /* this "outlet" is connected automatically by the Cib */
        CPWindow    theWindow;

        /* We create the outlets of the textfields here */
        @outlet CPTextField myTextField;
        @outlet CPTextField myLabel ;

        /* As you can see, the label is also a CPTextField, it's just not editable and not bordered.
           It is important you declare correctly the class names of the outlets, or Xcode, won't see them.
        */
    }

    - (void)awakeFromCib
    {
        /* This is called when the cib is done loading.
           You can implement this method on any object instantiated from a Cib.
           It's a useful hook for setting up current UI values, and other things.
           In this case, we want the window from Cib to become our full browser window
        */
        [theWindow setFullPlatformWindow:YES];

        [myTextField setCucappIdentifier:@"myTextField"];
        [myTextField setCucappIdentifier:@"myLabel"];
    }

    - (IBAction)sayHello:(id)aSender
    {
       /* We get the content of the textfield
          and we set it as the value of the label
       */
       [myLabel setStringValue:[myTextField stringValue]];
    }

    @end

Now, we need to write our test. The test will be very easy, we will simulate an user who is typing the word Cucumber, then hitting enter and finally we will check that the word Cucumber is shown in the label.

For that, open the file test_application.feature in the folder features and modify it as below :

    :::gherkin
    Feature: Demo of cucapp
    This test is used to make a demo of cucapp

      Scenario: Check if the demo application works
        Given the application is launched
        When I hit the keys cucumber
        When I hit the key enter
        Then the field with the property cucapp-identifier set to myLabel should have the value cucumber

These steps are provided by `Cucapp`. More default steps (click, drag and drop, scrolling etc.) can be used, you can find them in the [documentation](https://github.com/cappuccino/cucapp) of `Cucapp`.

#### Launch the tests

Simply use the command below :

    :::bash
    jake cucumber-test

And voilà! If everything worked as expected you should have seen that the browser opened itself, then actions were performed in the interface and finally you terminal showed that the tests passed.

![](cucapp-1-terminal.png)

You can find the source of this demo [here](files/AdvancedHelloWorldCucapp.zip).

### Additional Info

If you have suggestions for improvements to this guide, or if you have
questions that haven't been answered here, please let us know on
[gitter](https://gitter.im/cappuccino/cappuccino).