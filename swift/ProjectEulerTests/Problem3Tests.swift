import XCTest
import ProjectEuler

class Problem3Tests: XCTestCase {

  func testAnswerIsCorrect() {
    let guess = problem3(600851475143)
    XCTAssertEqual(guess, 6857)
  }

}
