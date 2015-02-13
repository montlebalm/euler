import XCTest
import ProjectEuler

class LcmTests: XCTestCase {

  func testDifferentNumbers() {
    XCTAssertEqual(lcm(1, 10), 10)
  }

  func testSameNumber() {
    XCTAssertEqual(lcm(10, 10), 10)
  }

}

class IsPrimeTests: XCTestCase {

  func testPrimeNumber() {
    XCTAssertTrue(isPrime(2))
  }

  func testNonPrimeNumber() {
    XCTAssertFalse(isPrime(100))
  }

}
