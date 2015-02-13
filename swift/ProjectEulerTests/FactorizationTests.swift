import XCTest
import ProjectEuler

class LcmTests: XCTestCase {

  func testLcmFor1And10() {
    XCTAssertEqual(lcm(1, 10), 10)
  }

  func testLcmFor10And20() {
    XCTAssertEqual(lcm(10, 20), 20)
  }

  func testLcmFor10And10() {
    XCTAssertEqual(lcm(10, 10), 10)
  }

}

class IsPrimeTests: XCTestCase {

  func test2IsPrime() {
    XCTAssertTrue(isPrime(2))
  }

  func test17IsPrime() {
    XCTAssertTrue(isPrime(17))
  }

  func test100IsNotPrime() {
    XCTAssertFalse(isPrime(100))
  }

}
