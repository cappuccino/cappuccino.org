###
# Compass
###

# Susy grids in Compass
# First: gem install susy --pre
# require 'susy'

# Change Compass configuration
# compass_config do |config|
#   config.output_style = :compact
# end

###
# Page options, layouts, aliases and proxies
###

# Per-page layout changes:
#
# With no layout
# page "/path/to/file.html", :layout => false
#
# With alternative layout
# page "/path/to/file.html", :layout => :otherlayout
#
# A path which all have the same layout
# with_layout :admin do
#   page "/admin/*"
# end

with_layout :learn do
  page "/learn/*"
end

# Proxy (fake) files
# page "/this-page-has-no-template.html", :proxy => "/template-file.html" do
#   @which_fake_page = "Rendering a fake page with a variable"
# end

###
# Helpers
###

# Automatic image dimensions on image_tag helper
activate :automatic_image_sizes

# Methods defined in the helpers block are available in templates
# helpers do
#   def some_helper
#     "Helping"
#   end
# end

set :css_dir, 'css'

set :js_dir, 'js'

set :images_dir, 'img'

# Prevent HAML from indenting everything, even <pre> content.
set :haml, { ugly: true }

require "redcarpet"
set :markdown_engine, :redcarpet
set :markdown, :fenced_code_blocks => true,
               :autolink => true,
               :smartypants => true,
               :tables => true,
               :gh_blockcode => true

require 'rack/codehighlighter'
require "pygments"
Pygments.start('/Users/siker/dev/pygments-main/')
use Rack::Codehighlighter,
  :pygments,
  :element => "pre>code",
  :pattern => /\A:::([-_+\w]+)\s*\n/,
  :markdown => true

activate :deploy do |deploy|
  deploy.method = :rsync
  deploy.user = "cappuccino"
  deploy.host = "cappuccino.slevenbits.com"
  deploy.path = "/www/cappuccino.org/www/"
  deploy.clean = true
end

activate :blog do |blog|
  blog.paginate = true
  blog.prefix = "blog"
  blog.permalink = ":year/:month/:title.html"
  blog.tag_template = "blog/tag.html"
  blog.layout = "blog_post"
end

page "/blog/feed.xml", :layout => false


require "builder"

# Build-specific configuration
configure :build do
  # For example, change the Compass output style for deployment
  activate :minify_css

  # Minify Javascript on build
  activate :minify_javascript

  activate :asset_hash,
    :ignore => [/blog\/uploads\/.*/, /downloads\/.*/]

  # Enable cache buster
  # activate :cache_buster

  # Use relative URLs
  # activate :relative_assets

  # Compress PNGs after build
  # First: gem install middleman-smusher
  # require "middleman-smusher"
  # activate :smusher

  # Or use a different image path
  # set :http_path, "/Content/images/"

  after_build do
    # The server uses the current Starter to serve /learn/documentation and Frameworks/ of demo apps.
    `cd build/downloads/ && rm -Rf Starter && unzip CappuccinoStarter-0.9.8.zip`
    `cd build/learn/ && curl -s -L http://github.com/cappuccino/cappuccino-demos/tarball/master >demos.tgz && tar -xzf demos.tgz && rm -Rf demos && mv cappuccino-cappuccino-demos-* demos`
    `cd build/aristo/showcase && rm -Rf Aristo2Showcase README __MACOSX Frameworks Resources && unzip ../../downloads/Aristo2Showcase.zip && mv Aristo2Showcase/* .`
    `find build/ -name .git -delete`
  end
end
