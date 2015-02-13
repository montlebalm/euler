import XCTest
import ProjectEuler

class Problem9Tests: XCTestCase {

  func testAnswerIsCorrect(sum: Int) {
    let guess = problem9(1000)
    XCTAssertEqual(guess, 31875000)
  }

}
