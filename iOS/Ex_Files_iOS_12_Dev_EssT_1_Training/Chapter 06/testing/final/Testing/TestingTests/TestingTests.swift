//
//  TestingTests.swift
//  TestingTests
//
//  Created by Todd Perkins on 10/4/18.
//  Copyright © 2018 Todd Perkins. All rights reserved.
//

import XCTest

class TestingTests: XCTestCase {

    override func setUp() {
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }

    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }
    
    func testPerson() {
        let name = "Todd"
        let person = Person(name: name)
        XCTAssert(person.name == name, "Name of person must match value passed in")
    }

    func testExample() {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
    }

    func testPerformanceExample() {
        // This is an example of a performance test case.
        self.measure {
            // Put the code you want to measure the time of here.
        }
    }

}
