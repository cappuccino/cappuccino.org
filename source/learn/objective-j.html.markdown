Objective-J is a new programming language based on Objective-C. It is a
superset of JavaScript, which means that any valid JavaScript code is
also valid Objective-J code. Anyone familiar with JavaScript and
object-oriented programming concepts, classical inheritance in
particular, should have no difficulty learning Objective-J. Familiarity
with Objective-C will be helpful, but it is not required.

### Classes

Objective-J has two types of objects: native JavaScript objects and
Objective-J objects. Native JS objects are exactly what they sound like,
the objects native to JavaScript. Objective-J objects are a special type
of native object added by Objective-J. These new objects are based on
classes and classical inheritance, like C++ or Java, instead of the
prototypal model.

Creating a class in Objective-J is simple. Here's an example of a Person
class that contains one member variable, name:

    :::objj
    @implementation Person : CPObject
    {
        CPString name;
    }

    @end

The beginning of a class is always the keyword `@implementation`, followed
by the class name. The third term, after the colon, is the class you
want to subclass. In this case, we're subclassing `CPObject`, which is the
root class for most classes. You don't need a superclass, but nearly all
the time you will want one.

After the declaration, a block enclosed with brackets is used to define
all your member variables. Each variable is declared on its own line
with a type and variable name, and a semicolon. Technically the type is
optional, but its highly recommended. Declaring your member variables is
important, because any variable used elsewhere in your class that isn't
declared will automatically become a global variable.

To end a class declaration, add the keyword @end.

### Methods

Just as with objects, native JavaScript functions work unchanged in
Objective-J. In addition to native functions, Objective-J adds methods
which are part of the new class system. Let's add a set of accessor
methods to our Person class:

    :::objj
    - (void)setName:(CPString)aName
    {
        name = aName;
    }

    - (CPString)name
    {
        return name;
    }

These lines go anywhere after the initial `@implementation` line and
instance variable declaration block, but before the `@end` keyword. This
syntax should be familiar to anyone who's programmed a C style language
before, including JavaScript. The only interesting thing is the method
declaration.

Each method signature starts with either a dash (-) or a plus (+).
Dashes are used for instance methods, which are methods you can call on
instance variables. Both of our methods above are instance methods,
which makes sense because they set and retrieve instance variables of
our `Person` objects.

Following the dash/plus is a return type, in parentheses. Nothing
special about this. Again, type declarations are optional but highly
recommended, as they help document your code. Finally, we declare the
method name. In Objective-J, method parameters are interspersed within
the method name. Our two methods above are name, and `setName:`. Note the
colon after "setName" - it indicates that a parameter follows.

When methods have more than one parameter, each parameter is separated
by a colon. In the declaration of such a method, parameters are split by
a label, followed by a colon, the type, and the parameter name:

    :::objj
    - (void)setJobTitle:(CPString)aJobTitle company:(CPString)aCompany

In Objective-J, method names are split across all of the arguments to a
method. These are not technically named arguments. The method above is
named `setJobTitle:company:`. This is achieved by concatenating the first
part of the method with all the subsequent labels, in order.

The parameters to a method must be passed in order, and all of the
parameters are required. To call such a multiple parameter method, we
pass our data after each label:

    :::objj
    [myPerson setJobTitle:"Founder" company:"Cappuccino Foundation"];

As you can see, each colon is followed by the input that will be mapped
to that parameter name. That sequence of label, colon, input is repeated
for each parameter.

You may be wondering why it matters what the actual name of the method
is. One pattern you'll find in Objective-J and Cappuccino is the idea of
passing a method as an argument to another method. This is used commonly
in delegation and in the event system. Since methods aren't first class
objects in the same way as JavaScript, we use a special notation to
refer to them, `@selector`. If I wanted to pass the previous method as an
argument to another method, I would use the following code:

    :::objj
    [fooObject setCallbackSelector:@selector(setJobTitle:company:)];

As you can see, the method name is passed to @selector complete with its
colons and parameter labels.

### Using Objects & Classes

