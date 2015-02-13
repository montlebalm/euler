import XCTest

class Problem6Tests: XCTestCase {

  func testAnswerIsCorrect() {
    var guess = problem6(100)
    let answer = 25164150
    XCTAssertEqual(guess, answer)
  }

}
