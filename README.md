## Cappuccino Website

This is the new GitHub forkable and pull-request ready, static HTML & JS modern Cappuccino website.

### How to Contribute to this Site

You will need Docker.

#### Build the site
```
docker build -t middleman .
docker run --rm --volume "$PWD":/app -t middleman bundle exec middleman build
```

#### Preview the site

```
docker run --rm --publish 4567:4567 --volume "$PWD":/app -t middleman bundle exec middleman server
```

Open [http://localhost:4567/](http://localhost:4567/) to view the site. When you're done stop the Docker container with Ctrl-C.

While it's running you can simply edit the markdown, HAML, CSS, JavaScript and so on which makes up the site. Middleman will automatically compile it as needed and you can preview the results in your browser.

When you are done, create a fork of this repository, make a branch of master, commit your changes, and make a pull request.

### How to Add a Blog Post

Copy an existing blog post to a file with a new name in the right folder. Then modify the preamble (the bit on the top of the post) to indicate the right date and author.

### How to Deploy

- Rsync the contents of `build/` to the hosting server.
- Clear the Cloudflare cache.

### Notes

#### Why is `pygments-main` copied into the `vendor` folder? 

I didn't find a git repo for this to clone so I checked out the mercurial version and hacked it to improve Objective-J support. Ideally we go to some less hacky solution in the long run.

### Credits

* [Bootstrap](http://twitter.github.com/bootstrap/)
* 1154865_61618748.jpeg http://www.sxc.hu/photo/1154865
* furley_bg.png [Dan Kruse](http://subtlepatterns.com/light-sketch/)

Based on Measure Bootstrap Theme, which in turn includes:

* Lato Google webfont http://www.google.com/webfonts/specimen/Lato
* Icons by Brankic1979 http://www.brankic1979.com/icons/
* Social icons from http://medialoot.com/item/round-social-media-icons/
