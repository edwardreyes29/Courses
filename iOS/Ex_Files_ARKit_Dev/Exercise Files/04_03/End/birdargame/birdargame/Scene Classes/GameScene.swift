//
//  GameScene.swift
//  LyndaARGame
//
//  Created by Brian Advent on 22.05.18.
//  Copyright © 2018 Brian Advent. All rights reserved.
//

import UIKit
import SpriteKit
import ARKit



class GameScene: SKScene {
    
    var numberOfBirds = 10
    var timerLabel:SKLabelNode!
    var counterLabel:SKLabelNode!

    static var gameState:GameState = .none
    
    override func didMove(to view: SKView) {
        let waitAction = SKAction.wait(forDuration: 0.5)
        let spwanAction = SKAction.run {
            self.performInitialSpwan()
        }
        
        self.run(SKAction.sequence([waitAction, spwanAction]))
        
    }
    
    override func update(_ currentTime: TimeInterval) {
        guard let sceneView = self.view as? ARSKView else {return}
        
        if let cameraZ = sceneView.session.currentFrame?.camera.transform.columns.3.z {
            for node in nodes(at: CGPoint.zero) {
                if let bird = node as? Bird {
                    
                    guard let anchors = sceneView.session.currentFrame?.anchors else {return}
                    
                    for anchor in anchors {
                        if abs(cameraZ - anchor.transform.columns.3.z) < 0.2 {
                            if let potentialTargetBird = sceneView.node(for: anchor) {
                                if bird == potentialTargetBird {
                                    bird.removeFromParent()
                                    spwanBird()
                                }
                            }
                        }
                        
                    }
                    
                    
                    
                }
            }
        }
        
    }
    
    
    func performInitialSpwan() {
        
        GameScene.gameState = .spwanBirds
        
        for _ in 1 ... numberOfBirds {
            spwanBird()
        }
    }
    
    
    func spwanBird() {
        
        guard let sceneView = self.view as? ARSKView else {return}
        
        if let currentFrame = sceneView.session.currentFrame {
            var translation = matrix_identity_float4x4
            
            translation.columns.3.x = randomPosition(lowerBound: -0.2, upperBound: 0.2) // -1.5 1.5
            translation.columns.3.y = randomPosition(lowerBound: -0.2, upperBound: 0.2) // -1.5 1.5
            translation.columns.3.z = randomPosition(lowerBound: -0.5, upperBound: -0.2) // -2 2
            
            let transform = simd_mul(currentFrame.camera.transform, translation)
            
            let anchor = ARAnchor(transform: transform)
            sceneView.session.add(anchor: anchor)
            
            
        }
        
    }

}


