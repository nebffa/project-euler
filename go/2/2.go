package main

import "fmt"


func main() {
    x, y:= 1, 2
    sum := 0

    for x + y < 4e6 {
        if y % 2 == 0 {
            sum += y
        }

        x, y = y, x + y
    }

    fmt.Println(sum)
}