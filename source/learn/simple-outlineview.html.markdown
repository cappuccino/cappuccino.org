In this tutorial we will create a simple view-based outline view. `CPOutlineView` displays data in hierarchical format. In other programming languages it is referred as Tree-view. Although `CPOutlineView` is a subclass of `CPTableView` and inherits the row and column format, the implementation is slightly different. We will create an organisation chart of a company with the ability to expand and collapse items.
![](simpleoutlineview/simpleoutlineview.png)

### Create the project
Run the `capp` command in your project folder:

    :::sh
    capp gen -l -t NibApplication SimpleOutlineView

This will generate an empty new project using the Nib template.

### Code
Our data source model will be created in a separate file to keep our code organised  In this way you can easily structure your project around MVC pattern. Create a new file with a name of `EmployeeData.j`.

    :::objj    
    @import <Foundation/CPObject.j>

    @implementation EmployeeData : CPObject
    {
        CPString       _name      @accessors;
        CPString       _title     @accessors;
        CPMutableArray _employees @accessors;
    }

    - (id)initWithDetails:(CPString)aName title:(CPString)aTitle
    {
        if (self = [super init])
        {
            _name = aName;
            _title = aTitle;
            _employees = [CPMutableArray array];
        }
        return self;
    }

    @end

Let’s go back to our AppController.j and import our previously created file:
`@import "EmployeeData.j"` 

Now, we can create the instance variable using the EmployeeData model and outlets for interaction between AppController and OutlineView.

    :::objj
    @implementation AppController : CPObject
    {
        @outlet CPWindow        theWindow;
        @outlet CPOutlineView   _outlineView;
        EmployeeData            ceo; // This will hold our root item
        EmployeeData            employee; // This will hold the leaf items
    }

Let's make a windowed application for this tutorial, by setting `setFullPlatformWindow:NO` in the `awakeFromCib` method:

    :::objj
    - (void)awakeFromCib
    {
        [theWindow setFullPlatformWindow:NO];
    }

In the `init` method we are defining the data source using our EmployeeData model.

    :::objj
    - (id)init
    {
        if (self = [super init])
        {
        
            // First we define our root item, the CEO
            ceo = [[EmployeeData alloc] initWithDetails: "Ben" title: "CEO"];

            // Then we create other employees and add them to their managers belong to
            var simon = [[EmployeeData alloc] initWithDetails: "Simon" title: "CFO"];

            // We collect CEO reportees to his _employees array defined in Employee.j
            // Simon reports directly to CEO
            [ceo._employees addObject:simon];

            var sarah = [[EmployeeData alloc] initWithDetails: "Sarah" title: "Assistant to CFO"];
            // Sarah report to Simon
            [simon._employees addObject:sarah];

            var maarten = [[EmployeeData alloc] initWithDetails:"Maarten" title: "VP of Marketing"];
            [ceo._employees addObject:maarten];

            var donny = [[EmployeeData alloc] initWithDetails:"Donny" title: "Head of Communication"];
            [maarten._employees addObject:donny];

            var ronan = [[EmployeeData alloc] initWithDetails: "Ronan" title: "Communication Specialist"];
            [donny._employees addObject:ronan];

            var dick = [[EmployeeData alloc] initWithDetails: "Dick" title: "Head of Legal"];
            [ceo._employees addObject:dick];

        }
        return self;
    }

