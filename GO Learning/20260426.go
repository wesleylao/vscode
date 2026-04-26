package main

import "fmt"

func main() {
	fmt.Println("this is the first learning section")

	// Println adds a new line automatically
	fmt.Println("This is line 1")
	fmt.Println("This is line 2")

	// Print stays on the same line
	fmt.Print("Hello, ")
	fmt.Print("World!\n") // You have to manually add '\n' to get a new line

	// Spacing difference with multiple arguments
	fmt.Print("A", "B", "C\n") // Outputs: ABC (no spaces added)
	fmt.Println("A", "B", "C") // Outputs: A B C (spaces automatically added)
}
