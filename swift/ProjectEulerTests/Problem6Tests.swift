import XCTest
import ProjectEuler

class Problem6Tests: XCTestCase {

  func testAnswerIsCorrect() {
    let guess = problem6(100)
    XCTAssertEqual(guess, 25164150)
  }

}
