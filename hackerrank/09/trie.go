package main

import (
    "fmt"
    "os"
    "bufio"
    "strconv"
    "strings"
    "errors"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    text, _ := reader.ReadString('\n')
    text = strings.TrimRight(text, "\n")
    n, _ := strconv.Atoi(text)
    head := node{count: 0, end: false}
    
    for i := 0; i < n; i++ {
        text, _ := reader.ReadString('\n')
        parsed := strings.TrimRight(text, "\n")
        words := strings.Split(parsed, " ")
        if len(words) != 2 {
            return
        }
        
        switch words[0] {
        case "find":
            fmt.Println(count(&head, words[1]))
        case "add":
            add(&head, words[1])
        }
    }
}

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

