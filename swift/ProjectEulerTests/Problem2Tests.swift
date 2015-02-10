import XCTest

class Problem2Tests: XCTestCase {

  func testTo10() {
    XCTAssertEqual(problem2(10), 10)
  }

  func testTo4000000() {
    XCTAssertEqual(problem2(4000000), 4613732)
  }
  
}
