---
title: Synthesizing Accessor Methods
author: Ross Boucher
author_email: ross@280north.com
wordpress_id: 114
wordpress_url: http://cappuccino.org/discuss/?p=114
date: '2008-10-26'
categories:
- Objective-J
tags:
- Objective-J
- Accessor Synthesizing
- ! '@accessors'
---


Yesterday, Francisco and Tom checked in a new feature to the Cappuccino git repository, called accessor synthesizing. This is a new language feature for Objective-J, and its designed to reduce the amount of boilerplate code developers have to write in a custom class. Normally, when you write a custom class in Objective-J, you also write a pair of getter and setter methods for each instance variable (ivar) that you want to expose. This usually means writing repetitive code that hardly ever changes each time you write it. With accessor synthesizing, developers will only have to write getter and setter methods when something truly interesting needs to happen in those methods.

Accessor synthesizing adds a new keyword to the Objective-J language, **@accessors**. When declaring your list of ivars in the **@implementation** block of your class, adding this one keyword will tell the Objective-J preprocessor to implement accessors for you. Let's see an example of a simple class written using the old method, and then the same class using **@accessors**.

This Person class has two ivars, firstname and lastname. Before **@accessors**, the class looks like this:

    @implementation Person : CPObject
    {
        CPString firstName;
        CPString lastName;
    }

    - (void)setFirstName:(CPString)aString
    {
        firstName = aString;
    }

    - (CPString)firstName
    {
        return firstName;
    }

    - (void)setLastName:(CPString)aString
    {
        lastName = aString;
    }

    - (CPString)lastName
    {
        return lastName;
    }

    @end




Using the new **@accessors** keyword, we can eliminate four methods:

    @implementation Person : CPObject
    {
        CPString firstName @accessors;
        CPString lastName @accessors;
    }
    @end


This second version is much more succinct than the first, and less tedious to program. We think this will be helpful for developers, and will increase productivity and code readability.

It's important to note that this doesn't change the way you use a class. For our Person class, in both cases, the code for getting the first and last names of a person (in the myPerson variable) would look something like this:

    var fullName = [myPerson firstName] + " " + [myPerson lastName];

Similarly, setting an ivar looks like this:

    [myPerson setFirstName:"Winston"];
    [myPerson setLastName:"Smith"];

Like any key-value-coding compliant class, the name of the instance variable becomes the "property" or "key", and that key name is used in the setter and getter methods. If your key is `firstName`, the getter for that key will be `firstName`, and the setter will be `setFirstName:`. The same pattern applies to any other key.

### Configuration

There are a few configuration options when using the new **@accessors** technique. Perhaps most importantly, is the ability to change the name of the property. For example, if you declared an instance variable like this:

    CPString _location @accessors;

Objective-J would generate two accessor methods called `_location` and `_setLocation:`. These are the expected accessor methods for a key called "_location". In order to generate more friendly versions without the leading underscore, you can modify your declaration like this:

    CPString _location @accessors(property=location);

The addition of the `property=location` tells Objective-J to use "location" as the new property name, instead of "_location", which will generate `location` and `setLocation:` methods without the underscore. In addition, you can also specify the specific name of both the getter and the setter method, like this:

    BOOL _hidden @accessors(getter=isHidden, setter=setIsHidden);

This code specified a boolean instance variable called `_hidden`; the getter method will be called `isHidden` and the setter method will be called `setIsHidden:`. One thing to keep in mind when specifying your own getter and setter method names is key-value-coding. Although we don't yet have much documentation on the subject (you can read Apple's documentation [here](http://developer.apple.com/documentation/Cocoa/Conceptual/KeyValueCoding/KeyValueCoding.html)), key-value-coding enables several important features in Cappuccino, so it's important to maintain key-value-coding compliance. Normally, the rules are that for a given key, say "foo", the getter is called `foo`, and the setter is called `setFoo:`. There's an additional rule for boolean values, which says that you can use `isFoo`, and `setIsFoo:`, in addition to the usual method names. In our case, thats why our custom getter and setter names are still key-value-coding compliant.

There are two additional configuration options, **readonly**, and **copy**. By default, **@accessors** will generate both a getter and a setter. If you only want to expose a getter method to the world, you can add the **readonly** value in the arguments. The other option, **copy**, has to do with how the setter works. Normally, when you pass an object to a setter, it's assigned directly. The generated setter looks like this:

    - (void)setFoo:(id)aFoo
    {
        foo = aFoo;
    }

When you specify **copy**, the argument is first sent the message copy, and the return value of that message is assigned to the instance variable:

    - (void)setFoo:(id)aFoo
    {
        if (foo !== aFoo)
            foo = [aFoo copy];
    }


This is useful if you want to ensure that an object you're passing isn't modified out from under you. Of course, it only applies to ivars that are both read and write, and cannot be combined with readonly. To summarize, you can use both of these options like this:

    @implementation FooBar : CPObject
    {
        id foo @accessors(readonly);
        id bar @accessors(copy);
    }


### History

Apple introduced properties in Objective-C 2.0, which added a new way to declare instance variables for your classes. The two key features were the ability to use what has become known as "the dot syntax" for accessing instance variables, and the second was the ability to have the compiler automatically generate accessor methods. Reducing code, especially code that doesn't change every time you write it, is certainly a worthwhile goal, so we thought it would be a good idea to bring this new idea to Objective-J. There are a lot of things about the Objective-C 2.0 implementation of properties that don't make sense for Objective-J, so we decided not to port them directly and instead developed a syntax that we believe makes the most sense.

The main goal we want to achieve is eliminating the need to write your own accessor methods. We don't, however, support the "dot syntax" aspect of Objective-C 2.0. This makes the dual @property and @synthesize syntax of Objective-C 2.0 redundant. Furthermore, rather than just choose one or the other, we decided to use a new keyword, **@accessors**. This will lesson the confusion for existing Cocoa developers trying to learn Objective-J. It will also make sure we don't have an incompatible syntax going forward, as we explore new ways to work with existing Objective-C code.

### Conclusion

Accessor synthesizing will reduce the amount of boilerplate code that needs to be written, and make the language just a little bit easier to develop in. Overall, we think it's a worthwhile addition to the language. If you have an opinion, we'd love to hear it, so sound off in the comments. Although this new syntax isn't yet written in stone, we won't expect to change it after version 0.6 of Cappuccino ships. Checkout the latest version of the git repository to start using this new feature.

We're also considering other language features that might make it easier to program in Objective-J. If you've got an idea, or you're interested in being part of the discussion, you should sign up for the [mailing list](/discuss/list.php), where we'll be discussing some of the new proposals.



