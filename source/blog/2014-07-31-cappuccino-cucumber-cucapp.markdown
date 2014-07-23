---
title: Cucumber + Cappuccino = Cucapp
author: Alexandre Wilhelm
author_email: alexandre.wilhelmfr@gmail.com
date: '2014-07-31'
tags:
- Cucumber
- Cucapp
- test
- Automation test
- Functional test
- Nuage Networks
---

At [Nuage Networks](http://www.nuagenetworks.net) we needed to find a solution regarding the testing of our [Cappuccino application](http://www.cappuccino-project.org/blog/2014/07/cappuccino-in-action-nuage-networks.html). We now have two different suits of tests : unit-test and functional-test.

[OJTest](https://github.com/cappuccino/OJTest) satisfies all of our needs for unit-testing. We found a large number of examples in Cappuccino itself to do what we wanted to do.

For the functional tests, we decided that [Cucumber](http://cukes.info) would be well suited to our needs. We took a look at [Cucapp](https://github.com/cappuccino/cucapp) and improved it. Guess what, it's awesome ! Let me explain how Cappuccino and Cucumber can work together.

### Philosophy of Cucapp

Cucapp is an interface between Cucumber and Cappuccino. The Cappuccino application is served by a [Thin](http://code.macournoyer.com/thin/) server and a small piece of code is injected into the Cappuccino application. This piece of code connects the Cucumber scripts and the Cappuccino application via AJAX requests.

Once Cucumber was able to talk to our Cappuccino application , we wanted to simulate what a user could do with the application. Our first thought was "Wow, a user can do whatever he wants, there are unlimited possibilities". In reality, a user can only do a small amount of things :

* He can hit a key(s) on his keyboard
* He can do basic actions with his mouse (left click, right click, moving etc etc...)

And that's it ! Our first job was to create new features in Cucapp for simulating user's action in our Cappuccino Application. We then added some features to help us easily launch our tests.

### Cucapp's features

##### Environment variables

Cucapp provides a set of environment variables :

* `CUCAPP_PORT` allows you to specify the port used by the server Thin.
* `CUCAPP_APPDIRECTORY` allows you to specify where the Cappuccino application is located.
* `CUCAPP_BUNDLE` allows you to specify if you want to use the compiled version of Cucapp.
* `CUCAPP_APPLOADINGMODE` allows you to specify which version (build or debug) of your Cappuccino application you want to test.

##### Core of Cucapp

The file Cucumber.j and HelperCategories.j (injected in the tested Cappuccino application) are the core of Cucapp. It's in these files (injected in our Cappuccino application when launching the test) that the relation between Cucumber and Cappuccino is made. What do these files do ?

- `Cappuccino+Cucumber.j` contains a category to the class `CPApplication`. The category adds the method `-(CPString)xmlDescription`. This method creates a XML dump which contains a reference of each `CPResponder` currently displayed. In the XML, each CPResponder is associated to a `xpath`. This unique xpath, which is a string (automatically generated from a CPResponder's title, identifier etc etc...), will be used in your test/features to target a specific CPResponder.
- The file Cucumber.j contains the class `Cucumber` which constantly listens the URI `/cucumber` on itself.
- The class `Cucumber` has a set of methods for simulating `CPEvent`.
- When launching a test, Cucapp will send requests POST on `/cucumber` with some data. This data contains information that the Cappuccino application will interprete. Basically, this data will be the name of a method (and their params) to call.

##### How does it work ?

Let's take an example of the simulation of a left click on a button.

Firstly, we create a feature which contains a simple scenario (these are cucumber features, you should take a look [here](https://github.com/cucumber/cucumber/wiki/Feature-Introduction))

    :::gherkin
    Scenario: Open the popover with a click on the add button
        Given the user make a left shift click on the add button

And then, we create our ruby step :

    :::ruby
    Given /^the user make a left shift click on the add button$/ do
      app.gui.simulate_left_click         "//CPButton[title='add']", [$CPShiftKeyMask]
    end

As you can see, the `simulate_left_click` method contains two params :

- The first param is the `xpath` of the button.
- The second params is an array of key masks you want to simulate (for example `$CPCommandKeyMask` or/and `$CPShiftKeyMask`). All of these masks are available in the framework Cucapp in `lib/encumber.rb`.

And this is it, simple as that ! You just simulated a left click on the button which has a title set to add.

##### What does Cucapp do for you ?

Once you tell Cucumber to simulate an event, Cucapp does the rest for you, it sends a request on `/cucumber` which asks to simulate a left click on a button. Data of the request contains the name of the method (simulateLeftClick:) to simulate the click and additional options (the key shift is pressed).

This is the final Objective-j method called in our Cappuccino application (this method is injected automatically by Cucapp, it comes from the file `lib/Cucumber.j`) :

    :::objj
    - (CPString)simulateLeftClick:(CPArray)params
    {
        var obj = cucumber_objects[params.shift()],
            locationWindowPoint;

        if (!obj)
            return '{"result" : "OBJECT NOT FOUND"}';

        if ([obj superview])
            locationWindowPoint = [[obj superview] convertPointToBase:CGPointMake(CGRectGetMidX([obj frame]), CGRectGetMidY([obj frame]))];
        else
            locationWindowPoint = CGPointMake(CGRectGetMidX([obj frame]), CGRectGetMidY([obj frame]));

        [self _perfomMouseEventOnPoint:locationWindowPoint toPoint:nil window:[obj window] eventType:CPLeftMouseDown numberOfClick:1 modifierFlags:params[0]];

        return '{"result" : "OK"}';
    }

##### Helpers

Two categories are used in Cucapp to help you to add new things and to use Cucapp more easily:

- `CPResponder+CuCapp.j` contains a category to the class CPResponder. The category adds the method `-(void)setCucappIdentifier:`. This cucappIdentifier could be used in the creating of xpath. You need to include this category in your Cappuccino application to use this category. With that, you can have xpath as //CPButton[cucappIdentifier='cucappIdentifier-button-bar-add'].

- `Cucumber+Extensions.j` will be loaded (optional) by Cucapp when launching Cucumber. This category allows you to add new Cappuccino methods needed for your tests (for instance a method to check the color of a CPView). This file has to be located in `features/support/Cucumber+CuCapp.j`.

##### Simulate user events

Cucapp provides a set of methods to simulate user events, here is what you can simulate from Cucumber:

    :::ruby
    def simulate_keyboard_event charac, flags
    def simulate_keyboard_events string, flags
    def simulate_left_click xpath, flags
    def simulate_left_click_on_point x, y, flags
    def simulate_double_click xpath, flags
    def simulate_double_click_on_point x, y, flags
    def simulate_dragged_click_view_to_view xpath1, xpath2, flags
    def simulate_dragged_click_view_to_point xpath1, x, y, flags
    def simulate_dragged_click_point_to_point x, y, x2, y2, flags
    def simulate_right_click xpath, flags
    def simulate_right_click_on_point x, y, flags
    def simulate_scroll_wheel xpath, deltaX, deltaY, flags


### Demo

A full demo of what Cucapp can do is available [here](https://github.com/Dogild/Cucapp-demo).

