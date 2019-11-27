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
        
       // [2]
        button.setTitleColor(.blue, for: .normal)
        button.setTitle("Tap Me", for: .normal)
        
        // [1]
        button.addTarget(self, action: #selector(buttonWasTapped), for: .touchUpInside)
    }
    
    @objc func buttonWasTapped() {
        label.text = "Hello!"
    }

}

// [1]
// Since were in viewController we will use 'self' unless we created another object that will handle events
// selector -> pass action method to call. #selector(object method). When selector is highlighted, it says objective-C method. Method needs to be exposed to objective-c

// [2]
// Default color of button is white
       // UIControl.State is the color of the state applied to
       // .normal sets color for all states
