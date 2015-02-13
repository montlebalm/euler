<?php

/*
 * Problem 4
 *
 * Question:
 *  A palindromic number reads the same both ways. The largest palindrome made
 *  from the product of two 2-digit numbers is 9009 = 91 × 99.
 *  Find the largest palindrome made from the product of two 3-digit numbers.
 *
 * Answer:
 *   906609
*/

require_once('helpers/palindromes.php');

function problem4($digits) {
  $high = round(pow(10, $digits) - 1);
  $low = round(pow(10, $digits - 1));
  list($a, $b) = [$high, $high];
  $palindrome = 0;

  while ($a >= $low && $b >= $low) {
    $a -= 1;
    $product = $a * $b;

    if ($product > $palindrome && isPalindrome($product)) {
      $palindrome = $product;
    }

    if ($a == $low) {
      $b -= 1;
      $a = $high;
    }
  }

  return $palindrome;
}
