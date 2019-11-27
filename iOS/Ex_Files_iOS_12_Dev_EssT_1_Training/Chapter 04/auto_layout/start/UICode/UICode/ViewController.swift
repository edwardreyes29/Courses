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
//        label.frame = CGRect(x: 50, y: 50, width: 200, height: 50)
        
        // if true, provides auto layout constraints, but you want to set your own so set to false
        label.translatesAutoresizingMaskIntoConstraints = false
        label.text = "Hello from code!"
        view.addSubview(label)
        
        // pin anchors to other anchors, so pin leadingAnchor of label to left or leading anchor of its super.view
        // Pick constraint with constant = 50, saying that the left edge of a label is going to be 50 points away fromt he left edge of th view
        label.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 50).isActive = true
        // Enables you to modify constraints at runtime. So If we save the value returned by this code, we could reference it later and change it to true or false, enabling me to modify our layout while app is running
        
        // Constrained to the right edge of the super.view minus 50
        label.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -50).isActive = true
        
        // topAnchor is all the way to the top of the screen
        // safeAreaLayoutGuide includes buffer for devices like iPhone 10, Xr, etc, that lip at the top
        label.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 100).isActive = true
        
        label.heightAnchor.constraint(equalToConstant: 150).isActive = true
        
        // [Modify fonts with code]
        label.font = UIFont.systemFont(ofSize: 150)
        // Make sure font scale appropriately
        label.minimumScaleFactor = 0.2 // 20% of original size whic is 30 points
        label.adjustsFontSizeToFitWidth = true
        
        
    }


}

