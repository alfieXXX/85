class Common {
    constructor(data) {
        this.data = data;            
    }
    URLOrigin = () => {
        return window.location.origin
    }
    ApiData = async() => {
        let $data = this.data,
            $base_host  = this.URLOrigin(),        
            $url = $base_host + $data.url,
            $options    = {},
            $payload    = JSON.stringify($data.payload),
            $headers 	= {
                'Content-type': 'application/json; charset=UTF-8',
            };                

            if($data.method_type == 'GET'){
                $options = { method: $data.method_type, headers: $headers};
            }else{
                $options = { method: $data.method_type, headers: $headers, body: $payload };
            }

            let response = await fetch($url, $options);
            if (response.status >= 200 && response.status <= 204) {
                const sleep = m => new Promise(r => setTimeout(r, m))
                const $body = document.body;

                $body.classList.add("loading");

                let return_data = await response.json();
                let errorCode = return_data.errorCode;

                await sleep(500)

                $body.classList.remove("loading");

                return return_data
            } else {
                  console.log(`something wrong, the server code: ${response.status}`);
            }                
    } 
    PHCurrency = async(number) => {
            number = (parseFloat(number)).toFixed(2);
            number = number.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            return "₱ "+number;
    }
    NumbersWithComma = async(number) => {
        var str = number.toString().split(".");
        str[0] = str[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        return str.join(".");
    }
    NumbersWithCommaDecimal = (number) => {
        number = parseFloat(number).toFixed(2)
        return Number(number).toLocaleString('en');
    }        
    IziToast = (route, message) =>{
        switch(route) {
            case 1: //Success
                    iziToast.success({
                            title    	: 'Success',
                            message  	: message,
                            position 	: 'topRight',
                            icon     	: 'fa fa-thumbs-up',
                            displayMode : 'replace'
                        });
            break;
            case 2: //Error
                    iziToast.error({
                        title    	: 'Error',
                        message  	: message,
                        position 	: 'topRight',
                        icon		: 'fa fa-exclamation',
                        displayMode : 'replace'
                    });
            break;
            case 3: //Info
                    iziToast.info({
                        title    	: 'Info',
                        message  	: message,
                        position 	: 'topRight',
                        icon     	: 'fa fa-info',
                        displayMode : 'replace'
                    });
            break;
            case 4: //Warning
                    iziToast.warning({
                        title    	: 'Warning',
                        message  	:  message,
                        position 	: 'topRight',
                        icon     	: 'fa fa-exclamation-triangle',
                        displayMode : 'replace'
                    });
            break;
            default: 
                    iziToast.warning({
                        title    	: 'Warning',
                        message  	:  'Route is required.',
                        position 	: 'topRight',
                        icon     	: 'fa fa-exclamation-triangle',
                        displayMode : 'replace'
                    });
        }
    }       
   
}

