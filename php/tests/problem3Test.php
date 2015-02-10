<?php

class Problem3Test extends PHPUnit_Framework_TestCase {

  public function testIsCorrect() {
    $answer = problem3(600851475143);
    $this->assertEquals(6857, $answer);
  }

}
