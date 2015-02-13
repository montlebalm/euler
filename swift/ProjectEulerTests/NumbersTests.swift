import XCTest
import ProjectEuler

class SquareTests: XCTestCase {

  func testPositiveNumber() {
    XCTAssertEqual(square(2), 4)
  }

  func testNegativeNumber() {
    XCTAssertEqual(square(-2), 4)
  }

}

class StringToDigitsTests: XCTestCase {

  func testNumericString() {
    XCTAssertEqual(stringToDigits("1234"), [1, 2, 3, 4])
  }
  
}
