package main

import (
	"net/http"
	"strconv"

	"github.com/joms/ledmastree/backend/ledcontroller"
	"github.com/labstack/echo"
	"github.com/labstack/echo/middleware"
)

var resOk = "200 OK"

func main() {
	e := echo.New()
	ledcontroller.Init()

	e.Use(middleware.LoggerWithConfig(middleware.LoggerConfig{
		Format: "method=${method}, uri=${uri}, status=${status}\n",
	  }))

	e.GET("/", func(c echo.Context) error {
		return c.String(http.StatusOK, resOk)
	})

	e.GET("/on", func(c echo.Context) error {
		ledcontroller.OnAll()
		return c.String(http.StatusOK, resOk)
	})

	e.GET("/on/:id", func(c echo.Context) error {
		id, err := strconv.Atoi(c.Param("id"))
		
		if err != nil {
			return c.String(http.StatusBadRequest, "Invalid input, id must be int")
		}

		ledcontroller.On(id)
		return c.String(http.StatusOK, resOk)
	})

	e.GET("/off", func(c echo.Context) error {
		ledcontroller.OffAll()
		return c.String(http.StatusOK, resOk)
	})

	e.GET("/off/:id", func(c echo.Context) error {
		id, err := strconv.Atoi(c.Param("id"))
		
		if err != nil {
			return c.String(http.StatusBadRequest, "Invalid input, id must be int")
		}

		ledcontroller.Off(id)
		return c.String(http.StatusOK, resOk)
	})

	e.Logger.Fatal(e.Start(":1337"))

}
