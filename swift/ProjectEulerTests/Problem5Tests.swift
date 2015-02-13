import XCTest
import ProjectEuler

class Problem5Tests: XCTestCase {

  func testAnswerIsCorrect() {
    let guess = problem5(Array(1...20))
    XCTAssertEqual(guess, 232792560)
  }

}
