@import <Foundation/CPObject.j>

@implementation Person : CPObject
{
    CPString name;
}

+ (id)personWithName:(CPString)aName
{
    return [[self alloc] initWithName:aName];
}

- (id)initWithName:(CPString)aName
{
    self = [super init];

    name = aName;

    return self;
}

- (void)setName:(CPString)aName
{
    name = aName;
}

- (CPString)name
{
    return name;
}

@end



// Reversing Category for CPString

import <Foundation/CPString.j>

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



// Here's some code that uses the class and category defined above.
// Code outside a class declaration is global, and will be executed when
// the file is imported, just like in C.


var john = [Person personWithName:"John"];

alert([john name]);

[john setName:"Ralph"];

alert("John changed his name to "+[john name]+" which is "+[[john name] reverse]+" backwards.");

