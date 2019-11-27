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
        label.translatesAutoresizingMaskIntoConstraints = false
        label.text = "Hello from code!"
        view.addSubview(label)
        
        // Add constraints relative to superview, so add auto constraints after object is added as a subview
        // 50 points away from left edge of view
        label.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 50).isActive = true
        // constraint to the right edge of label -50, -50 point to left
        label.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -50).isActive = true
        // safeArea include buffer for iphone versions with lip on top
        label.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 100).isActive = true
        label.heightAnchor.constraint(equalToConstant: 150).isActive = true
        
        
        
    }


}

