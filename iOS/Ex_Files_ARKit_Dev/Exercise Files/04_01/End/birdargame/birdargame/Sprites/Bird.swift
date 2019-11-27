//
//  Bird.swift
//  LyndaARGame
//
//  Created by Brian Advent on 24.05.18.
//  Copyright © 2018 Brian Advent. All rights reserved.
//

import SpriteKit
import GameplayKit

class Bird : SKSpriteNode {
 
    var mainSprite = SKSpriteNode()
    
    func setup(){
        
        mainSprite = SKSpriteNode(imageNamed: "bird1")
        self.addChild(mainSprite)
        
        let textureAtals = SKTextureAtlas(named: "bird")
        let frames = ["sprite_0", "sprite_1", "sprite_2", "sprite_3", "sprite_4", "sprite_5", "sprite_6"].map{textureAtals.textureNamed($0)}
        
        let atlasAnimation = SKAction.animate(with: frames, timePerFrame: 1/7, resize: true, restore: false)
        
        let animationAction = SKAction.repeatForever(atlasAnimation)
        mainSprite.run(animationAction)
        
        
        let left = GKRandomSource.sharedRandom().nextBool()
        if left {
            mainSprite.xScale = -1
        }
        
        let duration = randomNumber(lowerBound: 15, upperBound: 20)
        
        let fade = SKAction.fadeOut(withDuration: TimeInterval(duration))
        let removeBird = SKAction.run {
            // create a new bird
            self.removeFromParent()
        }
        
        let flySeqence = SKAction.sequence([fade, removeBird])
        
        mainSprite.run(flySeqence)
        
    }
    
}


