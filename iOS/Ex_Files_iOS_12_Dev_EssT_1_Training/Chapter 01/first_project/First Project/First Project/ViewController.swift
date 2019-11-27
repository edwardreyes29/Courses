//
//  ViewController.swift
//  First Project
//
//  Created by Edward Reyes on 10/30/19.
//  Copyright © 2019 VidTeam. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UITextFieldDelegate {
    
    @IBOutlet weak var label: UILabel!
    @IBOutlet weak var textField: UITextField!
       
    override func viewDidLoad() {
        super.viewDidLoad()

        label.text = "Hello from code!"
        label.textColor = UIColor.green
        textField.becomeFirstResponder()
        
        textField.delegate = self
    }

    @IBAction func buttonWasTapped(_ sender: Any) {
        label.text = "Hello \(textField.text!)"
        label.textColor = UIColor.red
        textField.resignFirstResponder() // Used to dismiss keyboard when button pressed
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        textField.resignFirstResponder()
    }
    
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        label.text = "Hello \(textField.text!)"
        label.textColor = UIColor.red
        view.endEditing(true)
        return false
    }
    
}


// [Ch 2]
// Model-View-Controller
// design pattern -> separates model data from visual objects and managing them using controllers
// Use assitant editor to connect code to label object

// (opt + click) -> opens assistan editor, placing current selected file on right side, current on left
// (right-click + drag) object to view controller to make into code object

// placement matters. Do it right underneath line that says class

// Optional() -> values that may possible not have a value -> use ! to unwrap, not best

// [First Responder] -> used to dismiss keyboad once done using text field
// - Object currently recieving events
// - When typing on text field, that current text field is the object
// - recieving info from the keyboard
// - To dismiss keyboard, tell text field to resing itself as first responder
// Dismiss keyboard from clicking anywhere off of the text field

// [Troubleshoot UI-to-code connections]
// Common mistakes deals with connecting user interface elemetns to code
// Troubleshoot connections
// 1. First place to look is in code to see if connections are made
//    to user interface objects. Look at line numbers and see if circles
//    are filled in. But it takes a couple of seconds for them to fill in.
// Ex. if 'func buttonWasTapped(_ sender: Any)' has no circle filled in.
//      1. go to Main.storyboard
//      2. Select View Controller or select button itself
//      3. Check inspector for invets, check outlets
//      4. Look at recived Actions with no circles, drag circle onto button

// Quiz
// 1. Possible to have substantial amount of code for model and view objects, most applications have the bulk of their code in the controller classes
// 2. Name of place that stores UI objects: Library
// 3. Documents Outline is an effective area of selecting UI objects, but not requires for modifyling lables or anything else
// 4. Outlets connect UI objects to variables, while Actions connect UI events to methods
//  - button connection normally use Action paramter instead of Outlet parameter
//  - @IBAction & @IBOutlet
// 5. text field will show the keyboard, a label will not
// 6. First repsonder refers to the object that is  urrently recieving UI events
// 7. Following can only be done with delegation: Using Text Field delegation is the only way to respond to a Text Fields events, like when the reutrn key is presseed
// 8. Broken connections can be diagnosed in the Connections Inspector, in code, and by extension the Assistant Editor
