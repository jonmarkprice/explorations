package main

import ("fmt")

func main() {
    s := "abc"
    for i := 0; i < len(s); i++ {
        fmt.Println(i)
    }
}
