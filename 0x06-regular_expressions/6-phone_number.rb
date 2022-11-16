#!/usr/bin/env ruby
#match a 10-digit number

puts ARGV[0].scan(/^\d{10,10}$/)
