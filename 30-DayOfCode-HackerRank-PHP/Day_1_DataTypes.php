<?php
$handle = fopen ("php://stdin","r");
$i = 4;
$d = 4.0;
$s = "HackerRank ";
// Declare second integer, double, and String variables.
$x;
$y;
$z;

// Read and save an integer, double, and String to your variables.
$x = readline();
$y = readline();
$z = readline();

// Print the sum of both integer variables on a new line.
echo $i+$x;
echo "\n";
printf ('%.1f',$d+$y);
echo "\n";
echo $s.$z;


// Print the sum of the double variables on a new line.

// Concatenate and print the String variables on a new line
// The 's' variable above should be printed first.

fclose($handle);
?>