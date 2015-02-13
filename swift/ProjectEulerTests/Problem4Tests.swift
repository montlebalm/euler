import XCTest
import ProjectEuler

class Problem4Tests: XCTestCase {

  func testAnswerIsCorrect() {
    let guess = problem4(3)
    XCTAssertEqual(guess, 906609)
  }
  
}
