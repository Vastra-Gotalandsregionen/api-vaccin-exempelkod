package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

var baseUrl = "https://test.api.vgregion.se/e-crm-scheduling-public/api/v1/testCenter"
var clientId = "c4d279f9b8094dbaafd0162c5a606623"
var clientSecret = "39D6cAB5D89c448ea3355aAC61De19e7"

func main() {
	client := &http.Client{}

	req, err := http.NewRequest("GET", "https://test.api.vgregion.se/e-crm-scheduling-public/api/v1/testCenter", nil)
	if err != nil {
		log.Fatalln(err)
	}
	req.Header.Add("client_id", clientId)
	req.Header.Add("client_secret", clientSecret)

	resp, err := client.Do(req)
	if err != nil {
		log.Fatalln(err)
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}

	jsonMap := make(map[string]interface{})
	err = json.Unmarshal(body, &jsonMap)
	if err != nil {
		panic(err)
	}

	for _, v := range jsonMap["testcenters"].([]interface{}) {
		valueMap := v.(map[string]interface{})
		fmt.Println(valueMap["title"], valueMap["urlBooking"])
	}
}
