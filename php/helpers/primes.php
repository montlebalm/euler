<?php

/*
 * Determine whether a given number is prime
 * @param int $num The number to be tested
 * @returns bool True if $num is prime
*/
function isPrime($num) {
  // Lol easy mode
  if ($num == 2) {
    return true;
  }

  if ($num < 2 || $num % 2 == 0) {
    return false;
  }

  for ($i = 3; $i < pow($num, .5); $i += 2) {
    if ($num % $i == 0) {
      return false;
    }
  }

  return true;
}