Now that we've covered the basics Objective-J objects and classes, let's
see how you use them. This block of code creates a new Person object,
and sets the name:

    :::objj
    var myPerson = [[Person alloc] init];
    [myPerson setName:"John"];

Method calls in Objective-J are called "messages", and you send an
object a message using bracket notation like this: `[object message]`. I
mentioned earlier that some methods are class methods, which are meant
to be called on a class itself -- alloc is one of these methods. Every
class in Objective-J has a special class method called `alloc`, which
returns a new instance of that class.

In the example above, we're calling the `alloc` method on the `Person`
class, which returns a `Person` instance. Then, we call the init method on
that instance. Both `alloc` and `init` return a reference to the object,
which we can assign our variable myPerson. Just like `alloc`, every class
inherits the `init` method from `CPObject`.

The `alloc` class method is analogous to the "new" keyword in many
languages like JavaScript, C++, and Java, in that they create a new
instance. The `init` instance methods are like the constructors in those
languages, in that they perform initialization on the newly created
instance.

Some classes specify their own custom `init` method, like `CPView`, which
uses the following signature:

    :::objj
    - (id)initWithFrame:(CGRect)aFrame

Every subclass should be sure to call its parent class's init method.
Here's a custom init method for our `Person` class which takes the name
directly:

    :::objj
    - (id)initWithName:(CPString)aName
    {
        self = [super init];
        if (self)
        {
            name = aName;
        }
        return self;
    }

First we call our superclass `init` method, which returns a reference to
the newly initialized instance. We must assign this reference to the
`self` variable (in case the super class's `init` method swapped out the
original instance for a new one). We check to make sure `self` was
returned correctly, and if so we can do our class specific task of
assigning `aName` to `name`, and finally, we return `self` so that calling
code will have a reference to the newly initialized object.

`self` is the Objective-J equivalent to JavaScript's `this`. Just as
`this` references the JavaScript object, `self` references the
Objective-J object. Like JavaScript, `self.foo` will refer to the `foo`
instance variable, but unlike JavaScript `self` isn't required, you can
just use `foo` within any instance methods.

Many classes in Cappuccino offer a slightly different model for creating
objects, which can be more convenient. Instead of calling `alloc` and
`init`, these classes implement their own class method to return new
objects. Note that in class methods, `self` refers to the class itself.

    :::objj
    + (id)personWithName:(CPString)aName
    {
        return [[self alloc] initWithName:aName];
    }

Which would be called like this:

    :::objj
    var joe = [Person personWithName:"Joe"];

### Importing Code

One commonly desired technique missing from JavaScript is the ability to
import code in the same way that languages like Java or C allow. To that
effect, Objective-J adds the `@import` statement:

    :::objj
    @import <Foundation/CPObject.j>
    @import <AppKit/CPView.j>
    @import "MyClass.j"

There are two types of import statements. The angle brackets indicate
framework code, while the quotation marks indicate local project code.
Framework imports use the built in search path mechanism to search for
the desired file in any of the defined locations. Local imports only
look in the location relative to the importing file.

### Memory Management

JavaScript is garbage collected, and so is Objective-J, so you won't see
any calls to `retain` or `release` in Objective-J code as you would in
Objective-C. Many common leaks caused by DOM manipulation are handled by
the Cappuccino frameworks.

That isn't to say it's impossible to leak objects. As with any garbage
collected language, it's possible to accidentally hold on to reference
to objects such that they can't be freed, so keep this in mind.

### Categories

Categories allow you to add methods to a class without needing to create
a new subclass or modify the class's source code. The new method (or
methods) become part of all instances of the class once the category is
loaded.

This is useful in many different scenarios, for example adding methods
to built-in classes. If you wanted all your `CPString` objects to have a
method that would return the reverse string, you could define a category
like this:

    :::objj
    @import <Foundation/CPString.j>

    @implementation CPString (Reversing)

    - (CPString)reverse
    {
        var reversedString = "",
            index = [self length];

        while(index--)
            reversedString += [self characterAtIndex:index];

        return reversedString;
    }

    @end

