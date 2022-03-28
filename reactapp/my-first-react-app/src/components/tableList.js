import React, {useState, useEffect} from 'react'
import getData from './feth'

function TableList({ Data, Open}) {

    
    // End of fetching

    const deleteDetail = (e) => {
        getData.delete(e.id)
    }

    function shorter(e) {
        if (e.length > 20) {
            // console.log(e)
            return e.slice(0, 20).concat('...')
        }
        return e
    }

    return (
        <div className='main'>
            <table style={{'margin': '0px'}} className='tablelist'>
            <colgroup>
                <col span="6" style={{"backgroundColor":"white"}}/>
            </colgroup>
                <thead>
                    <tr>
                        <th style={{'width': '5px'}}>Id</th>
                        <th style={{'width': '80px'}}>Name</th>
                        <th style={{'width': '5px'}}>Age</th>
                        <th style={{'width': '40px'}}>Birthday</th>
                        <th style={{'width': '55px','maxWidth': '60px', 'overflow': 'hidden'}}>Address</th>
                        <th style={{'width': '5px'}}>Sex</th>
                        <th style={{'width': '40px'}}>Contact Number</th>
                        <th style={{'width': '40px'}}>Action</th>
                    </tr>
                </thead>
                <tbody>
                    { Data.map(e => {
                        const name = e.lastName + ', ' + e.firstName
                            return(
                                <tr key={e.id} className='hoverDetails'>
                                    <td >{e.id}</td>
                                    <td >{name}</td>
                                    <td >{e.age}</td>
                                    <td >{e.birthday}</td>
                                    <td >{e.address}</td>
                                    <td >{e.sex}</td>
                                    <td >{e['contactNumber']}</td>
                                    <td ><button className='updatebtn' onClick={Open}>update</button><button className='deletebtn' onClick={() => deleteDetail(e)}>delete</button></td>
                                </tr>
                            )
                        })
                    }
                </tbody>
                
            </table>
            <button className="addButton">Add</button>
        </div>
    )
}

export default TableList
