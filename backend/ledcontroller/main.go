package ledcontroller

import (
	"fmt"
	"os"

	"github.com/stianeikeland/go-rpio/v4"
)

// LEDS All led pins
var LEDS = []int{2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}

func OnAll() {
	if err := rpio.Open(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	defer rpio.Close()

	for _, id := range LEDS {
		if ledIsValid(id) {
			pin := rpio.Pin(id)
			pin.Output()

			pin.High()
		}
	}
}

func On(id int) {
	if err := rpio.Open(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	defer rpio.Close()

	if ledIsValid(id) {
		pin := rpio.Pin(id)
		pin.Output()

		pin.High()
	}
}

func OffAll() {
	if err := rpio.Open(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	defer rpio.Close()

	for _, id := range LEDS {
		if ledIsValid(id) {
			pin := rpio.Pin(id)
			pin.Output()

			pin.Low()
		}
	}
}

func Off(id int) {
	if err := rpio.Open(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	defer rpio.Close()

	if ledIsValid(id) {
		pin := rpio.Pin(id)
		pin.Output()

		pin.Low()
	}
}

func ToggleAll() {
	if err := rpio.Open(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	defer rpio.Close()

	for _, id := range LEDS {
		if ledIsValid(id) {
			pin := rpio.Pin(id)
			pin.Output()

			pin.Toggle()
		}
	}
}

func Toggle(id int) {
	if err := rpio.Open(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	defer rpio.Close()

	if ledIsValid(id) {
		pin := rpio.Pin(id)
		pin.Output()

		pin.Toggle()
	}
}

func ledIsValid(id int) bool {
	for _, i := range LEDS {
		if i == id {
			return true
		}
	}
	return false
}
