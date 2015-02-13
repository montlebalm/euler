<?php

/*
 * Problem 3
 *
 * Question:
 *   The prime factors of 13195 are 5, 7, 13 and 29. What is the
 *   largest prime factor of the number 600851475143?
 *
 * Answer:
 *   6857
*/

require_once('helpers/primes.php');

function problem3($num) {
  // We only need to start at the square root of the maximum
  $start = round(pow($num, .5)) + 1;

  for ($i = $start; $i > 2; $i--) {
    if ($num % $i == 0 && isPrime($i)) {
      return $i;
    }
  }

  return 0;
}
