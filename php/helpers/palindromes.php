<?php

/*
 * Determine whether a given number is a palindrome
 */
function isPalindrome($num) {
  $str = strval($num);
  return $str == strrev($str);
}
