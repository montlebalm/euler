import XCTest

class Problem5Tests: XCTestCase {

  func test1to10() {
    XCTAssertEqual(problem5(Array(1...10)), 2520)
  }

  func test1to20() {
    XCTAssertEqual(problem5(Array(1...20)), 232792560)
  }
  
}