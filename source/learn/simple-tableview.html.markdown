In this tutorial we are creating a simple cell-based CTableView. CPTableView is one of the simplest way to organize our data into columns and rows. 
Following this tutorial you will be able to understand how populate data into CPTableView, how you can add or remove elements.
![](simpletableview/simpletableview1.png)

We assume you already read and understood the [Xcode Interface Builder tutorial](xcode-basics.html).

### Create the project

First, go to the folder in which you want create the project. Run
the `capp` command:

    :::sh
    capp gen -l -t NibApplication SimpleTableView

This will generate the startup project using the Nib template.

### Code

Let’s define the required instance variables:

	:::objj
	@implementation AppController : CPObject
	{
	    @outlet CPWindow    theWindow;
	    @outlet CPTableView tableView;
	    CPMutableArray      _names;
	}

Our dataSource will be CPMutableArray:
	
	:::objj
	- (id)init
	{
	    if (self = [super init]);
	    {
	        _names = [[CPMutableArray alloc] initWithObjects:"Alpha", "Beta", "Charlie", "Delta"];
	    }
	    return self;
	}

As we wouldn't like a full screen application, do the following change in `awakeFromCib` method:

	:::objj
	- (void)awakeFromCib
	{
	    // This is called when the cib is done loading.
	    // You can implement this method on any object instantiated from a Cib.
	    // It's a useful hook for setting up current UI values, and other things.

	    // In this case, we want the window from Cib to become our full browser window
	    [theWindow setFullPlatformWindow:NO];
	}

To present data in a CPTableView we need to define the number of rows and the data in each row as written in [CPTableView API](http://www.cappuccino-project.org/learn/documentation/interface_c_p_table_view.html):
> CPTableView object displays record-oriented data in a table and allows the user to edit values and resize and rearrange columns. A CPTableView requires you to either set a data source which implements `numberOfRowsInTableView:` and `tableView:objectValueForTableColumn:row:` , or alternatively to provide data through Key Value Bindings.

We are defining the number of rows of CPTableView, which is equivalent to the number of elements in our array.

	:::objj
	- (int)numberOfRowsInTableView:(CPTableView)aTableView
	{
	    return [_names count];
	}

This method will insert the elements of CPMutableArray into each row.

	:::objj
	- (id)tableView:(CPTableView)aTableView objectValueForTableColumn:(CPTableColumn)aColumn row:(CPInteger)aRowIndex
	{
	    return [_names objectAtIndex:aRowIndex];
	}

### Flush the template

Let’s start. First, we are opening the main window, by double clicking Window - Window in the Object navigator.
![](simpletableview/simpletableview2.png)

By default, there is a text field and a slider. Select and remove them (using the Delete key).


### Creating the new interface

Choose “Table View” from Object Library.
![](simpletableview/simpletableview3.png)

Drag and Drop “Table View” onto the Window.
![](simpletableview/simpletableview4.png)

By dragging the right corner of Table View, resize it to fill the Window.
![](simpletableview/simpletableview5.png)

Choose “Table View” from Document Outline, then Click on Attributes inspector on the top right side of the Xcode. 
In our tutorial we add cells instead of views to CPTableView, so we need to change the “Content Mode” from “View based” to “Cell based”.
![](simpletableview/simpletableview6.png)

As we need only one column, reduce the column number from 2 to 1. We don’t need Header, unselect it. Set the “Column Sizing” to “First Column Only”. Select “Alternating Rows” too.
![](simpletableview/simpletableview7.png)

We have to connect the dataSource and delegate outlets.
![](simpletableview/datasource.png)
![](simpletableview/delegate.png)
![](simpletableview/tableview.png)

### Run the application
Before opening our application in a browser, it is recommended to start a webserver:

	:::sh
	python -m SimpleHTTPServer

Now, open your browser and type the address given by SimpleHTTPServer: `localhost:8000`
![](simpletableview/simpletableview8.png)

### 'Add’ function
So far so good, but what if I want to add elements to our list.
We have to add two objects from the library. One is CPTextField, the second one is CPButton.
![](simpletableview/simpletableview9.png)
![](simpletableview/simpletableview11.png)

You can change the CPButton title on the Attributes inspector tab
![](simpletableview/simpletableview12.png)

Define the CPTextField as an outlet in the AppController. This will help us to get its value.

	:::objj
	@outlet CPTextField textField;

Create the CPButton as an action.

	:::objj
	- (@action)addItem:(id)sender
	{
	    // Get CPTextField value and add to our CPMutableArray 
	    [_names addObject: [textField stringValue]];

	    // Clear the CPTextField
	    [textField setStringValue:""];

	    // Reload CPTableView to see the changes
	    [tableView reloadData];
	}

Connect our newly added outlet and action.
![](simpletableview/textfield.png)
![](simpletableview/add.png)

### Run the application
Refresh your borwser.
![](simpletableview/simpletableview13.png)

### 'Remove’ function
If we are able to add, we would like to remove items as well. 

Let’s add another CPButton as 'Remove’ button.
![](simpletableview/simpletableview14.png)

By selecting a row, we define the element we want to remove. Using `selectedRow` we can easily tell the row index and pick the element and delete with 
`CPMutableArray removeObject: object`

	:::objj
	- (@action)removeItem:(id)sender
	{
	    // Check if any row selected, if not the value is -1
	    if ([tableView selectedRow] > -1)
	    {
	        [_names removeObject:[_names objectAtIndex:[tableView selectedRow]]];
	    }

	    // Reload CPTableView to see the changes
	    [tableView reloadData];
	}

Connect the button and the action:
![](simpletableview/remove.png)

Now, you have a fully functional application.

### Source
You can download the archive of this project [here](files/SimpleTableView.zip).