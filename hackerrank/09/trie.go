package main

import "fmt"
import "errors"

func count(head *node, keys string) int {
    if len(keys) == 0 {
        return 0
    } else {
        current := head 
        results := 0
        
        // Iterate through all the keys
        for i := 0; i < len(keys); i++ {
            key, _ := index(keys[i])
            // XXX: Do I really need current and new?
            if current.child[key] == nil {
                // There is no entry
                return 0
            } else {
                // Continue
                current = current.child[key]
            }
        }
        // TODO...
        if current != nil {
            results = current.count
        }
        return results
    }
}

func add(head *node, query string) {
    current := head
    for i := 0; i < len(query); i++ { // or try range
        var key uint8
        key, _ = index(query[i])
        
        if current.child[key] == nil {
            // Create a new branch
            current.child[key] = &node{} // zeros are false, 0, [nil]
        }
        current.child[key].count++
        current = current.child[key]
    }
    current.end = true
}

func index(char uint8) (uint8, error) {
    if char >= 97 && char <= 122 {
        return char - 97, nil
    }
    return 26, errors.New("Character not allowed")
}

type node struct {
    count   int
    end     bool
    child   [26]*node
}

func main() {
    //fmt.Println("Hello world!")
    head := node{count: 0, end: false}
    //fmt.Println(head.count)
    //fmt.Println(head.end)
    
    //head.child[0] = &node{count: 1, end: false}
    //(*head).child[0] = node{count: 0, end: false}

    //fmt.Println(head.child[0].count)
    
    /*for i := 0; i < 26; i++ {
        fmt.Println(head.child[i])
    }*/
    //fmt.Println(count(&head, "abc"))
    //fmt.Println(count(&head, ""))
    
    // Test of index
    /*
    fmt.Println(index('a'))
    fmt.Println(index('f'))
    fmt.Println(index('z'))
    */
    
    // Simple add tests
    //fmt.Println(head)
    add(&head, "abc")
    //fmt.Println(head)
    fmt.Println(count(&head, "a"))
    
}


