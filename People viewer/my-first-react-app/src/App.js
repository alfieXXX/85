import './App.css';
import TableList from './components/tableList';
import Form from './components/form'
import React, {useEffect} from 'react'
import {useState} from 'react'
import getData from './components/feth';

function App() {

  const [Data, setData] = useState([]);


    // This part is fetching the data from the RESTful API
    useEffect(() => {
        fetch('http://127.0.0.1:8000/apidet/list', {
                'method': 'GET',
                headers: {
                    'Content-type': 'application/json',
                    'Authorization': 'Token f421821841a1784203284cf4564e806cb858f0d3'
                }
            })
            .then(resp => resp.json())
            .then(resp => setData(resp))
            .catch(error => console.error(error))
    }, [])

  const [FormWindow, setFormWindow] = useState(false);

  const close = () => {
    return setFormWindow(!FormWindow)
  }

  const open = () => {
    console.log(Data)
    return setFormWindow(!FormWindow)
  }


  

  return (
    <div className="App">
      {FormWindow&&<Form Data={Data} close={close}/>}

      <TableList Data={Data} Open={open}/>
    </div>
  );
}

export default App;
