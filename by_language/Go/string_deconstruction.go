package main

import ("fmt")

func main() {
    s := "abc"

    var character uint8
    
    for i := 0; i < len(s); i++ {
        character = s[i]
        
        // 
        fmt.Println(character)        
        fmt.Println(s[i])
        
        // To print character, need string
        fmt.Println(string(s[i]))
    }
}
