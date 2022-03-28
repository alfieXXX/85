import React, {useState, useEffect} from 'react'


function FirstFunc(props) {
    const [Name, setName] = useState('Alfie');

    // useEffect(() => {
    //     fetch('http://127.0.0.1:8000/apidet/list', {
    //         'method': 'GET',
    //         headers: {
    //             'Content-type': 'application/json',
    //             'Authorization': 'Token f421821841a1784203284cf4564e806cb858f0d3'
    //         }
    //     })
    //     .then(resp => resp.json())
    //     .then(resp => console.log(resp))
    //     .catch(error => console.error(error))
    // }, [])

    return(
        <div>
            <h1>This is {Name}</h1>
        </div>
    )
}

export default FirstFunc;