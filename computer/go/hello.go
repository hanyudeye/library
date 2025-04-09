package main

// import "fmt"

func main() {
	var name string = "hello"
	if(name != "hello") {
		name = "world"
	} else {
		name = "hello world"
	}
	print(name)
}