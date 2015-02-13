import XCTest
import ProjectEuler

class Problem1Tests: XCTestCase {

  func testAnswerIsCorrect() {
    let guess = problem1(1000)
    XCTAssertEqual(guess, 233168)
  }

}
