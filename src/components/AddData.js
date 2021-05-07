import React, { useState } from 'react'
import firebase from '../utils/firebase'
import '../App2.css';


function AddData() {



    const createData = () => {
        var date = new Date().getDate();
        var hour = new Date().getHours();
        var min = new Date().getMinutes();
        var sec = new Date().getSeconds();
        var Time = (date) + "-" + (hour) + "-" + (min) + "-" + (sec)
        const dataRef = firebase.database().ref('student');
        const data = {
            personalID: "41419"
        }

        dataRef.child((Time)).update(data)
    }

    return (
        <div align="center">
            <button className='btn' onClick={createData}>ทดลองงาน</button>
        </div>
    )
}

export default AddData