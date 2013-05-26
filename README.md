## Cappuccino Website

This is the new GitHub forkable and pull-request ready, static HTML & JS modern Cappuccino website.

### How to Contribute to this Site

1. Install bundler.

        gem install bundler

2. Install the gems used by the site.

        cd /path/to/site
        bundle install

3. Run it in server mode:

        bundle exec middleman

4. Open [http://localhost:4567/](http://localhost:4567/) to view site.

Now you can simply edit the markdown, HAML, CSS, JavaScript and so on which makes up the site. Middleman will automatically compile it.

When you are done, create a fork of this repository, make a branch of master, commit your changes, and make a pull request.

### How to Add a Blog Post

    bundle exec middleman article "Article Title"

### How to Deploy

    bundle exec middleman build
    bundle exec middleman deploy

### Credits

* [Bootstrap](http://twitter.github.com/bootstrap/)
* 1154865_61618748.jpeg http://www.sxc.hu/photo/1154865
* furley_bg.png [Dan Kruse](http://subtlepatterns.com/light-sketch/)

Based on Measure Bootstrap Theme, which in turn includes:

* Lato Google webfont http://www.google.com/webfonts/specimen/Lato
* Icons by Brankic1979 http://www.brankic1979.com/icons/
* Social icons from http://medialoot.com/item/round-social-media-icons/
