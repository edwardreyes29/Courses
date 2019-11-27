//
//  ViewController.swift
//  UICode
//
//  Created by Todd Perkins on 9/27/18.
//  Copyright © 2018 Todd Perkins. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    let label = UILabel()

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        label.frame = CGRect(x: 10, y: 100, width: 100, height: 20)
        label.text = "Waiting..."
        view.addSubview(label)
        
        let button = UIButton()
        button.frame = CGRect(x: 10, y: 130, width: 100, height: 30)
        view.addSubview(button)
        
        button.setTitleColor(.blue, for: .normal)
        button.setTitle("Tap Me", for: .normal)
        button.addTarget(self, action: #selector(buttonWasTapped), for: .touchUpInside)
    }
    
    @objc func buttonWasTapped() {
        label.text = "Hello!"
    }

}

