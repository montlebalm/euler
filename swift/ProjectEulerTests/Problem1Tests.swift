import XCTest

class Problem1Tests: XCTestCase {

  func testTo10() {
    XCTAssertEqual(problem1(10), 23)
  }

  func testTo1000() {
    XCTAssertEqual(problem1(1000), 233168)
  }

}
