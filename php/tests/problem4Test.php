<?php

class Problem4Test extends PHPUnit_Framework_TestCase {

  public function testIsCorrect() {
    $answer = problem4(999);
    $this->assertEquals(906609, $answer);
  }

}
