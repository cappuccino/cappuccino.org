---
title: Getting Started With Cappuccino and Ruby on Rails
author: Tom Robinson
author_email: tom@280north.com
wordpress_id: 139
wordpress_url: http://cappuccino.org/discuss/?p=139
date: '2008-11-11'
categories:
- Cappuccino
- Tutorials
tags: []
---


Cappuccino is completely server agnostic, meaning Cappuccino applications can be served using any HTTP server (for example Apache, lighttpd, Microsoft IIS, etc) and can communicate with any server side technology over HTTP (Ruby on Rails, Django, PHP, ASP, Java, CouchDB, etc). This lets you choose your server-side components based on whatever criteria is important to you (experience, existing infrastructure, etc).

That said, many people have asked for examples of using Cappuccino with various server side technologies, especially Ruby on Rails. Since Cappuccino is server agnostic, it turns out to be very simple to get started.

### Setting Up a Project

The first step is to create your Rails project using the standard "rails _appname_" command:

	rails appname
	cd appname

Then create a new Cappuccino project in a temporary directory, either using the "steam create" command, or by downloading the ["Starter Package"](http://www.cappuccino-project.org/download/). Move the contents of the Cappuccino project to the Rails application's "public" directory. Here's an example using "steam create" (which will overwrite the default index.html):

	steam create temp
	mv temp/* public/.
	rmdir temp

That's it! Start the Rails webserver using "script/server". Point your browser to http://localhost:3000/ and you should see the "hello world" Cappuccino application.

### Exposing the Data

This alone isn't particularly interesting. For Rails to be useful in conjunction with Cappuccino you'll want to be able to transfer data between them. Rails makes this very easy.

Rails offers built in support for two common data exchange formats: JSON and XML. Of the two, JSON is typically prefered in Cappuccino. To output a Ruby data structure as JSON, simply call "render :json => object" in the controller action:

	 class TestController def movies
	 @movies = Movie.find(:all)
	 render :json => @movies
	 end
	end


This is getting all the "Movie" model objects, and simply serializing the array into JSON.

You can also filter or process the array before serializing it. When an ActiveRecord instance is converted to JSON it is wrapped in an extra object that's usually uneccessary (i.e. { "movie" : { "title" : "something", "description" : "a description" }}). Creating a plain Ruby object from each ActiveRecord object prevents this. Additionally, it allows you to perform other processing, such as excluding certain properties. Here we use "map" to convert each ActiveRecord object to a plain Ruby object:

	 def movies
	 @movies = Movie.find(:all).map {|m| { :title => m.title, :description => m.description } }
	 render :json => @movies
	end


Finally, if for some reason you need to use [JSONP](http://www.cappuccino-project.org/discuss/2008/10/08/xmlhttprequest-jsonp-cappuccino/) (be sure you understand why you need it, and the security implications!), Rails makes it very easy to wrap the JSON in callback:

	 def hello
	 render :json => { :hello => "world" }, :callback => params[:jsoncallback]
	end


This example also demonstrates accessing parameters that were passed in, namely the "jsoncallback" parameter.

### Getting and Submitting Data From Cappuccino

The typical way to retrieve or submit data from a Cappuccino application is to use [CPURLConnection](http://www.cappuccino-project.org/learn/documentation/classes/CPURLConnection.html). This is discussed extensively in [a previous blog post](http://www.cappuccino-project.org/discuss/2008/10/08/xmlhttprequest-jsonp-cappuccino/), and all of it applies to using Cappuccino with Rails.

### Scaffolding

In addition to HTML views Rails "scaffolding" also provides simple XML web services. You can also easily add JSON versions similar to the following:

	 def index
	 @movies = Movie.find(:all)



	 respond_to do |format|
	 format.html # index.html.erb
	 format.xml { render :xml => @movies }
	 format.json { render :json => @movies }
	 end
	end




### Conclusion

This covers the bare essentials of integrating a Cappuccino application with Rails. There is lots of potential for better Cappuccino integration with ActiveRecord and other server-side data technologies. Please feel free to make suggestions, or implement something and contribute it back!



