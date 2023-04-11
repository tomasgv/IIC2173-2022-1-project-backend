# syntax=docker/dockerfile:1
FROM ruby:3.0.2
RUN apt-get update -qq && apt-get install -y nodejs postgresql-client postgis

RUN mkdir /api/
WORKDIR /api/
COPY ./rest_api/Gemfile /api/Gemfile
COPY ./rest_api/Gemfile.lock /api/Gemfile.lock

COPY ./rest_api /api

RUN gem install bundler
RUN bundle install

# RUN bundle exec rake assets:precompile
# Add a script to be executed every time the container starts.
COPY ./rest_api/entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

EXPOSE 3000

# Configure the main process to run when running the image
# CMD ["rails", "server"]
CMD ["rails", "server", "-b", "0.0.0.0"]