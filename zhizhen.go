package main

import "fmt"

func main() {
	var foo int
	var bar *int

	bar = &foo

	fmt.Printf("%v %T \n", foo, foo)
	fmt.Printf("%v %T \n", *bar, bar)

}
