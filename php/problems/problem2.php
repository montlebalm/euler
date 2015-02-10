<?php

/*
 * Problem 2
 *
 * Question:
 *   Each new term in the Fibonacci sequence is generated by adding the
 *   previous two terms. By starting with 1 and 2, the first 10 terms will be:
 *   1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
 *   By considering the terms in the Fibonacci sequence whose values do not
 *   exceed four million, find the sum of the even-valued terms.
 *
 * Answer:
 *   4613732
*/

function problem2($max) {
  list($last, $current) = [1, 2];
  $total = $current;

  while ($last < $max) {
    list($last, $current) = [$current, $current + $last];

    if ($current % 2 == 0) {
      $total += $current;
    }
  }

  return $total;
}
