//Property of TrendSellers LLC 
//@author Ethen Pociask
package main


import (
	"os"
	"bytes"
	"strings"
	"time"
	"fmt"
)

func updateFile(name string, variable string, value string){

	fileName := name + "/" + name + variable + ".txt"
	file, err := os.OpenFile(fileName,  os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)

	if err != nil {

		panic(err)
	}
	time := time.Now()
	timeS := time.String()
	timeS = timeS[0 : len(timeS)- 26]

	formatString := "\n" + timeS + ", " + value

	 _, err = file.Write([]byte(formatString))	 
	

	if err != nil{
		panic(err)
	}

	file.Close()
} 


func distribute(name string){

	file, err := os.Open(name+ "/" + name + ".txt")

	if err != nil {
		panic(err)
	}

	buf := new(bytes.Buffer)
   buf.ReadFrom(file)
   contents := buf.String()

	jsonStr := contents

	file.Close()
	jsonStr = jsonStr[1 : len(jsonStr)-1]


	list := strings.Split(jsonStr, ",")
	list[2] = list[len(list)-1]
	list[len(list)-1] = ""
	list = list[:len(list) -1]

	m := make(map[string]string)
	for i := 4; i <= 10; i++ {
		temp  := list[i]
		key := temp[2 : strings.Index(temp, ":")-1]
		value := temp[strings.Index(temp, ":") + 3: len(temp)-1]
		value = strings.Replace(value, "'", "", 1)
		m[key] = value
	}


	for key, value := range m{

		updateFile(name, key, value)
	}
}

func main(){

	for{
	tick := time.Tick(5000 * time.Millisecond)
		for range tick {
    fmt.Println("Tick")
    distribute("ethereum")
    distribute("bitcoin")
		}
}
}

