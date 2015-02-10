<?php

class Problem2Test extends PHPUnit_Framework_TestCase {

  public function testIsCorrect() {
    $answer = problem2(4000000);
    $this->assertEquals(4613732, $answer);
  }

}
