<?php

class Problem1Test extends PHPUnit_Framework_TestCase {

  public function testIsCorrect() {
    $answer = problem1(1000);
    $this->assertEquals(233168, $answer);
  }

}
