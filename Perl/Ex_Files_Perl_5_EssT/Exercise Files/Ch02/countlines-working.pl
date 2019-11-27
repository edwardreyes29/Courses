#!/usr/bin/perl
# countlines.pl by Bill Weinman <http://bw.org/contact/>

use 5.18.0; # use -> import
use warnings;

# use a scalar variable for the name of the file
my $filename = "linesfile.txt";  # my keyword -> declares local variable / $variable -> scalar variable carries one value

open(FH, $filename);    # open the file
my @lines = <FH>;       # read the file: put file into array. @ - makes variable into an array, $ - makes variable into scalar
close(FH);              # close the file

my $count = scalar @lines;  # the number of lines in the file
say "There are $count lines in $filename";

# This script opens a file and tells you how many lines there are