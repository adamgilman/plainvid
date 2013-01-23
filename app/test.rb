require 'sinatra'
require "sinatra/reloader"

require 'embedly'
require 'json'
require 'open-uri'

max_width = 600
max_height = 800

get '/' do
	"It works!!"
end

get '/hi/:name' do
	"Hello #{params[:name]}!"
end

get '/plain/:url' do
	url = URI::dencode(url)
	embedly_api = Embedly::API.new :user_agent => 'Mozilla/5.0 (compatible; plainvid/1.0; app@plainvid.com)'
	plain = embedly_api.oembed :url => url
	plain = plain[0].html

	return "hello" + plain
end