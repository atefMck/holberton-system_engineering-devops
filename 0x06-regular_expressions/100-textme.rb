#!/usr/bin/env ruby
puts ARGV[0].scan(/from:(\w+)\b.*to:(\+\w+).*flags:([\w\+-:]+)/).join(',')
