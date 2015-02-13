<?php

class PalindromeTest extends PHPUnit_Framework_TestCase {

  public function trueForPalindrome() {
    $this->assertEquals(isPalindrome(1), true);
    $this->assertEquals(isPalindrome(101), true);
    $this->assertEquals(isPalindrome(2222), true);
  }

  public function falseForNonPalindrome() {
    $this->assertEquals(isPalindrome(12), false);
  }

}