Now you can call reverse on any string to get the reversed string.

    :::objj
    var myString = "hello world",
        reversed = [myString reverse];
    alert(reversed);  // alerts "dlrow olleh"

The syntax for the category is `@implementation`, followed by the class
you're adding to, followed by the name of your category in parentheses.
Any methods added before the `@end` keyword will be part of the category.
Note that you can't add instance variables via categories, though due to
the dynamic nature of JavaScript objects it's possible to add one by
simply modifying the object's properties directly:

    instance.newProperty = "foo";

It's interesting to note some of the techniques used in the
implementation of the reverse method above. For example, `reversedString`
is declared just like any typical JavaScript string. This is thanks to a
technique called toll-free bridging which allows any JavaScript object
like an array or a string to act both as a JavaScript object and a
Cappuccino object at the same time. It responds to `CPString` methods like
`length` and `characterAtIndex:`, as well as existing JavaScript methods
and operators such as `+`.

### Scope

Most of the time, Objective-J has the same scoping rules as JavaScript.
Variables not specifically declared with var become globals, while var'd
variables have function/method level scope. The two changes to these
rules are instance variables and file-scoped variables.

Instances variables are declared in the `@implementation` block, as seen
earlier in the tutorial. When you use those variables within your class,
they have object level scope -- they are not global, they belong to each
instance object. If you forget to declare one of your instance
variables, however, then it is treated as a global variable like any
other JavaScript code.

File-scoped variables are something introduced in Objective-J. When you
declare a variable with the var keyword outside a function or method
implementation, these variables (sometimes called statics) have file
level scope. They can only be accessed by other code within the same
file. This can be useful for implementing many shared object techniques
without needing to resort to global variables. If a file contains a
single class they can be thought of as "class variables".

The following is an example of the main scoping rules in Objective-J:

    :::objj
    globalScoped = "this becomes global";
    var fileScoped = "this stays scoped in the file";

    @implementation Foo : CPObject
    {
        CPString objectScoped;
    }

    - (void)baz
    {
        var methodScoped;

        methodScoped = "function scope, declared with var";
        anotherGlobal = "global scope, no var";
        objectScoped = "still object scoped";
        fileScoped = "still file scoped";
    }

    @end

### Accessors

Accessor synthesizing is a way of reducing the amount of boilerplate code
you need to write for getting and setting instance variables. Take the following code block for example:

    :::objj
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

With accessors, this can be shortened significantly:

    :::objj
    @implementation Person : CPObject
    {
        CPString firstName    @accessors;
        CPString lastName     @accessors;
    }

    @end

Under the hood, variables declared with the `@accessors` keyword are automatically
assigned getter and setter methods. These methods may be overwritten if you need to do
some additional processing before returning the variable:

    :::objj
    @implementation Person : CPObject
    {
        CPString firstName    @accessors;
        CPString lastName     @accessors;
    }

    - (CPString)firstName
    {
        return [firstName capitalizedString];  // a silly example.
    }

    @end

Additionally, you may configure your accessors to provide more friendly names
for your getters and setters than the underlying variable. The `property` argument
hides the underlying variable name and gives you a way of configuring the getter and setter method names:

    :::objj
    @implementation Person : CPObject
    {
        CPString _firstName    @accessors(property=firstName);
        CPString _lastName     @accessors(property=lastName);
    }

    @end

This code would generate the methods `firstName`, `setFirstName`, `lastName` and `setLastName`.

You can also completely change the generated method names (often useful for Boolean accessors) by using the `getter` and `setter` arguments:

    :::objj
    @implementation Person : CPObject
    {
        BOOL _cool    @accessors(getter=isCool, setter=setCool:);
    }

    @end