The [CPOutlineView API](http://www.cappuccino-project.org/learn/documentation/interface_c_p_outline_view.html) tells us clearly the required methods to implement and gives a good explanations as well:


- `(int)outlineView:(CPOutlineView)outlineView numberOfChildrenOfItem:(id)item; ` 

Returns the number of child items of a given item. If item is nil you should return the number of top level (root) items.


- `(BOOL)outlineView:(CPOutlineView)outlineView isItemExpandable:(id)item;` 

Returns YES if the item is expandable, otherwise NO.


- `(id)outlineView:(CPOutlineView)outlineView child:(CPInteger)index ofItem:(id)item;` 

Returns the child item at an index of a given item. If item is nil you should return the appropriate root item.


- `(id)outlineView:(CPOutlineView)outlineView objectValueForTableColumn:(CPTableColumn)tableColumn byItem:(id)item;` 

Returns the object value of the item in a given column.

#### Implementing the methods
Most probably the easiest method is the `numberOfChildrenOfItem` . 
The `item` will be nil, if it is the root item. Otherwise, we simply use the size of the `CPMutableArray` called `_employees` .

    :::objj
    - (int)outlineView:(CPOutlineView)outlineView numberOfChildrenOfItem:(id)item
    {
        if (item == nil)
        {
            // We have one root item, the CEO only
            return 1;
        }
        else
        {
            employee = item
            return ([employee._employees count]);
        }
    }

Next step to define whether the item has subitems. If it does, it will be expandable.

    :::objj
    - (BOOL)outlineView:(CPOutlineView)outlineView isItemExpandable:(id)item
    {
        if (item == nil)
        {
            return YES;
        }
        else
        {
            employee = item;
            return ([employee._employees count] != 0);
        }
    }

This method returns the child item at index of a item. If item is nil, returns the appropriate child item of the root object.

    :::objj
    - (id)outlineView:(CPOutlineView)outlineView child:(CPInteger)index ofItem:(id)item
    {
        if (item == nil)
        {
            // Our root item is the CEO
            return ceo;
        }
        else
        {
            employee = item;
            return (employee._employees[index]);
        }
    }

Finally, we are assigning the object values to columns. Our first column is “NameColumn”, the second is “TitleColumn”. We will setup these names later in the Interface Builder.

    :::objj
    - (id)outlineView:(id)outlineView viewForTableColumn:(id)tableColumn item:(id)items
    {
        var identifier = [tableColumn identifier];

        if (identifier == "NameColumn")
        {
            var view = [outlineView makeViewWithIdentifier:"NameCell" owner:self];
            [[view textField] setStringValue:item._name ];
        }
        else
        {
            var view = [outlineView makeViewWithIdentifier:"TitleCell" owner:self];
            [[view textField] setStringValue:item._title ];
        }
        
        return view;
    }

### Clean up the nib
First, open up the main window, by double clicking Window - Window in the Object navigator.
![](simpleoutlineview/simpleoutlineview2.png)

By default, there is a text field and a slider. Select and remove them (using the Delete key).

### Creating the new interface
Choose “Outline View” from Object Library.
![](simpleoutlineview/simpleoutlineview3.png)

Drag and Drop “Outline View” onto the Window.
![](simpleoutlineview/simpleoutlineview4.png)

By dragging the right corner of Outline View, resize it to fill the Window.
![](simpleoutlineview/simpleoutlineview5.png)

Remember that  in the `(id)outlineView:(id)outlineView viewForTableColumn:(id)tableColumn item:(id)item` method we have to use tableColumn identifier and view identifier. Let’s add these to our Interface Builder document.

Choose “Outline View” from Document Outline, expand the items until you reach Table Column. Now, let’s click on Identity Inspector on the top right side of the Xcode, set the Identifier to “NameColumn”.
![](simpleoutlineview/simpleoutlineview6.png)

Repeat the same for the second column, and set its Identifier to “TitleColumn”.
![](simpleoutlineview/simpleoutlineview7.png)

Expand the NameColumn and add “NameCell” to Table Cell View’s Identifier.
![](simpleoutlineview/simpleoutlineview8.png)

Do the same for TitleColumn with “TitleCell”.
![](simpleoutlineview/simpleoutlineview9.png)

Double click on the Header of the Ouline View, and set it “Name” and “Title”.
![](simpleoutlineview/simpleoutlineview10.png)
![](simpleoutlineview/simpleoutlineview11.png)

Before testing our new application, there is one more thing left. Connect CPOutlineView to our AppDelegate.
![](simpleoutlineview/simpleoutlineviewdatasource.png)
![](simpleoutlineview/simpleoutlineviewdelegate.png)
![](simpleoutlineview/simpleoutlineviewoutlet.png)

As usual the best way to run a Cappuccino app for testing is to start a local webserver. So in the root of your project folder, type:
    
    :::sh
    python -m SimpleHTTPServer

Now, open your browser and type in the address given by SimpleHTTPServer: `localhost:8000` 
![](simpleoutlineview/simpleoutlineview.png)

Now, you have a fully functioning application!

### Source

You can download the archive of this project [here](files/SimpleOutlineView.zip).
