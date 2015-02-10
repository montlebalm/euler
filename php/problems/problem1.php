<?php

/*
 * Problem 1
 *
 * Question:
 *   If we list all the natural numbers below 10 that are multiples of 3 or 5,
 *   we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of
 *   all the multiples of 3 or 5 below 1000.
 *
 * Answer:
 *   233168
*/

function problem1($max) {
  $multiples = array_filter(range(1, $max - 1), function($num) {
    return !($num % 3) || !($num % 5);
  });
  return array_sum($multiples);
}
