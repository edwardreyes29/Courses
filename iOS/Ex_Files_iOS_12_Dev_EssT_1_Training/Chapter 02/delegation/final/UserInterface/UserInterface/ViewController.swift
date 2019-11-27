//
//  ViewController.swift
//  UserInterface
//
//  Created by Todd Perkins on 9/13/18.
//  Copyright © 2018 Todd Perkins. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UITextFieldDelegate {
    
    @IBOutlet weak var label: UILabel!
    @IBOutlet weak var textField: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        label.text = "Hello from code!"
        textField.becomeFirstResponder()
        textField.delegate = self
    }
    
    @IBAction func buttonWasTapped(_ sender: Any) {
        
        label.text = "Hello \(textField.text!)"
        textField.resignFirstResponder()
        
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        textField.resignFirstResponder()
    }
    
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        view.endEditing(true)
        return false
    }

}

