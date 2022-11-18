#!/usr/bin/env ruby
#this script filters transactions and returns the sender,
#receiver and their address. using regex

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
