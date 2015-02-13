import XCTest

class Problem7Tests: XCTestCase {

  func testAnswerIsCorrect() {
    let guess = problem7(10001)
    XCTAssertEqual(guess, 104743)
  }

}
