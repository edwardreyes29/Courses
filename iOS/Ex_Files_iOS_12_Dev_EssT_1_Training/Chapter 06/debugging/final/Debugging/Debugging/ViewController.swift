//
//  ViewController.swift
//  Debugging
//
//  Created by Todd Perkins on 10/4/18.
//  Copyright © 2018 Todd Perkins. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    let items = ["Item 1", "Item 2", "Item 3"]
    var textView: UITextView!
    var currentIndex = 0

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        exampleFunc()
        textView.text = items[currentIndex]
    }
    
    func exampleFunc() {
        currentIndex = 3
    }

}

