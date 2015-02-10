import XCTest

class Problem4Tests: XCTestCase {

  func test2Digits() {
    XCTAssertEqual(problem4(2), 9009)
  }

  func test3Digits() {
    XCTAssertEqual(problem4(3), 906609)
  }
  
}
