FROM ruby:2.6.10

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get install -y \
  nodejs \
  unzip \
  python2.7 \
  && rm -rf /var/lib/apt/lists/*

# Link python2 and python to python2.7 because it's used by pygments.rb to load the pygments library.
RUN ln -s /usr/bin/python2.7 /usr/bin/python2
RUN ln -s /usr/bin/python2.7 /usr/bin/python

RUN gem install bundler:1.17.3

COPY Gemfile* /app/

RUN bundle _1.17.3_ install
