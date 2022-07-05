package main

import "fmt"

func main(){
	data :=[...]int{0,1,2,3,4,5,6,7,8}
	fmt.Println(data)
	fmt.Println(cap(data[:]))
}
