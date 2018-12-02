package ledcontroller

import (
	"fmt"
	"os"
	"time"
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
	go func() {
		fadeOnAll()
	}()
}

func On(id int) {
	go func() {
		fadeOn(id)
	}()
}

func OffAll() {
	go func() {
		fadeOffAll()
	}()
}

func Off(id int) {
	go func() {
		fadeOff(id)
	}()
}

func sendCommand(command string) {
    if _, err := file.WriteString(command+"\n"); err != nil {
      panic(err)
    }
}

func fadeOnAll() {
	for i := 0; i <= 100; i+=5 {
		val := float32(i) / 100.0
		sendCommand(fmt.Sprintf("*=%g", val))
		time.Sleep(time.Second / 100)
	}
}

func fadeOn(id int) {
	for i := 0; i <= 100; i+=5 {
		val := float32(i) / 100.0
		sendCommand(fmt.Sprintf("%d=%g", id, val))
		time.Sleep(time.Second / 100)
	}
}

func fadeOffAll() {
	for i := 100; i >= 0; i-=5 {
		val := float32(i) / 100.0
		sendCommand(fmt.Sprintf("*=%g", val))
		time.Sleep(time.Second / 100)
	}
}

func fadeOff(id int) {
	for i := 100; i >= 0; i-=5 {
		val := float32(i) / 100.0
		sendCommand(fmt.Sprintf("%d=%g", id, val))
		time.Sleep(time.Second / 100)
	}
}