

export default class getData {
    // constructor(props) {
    //     super(props)
    
    //     this.state = {
             
    //     }
    // }
    
    static putting = () => {
        return fetch('http://127.0.0.1:8000/apidet/list', {
            'method': 'GET',
            headers: {
                'Content-type': 'application/json',
                'Authorization': 'Token f421821841a1784203284cf4564e806cb858f0d3'
            },
            body: Response.body
        })
        .then(resp => resp.json())
    }

    static retrieve = () => {
        return fetch('http://127.0.0.1:8000/apidet/list', {
            'method': 'GET',
            headers: {
                'Content-type': 'application/json',
                'Authorization': 'Token f421821841a1784203284cf4564e806cb858f0d3'
            }
        })
        .then(resp => resp.json())
    }   

    static delete = (id) => {
        return fetch(`http://127.0.0.1:8000/apidet/list/${id}/`, {
            'method': 'DELETE',
            headers: {
                'Content-type': 'application/json',
                'Authorization': 'Token f421821841a1784203284cf4564e806cb858f0d3'
            }
        })
    }  
    
    static update = (id) => {
        return fetch("http://127.0.0.1:8000/apidet/list/28/", {
            'method': 'PUT',
            headers: {
                "Content-Type": "application/json",
                'Authorization': 'Token f421821841a1784203284cf4564e806cb858f0d3'
            },
            body: JSON.stringify({
                "firstName": "Alfie",
                "lastName": "Lianza",
                "age": 18,
                "birthday": "07-08-03",
                "address": "5747",
                "sex": "Male",
                "contactNumber": "09062817311",
                "data_created": "2021-12-10T20:04:52.924599Z"
            })
        })
        .then(resp => resp.json())
    }
}

