//
//  ViewController.swift
//  UICode
//
//  Created by Todd Perkins on 9/27/18.
//  Copyright © 2018 Todd Perkins. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        let label = UILabel()
        label.frame = CGRect(x: 50, y: 50, width: 200, height: 50)
        label.text = "Hello from code!"
        view.addSubview(label)
    }


}

