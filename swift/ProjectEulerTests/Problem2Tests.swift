import XCTest
import ProjectEuler

class Problem2Tests: XCTestCase {

  func testAnswerIsCorrect() {
    let guess = problem2(4000000)
    XCTAssertEqual(guess, 4613732)
  }
  
}
