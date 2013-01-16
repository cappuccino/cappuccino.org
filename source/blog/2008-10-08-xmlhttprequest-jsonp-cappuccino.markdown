---
title: XMLHTTPRequest, JSONP & Cappuccino
author: Ross Boucher
author_email: ross@280north.com
wordpress_id: 56
wordpress_url: http://cappuccino.org/discuss/?p=56
date: '2008-10-08'
categories:
- Cappuccino
- Tutorials
tags:
- CPURLConnection
- AJAX
- XMLHTTPRequest
- tutorial
---


If you're a veteran web developer, you're probably familiar with the XMLHTTPRequest (XHR for short), the bread and butter of "AJAX". XHRs are what make dynamic applications that don't reload the page possible. For an application framework like Cappuccino this is critical, since Cappuccino applications are designed to never reload the page -- so it's important to understand exactly how Cappuccino deals with these requests.

Before we get in too deep, a quick primer on exactly what I'm talking about. If you're comfortable with XMLHTTPRequests already, feel free to skip this paragraph. [XMLHTTPRequest](http://en.wikipedia.org/wiki/XMLHttpRequest) was introduced by Microsoft in Internet Exporer 5 as a way for scripts within a web page to send a remote request to another server without reloading the entire page. Although it started as a propriety Microsoft technology, it was later adopted by Mozilla, and eventually all the other major browsers. The term AJAX, which stands for Asynchronous JavaScript and XML, is essentially synonymous with the use of XMLHTTPRequests on a website. A website creates an XHR object with a specific URL, gives it a function to execute when the status of the request changes, and then executes the request. With this mechanism, your script can use most of the HTTP verbs, and can respond to specific HTTP response codes, which makes it a flexible and powerful API. If you're coming from Cocoa, or another desktop programming environment, you may be used to classes that perform similar functions like NSURLConnection or maybe even (approximately) curl and wget. There are, however, important limitations introduced by the browser security model that we'll discuss shortly.

### XMLHTTPRequest

In Objective-J and Cappuccino, asynchronous http requests are instrumental for creating a working app, beginning with the import statement. As you've probably noticed by now, Objective-J introduces the **import** keyword to JavaScript. Import statements pull in and execute Objective-J code at runtime, which lets us maintain dependency relationships across classes in Cappuccino, much like code in C or Java. These statements are actually asynchronous, and are implemented using XHRs. This means we only have to include one script tag in our _index.html_ file for Objective-J only, while the rest of Cappuccino is bootstrapped with these asynchronous requests. This is a fairly low level detail, but it illustrates the importance of the XHR when writing complex javascript based applications.

When writing a Cappuccino applications, XHRs are the primary way to communicate with your backend server. While most of your application logic may be running in the client, certain tasks will still need to run on a webserver. For example, consider an authentication system; in order for authentication to be meaningful, it will need to present credentials to a server for verification. Similarly, features like persistent data storage require server communication to actually store the data, otherwise it would dissappear when the user navigated away from the page. To put it another way, if your app doesn't talk to an outside server, it may be of limited utility.

### CPURLConnection

Like most things in Cappuccino, XMLHTTPRequests are abstracted at a higher level. In this case, the CPURLConnection class manages the communication. If we look at the [API Reference](http://www.cappuccino-project.org/learn/documentation/class_c_p_u_r_l_connection.html), we'll find a few different ways to create an instance. The easiest way is the class method **connectionWithRequest:delegate:**, which takes a CPURLRequest object and a delegate. CPURLRequest objects wrap a single request, including the URL, HTTP method, request body, and request headers. Like everywhere in Cappuccino, the delegate provides for the ability to customize the request's behavior. Let's look at the process of creating a CPURLConnection.

	var request = [CPURLRequest requestWithURL:"list.txt"];
	var connection = [CPURLConnection connectionWithRequest:request delegate:self];



As you can see, it's a simple process. Connections created with this class method fire immediately, without needing to explicitly call any additional methods. By default, the request object will be a GET request, with no additional data. Like any URL on a webpage, the URL will be treated as relative to your _index.html_ file unless you specify an absolute path or URL (e.g. preceding the URL with http://). To handle the response, we can implement these two optional delegate methods:

	 - (void)connection:(CPURLConnection) connection didReceiveData:(CPString)data
	{
	 //This method is called when a connection receives a response. in a
	 //multi-part request, this method will (eventually) be called multiple times,
	 //once for each part in the response.
	}



	- (void)connection:(CPURLConnection)connection didFailWithError:(CPString)error
	{
	 //This method is called if the request fails for any reason.
	}




After your request is created it will be fired, and later CPURLConnection will call the methods above on the connection's delegate. These methods are both optional, but are the minimum that you should implement in order to interact with your AJAX requests. The first is essential in processing any response, and the second is necessary for correctly dealing with errors, which is an important part of a well written application. Let's look at a real world implementation of these two methods, as well as the creation of a request, to get a sense for how all this works.

The following code is taken from 280 Slides. It deletes a photo from your library. In this first chunk, we'll construct and start our connection:

	 //BASE_URL is a 280 Slides global, which points to the base directory of our server structure
	var request = [CPURLRequest requestWithURL: BASE_URL+"Media/photo.php?id="+itemID];



	//we're using HTTP verbs to keep our backend as RESTful as possible
	[request setHTTPMethod: "DELETE"];

	//create the CPURLConnection and store it. the connection fires immediately
	_deletePhotoConnection = [CPURLConnection connectionWithRequest: request delegate: self];




Notice that we store a reference to the connection in the ivar __deletePhotoConnection_. This is so, if we have multiple connections, we can check to ensure we're responding to the right one. Now let's look at the delegate method implementations:

	 - (void)connection:(CPURLConnection)aConnection didReceiveData:(CPString)data
	{
	 //get a javascript object from the json response
	 var result = CPJSObjectCreateWithJSON(data);

	 //check if we're talking about the delete connection
	 if (aConnection == _deletePhotoConnection)
	 [self deletePhoto:result.id]; //deletes the specified photo

	 //clear out this connection's reference
	 [self clearConnection:aConnection];
	}



	- (void)connection:(CPURLConnection)aConnection didFailWithError:(CPError)anError
	{
	 if (aConnection == _deletePhotoConnection)
	 alert("There was an error deleting this photo. Please try again in a moment.");





	 [self clearConnection:aConnection];
	}





	- (void)clearConnection:(CPURLConnection)aConnection
	{
	 //we no longer need to hold on to a reference to this connection
	 if (aConnection == _deletePhotoConnection)
	 _deletePhotoConnection = nil;
	}




Again, the code is very simple. Since we send and receive data using JSON, the first call in our **connection:didReceiveData:** implementation turns that text response (_data_) into a javascript object using the JSON helper function **CPJSObjectCreateWithJSON()**. For the reverse operation, you can use the reverse function, **CPJSObjectCreateJSON()**. With the resulting object in hand, we check if the resulting connection is in fact our _deletePhotoConnection, and if it is, we proceed to delete the photo referenced in the object. In the alternate case, where our request is unsuccessful, we prompt the user to inform them that the request failed and do not delete the photo.

You'll notice that both methods call **clearConnection:**. This is a convenience method we've written to nil out our reference to the connection object once we've finished using it. Although not strictly necessary, keeping a pointer to the object means it won't be collected by the garbage collector. Removing the reference from our instance variable is the best practice since we know we will not be using it again.

Although it's not shown here, the reason we store a reference to the specific connection is that we use other connections in the same class, so we need a simple way to tell them apart. If you're only using one connection with your delegate, you may not need to use this technique or store a reference to the connection at all.

Finally, there are two additional CPURLConnection delegate methods we chose not to implement, but which you may be interested in for your own application. There's also a class delegate for handling request authentication at the application level. You can read more about these methods in the [API documentation](http://www.cappuccino-project.org/learn/documentation/class_c_p_u_r_l_connection.html).

### CPJSONPConnection

One of the limitations of the XHR is that it must follow what is known in the web security world as the [same origin policy](http://en.wikipedia.org/wiki/Same_origin_policy). The model requires that requests can only be sent to URLs with the same protocol, domain, and port number as the web page. This policy makes it difficult to interact with third party web services without having to proxy requests first through your own webserver. Several people developed their own workarounds to the limitation, but eventually [JSONP](http://bob.pythonmac.org/archives/2005/12/05/remote-json-jsonp/) emerged as the standard mechanism.

JSONP stands for JSON with Padding, and it comprises two components. The first part deals with getting around the same origin policy itself. XMLHTTPRequests may not work across multiple domains, but <script> tags have no such limitation. JSONP takes advantage of this by dynamically generating a <script> tag and appending it to the page. The script's src property is set to the URL of the remote API, including all request parameters in the query string. The second component of JSONP deals with what to do once the API returns a response.

As the name suggests, JSONP APIs return their data in the JSON format, but instead of returning a plain JSON string, they wrap the JSON response in a function call. This extra function call is the "padding" in JSONP, and it effectively works around the browser's security policy. Typically, function name is a parameter of the request, which you can see demonstrated in the Flickr API. This API allows you to specify _format=json_ to get a JSON response, and _jsoncallback=myfunctionname_ to specify your custom function wrapper for the response. An example request might look something like this:

	 var url = "http://www.flickr.com/services/rest/"+
	 "?method=flickr.interestingness.getList"+
	 "&format=json&jsoncallback=flickResponse&api_key=YOUR_KEY";


As you can imagine, generating your own dynamic script tags and managing global callback methods would be a serious hassle, which is why Cappuccino has built in support in the form of [CPJSONPConnection](http://www.cappuccino-project.org/learn/documentation/class_c_p_j_s_o_n_p_connection.html). You may have encountered this class in the source of our [Flickr Demo](http://www.cappuccino-project.org/learn/demos/FlickrPhotoDemo/). Creating an instance should look familiar:

	 var connection = [CPJSONPConnection sendRequest:aRequest callback:aCallbackParameter delegate:self];


The additional parameter, **callback:**, is a string that specifies the name of the parameter that allows us to specify the callback function's name in the JSONP API we're talking to. Similar to CPURLConnection, these two delegate methods are defined:

	 - (void)connection:(CPJSONPConnection)aConnection didReceiveData:(Object)data
	{
	 //called by the "padding" function when the request is complete

	 //depending on the third part API, data may be the native javascript object,
	 //or it may be a string. usually a js object is used, but if a string
	 //is passed, you can create a js object with CPJSObjectCreateWithJSON()
	}



	- (void)connection:(CPJSONPConnection)aConnection didFailWithError:(CPString)error
	{
	 //will be called if the connection fails
	 //will see improvements in an upcoming release
	}




Let's take a look at the actual implementation in our Flickr Demo:

	 - (void)applicationDidFinishLaunching
	{
	 ...

	 //Create the request, which contains all of our query parameters,
	 //except the jsoncallback parameter

	 var req = [CPURLRequest requestWithURL:
	 "http://www.flickr.com/services/rest/"+
	 "?method=flickr.interestingness.getList"+
	 "&per_page=20&format=json&api_key="+API_KEY];

	 //Create the connection, set the callback, and make ourselves the delegate.
	 //the connection fires immediately

	 var connection = [CPJSONPConnection sendRequest:req callback:"jsoncallback" delegate:self];
	}



	- (void)connection:(CPJSONPConnection)aConnection didReceiveData:(Object)data
	{
	 //the response from Flickr is the actual JS Object, which has an
	 //array of photos that we pass to our collection view
	 [self addImageList:data.photos.photo withIdentifier: lastIdentifier];
	}





	- (void)connection:(CPJSONPConnection)aConnection didFailWithError:(CPString)error
	{
	 //Ideally, we would do something smarter here.
	 alert(error);
	}




Due to the use of the script tag injection, as opposed to a traditional XHR object, we don't have any fine grained information about the response. We cannot detect status codes, and cannot natively access the response. Thankfully, CPJSONPConnection does a good job of managing the additional complexity, and massaging it into a familiar API. There is still some work to be done on generating more reliable errors, but it should be completed in the near future.

JSONP does have it's own security implications. Because you're essentially allowing arbitrary third party code to execute within the context of your own application, you should only use JSONP with providers you trust. It's also important to note that because these requests are sent to different domains, cookies from your own site will not be sent along with the request. This prevents third parties from stealing your sessions, but it also means that authenticating requests is significantly more complex.


### Conclusion

There's been some confusion about when to use CPURLConnection versus CPJSONPConnection, due largely in part to the lack of documentation or discussion on the issue. In general, you should only use JSONP with third-party services that you trust, and only when doing so doesn't involve sensitive information. For example, getting public Flickr photos, or performing a Google search using Google's AJAX search API. If you're communicating with your own service, even if you use JSON as the transmission format, you should use CPURLConnection. Their are numerous advantages to this approach, especially the additional security.

I hope this has illustrated both when and how to use CPURLConnection and CPJSONPConnection. As we continue to develop Cappuccino, we'll be improving both of these classes, and introducing new communication methods as well. If you have questions, sound off in the comments, or try the [mailing list or irc channel](http://www.cappuccino-project.org/discuss/list.php).



