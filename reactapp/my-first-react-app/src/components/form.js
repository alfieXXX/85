import React from 'react'
import getData from './feth'

function Form({close, Data}) {


    return (
        <div className='mainForm'>
            <div className='Form'>
                <h4 className='formTitle'>Form</h4>
                <form className="form2">
                <label htmlFor='name'>Name</label>
                <input className='formInput' type='text' name='name' placeholder='name here starts at "Last Name"'/>
                <label htmlFor='age'>Age</label>
                <input className='formInput' type='number' name='age' placeholder='age'/>
                <label htmlFor='birthday' >birthday</label>
                <input className='formInput' height='50px' type='date' name='birthday' placeholder='birthday"'/>
                <label htmlFor='address'>Address</label>
                <input className='formInput' type='text' name='address' placeholder='address'/>
                <label htmlFor='sex'>Sex</label>
                <select name='sex' defaultValue=''>
                    <option value='none'/>
                    <option value='Male'>Male</option>
                    <option value='Female'>Female</option>
                </select>
                <label htmlFor='contact number'>contact number</label>
                <input className='formInput' type='tel' name='contact number' placeholder='contac number'/>
                <button className='formUpdateBtn' onClick={() => getData.update(Data.id)}>Update</button>
                <button onClick={close} className='closeBtn'>Close Form</button>
                </form>
            </div>
        </div>
    )
}

export default Form