For more information about `@accessors` you should read the [annoucement blog post.](http://www.cappuccino-project.org/blog/2008/10/synthesizing-accessor-methods.html)

## Objective-J 2.0

These language features are only available if you are running Cappuccino > 0.9.6.

### Dictionary Literals

The syntax is `@{ key: value, key2: value2, ... }`, which is equivalent to the [same feature in Objective-C](http://clang.llvm.org/docs/ObjectiveCLiterals.html). Here's an example:

##### Before

    :::objj
    return [CPDictionary dictionaryWithObjects:[[CPNull null], [CPNull null], 1.0, 3.0, CGSizeMakeZero(), 6.0, [CPNull null], CGSizeMakeZero()]
                                       forKeys:[   @"background-color",
                                                   @"border-color",
                                                   @"border-width",
                                                   @"corner-radius",
                                                   @"inner-shadow-offset",
                                                   @"inner-shadow-size",
                                                   @"inner-shadow-color",
                                                   @"content-margin"]];

##### After

    :::objj
    return @{
            @"background-color": [CPNull null],
            @"border-color": [CPNull null],
            @"border-width": 1.0,
            @"corner-radius": 3.0,
            @"inner-shadow-offset": CGSizeMakeZero(),
            @"inner-shadow-size": 6.0,
            @"inner-shadow-color": [CPNull null],
            @"content-margin": CGSizeMakeZero(),
        };

The format should be familiar from languages such as Python and, of course, JavaScript itself.

Regular JavaScript dictionaries will continue to work as normal.

    :::objj
    // Objective-J Dictionary Literal
    var a = @{ @"count": 2 };

    // JavaScript Object
    var a = { @"count": 2 };

### Reference and Dereference

If you have programmed Objective-C, C or C++ you might think of an `@ref` reference as a JavaScript analog to a pointer. In C you might write:

    :::c
    int a;
    int *aPtr = &a;
    *aPtr = 5;
    printf("%d\n", *aPtr);  // Prints 5.
    printf("%d\n", a);      // Also prints 5.

Whereas in Objective-J you would use the `@ref` and `@deref` methods:

    :::objj
    var a,
        aRef = @ref(a);

    @deref(aRef) = 5;
    console.log(@deref(aRef));  // Logs 5.
    console.log(a);             // Also logs 5.

Once you have a reference you can pass it around, save it, and dereference it as needed. It's not an actual pointer though so pointer arithmetic is not possible. This is especially useful if you wish to have two return values. From `CPNumberFormatter.j`:

    :::objj
    -(BOOL)getObjectValue:(id)anObjectRef forString:(CPString)aString errorDescription:(CPStringRef)anErrorRef

This method returns a BOOL to indicate whether the object value was a valid value. However, with this method you can also pass in a string for the `errorDescription` parameter which, in the case of an error, will be populated with a description of why the value was not valid:

    :::objj
    var myError = @"",
        isValid = [numberFormatter getObjectValue:someObject forString:someString errorDescription:@ref(myError)];

    if (!isValid)
        console.log("The value " + someString + " is not a valid! Error: " + @deref(myError));


### Forward Class Declaration and Global Variables

One thing you may run into with Objective-J 2 is a circular dependency: class A imports class B, and somewhere in the import chain class A is imported. When that happens, the compiler will complain that it doesn't recognize class A, because in fact the `@implementation` has not yet been parsed.

To solve a circular dependency, you have to use `@class SomeClass` to declare the class in one of the files.

For example CPObject.j uses CPString and CPException, but these cannot be imported since they need CPObject (a circular dependency). To avoid this circular dependency, you would "forward declare" these classes in CPObject:

    :::objj
    @class CPString
    @class CPException

The `@global` declaration is needed to tell the compiler about a variable that is not yet declared. For example CPObject.j uses the global variable CPInvalidArgumentException which is actually declared in CPException.j but cannot be used for the same reason as above. To use it, declare it at the top of your file:

    :::objj
    @global CPInvalidArgumentException

### Wrapping Up

This concludes our basic overview of Objective-J. The language is a
simple and straightforward addition to JavaScript, and most developers
shouldn't have any trouble becoming familiar with it.

If you'd like to see the complete code listing from the tutorial, you
can download it all in a single file: [Person.j](files/Person.j).
