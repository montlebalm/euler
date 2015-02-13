<?php

class PrimeTest extends PHPUnit_Framework_TestCase {

  public function trueForPrime() {
    $this->assertEquals(isPrime(2), true);
    $this->assertEquals(isPrime(5), true);
    $this->assertEquals(isPrime(7), true);
  }

  public function falseForNonPrime() {
    $this->assertEquals(isPrime(4), false);
    $this->assertEquals(isPrime(10), false);
    $this->assertEquals(isPrime(20), false);
  }

}
