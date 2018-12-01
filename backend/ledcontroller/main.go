package ledcontroller

import (
	"fmt"
	"os"
)

var ledList []led;

// PWM Enable/disable fading algorithms
var PWM = false
var file *os.File

func Init() {
	f, err := os.OpenFile("/dev/pi-blaster", os.O_APPEND|os.O_WRONLY, 0600)
	if err != nil {
		panic(err)
	}

	file = f
}

func OnAll() {
	sendCommand("*=1")
}

func On(id int) {
	sendCommand(fmt.Sprintf("%d=1", id))
}

func OffAll() {
	sendCommand("*=0")
}

func Off(id int) {
	sendCommand(fmt.Sprintf("%d=0", id))
}

func sendCommand(command string) {
    if _, err := file.WriteString(command+"\n"); err != nil {
      panic(err)
    }
}