#!/usr/bin/env ruby

SENDER = ARGV[0].scan(/;SENDER:(.*?)\]/)
RECEIVER = ARGV[0].scan(/RECEIVER:(.*?)\]/)
FLAGS = ARGV[0].scan(/FLAGS:(.*?)\]/)
puts [SENDER, RECEIVER, FLAGS].join(',')
