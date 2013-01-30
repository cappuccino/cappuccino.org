xml.instruct!
xml.feed "xmlns" => "http://www.w3.org/2005/Atom" do
  xml.title "Cappuccino Project"
  xml.subtitle "Modern app development on the web"
  xml.id "http://www.cappuccino-project.org/blog/"
  xml.link "href" => "http://www.cappuccino-project.org/blog/"
  xml.link "href" => "http://www.cappuccino-project.org/blog/feed.xml", "rel" => "self"
  xml.updated blog.articles.first.date.to_time.iso8601
  xml.author { xml.name "Cappuccino Core Developers" }

  blog.articles[0..10].each do |article|
    xml.entry do
      xml.title article.title
      xml.link "rel" => "alternate", "href" => article.url
      xml.id article.url
      xml.published article.date.to_time.iso8601
      xml.updated article.date.to_time.iso8601
      xml.author { xml.name article.data.author }
      xml.summary article.summary, "type" => "html"
      xml.content article.body, "type" => "html"
    end
  end
end